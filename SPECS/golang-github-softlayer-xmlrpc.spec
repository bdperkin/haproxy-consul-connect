# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/softlayer/xmlrpc
%global goipath         github.com/softlayer/xmlrpc
Version:                1.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

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

