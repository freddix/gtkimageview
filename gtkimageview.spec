Summary:	Simple image viewer widget for GTK+
Name:		gtkimageview
Version:	1.6.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://trac.bjourne.webfactional.com/chrome/common/releases/%{name}-%{version}.tar.gz
# Source0-md5:	8346b42012a82d5fe6f1c151bae346c3
URL:		http://trac.bjourne.webfactional.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple image viewer widget for GTK+.

%package devel
Summary:	Header files for gtkimageview library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for gtkimageview library.

%package apidocs
Summary:	gtkimageview API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gtkimageview  API documentation.

%prep
%setup -q

# kill gnome common deps
%{__sed} -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libgtkimageview.so.?
%attr(755,root,root) %{_libdir}/libgtkimageview.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkimageview.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

