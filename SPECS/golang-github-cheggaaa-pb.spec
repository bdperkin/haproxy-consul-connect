# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/cheggaaa/pb
%global goipath         github.com/cheggaaa/pb
Version:                1.0.29

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE v3/LICENSE
%global godocs          README_V1.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/VividCortex/ewma)
BuildRequires:  golang(golang.org/x/sys/unix)

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

