%define 	module	shiny
Summary:	A collection of decorators to make your programs more shiny
Name:		python-%{module}
Version:	0.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/s/shiny/shiny-%{version}.tar.gz
# Source0-md5:	9a16cb60c1e2cfaa9f70e1b51019d96a
URL:		http://pypi.python.org/pypi/shiny
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module really is very shiny.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

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
