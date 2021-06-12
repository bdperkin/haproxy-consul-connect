# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/checkpoint-restore/go-criu
%global goipath         github.com/checkpoint-restore/go-criu/v4
%global forgeurl        https://github.com/checkpoint-restore/go-criu
Version:                4.1.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/thoas/go-funk)

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

