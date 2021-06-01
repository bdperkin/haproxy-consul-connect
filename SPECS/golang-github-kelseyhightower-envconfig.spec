# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/kelseyhightower/envconfig
%global goipath         github.com/kelseyhightower/envconfig
Version:                1.4.0

%gometa

%global common_description %{expand:
Golang library for managing configuration data from environment variables.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang library for managing configuration data from environment variables

License:        MIT
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

