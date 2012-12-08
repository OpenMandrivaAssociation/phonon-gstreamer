Name:		phonon-gstreamer
Summary:	GStreamer backend to Phonon
Group:		Sound
Version:	4.6.2
Release:	1
Epoch:		2
URL:		http://phonon.kde.org/
License:	LGPLv2+
Source0:	ftp://ftp.kde.org/pub/kde/unstable/phonon/phonon-backend-gstreamer/4.5.90/src/phonon-backend-gstreamer-%{version}.tar.xz
Patch1:		phonon-4.4.3-flac_mimetype.patch
Patch2:		phonon-backend-gstreamer-4.6.0-snapshot.patch
Patch3:		phonon-backend-gstreamer-4.6.2-fix-multiple-drive.patch

BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	automoc4
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(phonon)
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-base
Suggests:	gstreamer0.10-plugins-ugly
Suggests:	gstreamer0.10-ffmpeg
Suggests:	gstreamer0.10-soup
Suggests:	gstreamer0.10-pulse
Provides:	phonon-backend

%description
GStreamer backend to Phonon.

%files
%{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_iconsdir}/*/*/*/*

#--------------------------------------------------------------------
%prep
%setup -qn phonon-backend-gstreamer-%{version}
%apply_patches

%build
%cmake
%make

%install
%makeinstall_std -C build


%changelog
* Fri Aug 17 2012 Crispin Boylan <crisb@mandriva.org> 2:4.6.2-1
+ Revision: 815186
- New release

* Fri Apr 27 2012 Crispin Boylan <crisb@mandriva.org> 2:4.6.0-1
+ Revision: 793992
- New release

* Tue Dec 27 2011 Zé <ze@mandriva.org> 2:4.5.90-1
+ Revision: 745801
- 4.5.90
- clean patch 2 and 5 (code changed upstream)

* Thu Dec 22 2011 Zé <ze@mandriva.org> 2:4.5.1-2
+ Revision: 744299
- clean defattr, BR, clean section and mkrel
- also here makes no sense to use kde4 macros since theres no need to change install path when kde changes version, its compatible
- needs cmake

* Thu May 12 2011 Funda Wang <fwang@mandriva.org> 2:4.5.1-1
+ Revision: 673715
- New versio 4.5.1
- rediff seekable patch

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version 4.5.0

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 2:4.4.4-3
+ Revision: 640303
- rebuild to obsolete old packages

* Sun Jan 23 2011 Funda Wang <fwang@mandriva.org> 2:4.4.4-2
+ Revision: 632409
- use upstream icon

* Sat Jan 22 2011 Funda Wang <fwang@mandriva.org> 2:4.4.4-1
+ Revision: 632278
- br automoc
- update icon name
- clean up spec file
- split out gstreamer backend
- Created package structure for phonon-gstreamer.

