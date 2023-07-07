#
# Spec file for package kwinft
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

# Internal QML imports
%global __requires_exclude qmlimport\\((org\\.kde\\.private\\.kcms\\.kwin\\.effects|org\\.kde\\.kcms\\.kwinrules|org\\.kde\\.kwin\\.private\\.overview|org\\.kde.kwin\\.private\\.desktopgrid|org\\.kde\\.KWin\\.Effect\\.WindowView|org\\.kde\\.kwin\\.kwinxwaylandsettings).*

%global commit 582c5517cdda771e6823402a31e65d476b361924
%global min_qt_version 5.15.0
%global min_kf_version 5.102.0
#%%bcond_without  lang

Name:           kwinft
Version:        5.27.6
Release:        1
Summary:        Fast Track reboot of KWin
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://gitlab.com/kwinft/%{name}
Source:         %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
#Patch0:         path.patch
# PATCH-FIX-OPENSUSE
#Patch1:         0001-Use-fixed-absolute-path-instead-of-usr-bin-env-in-sh.patch
# Patch2:         qt6.patch
#Patch3:         compilar.patch
#Patch4:         272.diff
#Patch5:         firefox.patch
#Patch6:         qml.patch
#Patch8:         revertir.patch
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  fdupes
BuildRequires:  hwdata
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  ffmpeg-6-libavcodec-devel
BuildRequires:  ffmpeg-6-libavformat-devel
BuildRequires:  ffmpeg-6-libavfilter-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  libepoxy-devel
BuildRequires:  libva-devel
BuildRequires:  polkit-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(Wrapland)
BuildRequires:  cmake(Breeze) >= 5.9.0
BuildRequires:  cmake(KDecoration2) >= %{version}
BuildRequires:  cmake(KF5Activities) >= %{min_kf_version}
BuildRequires:  cmake(KF5Completion) >= %{min_kf_version}
BuildRequires:  cmake(KF5Archive) >= %{min_kf_version}
BuildRequires:  cmake(KF5Auth) >= %{min_kf_version}
BuildRequires:  cmake(KF5Config) >= %{min_kf_version}
BuildRequires:  cmake(KF5Codecs) >= %{min_kf_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{min_kf_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{min_kf_version}
BuildRequires:  cmake(KF5Crash) >= %{min_kf_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{min_kf_version}
BuildRequires:  cmake(KF5Declarative) >= %{min_kf_version}
BuildRequires:  cmake(KF5DocTools) >= %{min_kf_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{min_kf_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{min_kf_version}
BuildRequires:  cmake(KF5I18n) >= %{min_kf_version}
BuildRequires:  cmake(KF5IconThemes) >= %{min_kf_version}
BuildRequires:  cmake(KF5IdleTime) >= %{min_kf_version}
#BuildRequires:  cmake(KF5Init) >= %%{min_kf_version}
BuildRequires:  cmake(KF5ItemModels) >= %{min_kf_version}
BuildRequires:  cmake(KF5FrameworkIntegration) >= %{min_kf_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{min_kf_version}
BuildRequires:  cmake(KF5KIO) >= %{min_kf_version}
BuildRequires:  cmake(KF5NewStuff) >= %{min_kf_version}
BuildRequires:  cmake(KF5Notifications) >= %{min_kf_version}
BuildRequires:  cmake(KF5Package) >= %{min_kf_version}
BuildRequires:  cmake(KPipeWire) >= %{version}
BuildRequires:  cmake(KF5Plasma) >= %{min_kf_version}
BuildRequires:  cmake(KF5PlasmaQuick) >= %{min_kf_version}
BuildRequires:  cmake(KF5Runner) >= %{min_kf_version}
BuildRequires:  cmake(KF5Screen) >= %{version}
BuildRequires:  cmake(KF5Service) >= %{min_kf_version}
BuildRequires:  cmake(KF5Syndication) >= %{min_kf_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{min_kf_version}
BuildRequires:  cmake(KF5ThreadWeaver) >= %{min_kf_version}
BuildRequires:  cmake(KF5Wallet) >= %{min_kf_version}
BuildRequires:  cmake(KF5Wayland) >= %{min_kf_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{min_kf_version}
#BuildRequires:  cmake(KF5WindowSystem) >= %%{min_kf_version}
BuildRequires:  cmake(KF5XmlGui) >= %{min_kf_version}
BuildRequires:  cmake(KScreenLocker)
BuildRequires:  cmake(PlasmaWaylandProtocols)
#BuildRequires:  cmake(KF5ItemViews) >= %%{min_kf_version}
# The following RUNTIME packages have not been found:
BuildRequires:  cmake(KF5Kirigami2) >= %{min_kf_version}
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5LinguistTools)
# RUNTIME packages have not been found:
BuildRequires:  cmake(KScreenLocker)
BuildRequires:  cmake(QAccessibilityClient)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= %{min_qt_version}
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Sensors)
BuildRequires:  cmake(Qt5Sensors)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(PolkitQt5-1)
#
BuildRequires:  cmake(Qt5FontDatabaseSupport)
BuildRequires:  cmake(Qt5ThemeSupport)
BuildRequires:  cmake(Qt5EventDispatcherSupport)
#
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) >= 1.10
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-glx) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
#%%if %%{wayland}
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(wlroots) >= 0.17.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm) >= 2.4.62
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libgcrypt)
# Don't use pkgconfig here as that would cause unresolvables on 0.1 -> 0.2 -> 0.3 bumps
BuildRequires:  pipewire-devel
# xorg-x11-server-wayland is required by plasma5-session-wayland and kwin5 can run with just X11
Recommends:     xorg-x11-server-wayland
#%%endif
# new default decoration
Requires:       breeze5-decoration >= 5.23.0
#kwinft
Requires:       kdisplay
Requires:       disman-plugin
# Requires:       kdisplay-plasmoid
# Needed to show dialogs
Requires:       kdialog
# Needed for effects KCM at runtime
#Requires:       libQt5Multimedia5
# Needed for the virtual desktop KCM
Requires:       kirigami2
Requires:       kitemmodels-imports
%requires_eq    libQt5Core5 
%requires_eq    libQt5Gui5
Provides:       windowmanager
# For post and verifyscript
Requires(post): permissions
Requires(verify): permissions
%requires_ge Mesa-libEGL1
%requires_ge libKF5WindowSystem5
%requires_ge plasma-framework
# For displaying full monitor vendor names
#Requires:       hwdata
Provides:       qt5qmlimport(org.kde.kwin.2) = 0
Provides:       qt5qmlimport(org.kde.kwin.3) = 0
# We can reuse kwin5’s localization and doc files
Recommends:     kwin5-doc
Recommends:     kwin5-lang
Provides:       kwin5
Conflicts:      kwin5
Conflicts:      kwin-lowlatency
Conflicts:      disman-plugin-kwinft

%description
KWinFT (KWin Fast Track) is an easy to use, but flexible, composited window manager for X.Org
windowing systems (Wayland, X11) on Linux.
The KWinFT project consists of the window manager KWinFT and the accompanying but
independent libwayland wrapping Qt/C++ library Wrapland.

%package devel
Summary:        KWinFT: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= %{min_qt_version}
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       libepoxy-devel
Requires:       libkdecoration2-devel >= %{version}
Conflicts:      kdebase4-workspace-devel

%description devel
KWinFT (KWin Fast Track) is an easy to use, but flexible, composited window manager for X.Org
windowing systems (Wayland, X11) on Linux.
The KWinFT project consists of the window manager KWinFT and the accompanying but
independent libwayland wrapping Qt/C++ library Wrapland.

%prep
  %autosetup -p1 -n %{name}-%{commit}

%build
#fix fatal error: wayland-server.h: No such file or directory
#export CFLAGS="%%{optflags} -I%%{_includedir} -I%%{_includedir}/wayland"
#export CXXFLAGS="${CFLAGS}"
  %cmake_kf5 -d build
  %cmake_build

%install
%kf5_makeinstall -C build

sed -i 's#/usr/bin/env python[3]\?#/usr/bin/python3#' %{buildroot}%{_kf5_sharedir}/kconf_update/*.py

%fdupes %{buildroot}%{_kf5_libdir}
%fdupes %{buildroot}%{_datadir}

# Just use upstream KWin's help files and translations
rm -rf %{buildroot}%{_kf5_sharedir}/doc
rm -rf %{buildroot}%{_kf5_sharedir}/locale

%preun
%systemd_user_preun plasma-kwin_x11.service
%systemd_user_preun plasma-kwin_wayland.service

%post
/sbin/ldconfig
%set_permissions %{_kf5_bindir}/kwin_wayland
%systemd_user_post plasma-kwin_x11.service
%systemd_user_post plasma-kwin_wayland.service

%postun
/sbin/ldconfig
%systemd_user_postun plasma-kwin_x11.service
%systemd_user_postun plasma-kwin_wayland.service

%verifyscript
%verify_permissions -e %{_kf5_bindir}/kwin_wayland

%files
%license LICENSE*
%verify(not caps) %{_kf5_bindir}/kwin_wayland
%{_kf5_bindir}/kwin_wayland_wrapper
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/kwin_x11
%{_kf5_debugdir}/org_kde_kwin.categories
%{_kf5_knsrcfilesdir}/*.knsrc

%{_kf5_libdir}/kconf_update_bin/
%{_kf5_libdir}/libkwin*.so.*
%{_kf5_libdir}/libkcmkwincommon.*

%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/
%{_kf5_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%dir %{_kf5_plugindir}/kpackage/
%dir %{_kf5_plugindir}/kpackage/packagestructure/
%{_kf5_plugindir}/kpackage/packagestructure/kwin_aurorae.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_decoration.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_effect.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_script.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_windowswitcher.so
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_sharedir}/kpackage/kcms/kcm_kwin_scripts/
%dir %{_kf5_plugindir}/kwin/
%dir %{_kf5_plugindir}/kwin/effects/
%dir %{_kf5_plugindir}/kwin/effects/configs/
%{_kf5_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_cube_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_cubeslide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_desktopgrid_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_invert_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_lookingglass_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_magnifier_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_resize_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_showpaint_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_zoom_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_overview_config.so
%dir %{_kf5_plugindir}/org.kde.kdecoration2/
%{_kf5_plugindir}/org.kde.kdecoration2/org.kde.kwin.aurorae.so
#%%{_kf5_plugindir}/org.kde.kdecoration2/kwin5_aurorae.so

%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/kwin/
%{_kf5_qmldir}/org/kde/kwin/decoration/
%{_kf5_qmldir}/org/kde/kwin/decorations/
%{_kf5_qmldir}/org/kde/kwin/private/
#%%{_kf5_qmldir}/org/kde/kwin.2/

%{_kf5_sharedir}/config.kcfg/
%{_kf5_sharedir}/icons/hicolor/*/apps/kwin.png
%{_kf5_sharedir}/icons/hicolor/scalable/apps/kwin.svgz
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/kwin/
%{_kf5_sharedir}/kconf_update/
%{_kf5_notifydir}/
%dir %{_kf5_sharedir}/kpackage/
%{_kf5_sharedir}/kpackage/kcms/kcm_kwin_virtualdesktops
%{_kf5_sharedir}/kpackage/kcms/kcm_kwindecoration
%{_kf5_sharedir}/kpackage/kcms/kcm_kwin_effects
%{_kf5_sharedir}/kpackage/kcms/kcm_kwinrules
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin_rules_dialog
%{_userunitdir}/plasma-kwin_x11.service
%{_userunitdir}/plasma-kwin_wayland.service

%files devel
# %%license LICENSE*
%{_kf5_prefix}/include/*.h
%{_kf5_libdir}/libkwin*.so
%{_kf5_libdir}/cmake/KWinDBusInterface/
%{_kf5_sharedir}/dbus-1/interfaces/
%{_prefix}/include/kwineffects/
%{_prefix}/include/kwingl/
%{_prefix}/include/kwinxrender/
%{_kf5_cmakedir}/KWinEffects/

%changelog 
