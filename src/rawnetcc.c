/* rawnetcc - Compiles an executable using the librawnet library and gives
 *            CAP_NET_RAW and CAP_NET_ADMIN capabilities or sets the SUID bit
 *            to the generated executable.
 * Copyright (C) 2012 Manuel Urueña <muruenya@it.uc3m.es>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <libgen.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <errno.h>

#define ROOT_UID 0

extern int errno;

static char* MYSELF;

/* Prints the specified execv command as a single command line. */
void printcmd ( char* argv[] )
{
  int i = 0;
  char* arg = argv[0];

  while (arg != NULL) {
    if (i == 0) {
      printf("%s", arg);
    } else {
      printf(" %s", arg);
    }
    i++;
    arg = argv[i];
  }
  printf("\n");
}


/* Executes the specified command as a separate process with execv in order to 
 * work when called from a SUID program. */
int system_suid ( char* argv[] )
{
  int err;
  int wait_status;

  /* Print command to be executed */
  printcmd(argv);

  pid_t child_pid = fork();
  if (child_pid == -1) {
    /* Error in fork() */
    fprintf(stderr, "%s: Error in fork(): %s\n", 
            MYSELF, strerror(errno));
    return -1;

  } else if (child_pid == 0) {
    /* Child Process: Execute the command  */
    execv(argv[0], argv);

    /* This code should never execute but in case of execv Error: 
     *   Abort child process! */
    fprintf(stderr, "%s: Error in execv(\"%s\"): %s\n",
            MYSELF, argv[0], strerror(errno));
    exit(-2);
  }

  /* Parent Process: Wait for the child process */
  err = wait(&wait_status);
  if (err == -1) {
    fprintf(stderr, "%s: Error in wait(\"%s\"): %s\n", 
            MYSELF, argv[0], strerror(errno));
    return -3;
  }
  
  if (WIFEXITED(wait_status) == 0) {
    fprintf(stderr, "%s: Child process (\"%s\") has not exited normally\n",
            MYSELF, argv[0]);
    return -4;
  }
  
  return WEXITSTATUS(wait_status);
}


int main ( int argc, char* argv[] )
{
  /* Parse command line arguments */
  MYSELF = basename(argv[0]);
  if (argc <= 2) {
    printf("%s <exec> <file1.c> [<file2.c>...]\n", MYSELF);
    printf("     <exec>: Name of the executable to be created.\n");
    printf("   <file.c>: Source code of the executable.\n");
    exit(-1);
  }
  
  char* exec_file = argv[1];

  /* Check whether executable filename does not exists or it is not a ".c" file
   * Not providing an executable filename is a common user mistake, 
   * which could lead to overwrite source code. */
  int file_exists = (access(exec_file, F_OK) == 0);
  if (file_exists) {
    char* file_ext = rindex(exec_file, '.');
    int file_dot_c = (file_ext != NULL) && (strcasecmp(file_ext, ".c") == 0);
    if (file_dot_c) {
      fprintf(stderr, 
              "%s: Invalid executable file name: \"%s\". Aborting !!\n",
              MYSELF, exec_file);
      fprintf(stderr, "%s: Probably the <exec> parameter is missing.\n", 
              MYSELF);
      exit(-1);
    }
  }

  /* Give up superuser rights temporarily to compile, regain them later. */
  uid_t uid = getuid();
  int err = seteuid(uid);
  if (err != 0) {
    fprintf(stderr, "%s: Cannot set euid to %d: Aborting !!\n", 
            MYSELF, uid);
    exit(-1);
  }

  /* Generate compilation command & execute with system() call */
  int i;
  char gcc_command[1024];
  sprintf(gcc_command, "/usr/bin/gcc -Wall -g -o ");
  for (i=1; i<argc; i++) {
    strcat(gcc_command, argv[i]);
    strcat(gcc_command, " ");
  }
  strcat(gcc_command, "-lrawnet");

  printf("%s\n", gcc_command);

  err = system(gcc_command);
  if (err != 0) {
    exit(err);
  }

  /* Regain superuser rights to set capabilities/permissions */
  err = setuid(ROOT_UID);
  if (err != 0) {
    fprintf(stderr, "%s: Cannot set uid to %d: Aborting !!\n", 
            MYSELF, ROOT_UID);
    exit(-1);
  }

  /* Check super-user rights */
  uid_t euid = geteuid();
  if (euid != ROOT_UID) {
    fprintf(stderr, 
       "ERROR: %s MUST be executed with super-user rights or suid bit: Aborting!\n",
       MYSELF);
    fprintf(stderr,
       "%s is not correctly installed. Please contact the system's administrator.\n",
       MYSELF);
    exit(-1);
  }
  
  /* Generate setcap command (it may appear on /sbin/ or /usr/sbin/).
     It must be executed with execv() because of the suid bit */
  char* setcap_path = "/sbin/setcap";
  err = access(setcap_path, R_OK | X_OK); 
  if (err != 0) {
    setcap_path = "/usr/sbin/setcap";
  }

  int setcap_argc = 4;
  char* setcap_argv[setcap_argc + 1]; /* +1 because of final NULL */
  setcap_argv[0] = setcap_path;
  setcap_argv[1] = "-q";
  setcap_argv[2] = "cap_net_raw,cap_net_admin=eip";
  setcap_argv[3] = exec_file;
  setcap_argv[4] = NULL;

  err = system_suid(setcap_argv);
  if (err == 0) {
    /* Setcap has worked: Exit successfully */
    exit(0);
  }

  /* Setcap has failed: Change owner to root and set suid bit */
  int chown_argc = 3;
  char* chown_argv[chown_argc + 1];
  chown_argv[0] = "/bin/chown";
  chown_argv[1] = "root";
  chown_argv[2] = exec_file;
  chown_argv[3] = NULL;

  err = system_suid(chown_argv);
  if (err != 0) {
    fprintf(stderr, "%s: Cannot change owner of \"%s\" to root: Aborting !!\n",
            MYSELF, exec_file);
    exit(-1);
  }

  int chmod_argc = 3;
  char* chmod_argv[chmod_argc + 1];
  chmod_argv[0] = "/bin/chmod";
  chmod_argv[1] = "4775";
  chmod_argv[2] = exec_file;
  chmod_argv[3] = NULL;

  err = system_suid(chmod_argv);
  if (err != 0) {
    fprintf(stderr, "%s: Cannot set suid bit to \"%s\": Aborting !!\n", 
            MYSELF, exec_file);
    exit(-1);
  }

  return 0;
}
