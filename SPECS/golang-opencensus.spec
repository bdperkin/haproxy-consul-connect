# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/census-instrumentation/opencensus-go
%global goipath         go.opencensus.io
%global forgeurl        https://github.com/census-instrumentation/opencensus-go
Version:                0.23.0

%gometa

%global goaltipaths     github.com/census-instrumentation/opencensus-go

%global common_description %{expand:
Package opencensus contains Go support for OpenCensus.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package opencensus contains Go support for OpenCensus

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/stats)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(golang.org/x/net/http2)
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
%gocheck -r .*ochttp.*
%endif

%gopkgfiles

%changelog

