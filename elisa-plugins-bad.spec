%define debug_package	%{nil}

%define rel	2

%define svn	0
%define pre	0
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define dirname		%name
%else
%if %pre
%define release		%mkrel 0.%pre.%rel
%define distname	%name-%version.%pre.tar.gz
%define dirname		%name-%version.%pre
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif
%endif

# It's the same for releases, but different for pre-releases: please
# don't remove, even if it seems superfluous - AdamW 2008/03
%define fversion	%{version}

Summary:	'Bad' plugins for the Elisa media center
Name:		elisa-plugins-bad
Version:	0.5.35
Release:	%{release}
# For SVN:
# svn co https://code.fluendo.com/elisa/svn/trunk elisa
Source0:	http://elisa.fluendo.com/static/download/elisa/%{distname}
# Disable irrelevant plugin (now we can't do it in core...) - AdamW
# 2008/10
Patch0:		elisa-plugins-bad-0.5.22-unneeded.patch
# From Debian: use system Coherence - AdamW 2009/02
Patch1:		http://patch-tracking.debian.net/patch/series/dl/elisa-plugins-bad/0.5.28-1/40_use-system-coherence.patch
License:	GPLv3 and MIT
Group:		Development/Python
URL:		http://elisa.fluendo.com/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-devel
BuildRequires:	python-twisted
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer0.10-python
BuildRequires:	elisa-core = %{version}
Requires:	elisa-plugins-good = %{version}
# Needed for interface code, which is in this package - AdamW 2008/07
Requires:	python-cssutils
Suggests:	python-coherence
Suggests:	python-daap
# Needed for DAAP plugin
Suggests:	avahi-python
# Needed for yes.fm support
Suggests:	python-simplejson

%description
Elisa is a project to create an open source cross platform media center 
solution. This package contains 'bad' (somehow not up to planned
standards for plugins) plugins for Elisa.

%prep
%setup -q -n %{dirname}
%patch0 -p1 -b .unneeded
%patch1 -p1 -b .sys_coherence

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
%{py_puresitedir}/elisa_plugin_*-py%{pyver}.egg-info
%{py_puresitedir}/elisa_plugin_*-py%{pyver}-nspkg.pth

