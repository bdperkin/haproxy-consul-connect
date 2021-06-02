# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/tencentcloud/tencentcloud-sdk-go
%global goipath         github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common
%global forgeurl        https://github.com/tencentcloud/tencentcloud-sdk-go
Version:                1.0.173

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          examples README.md CHANGELOG.md products.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

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

