# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/ory/dockertest
%global goipath         github.com/ory/dockertest
Version:                3.3.5

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE DOCKER-LICENSE-docker LICENSE-docker
%global godocs          docs examples CONTRIBUTING.md README.md SECURITY.md\\\
                        AUTHORS-docker README-docker.markdown\\\
                        README-docker-pkg.md README-docker-pkg-archive.md\\\
                        README-docker-types-versions.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0 and BSD-2-Clause
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Azure/go-ansiterm)
BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/containerd/continuity/pathdriver)
BuildRequires:  golang(github.com/docker/go-connections/nat)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/Nvveen/Gotty)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/gotestyourself/gotestyourself/assert)
BuildRequires:  golang(github.com/gotestyourself/gotestyourself/assert/cmp)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv docker/DOCKER-LICENSE DOCKER-LICENSE-docker
mv docker/LICENSE LICENSE-docker
mv docker/AUTHORS AUTHORS-docker
mv docker/README.markdown README-docker.markdown
mv docker/pkg/README.md README-docker-pkg.md
mv docker/pkg/archive/README.md README-docker-pkg-archive.md
mv docker/types/versions/README.md README-docker-types-versions.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE DOCKER-LICENSE-docker LICENSE-docker
%doc docs examples CONTRIBUTING.md README.md SECURITY.md AUTHORS-docker
%doc README-docker.markdown README-docker-pkg.md README-docker-pkg-archive.md
%doc README-docker-types-versions.md

%gopkgfiles

%changelog

