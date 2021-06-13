# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/gotestyourself/gotestyourself
%global goipath         github.com/gotestyourself/gotestyourself
Version:                2.2.0

%gometa
%global extractdir      gotest.tools-%{version}

%global common_description %{expand:
Package gotesttools is a collection of packages to augment `testing` and
support common patterns.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package gotesttools is a collection of packages to augment `testing` and support common patterns

# Upstream license specification: Apache-2.0 and BSD-3-Clause
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/go/loader)
BuildRequires:  golang(golang.org/x/tools/imports)
BuildRequires:  golang(gotest.tools/assert)
BuildRequires:  golang(gotest.tools/assert/cmp)
BuildRequires:  golang(gotest.tools/internal/difflib)
BuildRequires:  golang(gotest.tools/internal/format)
BuildRequires:  golang(gotest.tools/internal/source)
BuildRequires:  golang(gotest.tools/x/subtest)

%if %{with check}
# Tests
BuildRequires:  golang(gotest.tools/env)
BuildRequires:  golang(gotest.tools/fs)
BuildRequires:  golang(gotest.tools/golden)
BuildRequires:  golang(gotest.tools/internal/maint)
BuildRequires:  golang(gotest.tools/skip)
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
%gocheck -r .*assert.* -r .*env.* -r .*fs.* -r .*golden.* -r .*icmd.* -r .*poll.*
%endif

%gopkgfiles

%changelog

