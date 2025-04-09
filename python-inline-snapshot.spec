%define module inline-snapshot
%define oname inline_snapshot
%bcond_without test

Name:		python-inline-snapshot
Version:	0.22.0
Release:	1
Summary:	Create and update inline snapshots in your python tests
URL:		https://pypi.org/project/inline-snapshot/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/i/inline-snapshot/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
%if %{with test}
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(black)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(dirty-equals)
BuildRequires:	python%{pyver}dist(hypothesis)
BuildRequires:	python%{pyver}dist(iniconfig)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(pygments)
BuildRequires:	python%{pyver}dist(markdown-it-py)
BuildRequires:	python%{pyver}dist(mdurl)
BuildRequires:	python%{pyver}dist(mypy)
BuildRequires:	python%{pyver}dist(pydantic)
BuildRequires:	python%{pyver}dist(pyright)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-freezer)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(pytest-subtests)
BuildRequires:	python%{pyver}dist(pytest-xdist)
BuildRequires:	python%{pyver}dist(time-machine)
%endif
Suggests:	python%{pyver}dist(black) >= 23.3.0
Suggests:	python%{pyver}dist(click) >= 8.1.4
Suggests:	python%{pyver}dist(dirty-equals) >= 0.9.0


%description
Create and update inline snapshots in your python tests.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
export PYTHONWARNINGS='ignore::DeprecationWarning'
pip install -e .[test]
%{__python} -m pytest -v -k "not test_docs and not test_typing \
and not test_format_command_fail and not test_pydantic \
and not test_format_command_fail and not test_xdist and not test_xfail \
and not test_external and not test_trailing_comma and not test_pytest_plugin"
#%%{__python} -m pytest --import-mode append -v -k "not test_typing and not test_format_command_fail and not test_pydantic and not test_format_command_fail"

%endif

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}*.*-info
%license LICENSE
%doc README.md
