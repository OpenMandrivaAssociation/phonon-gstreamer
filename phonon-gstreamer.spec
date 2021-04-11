%bcond_with qt4

Summary:	GStreamer backend to Phonon (Qt4)
Name:		phonon-gstreamer
Version:	4.10.0
Release:	4
License:	LGPLv2.1+
Group:		Sound
Url:		http://phonon.kde.org/
Source0:	http://download.kde.org/stable/phonon/phonon-backend-gstreamer/%{version}/phonon-backend-gstreamer-%{version}.tar.xz
%if %{with qt4}
BuildRequires:	automoc4
BuildRequires:	pkgconfig(phonon)
%endif
BuildRequires:	imagemagick
BuildRequires:	qmake5
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-audio-1.0)
# Not in gst 1.0 yet, at least not in 1.2.4
#BuildRequires:	pkgconfig(gstreamer-cdda-1.0})
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-riff-1.0)
BuildRequires:	pkgconfig(gstreamer-rtp-1.0)
BuildRequires:	pkgconfig(gstreamer-rtsp-1.0)
BuildRequires:	pkgconfig(gstreamer-sdp-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
Requires:	phonon-gstreamer-common
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-pulse
%ifnarch %{arm}
# ARM doesn't have -plugins-bad yet due to
# unexplained build failure
Requires:	gstreamer1.0-plugins-bad
%endif
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-soup
Suggests:	gstreamer1.0-ffmpeg
Provides:	phonon-backend

%description
GStreamer backend to Phonon (Qt4).

%if %{with qt4}
%files
%{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%endif

#----------------------------------------------------------------------------

%package common
Summary:	Files used by both Qt4 and Qt5 versions of Phonon GStreamer backend
Group:		Sound
Conflicts:	phonon-gstreamer < 2:4.8.2-3
# For gst-plugin-scanner
Requires:	gstreamer-tools

%description common
Files used by both Qt4 and Qt5 versions of Phonon GStreamer backend.

%files common
%{_iconsdir}/hicolor/*/apps/phonon-gstreamer.*

#----------------------------------------------------------------------------

%package -n phonon4qt5-gstreamer
Summary:	GStreamer backend to Phonon (Qt5)
Group:		Sound
Requires:	phonon-gstreamer-common
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-pulse
%ifnarch %{arm}
# ARM doesn't have -plugins-bad yet due to
# unexplained build failure
Requires:	gstreamer1.0-plugins-bad
%endif
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-soup
Suggests:	gstreamer1.0-ffmpeg
Provides:	phonon4qt5-backend

%description -n phonon4qt5-gstreamer
GStreamer backend to Phonon (Qt5).

%files -n phonon4qt5-gstreamer -f %{name}.lang
%{_qt5_plugindir}/phonon4qt5_backend/phonon_gstreamer.so

#----------------------------------------------------------------------------

%prep
%setup -qn phonon-backend-gstreamer-%{version}
%autopatch -p1

%if %{with qt4}
mkdir Qt4
mv `ls -1 |grep -v Qt4` Qt4
cp -a Qt4 Qt5
%endif

%build
%if %{with qt4}
pushd Qt4
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
    -DUSE_INSTALL_PLUGIN:BOOL=ON \
    -DPHONON_BUILD_PHONON4QT5:BOOL=OFF

%make
popd

pushd Qt5
%endif
%cmake_kde5 -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DUSE_INSTALL_PLUGIN:BOOL=ON \
	-DPHONON_BUILD_PHONON4QT5:BOOL=ON \
	-G Ninja

%ninja_build

%install
%if %{with qt4}
%makeinstall_std -C Qt4/build

%makeinstall_std -C Qt5/build
%else
%ninja_install -C build
%endif

find %{buildroot}%{_datadir}/locale -name "*.qm" |while read r; do
	L=`echo $r |rev |cut -d/ -f3 |rev`
	echo "%%lang($L) %%{_datadir}/locale/$L/LC_MESSAGES/*.qm" >>%{name}.lang
done
