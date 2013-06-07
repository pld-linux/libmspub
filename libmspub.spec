#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	A library providing ability to interpret and import Microsoft Publisher content
Summary(pl.UTF-8):	Biblioteka umożliwiająca interpretowanie i importowanie treści z Microsoft Publishera
Name:		libmspub
Version:	0.0.6
Release:	1
License:	GPL v2+ or LGPL v2+ or MPL v1.1
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	96a1f176abd683c6b1b02a08847c0616
URL:		http://www.freedesktop.org/wiki/Software/libmspub
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libwpg-devel >= 0.2
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmspub is library providing ability to interpret and import
Microsoft Publisher content into various applications. You can find it
being used in libreoffice.

%description -l pl.UTF-8
Libmspub to biblioteka umożliwiająca interpretowanie i importowanie
treści z Microsoft Publishera do wielu aplikacji. Jest wykorzystywana
przez libreoffice.

%package devel
Summary:	Development files for libmspub
Summary(pl.UTF-8):	Pliki nagłówkowe dla libmspub
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9
Requires:	libwpg-devel >= 0.2
Requires:	zlib-devel

%description devel
This package contains the header files for developing applications
that use libmspub.

%description devel -l pl.UTF-8
Pen pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
libmspub.

%package static
Summary:	Static libmspub library
Summary(pl.UTF-8):	Statyczna biblioteka libmspub
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmspub library.

%description static -l pl.UTF-8
Statyczna biblioteka libmspub.

%package apidocs
Summary:	libmspub API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmspub
Group:		Documentation

%description apidocs
API and internal documentation for libmspub library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmspub.

%package tools
Summary:	Tools to transform Microsoft Publisher content into other formats
Summary(pl.UTF-8):	Programy do przekształcania treści z Microsoft Publishera do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Microsoft Publisher content into other formats.
Currently supported: XHTML, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania treści z Microsoft Publishera do innych
formatów. Aktualnie obsługiwane są XHTML i raw.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--disable-werror

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libmspub-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmspub-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmspub-0.0.so
%{_includedir}/libmspub-0.0
%{_pkgconfigdir}/libmspub-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmspub-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pub2raw
%attr(755,root,root) %{_bindir}/pub2xhtml
