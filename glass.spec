Summary:	GLASS - openGL Articulated Structure System
Summary(pl):	GLASS - Biblioteka obs≥ugi struktur 3D OpenGL
Name:		glass
Version:	1.1.3
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Vendor:		Robert Cleaver Ancell <bob27@users.sourceforge.net>
URL:		http://glass.sourceforge.net
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-version.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLASS is a 3D library, designed to make easy use of structured models
(models, that are made up of components linked by basic transforms,for
example, rotations and translations) in open GL applications. By using
GLASS in an application, these models can be loaded, modified, and
displayed using a minimum of function calls.

%description -l pl
GLASS to biblioteka wspomagaj±ca projektowanie aplikacji 3D, stworzona
aby upro∂ciÊ uøycie modelu strukturalnego (modele, ktÛre sk≥adaj± siÍ
z po≥±czonych prostymi transformacjami czÍ∂ci, np. obrotÛw lub
przesuniÍÊ) w aplikacjach 3D OpenGL. GLASS pozwala za≥adowaÊ,
zmodyfikowaÊ i wy∂wietlaÊ te obiekty przy uøyciu minimalnej ilo∂ci
wywo≥aÒ (co upraszcza kod).

%prep
%setup -q
%patch -p1

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/local/include
install -d $RPM_BUILD_ROOT%{_libdir}
cp -f src/glass.h src/glass_types.h $RPM_BUILD_ROOT%{_prefix}/local/include
rm -f $RPM_BUILD_ROOT%{_libdir}/libglass.* 
cp -f libglass.so.* $RPM_BUILD_ROOT%{_libdir}

%post
echo Rejestrowanie bibliotek...
ln -fs /usr/lib/libglass.so.1 /usr/lib/libglass.so 
/sbin/ldconfig
echo Pliki nag≥Ûwkowe znajduj± siÍ w /usr/local/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING TODO
%{_prefix}/local/include/*
%{_libdir}/*
