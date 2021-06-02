# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/mongodb/go-client-mongodb-atlas
%global goipath         github.com/mongodb/go-client-mongodb-atlas
Version:                0.3.0

%gometa

%global common_description %{expand:
Go Client for MongoDB Atlas.}

%global golicenses      LICENSE
%global godocs          CODEOWNERS.md CHANGELOG.md CONTRIBUTING.md README.md\\\
                        pull_request_template.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go Client for MongoDB Atlas

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)
BuildRequires:  golang(github.com/openlyinc/pointy)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-test/deep)
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

