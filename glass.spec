Summary:	GLASS - openGL Articulated Structure System
Summary(pl.UTF-8):	GLASS - Biblioteka obsługi struktur 3D OpenGL
Name:		glass
Version:	1.3.1
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/glass/%{name}-%{version}.tar.gz
# Source0-md5:	bcde18e3ce0bebb19cf888d652f8b425
Patch0:		%{name}-LIBS.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://glass.sourceforge.net/
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GLASS is a 3D library, designed to make easy use of structured models
(models, that are made up of components linked by basic transforms,for
example, rotations and translations) in open GL applications. By using
GLASS in an application, these models can be loaded, modified, and
displayed using a minimum of function calls.

%description -l pl.UTF-8
GLASS to biblioteka wspomagająca projektowanie aplikacji 3D, stworzona
aby uprościć użycie modelu strukturalnego (modele, które składają się
z połączonych prostymi transformacjami części, np. obrotów lub
przesunięć) w aplikacjach 3D OpenGL. GLASS pozwala załadować,
zmodyfikować i wyświetlać te obiekty przy użyciu minimalnej ilości
wywołań (co upraszcza kod).

%package devel
Summary:	GLASS development package
Summary(pl.UTF-8):	Pakiet dla programistów GLASS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
GLASS header files. Contains also tutorial and specifications.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GLASS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

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

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libglass.so.*.*.* libglass.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libglass.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglass.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/*.html
%attr(755,root,root) %{_libdir}/libglass.so
%{_includedir}/glass
%{_examplesdir}/%{name}-%{version}
