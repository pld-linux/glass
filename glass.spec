Summary:	GLASS - openGL Articulated Structure System
Summary(pl):	GLASS - Biblioteka obs³ugi struktur 3D OpenGL
Name:		glass
Version:	1.1.3
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Vendor:		Robert Cleaver Ancell <bob27@users.sourceforge.net>
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-version.patch
Patch1:		%{name}-examples-CFLAGS_for_glut.patch
Patch2:		%{name}-LIBS.patch
BuildRequires:	OpenGL-devel
Requires:	OpenGL
URL:		http://glass.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GLASS is a 3D library, designed to make easy use of structured models
(models, that are made up of components linked by basic transforms,for
example, rotations and translations) in open GL applications. By using
GLASS in an application, these models can be loaded, modified, and
displayed using a minimum of function calls.

%description -l pl
GLASS to biblioteka wspomagaj±ca projektowanie aplikacji 3D, stworzona
aby upro¶ciæ u¿ycie modelu strukturalnego (modele, które sk³adaj± siê
z po³±czonych prostymi transformacjami czê¶ci, np. obrotów lub
przesuniêæ) w aplikacjach 3D OpenGL. GLASS pozwala za³adowaæ,
zmodyfikowaæ i wy¶wietlaæ te obiekty przy u¿yciu minimalnej ilo¶ci
wywo³añ (co upraszcza kod).

%package devel
Summary:	GLASS development package
Summary(pl):	Pakiet dla programistów GLASS
Group:		Development/Building
Group(de):	Entwicklung/Bauen
Group(pl):	Programowanie/Budowanie
Requires:	%{name} = %{version}

%description devel
GLASS header files. Contains also tutorial and specifications.

%description devel -l pl
Pliki nag³ówkowe biblioteki GLASS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} all \
	CFLAGS="%{rpmcflags} -fPIC -I/usr/X11R6/include -DVERSION_STRING=\"\\\"%{version}\"\\\"" \
	LIBS="-L/usr/X11R6/lib -lGL" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_examplesdir}/%{name}}

install src/glass.h src/glass_types.h $RPM_BUILD_ROOT%{_includedir}
install libglass.so* $RPM_BUILD_ROOT%{_libdir}

ln -s libglass.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libglass.so
cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz TODO.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/* ChangeLog.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_examplesdir}/%{name}
