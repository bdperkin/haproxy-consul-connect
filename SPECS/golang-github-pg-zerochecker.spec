# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-pg/zerochecker
%global goipath         github.com/go-pg/zerochecker
Version:                0.2.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: BSD-2-Clause
License:        BSD
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
%gocheck
%endif

%gopkgfiles

%changelog

