 SRC_DIR=src
 OBJ_DIR=obj
 LIB_DIR=lib
 BIN_DIR=bin
 MAN_DIR=man
INCL_DIR=include

CC=gcc
CFLAGS=-I$(INCL_DIR) -Wall

_DEPS = rawnet.h timerms.h
RAWNET_DEPS = $(patsubst %,$(INCL_DIR)/%,$(_DEPS))

_OBJ = rawnet.o timerms.o
OBJ = $(patsubst %,$(OBJ_DIR)/%,$(_OBJ))

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(DEPS)
	$(CC) $(CFLAGS) -fPIC -c -o $@ $<

$(LIB_DIR)/librawnet.a: $(OBJ)
	ar -cq $@ $^

$(LIB_DIR)/librawnet.so.1.0: $(OBJ)
	$(CC) $(CFLAGS) -shared -Wl,-soname,librawnet.so.1 -o $@ $^

$(BIN_DIR)/rawnetcc: $(SRC_DIR)/rawnetcc.c
	$(CC) $(CFLAGS) -o $@ $<

.PHONY: clean all install uninstall

all: $(LIB_DIR)/librawnet.so.1.0 $(LIB_DIR)/librawnet.a $(BIN_DIR)/rawnetcc

clean:
	rm -f $(LIB_DIR)/librawnet.so.1.0 $(LIB_DIR)/librawnet.a $(BIN_DIR)/rawnetcc $(OBJ_DIR)/*.o *~ $(SRC_DIR)/*~ $(INCL_DIR)/*~

install: all
	install -m 4755 $(BIN_DIR)/rawnetcc /usr/bin/

	install -m 644  $(LIB_DIR)/librawnet.a /usr/lib/
	install -m 644  $(LIB_DIR)/librawnet.so.1.0 /usr/lib/
	ldconfig -n /usr/lib/
	ln -s librawnet.so.1 /usr/lib/librawnet.so

	install -m 644  $(INCL_DIR)/rawnet.h /usr/include/
	install -m 644  $(INCL_DIR)/timerms.h /usr/include/

	install -m 644  $(MAN_DIR)/rawnet.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawiface.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawiface_open.3.lzma  /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawiface_getname.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawiface_getaddr.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawiface_getmtu.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawiface_close.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawnet_send.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawnet_recv.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawnet_poll.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/rawnet_strerror.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/timerms.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/timerms_reset.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/timerms_elapsed.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/timerms_left.3.lzma /usr/share/man/man3/
	install -m 644  $(MAN_DIR)/timerms_time.3.lzma /usr/share/man/man3/

	install -m 644  $(MAN_DIR)/es/rawnet.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawiface.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawiface_open.3.lzma  /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawiface_getname.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawiface_getaddr.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawiface_getmtu.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawiface_close.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawnet_send.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawnet_recv.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawnet_poll.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/rawnet_strerror.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/timerms.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/timerms_reset.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/timerms_elapsed.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/timerms_left.3.lzma /usr/share/man/es/man3/
	install -m 644  $(MAN_DIR)/es/timerms_time.3.lzma /usr/share/man/es/man3/

uninstall:
	rm -f /usr/bin/rawnetcc

	rm -f /usr/lib/librawnet.a
	rm -f /usr/lib/librawnet.so.1.0
	rm -f /usr/lib/librawnet.so.1
	rm -f /usr/lib/librawnet.so

	rm -f /usr/include/rawnet.h
	rm -f /usr/include/timerms.h

	rm -f /usr/share/man/man3/rawnet.3.lzma
	rm -f /usr/share/man/man3/rawiface.3.lzma
	rm -f /usr/share/man/man3/rawiface_open.3.lzma
	rm -f /usr/share/man/man3/rawiface_getname.3.lzma
	rm -f /usr/share/man/man3/rawiface_getaddr.3.lzma
	rm -f /usr/share/man/man3/rawiface_getmtu.3.lzma
	rm -f /usr/share/man/man3/rawiface_close.3.lzma
	rm -f /usr/share/man/man3/rawnet_send.3.lzma
	rm -f /usr/share/man/man3/rawnet_recv.3.lzma
	rm -f /usr/share/man/man3/rawnet_poll.3.lzma
	rm -f /usr/share/man/man3/rawnet_strerror.3.lzma
	rm -f /usr/share/man/man3/timerms.3.lzma
	rm -f /usr/share/man/man3/timerms_reset.3.lzma
	rm -f /usr/share/man/man3/timerms_elapsed.3.lzma
	rm -f /usr/share/man/man3/timerms_left.3.lzma
	rm -f /usr/share/man/man3/timerms_time.3.lzma

	rm -f /usr/share/man/es/man3/rawnet.3.lzma
	rm -f /usr/share/man/es/man3/rawiface.3.lzma
	rm -f /usr/share/man/es/man3/rawiface_open.3.lzma
	rm -f /usr/share/man/es/man3/rawiface_getname.3.lzma
	rm -f /usr/share/man/es/man3/rawiface_getaddr.3.lzma
	rm -f /usr/share/man/es/man3/rawiface_getmtu.3.lzma
	rm -f /usr/share/man/es/man3/rawiface_close.3.lzma
	rm -f /usr/share/man/es/man3/rawnet_send.3.lzma
	rm -f /usr/share/man/es/man3/rawnet_recv.3.lzma
	rm -f /usr/share/man/es/man3/rawnet_poll.3.lzma
	rm -f /usr/share/man/es/man3/rawnet_strerror.3.lzma
	rm -f /usr/share/man/es/man3/timerms.3.lzma
	rm -f /usr/share/man/es/man3/timerms_reset.3.lzma
	rm -f /usr/share/man/es/man3/timerms_elapsed.3.lzma
	rm -f /usr/share/man/es/man3/timerms_left.3.lzma
	rm -f /usr/share/man/es/man3/timerms_time.3.lzma
