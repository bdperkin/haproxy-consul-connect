# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-stomp/stomp
%global goipath         github.com/go-stomp/stomp
Version:                2.1.4

%gometa

%global common_description %{expand:
Go language library for STOMP protocol.}

%global golicenses      LICENSE.txt
%global godocs          examples AUTHORS.md README.md breaking_changes.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go language library for STOMP protocol

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/check.v1)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in stompd; do
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
%license LICENSE.txt
%doc examples AUTHORS.md README.md breaking_changes.md
%{_bindir}/*

%gopkgfiles

%changelog

