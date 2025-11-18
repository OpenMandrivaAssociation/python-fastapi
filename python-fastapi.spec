Name:		python-fastapi
Version:	0.121.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/fastapi/fastapi-%{version}.tar.gz
Summary:	FastAPI framework, high performance, easy to learn, fast to code, ready for production
URL:		https://pypi.org/project/fastapi/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildSystem:	python
BuildArch:	noarch

%description
FastAPI framework, high performance, easy to learn, fast to code, ready for production

%files
%{_bindir}/fastapi
%{py_sitedir}/fastapi
%{py_sitedir}/fastapi-*.*-info
