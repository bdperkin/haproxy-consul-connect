# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/softlayer/softlayer-go
%global goipath         github.com/softlayer/softlayer-go
Version:                1.0.3

%gometa

%global common_description %{expand:
SoftLayer API Client for the Go Language.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        SoftLayer API Client for the Go Language

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/softlayer/xmlrpc)
BuildRequires:  golang(golang.org/x/tools/imports)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/jarcoal/httpmock)
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

%files
%license LICENSE
%doc examples README.md

%gopkgfiles

%changelog

