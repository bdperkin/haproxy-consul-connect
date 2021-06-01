# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/zvelo/ttlru
%global goipath         zvelo.io/ttlru
%global forgeurl        https://github.com/zvelo/ttlru
Version:                1.0.10

%gometa

%global common_description %{expand:
A simple, goroutine-safe, cache with a global TTL, a fixed size and an LRU
eviction policy for Go (golang).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A simple, goroutine-safe, cache with a global TTL, a fixed size and an LRU eviction policy for Go (golang)

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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

