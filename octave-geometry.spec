%global octpkg geometry

Summary:	Library for geometric computing extending MatGeom functions
Name:		octave-geometry
Version:	4.0.0
Release:	2
License:	GPLv3+ and BSD and Boost Software License
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/geometry/
Source0:	https://downloads.sourceforge.net/octave/geometry-%{version}.tar.gz

BuildRequires:	octave-devel >= 4.2.0
BuildRequires:	octave-matgeom >= 1.0.0
BuildRequires:	stdc++-devel

Requires:	octave(api) = %{octave_api}
Requires:  	octave-matgeom >= 1.0.0

Requires(post): octave
Requires(postun): octave

%description
This library extends MatGeom functionality.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

