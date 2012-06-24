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
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
GLASS header files.

%description devel -l pl
Pliki nag��wkowe biblioteki GLASS.

%prep
%setup -q
%patch -p1

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

install src/glass.h src/glass_types.h $RPM_BUILD_ROOT%{_includedir}
install libglass.so* $RPM_BUILD_ROOT%{_libdir}

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz TODO.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*
