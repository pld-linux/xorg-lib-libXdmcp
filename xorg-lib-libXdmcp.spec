#
# Conditional build:
%bcond_without	libbsd	# libbsd arc4random instead of Linux implementation

Summary:	X Display Manager Control Protocol library
Summary(pl.UTF-8):	Biblioteka protokołu XDMCP
Name:		xorg-lib-libXdmcp
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
# Source0-md5:	115c5c12ecce0e749cd91d999a5fd160
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
%{!?with_libbsd:BuildRequires:	glibc-devel >= 6:2.25}
%{?with_libbsd:BuildRequires:	libbsd-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.16
# getentropy() requires Linux 3.17+ (to avoid CVE-2017-2625 when building without libbsd)
%{!?with_libbsd:Requires:	uname(release) >= 3.17}
Obsoletes:	libXdmcp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Display Manager Control Protocol library.

%description -l pl.UTF-8
Biblioteka protokołu XDMCP (X Display Manager Control Protocol).

%package devel
Summary:	Header files for libXdmcp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXdmcp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXdmcp-devel

%description devel
X Display Manager Control Protocol library.

This package contains the header files needed to develop programs that
use libXdmcp.

%description devel -l pl.UTF-8
Biblioteka protokołu XDMCP (X Display Manager Control Protocol).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXdmcp.

%package static
Summary:	Static libXdmcp library
Summary(pl.UTF-8):	Biblioteka statyczna libXdmcp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXdmcp-static

%description static
X Display Manager Control Protocol library.

This package contains the static libXdmcp library.

%description static -l pl.UTF-8
Biblioteka protokołu XDMCP (X Display Manager Control Protocol).

Pakiet zawiera statyczną bibliotekę libXdmcp.

%prep
%setup -q -n libXdmcp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_libbsd:ac_cv_lib_bsd_arc4random_buf=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# (.html version) packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXdmcp/xdmcp.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXdmcp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXdmcp.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/xdmcp.html
%attr(755,root,root) %{_libdir}/libXdmcp.so
%{_libdir}/libXdmcp.la
%{_includedir}/X11/Xdmcp.h
%{_pkgconfigdir}/xdmcp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXdmcp.a
