# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/coreos/go-etcd
%global goipath         github.com/coreos/go-etcd
Version:                2.0.0

%gometa

%global common_description %{expand:
DEPRECATED - please use the official client at
https://github.com/coreos/etcd/tree/master/client.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        DEPRECATED - please use the official client at https://github.com/coreos/etcd/tree/master/client

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -r .*etcd.*
%endif

%gopkgfiles

%changelog

