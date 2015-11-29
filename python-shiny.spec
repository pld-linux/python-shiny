%define		bzrrev	4
%define		rel		1
%define 	module	shiny
Summary:	A collection of decorators to make your programs more shiny
Name:		python-%{module}
Version:	0.1
Release:	1.%{bzrrev}.%{rel}
License:	BSD
Group:		Development/Languages/Python
# bzr branch lp:~alsuren/python-shiny/shiny
# tar --exclude-vcs -cjf spyke-$(bzr revno spyke).tar.bz2 spyke
# ../dropin spyke-$(bzr revno spyke).tar.bz2
Source0:	shiny-4.tar.bz2
# Source0-md5:	6b4a80afe4328e4c3d8a750b1532fcd9
URL:		https://code.launchpad.net/python-shiny
BuildRequires:	python-devel
BuildRequires:	python-devel-tools
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module really is very shiny.

%prep
%setup -q -n %{module}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/shiny/test.py*

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/shiny
%{py_sitescriptdir}/shiny/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/shiny-*.egg-info
%endif
