# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/c2h5oh/datasize
%global goipath         github.com/c2h5oh/datasize
%global commit          48ed595a09d275d12122c3650ff5bd42525b91d7

%gometa

%global common_description %{expand:
Golang helpers for data sizes (kilobytes, petabytes), human readable sizes,
parsing.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Golang helpers for data sizes (kilobytes, petabytes), human readable sizes, parsing

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

