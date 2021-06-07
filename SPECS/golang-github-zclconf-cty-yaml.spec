# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/zclconf/go-cty-yaml
%global goipath         github.com/zclconf/go-cty-yaml
Version:                1.0.2

%gometa

%global common_description %{expand:
YAML marshalling and unmarshalling for go-cty.}

%global golicenses      LICENSE LICENSE.libyaml NOTICE
%global godocs          CHANGELOG.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        YAML marshalling and unmarshalling for go-cty

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/zclconf/go-cty/cty)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/convert)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/function)

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

