%global octpkg geometry

Summary:	Library for geometric computing extending MatGeom functions
Name:		octave-%{octpkg}
Version:	4.0.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and BSD and Boost Software License
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.2.0
BuildRequires:	octave-matgeom >= 1.0.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-matgeom >= 1.0.0

Requires(post): octave
Requires(postun): octave

%description
This library extends MatGeom functionality.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

