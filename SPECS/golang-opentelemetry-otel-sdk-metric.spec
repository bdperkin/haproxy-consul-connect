# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/open-telemetry/opentelemetry-go
%global goipath         go.opentelemetry.io/otel/sdk/metric
%global forgeurl        https://github.com/open-telemetry/opentelemetry-go
Version:                0.20.0

%gometa

%global goaltipaths     github.com/open-telemetry/opentelemetry-go/sdk/metric

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          example VERSIONING.md CHANGELOG.md CONTRIBUTING.md\\\
                        README.md RELEASING.md bridge/opencensus/README.md\\\
                        exporters/README.md\\\
                        exporters/metric/prometheus/README.md\\\
                        exporters/otlp/README.md\\\
                        exporters/trace/jaeger/README.md sdk/README.md\\\
                        website_docs/_index.md website_docs/exporting_data.md\\\
                        website_docs/getting-started.md\\\
                        website_docs/instrumentation.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/benbjohnson/clock)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/openzipkin/zipkin-go/model)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.opencensus.io/metric)
BuildRequires:  golang(go.opencensus.io/metric/metricdata)
BuildRequires:  golang(go.opencensus.io/metric/metricexport)
BuildRequires:  golang(go.opencensus.io/metric/metricproducer)
BuildRequires:  golang(go.opencensus.io/resource)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opentelemetry.io/otel)
BuildRequires:  golang(go.opentelemetry.io/otel/attribute)
BuildRequires:  golang(go.opentelemetry.io/otel/baggage)
BuildRequires:  golang(go.opentelemetry.io/otel/bridge/opencensus)
BuildRequires:  golang(go.opentelemetry.io/otel/bridge/opencensus/utils)
BuildRequires:  golang(go.opentelemetry.io/otel/bridge/opentracing/migration)
BuildRequires:  golang(go.opentelemetry.io/otel/codes)
BuildRequires:  golang(go.opentelemetry.io/otel/example/namedtracer/foo)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/metric/prometheus)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp/internal/otlpconfig)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp/internal/transform)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp/otlpgrpc)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/stdout)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/jaeger)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/jaeger/internal/gen-go/agent)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/jaeger/internal/gen-go/jaeger)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/jaeger/internal/gen-go/zipkincore)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/jaeger/internal/third_party/thrift/lib/go/thrift)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/trace/zipkin)
BuildRequires:  golang(go.opentelemetry.io/otel/internal)
BuildRequires:  golang(go.opentelemetry.io/otel/internal/baggage)
BuildRequires:  golang(go.opentelemetry.io/otel/internal/global)
BuildRequires:  golang(go.opentelemetry.io/otel/internal/internaltest)
BuildRequires:  golang(go.opentelemetry.io/otel/internal/matchers)
BuildRequires:  golang(go.opentelemetry.io/otel/internal/metric)
BuildRequires:  golang(go.opentelemetry.io/otel/internal/trace/noop)
BuildRequires:  golang(go.opentelemetry.io/otel/metric)
BuildRequires:  golang(go.opentelemetry.io/otel/metric/global)
BuildRequires:  golang(go.opentelemetry.io/otel/metric/number)
BuildRequires:  golang(go.opentelemetry.io/otel/metric/registry)
BuildRequires:  golang(go.opentelemetry.io/otel/propagation)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/export/metric)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/export/metric/aggregation)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/instrumentation)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/internal)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/resource)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/trace)
BuildRequires:  golang(go.opentelemetry.io/otel/semconv)
BuildRequires:  golang(go.opentelemetry.io/otel/trace)
BuildRequires:  golang(go.opentelemetry.io/otel/unit)
BuildRequires:  golang(go.opentelemetry.io/proto/otlp/collector/metrics/v1)
BuildRequires:  golang(go.opentelemetry.io/proto/otlp/collector/trace/v1)
BuildRequires:  golang(go.opentelemetry.io/proto/otlp/common/v1)
BuildRequires:  golang(go.opentelemetry.io/proto/otlp/metrics/v1)
BuildRequires:  golang(go.opentelemetry.io/proto/otlp/resource/v1)
BuildRequires:  golang(go.opentelemetry.io/proto/otlp/trace/v1)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/encoding/gzip)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/protobuf/encoding/protojson)
BuildRequires:  golang(google.golang.org/protobuf/proto)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(go.opencensus.io/trace/tracestate)
BuildRequires:  golang(go.opentelemetry.io/otel/bridge/opentracing/internal)
BuildRequires:  golang(go.opentelemetry.io/otel/oteltest)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/export/metric/metrictest)
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

