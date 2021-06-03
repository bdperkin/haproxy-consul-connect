# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/haproxytech/haproxy-consul-connect
%global goipath         github.com/haproxytech/haproxy-consul-connect
Version:                0.9.0

%gometa

%global common_description %{expand:
HaProxy Connector for Consul Connect. Enables Service Mesh with Consul and
HaProxy using TLS and Consul Discovery.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        HaProxy Connector for Consul Connect. Enables Service Mesh with Consul and HaProxy using TLS and Consul Discovery

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/criteo/haproxy-spoe-go)
BuildRequires:  golang(github.com/haproxytech/models/v2)
BuildRequires:  golang(github.com/hashicorp/consul/agent/connect)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hashicorp/consul/command/connect/proxy)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promauto)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(gopkg.in/d4l3k/messagediff.v1)
BuildRequires:  golang(gopkg.in/mcuadros/go-syslog.v2)
BuildRequires:  golang(zvelo.io/ttlru)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/facebookgo/freeport)
BuildRequires:  golang(github.com/hashicorp/consul/agent)
BuildRequires:  golang(github.com/hashicorp/consul/testrpc)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/haproxy-consul-connect %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog

