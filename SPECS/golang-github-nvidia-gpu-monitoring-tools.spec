# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/NVIDIA/gpu-monitoring-tools
%global goipath         github.com/NVIDIA/gpu-monitoring-tools
Version:                2.4.0~rc.2
%global tag             2.4.0-rc.2

%gometa
%global extractdir      gpu-monitoring-tools-2.4.0-rc.2

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md RELEASE.md\\\
                        README-bindings-go-samples-dcgm.md\\\
                        README-bindings-go-samples-dcgm-restApi.md\\\
                        README-bindings-go-samples-nvml.md\\\
                        NOTES-deployment-dcgm-exporter-templates.txt

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/Masterminds/semver)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/urfave/cli/v2)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(k8s.io/kubelet/pkg/apis/podresources/v1alpha1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(k8s.io/kubernetes/pkg/kubelet/apis/podresources/v1alpha1)
BuildRequires:  golang(k8s.io/kubernetes/pkg/kubelet/util)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv bindings/go/samples/dcgm/README.md README-bindings-go-samples-dcgm.md
mv bindings/go/samples/dcgm/restApi/README.md README-bindings-go-samples-dcgm-restApi.md
mv bindings/go/samples/nvml/README.md README-bindings-go-samples-nvml.md
mv deployment/dcgm-exporter/templates/NOTES.txt NOTES-deployment-dcgm-exporter-templates.txt

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md RELEASE.md README-bindings-go-samples-dcgm.md
%doc README-bindings-go-samples-dcgm-restApi.md
%doc README-bindings-go-samples-nvml.md
%doc NOTES-deployment-dcgm-exporter-templates.txt

%gopkgfiles

%changelog

