%define oname plasma-sdk

Summary:	Plasma 5 SDK
Name:		plasma5-sdk
Version:	5.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{version}/%{oname}-%{version}.tar.xz
BuildRequires:	extra-cmake-modules
BuildRequires:	kf5archive-devel
BuildRequires:	kf5completion-devel
BuildRequires:	kf5config-devel
BuildRequires:	kf5configwidgets-devel
BuildRequires:	kf5coreaddons-devel
BuildRequires:	kf5declarative-devel
BuildRequires:	kf5i18n-devel
BuildRequires:	kf5iconthemes-devel
BuildRequires:	kf5kio-devel
BuildRequires:	kf5newstuff-devel
BuildRequires:	kf5parts-devel
BuildRequires:	kf5plasma-devel
BuildRequires:	kf5service-devel
BuildRequires:	kf5texteditor-devel
BuildRequires:	kf5widgetsaddons-devel
BuildRequires:	kf5windowsystem-devel
BuildRequires:	kf5xmlgui-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
Requires:	plasma5-cuttlefish
Requires:	plasma5-engineexplorer
Requires:	plasma5-plasmoidviewer
Requires:	plasma5-themeexplorer

%description
Plasma 5 SDK.

%files

#----------------------------------------------------------------------------

%package -n plasma5-cuttlefish
Summary:	Plasma 5 icon browser
Group:		Graphical desktop/KDE

%description -n plasma5-cuttlefish
Plasma 5 icon browser.

%files -n plasma5-cuttlefish -f cuttlefish.lang
%{_kde5_bindir}/cuttlefish
%dir %{_kde5_datadir}/plasma/packages/org.kde.plasma.cuttlefish/
%{_kde5_datadir}/plasma/packages/org.kde.plasma.cuttlefish/*
%{_kde5_services}/plasma-package-org.kde.plasma.cuttlefish.desktop
%{_qt5_plugindir}/ktexteditor/cuttlefishplugin.so

#----------------------------------------------------------------------------

%package -n plasma5-engineexplorer
Summary:	Plasma 5 engine explorer
Group:		Graphical desktop/KDE
Conflicts:	plasmate

%description -n plasma5-engineexplorer
Plasma 5 engine explorer. It's used to explore plasma data engines.

%files -n plasma5-engineexplorer -f plasmaengineexplorer.lang
%{_kde5_bindir}/plasmaengineexplorer

#----------------------------------------------------------------------------

%package -n plasma5-plasmoidviewer
Summary:	Plasma 5 plasmoid viewer
Group:		Graphical desktop/KDE
Requires:	plasma5-shell-plasmoidviewer
Conflicts:	plasmate

%description -n plasma5-plasmoidviewer
Plasma 5 plasmoid viewer. It's used to run plasmoids in their own window.

%files -n plasma5-plasmoidviewer -f plasmoidviewer.lang
%{_kde5_bindir}/plasmoidviewer

#----------------------------------------------------------------------------

%package -n plasma5-shell-plasmoidviewer
Summary:	Plasma 5 plasmoid viewer shell
Group:		Graphical desktop/KDE
# Not sure if it's required
Suggests:	plasma5-plasmoidviewer

%description -n plasma5-shell-plasmoidviewer
Plasma 5 plasmoid viewer shell.

%files -n plasma5-shell-plasmoidviewer
%dir %{_kde5_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/
%{_kde5_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/*
%{_kde5_services}/plasma-shell-org.kde.plasma.plasmoidviewershell.desktop

#----------------------------------------------------------------------------

%package -n plasma5-themeexplorer
Summary:	Plasma 5 theme explorer
Group:		Graphical desktop/KDE

%description -n plasma5-themeexplorer
Plasma 5 theme explorer. It's used to explore and edit plasma themes.

%files -n plasma5-themeexplorer -f themeexplorer.lang
%{_kde5_bindir}/plasmathemeexplorer
%dir %{_kde5_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/
%{_kde5_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
# Must not be plasma_shell_org.kde.desktop, should be checked if fixed
rm -f po/*/plasma_shell_org.kde.desktop.po
# Don't ship translations if we don't ship package itself
rm -f po/*/kdevpackagemanagerview.po
rm -f po/*/plasmate.po
rm -f po/*/plasmawallpaperviewer.po
rm -f po/*/remote-widgets-browser.po

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

%find_lang cuttlefish
%find_lang plasmaengineexplorer
%find_lang plasmoidviewer
%find_lang themeexplorer
