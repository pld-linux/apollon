Summary:	KDE-based client for the p2p-protocol giFT (OpenFT, FastTrack(Kazaa))
Summary(pl):	Klient bazuj±cy na KDE dla protoko³u p2p giFT (OpenFT, FastTrack(Kazaa))
Name:		apollon
Version:	0.8
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	e9290cecf95033594ec1029727790a53
URL:		http://apollon.sourceforge.net/
BuildRequires:	giFT-devel
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apollon is a KDE-based client for the p2p-protocol giFT (OpenFT,
FastTrack(Kazaa!),..). It is very userfriendly, intuitively, offers an
inline Mediaplayer for previews of downloaded files, etc etc.

%description -l pl
Apollon jest graficznym klientem dla protoko³u p2p giFT (OpenFT,
FastTrack(Kazaa!),..) bazuj±cym na KDE. Jest on bardzo przyjazny
u¿ytkownikowi, intuicyjny, oferuje wewnêtrzny odtwarzacz plików
multimedialnych do podgl±du ¶ci±gniêtych plików, itd., itd.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_docdir}/HTML/en/%{name}
