Summary:	GLASS - openGL Articulated Structure System
Summary(pl):	GLASS - Biblioteka obs�ugi struktur 3D OpenGL
Name:		glass
Version:	1.1.3
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Vendor:		Robert Cleaver Ancell <bob27@users.sourceforge.net>
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-version.patch
Patch1:		%{name}-examples-CFLAGS_for_glut.patch
URL:		http://glass.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Group:		Development/Building
Group(de):	Entwicklung/Bauen
Group(pl):	Programowanie/Budowanie
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
	CFLAGS="%{rpmcflags} -fPIC -I/usr/X11R6/include -DVERSION_STRING=\"%{version}\"" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_exampledir}/%{name}}

install src/glass.h src/glass_types.h $RPM_BUILD_ROOT%{_includedir}
install libglass.so* $RPM_BUILD_ROOT%{_libdir}

ln -s libglass.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libglass.so
cp -ar examples/* $RPM_BUILD_ROOT%{_exampledir}/%{name}

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
