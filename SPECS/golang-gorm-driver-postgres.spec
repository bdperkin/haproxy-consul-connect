# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-gorm/postgres
%global goipath         gorm.io/driver/postgres
%global forgeurl        https://github.com/go-gorm/postgres
Version:                1.1.0

%gometa

%global common_description %{expand:
# FIXME}

%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jackc/pgx/v4)
BuildRequires:  golang(github.com/jackc/pgx/v4/stdlib)
BuildRequires:  golang(gorm.io/gorm)
BuildRequires:  golang(gorm.io/gorm/callbacks)
BuildRequires:  golang(gorm.io/gorm/clause)
BuildRequires:  golang(gorm.io/gorm/logger)
BuildRequires:  golang(gorm.io/gorm/migrator)
BuildRequires:  golang(gorm.io/gorm/schema)

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

