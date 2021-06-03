# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/open-telemetry/opentelemetry-go-contrib
%global goipath         go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
%global forgeurl        https://github.com/open-telemetry/opentelemetry-go-contrib
Version:                0.20.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          RELEASING.md CHANGELOG.md CONTRIBUTING.md README.md\\\
                        example exporters/metric/cortex/README.md\\\
                        exporters/metric/cortex/utils/README.md\\\
                        instrumentation/README.md example example example\\\
                        example example example example example example\\\
                        example example example example example example\\\
                        example examples propagators/opencensus/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(github.com/astaxie/beego)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/aws/middleware)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/dynamodb)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/s3)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/smithy-go/middleware)
BuildRequires:  golang(github.com/aws/smithy-go/transport/http)
BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/DataDog/datadog-go/statsd)
BuildRequires:  golang(github.com/emicklei/go-restful/v3)
BuildRequires:  golang(github.com/felixge/httpsnoop)
BuildRequires:  golang(github.com/gin-gonic/gin)
BuildRequires:  golang(github.com/go-kit/kit/endpoint)
BuildRequires:  golang(github.com/go-kit/kit/sd/lb)
BuildRequires:  golang(github.com/gocql/gocql)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/labstack/echo/v4)
BuildRequires:  golang(github.com/prometheus/prometheus/prompb)
BuildRequires:  golang(github.com/shirou/gopsutil/cpu)
BuildRequires:  golang(github.com/shirou/gopsutil/mem)
BuildRequires:  golang(github.com/shirou/gopsutil/net)
BuildRequires:  golang(github.com/shirou/gopsutil/process)
BuildRequires:  golang(github.com/Shopify/sarama)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson)
BuildRequires:  golang(go.mongodb.org/mongo-driver/event)
BuildRequires:  golang(go.opencensus.io/examples/exporter)
BuildRequires:  golang(go.opencensus.io/examples/grpc/proto)
BuildRequires:  golang(go.opencensus.io/plugin/ocgrpc)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/propagation)
BuildRequires:  golang(go.opentelemetry.io/contrib)
BuildRequires:  golang(go.opentelemetry.io/contrib/exporters/metric/cortex)
BuildRequires:  golang(go.opentelemetry.io/contrib/exporters/metric/cortex/utils)
BuildRequires:  golang(go.opentelemetry.io/contrib/exporters/metric/dogstatsd/internal/statsd)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/astaxie/beego/otelbeego)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/aws/aws-sdk-go-v2/otelaws)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/bradfitz/gomemcache/memcache/otelmemcache)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/emicklei/go-restful/otelrestful)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/go-kit/kit/otelkit)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/gocql/gocql/otelgocql)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/gorilla/mux/otelmux)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/labstack/echo/otelecho)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/Shopify/sarama/otelsarama)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/github.com/Shopify/sarama/otelsarama/example)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc/example/api)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc/example/config)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/gopkg.in/macaron.v1/otelmacaron)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/host)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/runtime)
BuildRequires:  golang(go.opentelemetry.io/contrib/propagation/opencensus)
BuildRequires:  golang(go.opentelemetry.io/otel)
BuildRequires:  golang(go.opentelemetry.io/otel/attribute)
BuildRequires:  golang(go.opentelemetry.io/otel/baggage)
BuildRequires:  golang(go.opentelemetry.io/otel/bridge/opencensus/utils)
BuildRequires:  golang(go.opentelemetry.io/otel/codes)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/metric/prometheus)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/stdout)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/zipkin)
BuildRequires:  golang(go.opentelemetry.io/otel/metric)
BuildRequires:  golang(go.opentelemetry.io/otel/metric/global)
BuildRequires:  golang(go.opentelemetry.io/otel/metric/number)
BuildRequires:  golang(go.opentelemetry.io/otel/propagation)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/export/metric)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/export/metric/aggregation)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/aggregator/histogram)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/controller/basic)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/processor/basic)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/selector/simple)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/resource)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/trace)
BuildRequires:  golang(go.opentelemetry.io/otel/semconv)
BuildRequires:  golang(go.opentelemetry.io/otel/trace)
BuildRequires:  golang(go.opentelemetry.io/otel/unit)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/macaron.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/astaxie/beego/context)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/route53)
BuildRequires:  golang(github.com/aws/aws-sdk-go-v2/service/route53/types)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/Shopify/sarama/mocks)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo/options)
BuildRequires:  golang(go.opentelemetry.io/contrib/internal/util)
BuildRequires:  golang(go.opentelemetry.io/contrib/propagators/b3)
BuildRequires:  golang(go.opentelemetry.io/otel/oteltest)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/export/metric/metrictest)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/aggregator/aggregatortest)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/aggregator/lastvalue)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/aggregator/minmaxsumcount)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/metric/aggregator/sum)
BuildRequires:  golang(go.uber.org/goleak)
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

