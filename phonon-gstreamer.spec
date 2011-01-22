Name: phonon-gstreamer
Summary: GStreamer backend to Phonon
Version: 4.4.4
Release: %mkrel 1
Epoch: 2
Url: http://phonon.kde.org/
License: LGPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-gstreamer/%version/phonon-backend-gstreamer-%version.tar.bz2
Source1: %{name}.svg
Patch2: phonon-gstreamer-4.4.4-fix-seekable-query-failed.patch
Patch5: phonon-gstreamer-4.4.4-use-decodebin.patch
BuildRequires: libgstreamer-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: imagemagick
BuildRequires: phonon-devel >= 2:4.4.4
BuildRequires: kde4-macros
BuildRequires: automoc4
Requires: gstreamer0.10-plugins-good
Requires: gstreamer0.10-plugins-base
Suggests: gstreamer0.10-ffmpeg
Suggests: gstreamer0.10-soup
Suggests: gstreamer0.10-pulse
%if %mdkversion >= 201000
Obsoletes:      arts < 30000001:1.5.10-9
Obsoletes:      arts3 < 30000001:1.5.10-9
%endif
Provides: phonon-backend

%description
GStreamer backend to Phonon.

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plugins/phonon_backend/phonon_gstreamer.so
%_kde_datadir/kde4/services/phononbackends/gstreamer.desktop
%_datadir/icons/hicolor/*

#--------------------------------------------------------------------

%prep
%setup -qn phonon-backend-gstreamer-%version
%apply_patches

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

# Make a nice icon
install -D -m 0644 %{_sourcedir}/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
for size in 16 22 32 48 64 128; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
  convert -geometry ${size}x${size} %{_sourcedir}/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%clean
rm -rf "%{buildroot}"
