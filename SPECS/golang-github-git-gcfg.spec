# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-git/gcfg
%global goipath         github.com/go-git/gcfg
Version:                1.5.0

%gometa

%global common_description %{expand:
Go-gcfg/gcfg fork for usage in src-d/go-git.}

%global golicenses      LICENSE
%global godocs          README

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go-gcfg/gcfg fork for usage in src-d/go-git

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/warnings.v0)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/pkg/errors)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -r .*types.*
%endif

%gopkgfiles

%changelog

