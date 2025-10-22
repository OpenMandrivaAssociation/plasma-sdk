%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Plasma 6 SDK
Name:		plasma-sdk
Version:	6.5.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-sdk/-/archive/%{gitbranch}/plasma-sdk-%{gitbranchd}.tar.bz2#/plasma-sdk-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/plasma-sdk-%{version}.tar.xz
%endif
# The desktop file has gone missing in the kpackage .desktop -> .json transition
Source1:	https://invent.kde.org/plasma/plasma-sdk/-/raw/Plasma/5.27/lookandfeelexplorer/package/metadata.desktop
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick) >= 5.90.0
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(Plasma5Support)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	qml(org.kde.kirigami)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	plasma-desktop
Requires:	iconexplorer
Requires:	engineexplorer
Requires:	plasmoidviewer
Requires:	themeexplorer
Requires:	lookandfeelexplorer
# Renamed after 6.0 2025-05-03
%rename plasma6-sdk

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Plasma 6 SDK.

%files

#----------------------------------------------------------------------------

%package -n iconexplorer
Summary:	Plasma 6 icon browser
Group:		Graphical desktop/KDE
# Renamed after 6.0 2025-05-03
%rename plasma6-cuttlefish
%rename plasma6-iconexplorer

%description -n iconexplorer
Plasma 6 icon browser.

%files -n iconexplorer
%{_bindir}/iconexplorer
%{_datadir}/metainfo/org.kde.plasma.iconexplorer.appdata.xml
%{_datadir}/applications/org.kde.iconexplorer.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.iconexplorer.svg
%{_qtdir}/plugins/kf6/ktexteditor/iconexplorerplugin.so

#----------------------------------------------------------------------------

%package -n engineexplorer
Summary:	Plasma 6 engine explorer
Group:		Graphical desktop/KDE
Conflicts:	plasmate
# Renamed after 6.0 2025-05-03
%rename plasma6-engineexplorer

%description -n engineexplorer
Plasma 6 engine explorer. It's used to explore plasma data engines.

%files -n engineexplorer
%{_bindir}/plasmaengineexplorer
%{_mandir}/man1/plasmaengineexplorer.1.*
%{_datadir}/applications/org.kde.plasmaengineexplorer.desktop
%{_datadir}/metainfo/org.kde.plasmaengineexplorer.appdata.xml

#----------------------------------------------------------------------------

%package -n plasmoidviewer
Summary:	Plasma 6 plasmoid viewer
Group:		Graphical desktop/KDE
Requires:	plasma-shell-plasmoidviewer
Conflicts:	plasmate
# Renamed after 6.0 2025-05-03
%rename plasma6-plasmoidviewer

%description -n plasmoidviewer
Plasma 6 plasmoid viewer. It's used to run plasmoids in their own window.

%files -n plasmoidviewer
%{_bindir}/plasmoidviewer
%{_mandir}/man1/plasmoidviewer.1*
%{_datadir}/applications/org.kde.plasmoidviewer.desktop
%{_datadir}/metainfo/org.kde.plasmoidviewer.appdata.xml
# FIXME this file should be packaged here, but seems to cause a bug
# in rpm -- packaging simply aborts without showing an error message
# (but without creating the binary packages) if the file is being
# packaged. Fortunately it's not a vital function.
#{_datadir}/zsh/site-functions/_plasmoidviewer

#----------------------------------------------------------------------------

%package -n plasma-shell-plasmoidviewer
Summary:	Plasma 6 plasmoid viewer shell
Group:		Graphical desktop/KDE
# Not sure if it's required
Suggests:	plasmoidviewer
# Renamed after 6.0 2025-05-03
%rename plasma6-shell-plasmoidviewer

%description -n plasma-shell-plasmoidviewer
Plasma 6 plasmoid viewer shell.

%files -n plasma-shell-plasmoidviewer
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/*

#----------------------------------------------------------------------------

%package -n themeexplorer
Summary:	Plasma 6 theme explorer
Group:		Graphical desktop/KDE
# Renamed after 6.0 2025-05-03
%rename plasma6-themeexplorer

%description -n themeexplorer
Plasma 6 theme explorer. It's used to explore and edit plasma themes.

%files -n themeexplorer
%{_bindir}/plasmathemeexplorer
%{_datadir}/applications/org.kde.plasma.themeexplorer.desktop
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/*

#----------------------------------------------------------------------------

%package -n lookandfeelexplorer
Summary:	Plasma 6 lookandfeel explorer
Group:		Graphical desktop/KDE
# Renamed after 6.0 2025-05-03
%rename plasma6-lookandfeelexplorer

%description -n lookandfeelexplorer
Plasma 6 lookandfeel explorer. It's used to explore and edit plasma themes.

%files -n lookandfeelexplorer
%{_bindir}/lookandfeelexplorer
%{_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop

#----------------------------------------------------------------------------

%package -n kqml
Summary:	Plasma 6 QML viewer
Group:		Graphical desktop/KDE
# Renamed after 6.0 2025-05-03
%rename plasma6-kqml

%description -n kqml
Plasma 6 QML viewer

%files -n kqml
%{_bindir}/kqml
%{_mandir}/man1/kqml.1*
%{_datadir}/zsh/site-functions/_kqml

#----------------------------------------------------------------------------

%install -a
# FIXME workaround for rpm 4.19.0 crashing silently on packaging the
# translations, localized man pages and zsh completions
rm -rf %{buildroot}%{_mandir}/*/man1 %{buildroot}%{_datadir}/locale \
	%{buildroot}%{_datadir}/zsh/site-functions/_plasmoidviewer

# Put back missing desktop file for lookandfeelexplorer
sed -e 's,^Icon=.*,Icon=preferences-desktop-theme-global,' %{S:1} >%{buildroot}%{_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop
