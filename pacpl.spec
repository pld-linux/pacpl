%include	/usr/lib/rpm/macros.perl
Summary:	Perl Audio Converter
Summary(pl.UTF-8):	Perlowy konwerter audio
Name:		pacpl
Version:	4.0.1
Release:	0.2
License:	GPL v3
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/pacpl/%{name}-%{version}.tar.bz2
# Source0-md5:	8571cb1e431c1885aec0cee0f2911c97
Patch0:		%{name}-po.patch
URL:		http://viiron.googlepages.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-Audio-FLAC-Header
BuildRequires:	perl-Audio-Musepack
BuildRequires:	perl-Audio-WMA
BuildRequires:	perl-CDDB_get
BuildRequires:	perl-Devel-Symdump
BuildRequires:	perl-IO-String
BuildRequires:	perl-Inline-C
BuildRequires:	perl-MP3-Info
BuildRequires:	perl-MP3-Tag
BuildRequires:	perl-MP4-Info
BuildRequires:	perl-Ogg-Vorbis-Header
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-Switch
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	rpm-perlprov >= 4.1-13
#Suggests:???
# checking for lame... yes
# checking for toolame... no
# checking for gogo... no
# checking for bladeenc... no
# checking for oggenc... yes
# checking for oggdec... yes
# checking for speexenc... no
# checking for speexdec... no
# checking for flac... yes
# checking for mac... no
# checking for shorten... no
# checking for sox... no
# checking for faac... no
# checking for faad... no
# checking for ffmpeg... no
# checking for mplayer... yes
# checking for la... no
# checking for bonk... no
# checking for mppenc... no
# checking for mppdec... no
# checking for ofr... no
# checking for ofs... no
# checking for lpac... no
# checking for ttaenc... no
# checking for wavpack... yes
# checking for wvunpack... yes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/pacpl-%{version}-root-%(id -u -n)

%description
Perl Audio Converter is a tool for converting multiple audio types
from one format to another. It supports AAC, AC3, AIFF, APE, AU, AVR,
BONK, CAF, CDR, FAP, FLA, FLAC, IRCAM, LA, LPAC, MAT, MAT4, MAT5, M4A,
MP2, MP3, MP4, MPC, MPP, NIST, OFR, OFS, OGG, PAC, PAF, PVF, RA, RAM,
RAW, SD2, SF, SHN, SMP, SND, SPX, TTA, VOC, W64, WAV, WMA, and WV. It
can also convert audio from the following video extensions: RM, RV,
ASF, DivX, MPG, MKV, MPEG, AVI, MOV, OGM, QT, VCD, SVCD, M4V, NSV,
NUV, PSP, SMK, VOB, FLV, and WMV. A CD ripping function with CDDB
support, batch conversion, tag preservation for most supported
formats, independent tag reading/writing, and extensions for Amarok,
Dolphin, and Konqueror are also provided.

%description -l pl.UTF-8
Perl Audio Converter to narzędzie do konwersji wielu rodzajów plików
dźwiękowych z jednego formatu do innego. Obsługuje formaty AAC, AC3,
AIFF, APE, AU, AVR, BONK, CAF, CDR, FAP, FLA, FLAC, IRCAM, LA, LPAC,
MAT, MAT4, MAT5, M4A, MP2, MP3, MP4, MPC, MPP, NIST, OFR, OFS, OGG,
PAC, PAF, PVF, RA, RAM, RAW, SD2, SF, SHN, SMP, SND, SPX, TTA, VOC,
W64, WAV, WMA oraz WV. Potrafi także konwertować dźwięk z
następujących formatów filmów: RM, RV, ASF, DivX, MPG, MKV, MPEG, AVI,
MOV, OGM, QT, VCD, SVCD, M4V, NSV, NUV, PSP, SMK, VOB, FLV oraz WMV.
Dostępne są także: rippowanie płyt CD z obsługą CDDB, konwersja
wsadowa, zachowywanie znaczników w większości z obsługiwanych
formatów, niezależne odczytywanie i zapisywanie znaczników, a także
rozszerzenia dla Amaroka, Dolphina i Konquerora.

%prep
%setup -q
%patch0 -p1

%build
mv -f ac{local,include}.m4
%{__aclocal}
%{__autoconf}
%configure \
	--enable-all
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/{amarok/scripts/pacx,{dolphin,konqueror}/servicemenus}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/pacpl/po/{fr_FR,fr}.po
mv $RPM_BUILD_ROOT%{_datadir}/pacpl/po/{ru_RU,ru}.po

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO extra
%attr(755,root,root) %{_bindir}/pacpl
%dir %{_sysconfdir}/pacpl
# XXX: maybe modules should go to datadir
%dir %{_sysconfdir}/pacpl/modules
%{_sysconfdir}/pacpl/modules/sample.m
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pacpl/pacpl.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pacpl/codecs.conf
%dir %{_datadir}/pacpl
%dir %{_datadir}/pacpl/po
%lang(de) %{_datadir}/pacpl/po/de.po
%lang(en_US) %{_datadir}/pacpl/po/en_US.po
%lang(es) %{_datadir}/pacpl/po/es.po
%lang(pl) %{_datadir}/pacpl/po/pl.po
%lang(pt) %{_datadir}/pacpl/po/pt.po
%lang(zh_CN) %{_datadir}/pacpl/po/zh_CN.po
%lang(ca) %{_datadir}/pacpl/po/ca.po
%lang(et) %{_datadir}/pacpl/po/et.po
%lang(fr) %{_datadir}/pacpl/po/fr.po
%lang(ru) %{_datadir}/pacpl/po/ru.po
%lang(tr) %{_datadir}/pacpl/po/tr.po
# mark as %dir directories provided by other packages to avoid unnecessary requires:
%dir %{_datadir}/apps
%dir %{_datadir}/apps/amarok
%dir %{_datadir}/apps/amarok/scripts
%dir %{_datadir}/apps/amarok/scripts/pacx
%{_datadir}/apps/amarok/scripts/pacx/pacx
%dir %{_datadir}/apps/dolphin
%dir %{_datadir}/apps/dolphin/servicemenus
%{_datadir}/apps/dolphin/servicemenus/pacpl.desktop
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/pacpl.desktop
%{_mandir}/man1/pacpl.1*
%{_datadir}/mimelnk/audio/x-ape.desktop
%{_datadir}/mimelnk/audio/x-bonk.desktop
%{_datadir}/mimelnk/audio/x-la.desktop
%{_datadir}/mimelnk/audio/x-lpac.desktop
%{_datadir}/mimelnk/audio/x-ofr.desktop
%{_datadir}/mimelnk/audio/x-ofs.desktop
%{_datadir}/mimelnk/audio/x-rm.desktop
%{_datadir}/mimelnk/audio/x-shn.desktop
%{_datadir}/mimelnk/audio/x-tta.desktop
%{_datadir}/mimelnk/audio/x-wavpack.desktop
