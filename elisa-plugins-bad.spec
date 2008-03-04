%define debug_package	%{nil}
%define svn	0
%define pre	0
%if %svn
%define release	%mkrel 0.%svn.1
%else
%if %pre
%define release %mkrel 0.%pre.1
%else
%define release	%mkrel 1
%endif
%endif

%define fversion	%{version}

Summary:	'Bad' plugins for the Elisa media center
Name:		elisa-plugins-bad
Version:	0.3.4
Release:	%{release}
%if %svn
# svn co https://code.fluendo.com/elisa/svn/trunk elisa
Source0:	%{name}-%{svn}.tar.lzma
%else
%if %pre
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.%{pre}.tar.gz
%else
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
%endif
%endif
License:	GPLv3 and MIT
Group:		Development/Python
URL:		http://elisa.fluendo.com/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:	python-twisted
BuildRequires:	ImageMagick
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer0.10-python
BuildRequires:	elisa-core = %{version}
Requires:	elisa-plugins-good = %{version}
Suggests:	python-lirc
Suggests:	python-coherence

%description
Elisa is a project to create an open source cross platform media center 
solution. This package contains 'bad' (somehow not up to planned
standards for plugins) plugins for Elisa.

%prep
%if %svn
%setup -q -n %{name}
%else
%if %pre
%setup -q -n %{name}-%{version}.%{pre}
%else
%setup -q
%endif
%endif

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --single-version-externally-managed --compile --optimize=2
# already in -good
rm -f %{buildroot}%{py_puresitedir}/elisa/plugins/__init__*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/elisa/plugins/*
%{py_puresitedir}/elisa_plugins_bad-%{fversion}-py%{pyver}.egg-info
%{py_puresitedir}/elisa_plugins_bad-%{fversion}-py%{pyver}-nspkg.pth

