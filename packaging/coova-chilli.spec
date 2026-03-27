Name:           coova-chilli
Version:        1.8
Release:        1%{?dist}
Summary:        CoovaChilli is an open source captive portal or wireless LAN access point controller
License:        GPL-2.0
URL:            https://coova.github.io/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gengetopt

%description
CoovaChilli is an open source access controller for wireless LAN access
points and is based on the CoovaChilli software. It is used for authenticating
users of a wireless LAN and supports a number of authentication mechanisms.

%prep
%setup -q -n coova-chilli-%{version}
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
%{_sysconfdir}/*

%changelog
* Fri Mar 27 2026 Coova Chilli Packager <packager@example.com> - 1.8-1
- Initial RPM packaging for coova-chilli 1.8