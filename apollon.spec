Summary:	KDE-based client for the p2p-protocol giFT (OpenFT, FastTrack(Kazaa), Gnutella)
Summary(pl):	Klient bazuj±cy na KDE dla protoko³u p2p giFT (OpenFT, FastTrack(Kazaa), Gnutella)
Name:		apollon
Version:	0.9.3
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-2.tar.bz2
# Source0-md5:	76ff5fcd1b8eef1d745405b14652fba2
Patch0:		%{name}-dtd-location.patch
URL:		http://apollon.sourceforge.net/
Requires:	giFT-openft
BuildRequires:	giFT-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libmagic-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
Apollon is a KDE-based client for the p2p-protocol giFT (OpenFT,
FastTrack(Kazaa!), Gnutella). It is very userfriendly, intuitively,
offers an inline Mediaplayer for previews of downloaded files, etc.

%description -l pl
Apollon jest graficznym klientem dla protoko³u p2p giFT (OpenFT,
FastTrack(Kazaa!), Gnutella) bazuj±cym na KDE. Jest on bardzo
przyjazny u¿ytkownikowi, intuicyjny, oferuje wewnêtrzny odtwarzacz
plików multimedialnych do podgl±du ¶ci±gniêtych plików, itd., itd.

%prep
%setup -q
%patch0 -p1

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

# Ugly hack, but works.
# Without this in apollon are no icons.
mkdir $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/16x16/apps
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/16x16/apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/16x16/apps
mkdir $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/32x32/apps
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/32x32/apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/32x32/apps
mkdir $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/48x48/apps
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/48x48/apps
mkdir $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/64x64/apps
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/64x64/apps/* $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/64x64/apps

mkdir $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/16x16/actions
mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/16x16/actions/* $RPM_BUILD_ROOT%{_pixmapsdir}/crystalsvg/16x16/actions

rm -rf $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/*.la
%{_datadir}/apps/apollon
%{_applnkdir}/Network/Misc/*
%{_pixmapsdir}/*/*/*/*
