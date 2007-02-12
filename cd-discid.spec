Summary:	Backend utility to get CDDB discid information from a CD-ROM
Summary(pl.UTF-8):   Narzędzie do pobierania identyfikatora CDDB kompaktu
Name:		cd-discid
Version:	0.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://lly.org/~rcw/cd-discid/cd-discid_%{version}.orig.tar.gz
# Source0-md5:	64677b8b63d1db0db015043f5455171a
URL:		http://lly.org/~rcw/cd-discid/page/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cd-discid is a backend utility to get CDDB discid information from a CD-ROM
disc.

%description -l pl.UTF-8
Cd-discid jest programem do pobierania identyfikatora CDDB kompaktu.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} -o cd-discid cd-discid.c

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
