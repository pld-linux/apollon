Summary:	KDE-based client for the p2p-protocol giFT (OpenFT, FastTrack(Kazaa))
Summary(pl):	Klient bazuj±cy na KDE dla protoko³u p2p giFT (OpenFT, FastTrack(Kazaa))
Name:		apollon
Version:	0.8.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a859b6d244e47cc259135d64f63df953
URL:		http://apollon.sourceforge.net/
BuildRequires:	giFT-devel
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

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
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications/*.desktop,Network/Misc}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/hicolor/*/apps/*
