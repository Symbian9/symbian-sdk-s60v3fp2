Summary:	Symbian s60v3 FP2 SDK
Summary(pl.UTF-8):	SDK Symbiana s60v3 FP2
Name:		symbian-sdk-s60v3fp2
Version:	1.09
Release:	1
License:	Nokia EULA
Group:		Developement
Source0:	http://www.martin.st/symbian/gnupoc-package-%{version}.tar.gz
# Source0-md5:	67b86eb218fe390ef0eddf837fbce796
Source1:	S60-3.2-SDK-f.inc3.2130.zip
URL:		http://www.martin.st/symbian/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1
%define		_noautoreq	/c/Perl/bin/perl

%description
Symbian s60v3 FP2 SDK.

%description -l pl.UTF-8
SDK Symbiana s60v3 FP2.

%prep
%setup -n gnupoc-package-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

cd sdks
./install_gnupoc_s60_32 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp2

rm -rf $RPM_BUILD_ROOT%{_datadir}/symbian/s60v3fp2/epoc32/tools_orig

install makelinkdir $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sdks/README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/symbian
%dir %{_datadir}/symbian/s60v3fp2
%{_datadir}/symbian/s60v3fp2/examples
%{_datadir}/symbian/s60v3fp2/GCCE_readme.txt
%{_datadir}/symbian/s60v3fp2/Nokia_EULA.txt
%{_datadir}/symbian/s60v3fp2/releasenotes.txt
%{_datadir}/symbian/s60v3fp2/S60_3rd_Edition_FP2_SDK_for_Symbian_OS_Installation_Guide_V1.0.pdf
%{_datadir}/symbian/s60v3fp2/s60cppexamples
%{_datadir}/symbian/s60v3fp2/s60tools
%{_datadir}/symbian/s60v3fp2/series60doc

%dir %{_datadir}/symbian/s60v3fp2/epoc32
%{_datadir}/symbian/s60v3fp2/epoc32/cshlpcmp_template
%{_datadir}/symbian/s60v3fp2/epoc32/data
%{_datadir}/symbian/s60v3fp2/epoc32/gcc
%{_datadir}/symbian/s60v3fp2/epoc32/include
%{_datadir}/symbian/s60v3fp2/epoc32/release
%{_datadir}/symbian/s60v3fp2/epoc32/winscw

%dir %{_datadir}/symbian/s60v3fp2/epoc32/tools
%{_datadir}/symbian/s60v3fp2/epoc32/tools/alp2csh
%{_datadir}/symbian/s60v3fp2/epoc32/tools/build
%{_datadir}/symbian/s60v3fp2/epoc32/tools/captools
%{_datadir}/symbian/s60v3fp2/epoc32/tools/cdb
%{_datadir}/symbian/s60v3fp2/epoc32/tools/charconv
%{_datadir}/symbian/s60v3fp2/epoc32/tools/commdb-schema
%{_datadir}/symbian/s60v3fp2/epoc32/tools/compilation_config
%{_datadir}/symbian/s60v3fp2/epoc32/tools/cshlpcmp
%{_datadir}/symbian/s60v3fp2/epoc32/tools/depcheck
%{_datadir}/symbian/s60v3fp2/epoc32/tools/depmodel
%{_datadir}/symbian/s60v3fp2/epoc32/tools/distrib
%{_datadir}/symbian/s60v3fp2/epoc32/tools/ecmt
%{_datadir}/symbian/s60v3fp2/epoc32/tools/j2me
%{_datadir}/symbian/s60v3fp2/epoc32/tools/mds
%{_datadir}/symbian/s60v3fp2/epoc32/tools/perl
%{_datadir}/symbian/s60v3fp2/epoc32/tools/perllib
%{_datadir}/symbian/s60v3fp2/epoc32/tools/productinstaller
%{_datadir}/symbian/s60v3fp2/epoc32/tools/shell
%{_datadir}/symbian/s60v3fp2/epoc32/tools/systemdefinition
%{_datadir}/symbian/s60v3fp2/epoc32/tools/tz
%{_datadir}/symbian/s60v3fp2/epoc32/tools/variant

%{_datadir}/symbian/s60v3fp2/epoc32/tools/aiftool
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.bat
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.bsf
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.cmd
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.cwlink
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.dll
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.dtd
%{_datadir}/symbian/s60v3fp2/epoc32/tools/emulatorbuild
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.exe
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.jar
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.pm
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.txt
%{_datadir}/symbian/s60v3fp2/epoc32/tools/*.xml
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/abld
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/bldmake
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/bmconv
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/elf2e32
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/epoc
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/eshell
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/extmake
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/makekeys
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/makesis
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/makmake
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/mifconv
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/petran
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/pfsdump
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/*.pl
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/rcomp
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/setupcomms
%attr(755,root,root) %{_datadir}/symbian/s60v3fp2/epoc32/tools/signsis
