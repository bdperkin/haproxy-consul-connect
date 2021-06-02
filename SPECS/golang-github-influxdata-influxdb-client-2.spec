# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/influxdata/influxdb-client-go
%global goipath         github.com/influxdata/influxdb-client-go/v2
%global forgeurl        https://github.com/influxdata/influxdb-client-go
Version:                2.3.0

%gometa

%global common_description %{expand:
InfluxDB 2 Go Client.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md domain/Readme.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        InfluxDB 2 Go Client

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/deepmap/oapi-codegen/pkg/runtime)
BuildRequires:  golang(github.com/influxdata/line-protocol)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/net/publicsuffix)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
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

