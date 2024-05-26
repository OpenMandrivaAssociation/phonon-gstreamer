%bcond_without qt5
%bcond_without qt6

Summary:	GStreamer backend to Phonon (Qt5 and Qt6)
Name:		phonon-gstreamer
Version:	4.10.0
Release:	8
License:	LGPLv2.1+
Group:		Sound
Url:		https://phonon.kde.org/
Source0:	phonon-gstreamer-%{version}.tar.xz
#Source0:	https://download.kde.org/stable/phonon/phonon-backend-gstreamer/%{version}/phonon-backend-gstreamer-%{version}.tar.xz
# Port it to Qt6. Patch from https://aur.archlinux.org/cgit/aur.git/tree/qt6_build_patch.patch?h=phonon-qt6-gstreamer-git
Patch0:		port-to-qt6.patch

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
%if %{with qt5}
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5X11Extras)
%endif
%if %{with qt6}
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6XcbQpaPrivate)
BuildRequires:  cmake(Phonon4Qt6)
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	pkgconfig(xcb-cursor)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xkbcommon-x11)

Requires:	phonon-gstreamer-common
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-pulse
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-soup

%description
GStreamer backend to Phonon (Qt6 and Qt5).

#----------------------------------------------------------------------------

%package common
Summary:	Files used by both Qt6 and Qt5 versions of Phonon GStreamer backend
Group:		Sound
Conflicts:	phonon-gstreamer < 2:4.8.2-3
# For gst-plugin-scanner
Requires:	gstreamer-tools

%description common
Files used by both Qt6 and Qt5 versions of Phonon GStreamer backend.

%files common -f %{name}.lang
%{_iconsdir}/hicolor/*/apps/phonon-gstreamer.*

#----------------------------------------------------------------------------
%if %{with qt5}
%package -n phonon4qt5-gstreamer
Summary:	GStreamer backend to Phonon (Qt5)
Group:		Sound
Requires:	phonon-gstreamer-common
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-pulse
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-soup
Provides:	phonon4qt5-backend
Provides:	phonon-backend

%description -n phonon4qt5-gstreamer
GStreamer backend to Phonon (Qt5).

%files -n phonon4qt5-gstreamer
%{_libdir}/plugins/phonon4qt5_backend/phonon_gstreamer.so
%endif
#----------------------------------------------------------------------------
%if %{with qt6}
%package -n phonon4qt6-gstreamer
Summary:	GStreamer backend to Phonon (Qt6)
Group:		Sound
Requires:	phonon-gstreamer-common
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-pulse
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-soup
Provides:	phonon4qt6-backend
Provides:	phonon-backend

%description -n phonon4qt6-gstreamer
GStreamer backend to Phonon (Qt6).

%files -n phonon4qt6-gstreamer
%{_libdir}/plugins/phonon4qt6_backend/phonon_gstreamer.so
%endif
#----------------------------------------------------------------------------

%prep
%autosetup -n phonon-gstreamer-%{version} -p1

%build
%if %{with qt5}
export CMAKE_BUILD_DIR=build-qt5
%cmake_qt5 -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DUSE_INSTALL_PLUGIN:BOOL=ON \
	-DPHONON_BUILD_PHONON4QT5:BOOL=ON
%make_build
cd .. 
%endif
%if %{with qt6}
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
    	-DUSE_INSTALL_PLUGIN:BOOL=ON \
    	-DPHONON_BUILD_PHONON4QT5:BOOL=OFF \
     	-DQT_MAJOR_VERSION=6 

%make_build
cd ..
%endif

%install
%if %{with qt5}
%make_install -C build
%endif
%if %{with qt6}
%make_install -C build-qt6
%endif

find %{buildroot}%{_datadir}/locale -name "*.qm" |while read r; do
	L=`echo $r |rev |cut -d/ -f3 |rev`
	echo "%%lang($L) %%{_datadir}/locale/$L/LC_MESSAGES/*.qm" >>%{name}.lang
done
