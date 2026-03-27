Name:           coova-chilli
Version:        1.8
Release:        1%{?dist}
Summary:        Coova Chilli - Wireless LAN Access Point Controller
License:        GPL
URL:            http://coova.org/
Source:         coova-chilli-1.8.tar.gz

%description
Coova Chilli is an open-source access point controller for wireless networks.

%prep
%setup -q -n coova-chilli-1.8
mkdir -p m4