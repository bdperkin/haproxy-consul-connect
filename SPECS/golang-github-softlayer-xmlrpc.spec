# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/softlayer/xmlrpc
%global goipath         github.com/softlayer/xmlrpc
Version:                1.0
%global commit          5f089df7cb7e37ba0cba4e7790910af66f0f7b1a

%gometa

%global common_description %{expand:
Implementation of XMLRPC protocol in Go language with some changes to interact
with the SoftLayer api.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Implementation of XMLRPC protocol in Go language with some changes to interact with the SoftLayer api

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/encoding/charmap)

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/text/transform)
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

