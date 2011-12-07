Summary:        Libraries for the Matchbox Desktop
Name:           libmatchbox 
Version:        1.9
Release:        6.1%{?dist}
Url:            http://projects.o-hand.com/matchbox/
License:        LGPLv2+
Group:          Development/Libraries 
Source:         http://projects.o-hand.com/matchbox/sources/libmatchbox/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  pango-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package devel
Group:          Development/C
Summary:        Static libraries and header files from %{name}
Provides:       matchbox-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       libmb-devel = %{version}-%{release}
Requires:       libmatchbox = %{version}
Requires:       pkgconfig

%description devel
Static libraries and header files from %{name}

%prep
%setup -q

%build
%configure --enable-png --enable-jpeg --enable-pango
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root, -)
%_libdir/*.so.*

%files devel
%defattr(-,root,root, -)
%doc AUTHORS ChangeLog README COPYING
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%dir %{_includedir}/libmb
%{_includedir}/libmb/*.h

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.9-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.9-4
- fix license tag

* Tue Jun 19 2007 John (J5) Palmieri <johnp@redhat.com> 1.9-3
- Fixed License to be LGPL
- Add COPYING license file to docs
- Fixed Group
- Fixed buildroot
- Added {} braces around % macros
- Removed .la and .a files 
- Own {_includedir}/libmb directory
- Add dist tag to release
- Add smpflags  flag to make
- Remove use of boken makeinstall macro
 
* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.9-2
- Disable xsettings

* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.9-1
- Update to 1.9

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 1.7-1mdk
- New release 1.7
- fix URLs

* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 1.6-1mdk
- 1.6

* Tue Jan 4 2005 Austin Acton <austin@mandrake.org> 1.5-1mdk
- 1.5

* Wed Sep 29 2004 Austin Acton <austin@mandrake.org> 1.4-1mdk
- 1.4

* Mon Aug 23 2004 Austin Acton <austin@mandrake.org> 1.3-1mdk
- 1.3

* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 1.2-1mdk
- initial package
