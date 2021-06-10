# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/oleiade/reflections
%global goipath         github.com/oleiade/reflections
Version:                1.0.1

%gometa

%global common_description %{expand:
Package reflections provides high level abstractions above the reflect
library. Reflect library is very low-level and as can be quite complex when it
comes to do simple things like accessing a structure field value, a field
tag...}

%global golicenses      LICENSE
%global godocs          AUTHORS.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package reflections provides high level abstractions above the reflect library

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
%gocheck
%endif

%gopkgfiles

%changelog

