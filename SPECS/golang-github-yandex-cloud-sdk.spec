# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/yandex-cloud/go-sdk
%global goipath         github.com/yandex-cloud/go-sdk
%global commit          60f10506e77bfa48f0cc4c65bf24f8232697febb

%gometa

%global common_description %{expand:
Yandex.Cloud Go SDK.}

%global golicenses      LICENSE dial/LICENSE pkg/singleflight/LICENSE
%global godocs          examples AUTHORS CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Yandex.Cloud Go SDK

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/c2h5oh/datasize)
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/ghodss/yaml)
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/mitchellh/go-testing-interface)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/access)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/ai/stt/v2)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/ai/translate/v2)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/certificatemanager/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1/instancegroup)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/dns/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/endpoint)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1/awscompatibility)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/k8s/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/loadbalancer/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/marketplace/v1/metering)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/redis/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/mdb/sqlserver/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/operation)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/quota)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/serverless/apigateway/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/serverless/functions/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1)
BuildRequires:  golang(github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires:  golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
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

