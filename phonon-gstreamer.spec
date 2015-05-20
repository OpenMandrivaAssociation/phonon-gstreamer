Summary:	GStreamer backend to Phonon
Name:		phonon-gstreamer
Version:	4.8.2
Release:	0.1
Epoch:		2
License:	LGPLv2+
Group:		Sound
Url:		http://phonon.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-gstreamer/%{version}/phonon-backend-gstreamer-%{version}.tar.xz
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(phonon)
# Yes, really...
# The bit we need is the qt5_use_modules cmake macro.
BuildRequires:	pkgconfig(Qt5Core)
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-base
Suggests:	gstreamer1.0-plugins-bad
Suggests:	gstreamer1.0-plugins-ugly
Suggests:	gstreamer1.0-libav
Suggests:	gstreamer1.0-soup
Requires:	gstreamer1.0-pulse
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

