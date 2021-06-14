# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/google/go-github
%global goipath         github.com/google/go-github/v28
%global forgeurl        https://github.com/google/go-github
Version:                28.1.1

%gometa

%global common_description %{expand:
Go library for accessing the GitHub API.}

%global golicenses      LICENSE licenses-github.go licenses_test-github.go
%global godocs          example AUTHORS CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for accessing the GitHub API

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(google.golang.org/appengine)
BuildRequires:  golang(google.golang.org/appengine/log)

%description
%{common_description}

%gopkg

%prep
%goprep
mv github/licenses.go licenses-github.go
mv github/licenses_test.go licenses_test-github.go

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE licenses-github.go licenses_test-github.go
%doc example AUTHORS CONTRIBUTING.md README.md

%gopkgfiles

%changelog

