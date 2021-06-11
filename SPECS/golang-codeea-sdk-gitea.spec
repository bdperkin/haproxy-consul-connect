# Generated by go2rpm 1.3
%bcond_without check

# https://gitea.com/gitea/go-sdk
%global goipath         code.gitea.io/sdk/gitea
%global forgeurl        https://gitea.com/gitea/go-sdk
Version:                0.13.3
%global tag             gitea/v0.13.3

%gometa

%global goaltipaths     gitea.com/gitea/go-sdk codeea.io/sdk/gitea

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          docs CONTRIBUTING.md CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-version)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
%gocheck -r .*gitea.*
%endif

%gopkgfiles

%changelog

