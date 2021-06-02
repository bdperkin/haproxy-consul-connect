# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/cenkalti/backoff
%global goipath         github.com/cenkalti/backoff/v3
%global forgeurl        https://github.com/cenkalti/backoff
Version:                3.2.2

%gometa

%global common_description %{expand:
Package backoff implements backoff algorithms for retrying operations. Use
Retry function for retrying operations that may fail.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package backoff implements backoff algorithms for retrying operations

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

