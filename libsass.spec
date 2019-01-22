%define major 1
%define libname %mklibname sass %{major}
%define devname %mklibname sass -d

Summary:	C/C++ port of the Sass CSS precompiler
Name:		libsass
Version:	3.5.5
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://sass-lang.com/libsass
Source0:	https://github.com/sass/libsass/archive/%{version}.tar.gz

%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original
version was written in Ruby, but this version is meant for
efficiency and portability.

This library strives to be light, simple, and easy to build and
integrate with a variety of platforms and languages.

Libsass is just a library, but if you want to RUN libsass, install
the sassc package.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	C/C++ port of the Sass CSS precompiler
Group:		System/Libraries

%description -n %{libname}
This package contains the library files required for running
services built using %{name}.

%files -n %{libname}
%doc Readme.md SECURITY.md LICENSE
%{_libdir}/libsass.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains the static libraries, headers, and other
support files required for developing applications against %{name}.

%files -n %{devname}
%{_includedir}/sass.h
%{_includedir}/sass2scss.h
%dir %{_includedir}/sass/
%{_includedir}/sass/*.h
%{_libdir}/libsass.so
%{_libdir}/pkgconfig/libsass.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1
export LIBSASS_VERSION=%{version}
autoreconf --force --install

%build
%configure
%make_build

%install
%make_install
