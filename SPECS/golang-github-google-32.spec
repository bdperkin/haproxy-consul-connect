# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/google/go-github
%global goipath         github.com/google/go-github/v32
%global forgeurl        https://github.com/google/go-github
Version:                32.1.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE licenses-github.go licenses_test-github.go
%global godocs          example AUTHORS CONTRIBUTING.md README.md example\\\
                        README-scrape.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)
BuildRequires:  golang(github.com/PuerkitoBio/goquery)
BuildRequires:  golang(github.com/xlzd/gotp)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/publicsuffix)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(google.golang.org/appengine)
BuildRequires:  golang(google.golang.org/appengine/log)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv github/licenses.go licenses-github.go
mv github/licenses_test.go licenses_test-github.go
mv scrape/README.md README-scrape.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck -r .*github.*
%endif

%files
%license LICENSE licenses-github.go licenses_test-github.go
%doc example AUTHORS CONTRIBUTING.md README.md example README-scrape.md

%gopkgfiles

%changelog

