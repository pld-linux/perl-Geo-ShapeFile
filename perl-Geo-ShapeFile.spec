#
# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%define		pdir	Geo
%define		pnam	ShapeFile
%include	/usr/lib/rpm/macros.perl
Summary:	Geo::ShapeFile - Perl extension for handling ESRI GIS Shapefiles
Summary(pl.UTF-8):	Geo::ShapeFile - rozszerzenie Perla do obsługi plików w formacie ESRI Shapefile
Name:		perl-Geo-ShapeFile
Version:	2.60
Release:	1
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Geo/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25a95e2b9644b78a8d0810d1a5d3b13b
URL:		http://search.cpan.org/dist/Geo-ShapeFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(rlib)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Geo::ShapeFile module reads ESRI ShapeFiles containing GIS
mapping data, it has support for shp (shape), shx (shape index),
and dbf (data base) formats.

%description -l pl.UTF-8
Moduł Geo::ShapeFile czyta pliki w formacie ESRI ShapeFile
zawierające dane GIS. Rozpoznaje pliki shp (kształty),
shx (indeksy) i dbf (dane atrybutów).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Geo/*.pm
%{perl_vendorlib}/Geo/ShapeFile
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
