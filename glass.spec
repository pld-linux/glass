Summary:	GLASS - openGL Articulated Structure System
Summary(pl):	GLASS - Biblioteka obs�ugi struktur 3D OpenGL
Name:		glass
Version:	1.3.1
Release:	2
License:	GPL
Group:		X11/Libraries
Vendor:		Robert Cleaver Ancell <bob27@users.sourceforge.net>
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bcde18e3ce0bebb19cf888d652f8b425
Patch0:		%{name}-LIBS.patch
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	OpenGL-devel
Requires:	OpenGL
URL:		http://glass.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GLASS is a 3D library, designed to make easy use of structured models
(models, that are made up of components linked by basic transforms,for
example, rotations and translations) in open GL applications. By using
GLASS in an application, these models can be loaded, modified, and
displayed using a minimum of function calls.

%description -l pl
GLASS to biblioteka wspomagaj�ca projektowanie aplikacji 3D, stworzona
aby upro�ci� u�ycie modelu strukturalnego (modele, kt�re sk�adaj� si�
z po��czonych prostymi transformacjami cz�ci, np. obrot�w lub
przesuni��) w aplikacjach 3D OpenGL. GLASS pozwala za�adowa�,
zmodyfikowa� i wy�wietla� te obiekty przy u�yciu minimalnej ilo�ci
wywo�a� (co upraszcza kod).

%package devel
Summary:	GLASS development package
Summary(pl):	Pakiet dla programist�w GLASS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
GLASS header files. Contains also tutorial and specifications.

%description devel -l pl
Pliki nag��wkowe biblioteki GLASS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -I/usr/X11R6/include -DVERSION_STRING=\"\\\"%{version}\"\\\"" \
	LIBS="-L/usr/X11R6/%{_lib} -lGL"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INCLUDEDIR=%{_includedir}/glass \
	LIBDIR=%{_libdir}

cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/glass
%{_examplesdir}/%{name}-%{version}
