
#
# todo: pl description and summary
#

Summary:	Backend utility to get CDDB discid information from a CD-ROM
Name:		cd-discid
Version:	0.7
Release:	1
License:	GPL
Group:		Applications
Source0:	http://lly.org/~rcw/cd-discid/cd-discid_%{version}.orig.tar.gz
URL:		http://lly.org/~rcw/cd-discid/page
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cd-discid is a backend utility to get CDDB discid information from a CD-ROM
disc. It was originally designed for cdgrab (now abcde), but can be used
for any purpose requiring CDDB data.

%prep
%setup -q

%build
gcc %{rpmcflags} -o cd-discid cd-discid.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install cd-discid $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
