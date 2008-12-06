%define		source_name gmpc-lyrics
Summary:	Lyrics provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca słowa piosenek dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-lyrics-provider
Version:	0.16.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/0.16.0/gmpc-lyrics-%{version}.tar.gz
# Source0-md5:	7bb9c502771cffc0171620f46942bba9
URL:		http://gmpc.sarine.nl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.15.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libtool
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
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
