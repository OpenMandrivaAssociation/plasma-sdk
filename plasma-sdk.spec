Summary:	Plasma 5 SDK
Name:		plasma-sdk
Version:	5.6.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Test)
Requires:	plasma-cuttlefish
Requires:	plasma-engineexplorer
Requires:	plasma-plasmoidviewer
Requires:	plasma-themeexplorer

%description
Plasma 5 SDK.

%files

#----------------------------------------------------------------------------

%package -n plasma-cuttlefish
Summary:	Plasma 5 icon browser
Group:		Graphical desktop/KDE

%description -n plasma-cuttlefish
Plasma 5 icon browser.

%files -n plasma-cuttlefish -f cuttlefish.lang,cuttlefish_editorplugin.lang
%{_kde5_bindir}/cuttlefish
%{_datadir}/applications/cuttlefish.desktop
%dir %{_kde5_datadir}/plasma/packages/org.kde.plasma.cuttlefish/
%{_kde5_datadir}/plasma/packages/org.kde.plasma.cuttlefish/*
%{_kde5_services}/plasma-package-org.kde.plasma.cuttlefish.desktop
%{_qt5_plugindir}/ktexteditor/cuttlefishplugin.so

#----------------------------------------------------------------------------

%package -n plasma-engineexplorer
Summary:	Plasma 5 engine explorer
Group:		Graphical desktop/KDE
Conflicts:	plasmate

%description -n plasma-engineexplorer
Plasma 5 engine explorer. It's used to explore plasma data engines.

%files -n plasma-engineexplorer -f plasmaengineexplorer.lang
%{_kde5_bindir}/plasmaengineexplorer

#----------------------------------------------------------------------------

%package -n plasma-plasmoidviewer
Summary:	Plasma 5 plasmoid viewer
Group:		Graphical desktop/KDE
Requires:	plasma-shell-plasmoidviewer
Conflicts:	plasmate

%description -n plasma-plasmoidviewer
Plasma 5 plasmoid viewer. It's used to run plasmoids in their own window.

%files -n plasma-plasmoidviewer -f plasmoidviewer.lang
%{_kde5_bindir}/plasmoidviewer

#----------------------------------------------------------------------------

%package -n plasma-shell-plasmoidviewer
Summary:	Plasma 5 plasmoid viewer shell
Group:		Graphical desktop/KDE
# Not sure if it's required
Suggests:	plasma-plasmoidviewer

%description -n plasma-shell-plasmoidviewer
Plasma 5 plasmoid viewer shell.

%files -n plasma-shell-plasmoidviewer -f plasma_shell_org.kde.plasmoidviewershell.lang
%dir %{_kde5_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/
%{_kde5_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/*
%{_kde5_services}/plasma-shell-org.kde.plasma.plasmoidviewershell.desktop

#----------------------------------------------------------------------------

%package -n plasma-themeexplorer
Summary:	Plasma 5 theme explorer
Group:		Graphical desktop/KDE

%description -n plasma-themeexplorer
Plasma 5 theme explorer. It's used to explore and edit plasma themes.

%files -n plasma-themeexplorer -f themeexplorer.lang
%{_kde5_bindir}/plasmathemeexplorer
%{_datadir}/applications/org.kde.plasma.themeexplorer.desktop
%dir %{_kde5_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/
%{_kde5_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/*

#----------------------------------------------------------------------------

%prep
%setup -q
# Must not be plasma_shell_org.kde.desktop, should be checked if fixed
rm -f po/*/plasma_shell_org.kde.desktop.po
# Don't ship translations if we don't ship package itself
rm -f po/*/kdevpackagemanagerview.po
rm -f po/*/plasmate.po
rm -f po/*/plasmawallpaperviewer.po
rm -f po/*/remote-widgets-browser.po

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang cuttlefish
%find_lang cuttlefish_editorplugin
%find_lang plasmaengineexplorer
%find_lang plasmoidviewer
%find_lang themeexplorer
%find_lang plasma_shell_org.kde.plasmoidviewershell
