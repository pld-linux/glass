Summary: 	GLASS - openGL Articulated Structure System
Name: 		glass
Version: 	1.1.3
Release: 	1
License: 	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Vendor:		Robert Cleaver Ancell <bob27@users.sourceforge.net>
URL: 		http://glass.sourceforge.net
Source: 	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch:		glass-version.patch
BuildRoot: 	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLASS is a 3D library, designed to make easy use of structured models (models,
that are made up of components linked by basic transforms,for example, rotations
and translations) in open GL applications. By using GLASS in an application,
these models can be loaded, modified, and displayed using a minimum of function 
calls.

%prep
%setup -q
%patch -p1

%build
make all

%install
#$RPM_BUILD_ROOT/usr/local/lib
#$RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
cp -f src/glass.h src/glass_types.h $RPM_BUILD_ROOT/usr/local/include
rm -f $RPM_BUILD_ROOT/usr/local/lib/libglass.* 
cp -f libglass.so.* $RPM_BUILD_ROOT/usr/local/lib

%post
ln -fs /usr/local/lib/libglass.so.1 /usr/local/lib/libglass.so 
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README COPYING TODO
/usr/local/include/*
/usr/local/lib/*
