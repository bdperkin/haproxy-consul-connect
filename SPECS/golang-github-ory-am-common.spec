# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/ory-am/common
%global goipath         github.com/ory-am/common
Version:                0.4.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          README.md compiler/README.md env/README.md\\\
                        rand/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/go-redis/redis)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/nats-io/go-nats)
BuildRequires:  golang(github.com/oleiade/reflections)
BuildRequires:  golang(github.com/ory-am/dockertest)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/Sirupsen/logrus)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/gorethink/gorethink.v3)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/ory-am/dockertest.v3)
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

