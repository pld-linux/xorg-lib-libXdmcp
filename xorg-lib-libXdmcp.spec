Summary:	X Display Manager Control Protocol library
Summary(pl):	Biblioteka protokołu XDMCP
Name:		xorg-lib-libXdmcp
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXdmcp-%{version}.tar.bz2
# Source0-md5:	99ddb6fa2cb00f4cef3d0fffb16229fb
Source1:	libXdmcp-Wraphelp.c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXdmcp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Display Manager Control Protocol library.

%description -l pl
Biblioteka protokołu XDMCP (X Display Manager Control Protocol).

%package devel
Summary:	Header files libXdmcp development
Summary(pl):	Pliki nagłówkowe do biblioteki libXdmcp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXdmcp-devel

%description devel
X Display Manager Control Protocol library.

This package contains the header files needed to develop programs that
use these libXdmcp.

%description devel -l pl
Biblioteka protokołu XDMCP (X Display Manager Control Protocol).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXdmcp.

%package static
Summary:	Static libXdmcp library
Summary(pl):	Biblioteka statyczna libXdmcp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXdmcp-static

%description static
X Display Manager Control Protocol library.

This package contains the static libXdmcp library.

%description static -l pl
Biblioteka protokołu XDMCP (X Display Manager Control Protocol).

Pakiet zawiera statyczną bibliotekę libXdmcp.

%prep
%setup -q -n libXdmcp-%{version}

install -m 644 %{SOURCE1} Wraphelp.c

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libXdmcp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXdmcp.so
%{_libdir}/libXdmcp.la
%{_includedir}/X11/Xdmcp.h
%{_pkgconfigdir}/xdmcp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXdmcp.a
