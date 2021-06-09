# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/araddon/gou
%global goipath         github.com/araddon/gou
%global commit          c797efecbb6162ea2d4200cdf779c8b73da7233c

%gometa

%global common_description %{expand:
Go Utilities - logging and json helpers.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go Utilities - logging and json helpers

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

