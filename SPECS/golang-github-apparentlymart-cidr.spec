# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/apparentlymart/go-cidr
%global goipath         github.com/apparentlymart/go-cidr
Version:                1.1.0

%gometa

%global common_description %{expand:
Package cidr is a collection of assorted utilities for computing network and
host addresses within network ranges. It expects a CIDR-type address structure
where addresses are divided into}

%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package cidr is a collection of assorted utilities for computing network and host addresses within network ranges

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

