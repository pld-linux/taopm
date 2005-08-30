Summary:	Tao is a synthesizer for modelling sounds with physical simulations
Name:		taopm
Version:	1.0beta
%define snap 20050827
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/taopm/tao-1.0-beta-27Aug2005.tar.gz
# Source0-md5:	fc9e13cd59407fe05dfdbd56630529b1
URL:		http://taopm.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tao is a software package for sound synthesis using physical models.
It provides a virtual acoustic material constructed from masses and
springs which can be used as the basis for building quite complex
virtual musical instruments. Tao comes with a synthesis language for
creating and playing instruments and a fully documented (eventually)
C++ API for those who would like to use it as an object library.

%package devel
Summary:	Development libraries and header files for tao library
Group:		Development/Libraries

%description devel
This is the package containing the development libraries and header
files for tao

%package static
Summary:	Static tao library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tao library.

%prep
%setup -q -n tao-1.0-beta-27Aug2005

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/tao
%attr(755,root,root) %{_bindir}/tao2*
%attr(755,root,root) %{_bindir}/taoparse
%attr(755,root,root) %{_libdir}/libtao.so.0.0.0
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tao-config
%{_libdir}/libtao.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libtao.a
