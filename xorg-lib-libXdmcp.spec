Summary:	X Display Manager Control Protocol library
Summary(pl.UTF-8):	Biblioteka protokołu XDMCP
Name:		xorg-lib-libXdmcp
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
# Source0-md5:	762b6bbaff7b7d0831ddb4f072f939a5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXdmcp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXdmcp.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,css}
%attr(755,root,root) %{_libdir}/libXdmcp.so
%{_libdir}/libXdmcp.la
%{_includedir}/X11/Xdmcp.h
%{_pkgconfigdir}/xdmcp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXdmcp.a
