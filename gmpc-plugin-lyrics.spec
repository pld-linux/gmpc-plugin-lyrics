%define		source_name gmpc-lyrics
Summary:	Lyrics provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca słowa piosenek dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-lyrics-provider
Version:	0.18.100
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
#Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
Source0:	http://download.sarine.nl/Programs/gmpc/0.19.0-rc1/%{source_name}-%{version}.tar.gz
# Source0-md5:	cbe0a6d8dbfa6aba92064ddd13791633
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_LYRICS
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gmpc-devel >= 0.18.100
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Requires:	gmpc >= 0.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin fetches lyrics from the internet. It uses the following
websites as sources:
- LyricWiki
- LeosLyrics
- Lyrics Tracker

%description -l pl.UTF-8
Ta wtyczka pobiera słowa piosenek z następujęcych serwisów
internetowych:
- LyricWiki
- LeosLyrics
- Lyrics Tracker

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/lyricsplugin.so
