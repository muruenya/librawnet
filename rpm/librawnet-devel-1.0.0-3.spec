Summary: Library to develop "raw" network protocols.
Name: librawnet-devel
Version: 1.0.0
Release: 3
Copyright: GPL
Group: Development/Libraries
Source: http://www.it.uc3m.es/muruenya/librawnet-devel-1.0.0.tar.gz
#Patch: librawnet-devel-1.0.0-buildroot.patch
BuildRoot: /var/tmp/%{name}-buildroot
#Requires: librawnet

%description
This library enables developing network protocols bypassing the Linux kernel 
stack. It access directly to the host interfaces and allows sending and
receiving "raw" packets by means of a Packet socket.

Install librawnet if you would like to develop a network stack from scratch.

%prep
%setup -q
#%patch -p1 -b .buildroot

%build
make all RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man3/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/es/man3/

install -m 755 lib/librawnet.so.1.0 $RPM_BUILD_ROOT/%{_libdir}
ln -s librawnet.so.1 $RPM_BUILD_ROOT/%{_libdir}/librawnet.so

install -m 4755 bin/rawnetcc $RPM_BUILD_ROOT/%{_bindir}

install -m 644 include/rawnet.h $RPM_BUILD_ROOT/%{_includedir}
install -m 644 include/timerms.h $RPM_BUILD_ROOT/%{_includedir}

install -m 644 man/rawnet.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawiface.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawiface_open.3.lzma  $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawiface_getname.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawiface_getaddr.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawiface_getmtu.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawiface_close.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawnet_send.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawnet_recv.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawnet_poll.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/rawnet_strerror.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/timerms.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/timerms_reset.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/timerms_elapsed.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/timerms_left.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/
install -m 644 man/timerms_time.3.lzma $RPM_BUILD_ROOT/%{_mandir}/man3/

install -m 644 man/es/rawnet.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawiface.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawiface_open.3.lzma  $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawiface_getname.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawiface_getaddr.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawiface_getmtu.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawiface_close.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawnet_send.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawnet_recv.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawnet_poll.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/rawnet_strerror.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/timerms.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/timerms_reset.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/timerms_elapsed.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/timerms_left.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/
install -m 644 man/es/timerms_time.3.lzma $RPM_BUILD_ROOT/%{_mandir}/es/man3/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING CHANGELOG

%{_libdir}/librawnet.so.1.0
%{_libdir}/librawnet.so.1
%{_libdir}/librawnet.so
%{_bindir}/rawnetcc
%{_includedir}/rawnet.h
%{_includedir}/timerms.h
%{_mandir}/man3/rawnet.3.lzma
%{_mandir}/man3/rawiface.3.lzma
%{_mandir}/man3/rawiface_open.3.lzma
%{_mandir}/man3/rawiface_getname.3.lzma
%{_mandir}/man3/rawiface_getaddr.3.lzma
%{_mandir}/man3/rawiface_getmtu.3.lzma
%{_mandir}/man3/rawiface_close.3.lzma
%{_mandir}/man3/rawnet_send.3.lzma
%{_mandir}/man3/rawnet_recv.3.lzma
%{_mandir}/man3/rawnet_poll.3.lzma
%{_mandir}/man3/rawnet_strerror.3.lzma
%{_mandir}/man3/timerms.3.lzma
%{_mandir}/man3/timerms_reset.3.lzma
%{_mandir}/man3/timerms_elapsed.3.lzma
%{_mandir}/man3/timerms_left.3.lzma
%{_mandir}/man3/timerms_time.3.lzma
%{_mandir}/es/man3/rawnet.3.lzma
%{_mandir}/es/man3/rawiface.3.lzma
%{_mandir}/es/man3/rawiface_open.3.lzma
%{_mandir}/es/man3/rawiface_getname.3.lzma
%{_mandir}/es/man3/rawiface_getaddr.3.lzma
%{_mandir}/es/man3/rawiface_getmtu.3.lzma
%{_mandir}/es/man3/rawiface_close.3.lzma
%{_mandir}/es/man3/rawnet_send.3.lzma
%{_mandir}/es/man3/rawnet_recv.3.lzma
%{_mandir}/es/man3/rawnet_poll.3.lzma
%{_mandir}/es/man3/rawnet_strerror.3.lzma
%{_mandir}/es/man3/timerms.3.lzma
%{_mandir}/es/man3/timerms_reset.3.lzma
%{_mandir}/es/man3/timerms_elapsed.3.lzma
%{_mandir}/es/man3/timerms_left.3.lzma
%{_mandir}/es/man3/timerms_time.3.lzma

%changelog
* Wed Sep 01 2010 Manuel Urueña <muruenya@it.uc3m.es> 
- Initial release.
