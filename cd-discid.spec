Summary:	Backend utility to get CDDB discid information from a CD-ROM
Summary(pl.UTF-8):	Narzędzie do pobierania identyfikatora CDDB kompaktu
Name:		cd-discid
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
#Source0Download: https://github.com/taem/cd-discid/tags
Source0:	https://github.com/taem/cd-discid/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	960c613556e5f220021781ef801e2409
URL:		https://github.com/taem/cd-discid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cd-discid is a backend utility to get CDDB discid information from a
CD-ROM disc.

%description -l pl.UTF-8
Cd-discid jest programem do pobierania identyfikatora CDDB kompaktu.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	STRIP=true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog
%attr(755,root,root) %{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*
