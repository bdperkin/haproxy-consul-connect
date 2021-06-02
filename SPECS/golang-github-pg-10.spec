# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-pg/pg
%global goipath         github.com/go-pg/pg/v10
%global forgeurl        https://github.com/go-pg/pg
Version:                10.9.3

%gometa

%global common_description %{expand:
pg provides PostgreSQL client.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md example extra/pgotel/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        pg provides PostgreSQL client

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-pg/zerochecker)
BuildRequires:  golang(github.com/jinzhu/inflection)
BuildRequires:  golang(github.com/segmentio/encoding/json)
BuildRequires:  golang(github.com/tmthrgd/go-hex)
BuildRequires:  golang(github.com/vmihailenco/bufpool)
BuildRequires:  golang(github.com/vmihailenco/msgpack/v5)
BuildRequires:  golang(github.com/vmihailenco/tagparser)
BuildRequires:  golang(go.opentelemetry.io/otel)
BuildRequires:  golang(go.opentelemetry.io/otel/attribute)
BuildRequires:  golang(go.opentelemetry.io/otel/codes)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/stdout)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/trace)
BuildRequires:  golang(go.opentelemetry.io/otel/trace)
BuildRequires:  golang(mellium.im/sasl)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
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

