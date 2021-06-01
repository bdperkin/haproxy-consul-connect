# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/sethgrid/curse
%global goipath         github.com/sethgrid/curse
%global commit          d4ee583ebf0f588f3594a262c5e2726ddebda2cc

%gometa

%global common_description %{expand:
Basic terminal cursor manipulation.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Basic terminal cursor manipulation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/kless/term)
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

