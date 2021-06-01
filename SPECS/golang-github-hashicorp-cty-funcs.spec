# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/hashicorp/go-cty-funcs
%global goipath         github.com/hashicorp/go-cty-funcs
%global commit          2721b1e368400d56e5ade1763ae55ff2367897b5

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        None

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/apparentlymart/go-cidr/cidr)
BuildRequires:  golang(github.com/bmatcuk/doublestar)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/zclconf/go-cty/cty)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/convert)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/function)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/gocty)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)

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

