Name:           coova-chilli
Version:        1.8
Release:        1%{?dist}
Summary:        Secure hotspot access controller

License:        GPLv2+
URL:            https://github.com/coova/coova-chilli
Source0:        coova-chilli-1.8.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  libnl-devel
BuildRequires:  curl-devel
BuildRequires:  gmp-devel
BuildRequires:  gengetopt
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig

Requires:       openssl

%description
CoovaChilli is a captive portal system for providing secure wireless (or wired)
access with 802.1X and RADIUS integration.

%prep
%setup -q -n coova-chilli-%{version}

%build
autoreconf -fi
%configure \
  --prefix=/usr \
  --sysconfdir=/etc \
  --localstatedir=/var
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README NEWS AUTHORS COPYING
%config(noreplace) /etc/chilli.conf
%{_sbindir}/chilli*
%{_libexecdir}/chilli*
%{_datadir}/chilli

%changelog
* Mon Mar 16 2026 GitHub Actions Builder <actions@github.com> - 1.8-1
- Automated CentOS 6 RPM build