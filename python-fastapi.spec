%define module fastapi

Name:		python-fastapi
Version:	0.135.2
Release:	1
Summary:	FastAPI framework, high performance, easy to learn, fast to code, ready for production
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/fastapi/
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
FastAPI framework, high performance, easy to learn,
fast to code, ready for production.

%files
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
