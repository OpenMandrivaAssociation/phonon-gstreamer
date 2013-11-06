Summary:	GStreamer backend to Phonon
Name:		phonon-gstreamer
Version:	4.7.0
Release:	1
Epoch:		2
License:	LGPLv2+
Group:		Sound
Url:		http://phonon.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-gstreamer/%{version}/src/phonon-backend-gstreamer-%{version}.tar.xz
Patch0:		phonon-4.4.3-flac_mimetype.patch
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(phonon)
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-base
Suggests:	gstreamer0.10-plugins-bad
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

