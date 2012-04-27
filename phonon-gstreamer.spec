Name:		phonon-gstreamer
Summary:	GStreamer backend to Phonon
Group:		Sound
Version:	4.6.0
Release:	1
Epoch:		2
URL:		http://phonon.kde.org/
License:	LGPLv2+
Source0:	ftp://ftp.kde.org/pub/kde/unstable/phonon/phonon-backend-gstreamer/4.5.90/src/phonon-backend-gstreamer-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: libgstreamer-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: imagemagick
BuildRequires: phonon-devel >= 2:4.5.0
BuildRequires: automoc4
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-plugins-base
Suggests: gstreamer0.10-ffmpeg
Suggests: gstreamer0.10-soup
Suggests: gstreamer0.10-pulse
%if %mdkversion >= 201000
Obsoletes: arts < 30000001:1.5.10-9
Obsoletes: arts3 < 30000001:1.5.10-9
%endif
Provides: phonon-backend

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
rm -fr %buildroot
%makeinstall_std -C build

# Make a nice icon
for size in 16 22 32 48 64 128; do
  mkdir -p %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps
  convert -geometry ${size}x${size} %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svgz %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
done
