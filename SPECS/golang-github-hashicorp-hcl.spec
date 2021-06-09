# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/hashicorp/hcl
%global goipath         github.com/hashicorp/hcl
Version:                1.0.0

%gometa

%global common_description %{expand:
HCL is the HashiCorp configuration language.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        HCL is the HashiCorp configuration language

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
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
%gocheck -r .*parser.*
%endif

%gopkgfiles

%changelog

