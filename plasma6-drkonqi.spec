%define git 20230707

Name: plasma6-drkonqi
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/plasma/drkonqi/-/archive/master/drkonqi-master.tar.bz2#/drkonqi-%{git}.tar.bz2
Summary: Crash handler for KDE software
URL: https://invent.kde.org/plasma/drkonqi
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KUserFeedbackQt6)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: systemd
# Avoid pulling in Plasma5
BuildRequires: plasma6-xdg-desktop-portal-kde

%description
Crash handler for KDE software

%prep
%autosetup -p1 -n drkonqi-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/drkonqi.*
%{_bindir}/drkonqi-coredump-gui
%{_prefix}/lib/systemd/system/drkonqi-coredump-processor@.service
%{_prefix}/lib/systemd/user/drkonqi-coredump-cleanup.service
%{_prefix}/lib/systemd/user/drkonqi-coredump-cleanup.timer
%{_prefix}/lib/systemd/user/drkonqi-coredump-launcher.socket
%{_prefix}/lib/systemd/user/drkonqi-coredump-launcher@.service
%{_libdir}/libexec/drkonqi
%{_libdir}/libexec/drkonqi-coredump-cleanup
%{_libdir}/libexec/drkonqi-coredump-launcher
%{_libdir}/libexec/drkonqi-coredump-processor
%{_qtdir}/plugins/drkonqi
%{_datadir}/applications/org.kde.drkonqi.coredump.gui.desktop
%{_datadir}/applications/org.kde.drkonqi.desktop
%{_datadir}/drkonqi
