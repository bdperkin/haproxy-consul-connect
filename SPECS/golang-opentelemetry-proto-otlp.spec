# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/open-telemetry/opentelemetry-proto-go
%global goipath         go.opentelemetry.io/proto/otlp
%global forgeurl        https://github.com/open-telemetry/opentelemetry-proto-go
Version:                0.9.0

%gometa

%global goaltipaths     github.com/open-telemetry/opentelemetry-proto-go/otlp

%global common_description %{expand:
Generated code for OpenTelemetry protobuf data model.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Generated code for OpenTelemetry protobuf data model

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
BuildRequires:  golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)

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

