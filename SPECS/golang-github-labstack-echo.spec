# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/labstack/echo
%global goipath         github.com/labstack/echo
Version:                4.3.0

%gometa

%global common_description %{expand:
High performance, minimalist Go web framework.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md _fixture/_fixture/README.md\\\
                        _fixture/certs/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        High performance, minimalist Go web framework

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/labstack/gommon/bytes)
BuildRequires:  golang(github.com/labstack/gommon/color)
BuildRequires:  golang(github.com/labstack/gommon/log)
BuildRequires:  golang(github.com/labstack/gommon/random)
BuildRequires:  golang(github.com/valyala/fasttemplate)
BuildRequires:  golang(golang.org/x/crypto/acme)
BuildRequires:  golang(golang.org/x/crypto/acme/autocert)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/h2c)
BuildRequires:  golang(golang.org/x/time/rate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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

