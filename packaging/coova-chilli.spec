Name:           coova-chilli
Version:        1.8
Release:        1%{?dist}
Summary:        CoovaChilli is an open-source access controller for wireless LAN

License:        GPLv2+
URL:            https://github.com/coova/coova-chilli
Source0:        coova-chilli-1.8.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  curl-devel

%description
CoovaChilli is an open-source software access controller for wireless
LAN. It is used for authenticating users of a wireless (or wired) LAN.
It is based on the ChilliSpot project.

%prep
%setup -q -n coova-chilli-1.8
mkdir -p m4

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/*
%{_sysconfdir}/chilli*
%{_datadir}/doc/%{name}*

%changelog
* Fri Mar 27 2026 CoovaChilli Maintainers <maintainers@example.com> - 1.8-1
- Initial RPM package for CoovaChilli 1.8