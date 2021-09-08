Summary:	Backup and restore your gmail account
Name:		gmvault
Version:	1.9.1
Release:	1
License:	AGPL v3.0
Group:		Libraries/Python
Source0:	https://pypi.debian.net/gmvault/%{name}-%{version}.tar.gz
# Source0-md5:	4ad5ebd59147f12e30e6ba971ace7834
URL:		http://gmvault.org/
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmvault is a tool for backing up your gmail account and never lose
email correspondence. 

%prep
%setup -q

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python2(\s|$),#!%{__python}\1,' -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python}\1,' \
      src/gmv/blowfish.py

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+bash(\s|$),#!/bin/bash\1,' \
      etc/scripts/gmvault

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE-NOTE.txt
%attr(755,root,root) %{_bindir}/gmvault
%{py_sitescriptdir}/gmv
%{py_sitescriptdir}/gmv*.egg-info
