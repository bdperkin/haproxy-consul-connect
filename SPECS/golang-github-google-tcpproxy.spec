# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/google/tcpproxy
%global goipath         github.com/google/tcpproxy
%global commit          b6bb9b5b82524122bcf27291ede32d1517a14ab8

%gometa

%global common_description %{expand:
Proxy TCP connections based on static rules, HTTP Host headers, and SNI server
names (Go package or binary).}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md README-cmd-tlsrouter.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Proxy TCP connections based on static rules, HTTP Host headers, and SNI server names (Go package or binary)

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/armon/go-proxyproto)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv cmd/tlsrouter/README.md README-cmd-tlsrouter.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck -r .*tcpproxy.*
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md README-cmd-tlsrouter.md

%gopkgfiles

%changelog

