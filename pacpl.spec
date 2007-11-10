Summary:	Perl Audio Converter
Summary(pl.UTF-8):	Perlowy konwerter audio
Name:		pacpl
Version:	4.0.0
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	http://dl.sourceforge.net/paclpl/%{name}-%{version}.tar.bz2
URL:		http://viiron.googlepages.com/
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

#%description -l pl.UTF-8

%prep
%setup -q

%build
mv -f ac{local,include}.m4
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO extra
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/pacpl
%dir %{_sysconfdir}/pacpl/modules
%{_sysconfdir}/pacpl/modules/sample.m
%{_sysconfdir}/pacpl/pacpl.conf
%dir %{_sysconfdir}/pacpl/po
%{_sysconfdir}/pacpl/po/de.po
%{_sysconfdir}/pacpl/po/en_US.po
%{_sysconfdir}/pacpl/po/es.po
%{_sysconfdir}/pacpl/po/pl.po
%{_sysconfdir}/pacpl/po/pt.po
%{_sysconfdir}/pacpl/po/zh_CN.po
%dir %{_datadir}/apps/amarok/scripts/pacx
%{_datadir}/apps/amarok/scripts/pacx/pacx
%{_datadir}/apps/dolphin/servicemenus/pacpl.desktop
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
