# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/Sectorbob/mlab-ns2
%global goipath         github.com/Sectorbob/mlab-ns2
%global commit          d3aa0c295a8a0ea732210752d5588e16090c58ef

%gometa

%global common_description %{expand:
Automatically exported from code.google.com/p/mlab-ns2.}

%global golicenses      COPYING
%global godocs          CONTRIBUTORS gae/static/robots.txt

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Automatically exported from code.google.com/p/mlab-ns2

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(code.google.com/p/google-api-go-client/bigquery/v2)
BuildRequires:  golang(code.google.com/p/mlab-ns2/gae/ns/data)

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

