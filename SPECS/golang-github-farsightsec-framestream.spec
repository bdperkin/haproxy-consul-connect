# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/farsightsec/golang-framestream
%global goipath         github.com/farsightsec/golang-framestream
Version:                0.3.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      COPYRIGHT LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in framestream_dump; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license COPYRIGHT LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog

