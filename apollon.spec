Summary:	KDE-based client for the p2p-protocol giFT (OpenFT, FastTrack(Kazaa), Gnutella)
Summary(pl):	Klient bazuj±cy na KDE dla protoko³u p2p giFT (OpenFT, FastTrack(Kazaa), Gnutella)
Name:		apollon
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a7e656f61c4fc4815aa7150c6b02d1ca
Patch0:		%{name}-dtd-location.patch
URL:		http://apollon.sourceforge.net/
BuildRequires:	giFT-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libmagic-devel
Requires:	giFT-openft
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
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_desktopdir}/{Applications/*.desktop,}

# Ugly hack, but works.
# Without this in apollon are no icons.
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/16x16/apps
mv -f $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/* $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/32x32/apps
mv -f $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/* $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/32x32/apps

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/16x16/actions
mv -f $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions/* $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg/16x16/actions

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/*.la
%{_datadir}/apps/apollon
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/*
