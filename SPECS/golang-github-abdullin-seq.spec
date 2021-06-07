# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/abdullin/seq
%global goipath         github.com/abdullin/seq
%global commit          d5467c17e7afe8d8f08f556c6c811a50c3feb28d

%gometa

%global common_description %{expand:
Structural equality library for golang.}

%global golicenses      LICENSE
%global godocs          Readme.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Structural equality library for golang

# Upstream license specification: BSD-2-Clause
License:        BSD
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

