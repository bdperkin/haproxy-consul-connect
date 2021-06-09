# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/hashicorp/go-envparse
%global goipath         github.com/hashicorp/go-envparse
%global commit          d9cfd743a15e3ab6eb52918f9b23bb27042ac8fd

%gometa

%global common_description %{expand:
Minimal environment variable parser for Go.}

%global golicenses      LICENSE NOTICES.txt
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Minimal environment variable parser for Go

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

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

