# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/tidwall/lotsa
%global goipath         github.com/tidwall/lotsa
Version:                1.0.2

%gometa

%global common_description %{expand:
Simple Go library for executing lots of operations spread over any number of
threads.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple Go library for executing lots of operations spread over any number of threads

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

