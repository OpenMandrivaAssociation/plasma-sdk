%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20231023

Summary:	Plasma 6 SDK
Name:		plasma6-sdk
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-sdk/-/archive/master/plasma-sdk-master.tar.bz2#/plasma-sdk-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%endif
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
BuildRequires:	cmake(KF6Plasma)
BuildRequires:	cmake(KF6PlasmaQuick)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Plasma5Support)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	qml(org.kde.kirigami)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	plasma6-desktop
BuildRequires:	plasma6-xdg-desktop-portal-kde
Requires:	plasma6-cuttlefish
Requires:	plasma6-engineexplorer
Requires:	plasma6-plasmoidviewer
Requires:	plasma6-themeexplorer
Requires:	plasma6-lookandfeelexplorer

%description
Plasma 6 SDK.

%files

#----------------------------------------------------------------------------

%package -n plasma6-cuttlefish
Summary:	Plasma 6 icon browser
Group:		Graphical desktop/KDE

%description -n plasma6-cuttlefish
Plasma 6 icon browser.

%files -n plasma6-cuttlefish -f cuttlefish.lang -f cuttlefish_editorplugin.lang
%{_bindir}/cuttlefish
%{_qtdir}/plugins/ktexteditor/cuttlefishplugin.so
%{_datadir}/metainfo/org.kde.plasma.cuttlefish.appdata.xml
%{_datadir}/applications/org.kde.cuttlefish.desktop

#----------------------------------------------------------------------------

%package -n plasma6-engineexplorer
Summary:	Plasma 6 engine explorer
Group:		Graphical desktop/KDE
Conflicts:	plasmate

%description -n plasma6-engineexplorer
Plasma 6 engine explorer. It's used to explore plasma data engines.

%files -n plasma6-engineexplorer -f plasmaengineexplorer.lang
%{_bindir}/plasmaengineexplorer
%{_mandir}/man1/plasmaengineexplorer.1.*
%{_datadir}/applications/org.kde.plasmaengineexplorer.desktop
%{_datadir}/metainfo/org.kde.plasmaengineexplorer.appdata.xml

#----------------------------------------------------------------------------

%package -n plasma6-plasmoidviewer
Summary:	Plasma 5 plasmoid viewer
Group:		Graphical desktop/KDE
Requires:	plasma6-shell-plasmoidviewer
Conflicts:	plasmate

%description -n plasma6-plasmoidviewer
Plasma 5 plasmoid viewer. It's used to run plasmoids in their own window.

%files -n plasma6-plasmoidviewer -f plasmoidviewer.lang
%{_bindir}/plasmoidviewer
%{_mandir}/man1/plasmoidviewer.1.*
%{_datadir}/applications/org.kde.plasmoidviewer.desktop
%{_datadir}/metainfo/org.kde.plasmoidviewer.appdata.xml
%{_datadir}/zsh/site-functions/_plasmoidviewer

#----------------------------------------------------------------------------

%package -n plasma6-shell-plasmoidviewer
Summary:	Plasma 6 plasmoid viewer shell
Group:		Graphical desktop/KDE
# Not sure if it's required
Suggests:	plasma6-plasmoidviewer

%description -n plasma6-shell-plasmoidviewer
Plasma 6 plasmoid viewer shell.

%files -n plasma6-shell-plasmoidviewer -f plasma_shell_org.kde.plasmoidviewershell.lang
%dir %{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell/*
%{_datadir}/metainfo/org.kde.plasma.plasmoidviewershell.appdata.xml
#----------------------------------------------------------------------------

%package -n plasma6-themeexplorer
Summary:	Plasma 6 theme explorer
Group:		Graphical desktop/KDE

%description -n plasma6-themeexplorer
Plasma 6 theme explorer. It's used to explore and edit plasma themes.

%files -n plasma6-themeexplorer -f org.kde.plasma.themeexplorer.lang
%{_bindir}/plasmathemeexplorer
%{_datadir}/applications/org.kde.plasma.themeexplorer.desktop
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/
%{_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer/*
%{_datadir}/metainfo/org.kde.plasma.themeexplorer.appdata.xml

#----------------------------------------------------------------------------

%package -n plasma6-lookandfeelexplorer
Summary:	Plasma 6 lookandfeel explorer
Group:		Graphical desktop/KDE

%description -n plasma6-lookandfeelexplorer
Plasma 6 lookandfeel explorer. It's used to explore and edit plasma themes.

%files -n plasma6-lookandfeelexplorer -f org.kde.plasma.lookandfeelexplorer.lang
%{_bindir}/lookandfeelexplorer
%dir %{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/
%{_datadir}/metainfo/org.kde.plasma.lookandfeelexplorer.appdata.xml
%{_datadir}/kpackage/genericqml/org.kde.plasma.lookandfeelexplorer/*

#----------------------------------------------------------------------------

%package -n plasma6-kqml
Summary:	Plasma 6 QML viewer
Group:		Graphical desktop/KDE

%description -n plasma6-kqml
Plasma 6 QML viewer

%files -n plasma6-kqml
%{_bindir}/kqml
%{_mandir}/man1/kqml.1*
%{_datadir}/zsh/site-functions/_kqml

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n plasma-sdk-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang cuttlefish || touch cuttlefish.lang
%find_lang cuttlefish_editorplugin || touch cuttlefish_editorplugin.lang
%find_lang plasmaengineexplorer --with-man || touch plasmaengineexplorer.lang
%find_lang plasmoidviewer --with-man || touch plasmoidviewer.lang
%find_lang plasma_shell_org.kde.plasmoidviewershell || touch plasma_shell_org.kde.plasmoidviewershell.lang
%find_lang org.kde.plasma.themeexplorer || touch org.kde.plasma.themeexplorer.lang
%find_lang org.kde.plasma.lookandfeelexplorer || touch org.kde.plasma.lookandfeelexplorer.lang
