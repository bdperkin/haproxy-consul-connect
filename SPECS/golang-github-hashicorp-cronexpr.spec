# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/hashicorp/cronexpr
%global goipath         github.com/hashicorp/cronexpr
Version:                1.1.1

%gometa

%global common_description %{expand:
# FIXME}

%global godocs          README.md cronexpr/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gorhill/cronexpr)

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

%files
%doc README.md cronexpr/README.md

%gopkgfiles

%changelog

