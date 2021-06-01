# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/google/go-metrics-stackdriver
%global goipath         github.com/google/go-metrics-stackdriver
Version:                0.2.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          example CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(cloud.google.com/go/monitoring/apiv3)
BuildRequires:  golang(github.com/armon/go-metrics)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/distribution)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/metric)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires:  golang(google.golang.org/genproto/googleapis/monitoring/v3)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/test/bufconn)
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

