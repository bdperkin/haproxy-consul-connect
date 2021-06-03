# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/benbjohnson/tmpl
%global goipath         github.com/benbjohnson/tmpl
Version:                1.1.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dustin/go-humanize/english)
BuildRequires:  golang(github.com/Masterminds/sprig)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/tmpl %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog

