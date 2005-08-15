
#
Summary:	X Display Manager Control Protocol library
Summary(pl):	Biblioteka protoko³u XDMCP
Name:		xorg-lib-libXdmcp
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXdmcp-%{version}.tar.bz2
# Source0-md5:	bb45d98b1319e40d0515a11fe4bd45b9
Source1:	libXdmcp-Wraphelp.c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/libXdmcp-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X Display Manager Control Protocol library.

%description -l pl
Biblioteka protoko³u XDMCP (X Display Manager Control Protocol).


%package devel
Summary:	Header files libXdmcp development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXdmcp
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXdmcp = %{version}-%{release}
Requires:	xorg-proto-xproto-devel

%description devel
X Display Manager Control Protocol library.

This package contains the header files needed to develop programs that
use these libXdmcp.

%description devel -l pl
Biblioteka protoko³u XDMCP (X Display Manager Control Protocol).

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXdmcp.


%package static
Summary:	Static libXdmcp libraries
Summary(pl):	Biblioteki statyczne libXdmcp
Group:		Development/Libraries
Requires:	xorg-lib-libXdmcp-devel = %{version}-%{release}

%description static
X Display Manager Control Protocol library.

This package contains the static libXdmcp library.

%description static -l pl
Biblioteka protoko³u XDMCP (X Display Manager Control Protocol).

Pakiet zawiera statyczne biblioteki libXdmcp.


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
%attr(755,root,wheel) %{_libdir}/libXdmcp.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xdmcp.h
%{_libdir}/libXdmcp.la
%attr(755,root,wheel) %{_libdir}/libXdmcp.so
%{_pkgconfigdir}/xdmcp.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXdmcp.a
