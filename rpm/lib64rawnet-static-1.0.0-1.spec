Summary: Library to develop "raw" network protocols.
Name: lib64rawnet-static
Version: 1.0.0
Release: 1
Copyright: GPL
Group: Development/Libraries
Source: http://www.it.uc3m.es/muruenya/lib64rawnet-static-1.0.0.tar.gz
#Patch: librawnet-devel-1.0.0-buildroot.patch
BuildRoot: /var/tmp/%{name}-buildroot
Provides: lib64rawnet

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

mkdir -p $RPM_BUILD_ROOT/%{_libdir}

install -m 644 lib/librawnet.a $RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING CHANGELOG

%{_libdir}/librawnet.a

%changelog
* Wed Sep 01 2010 Manuel Urueña <muruenya@it.uc3m.es> 
- Initial release.
