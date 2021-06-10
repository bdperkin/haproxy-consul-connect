# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/infobloxopen/go-trees
%global goipath         github.com/infobloxopen/go-trees
%global commit          96a057b8dfb9e64b6d71bbc262f20b6060d34ea0

%gometa

%global common_description %{expand:
Go packages for radix and other trees.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go packages for radix and other trees

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)
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
%doc README.md

%gopkgfiles

%changelog

