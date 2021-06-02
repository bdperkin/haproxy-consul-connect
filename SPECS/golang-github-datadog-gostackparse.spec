# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/DataDog/gostackparse
%global goipath         github.com/DataDog/gostackparse
Version:                0.5.0

%gometa

%global common_description %{expand:
Package gostackparse parses goroutines stack traces as produced by panic() or
debug.Stack() at ~300 MiB/s.}

%global golicenses      LICENSE-3rdparty.csv LICENSE-APACHE LICENSE-BSD3\\\
                        LICENSE
%global godocs          example CONTRIBUTING.md README.md test-\\\
                        fixtures/cgo.txt test-fixtures/empty_input.txt test-\\\
                        fixtures/empty_stack.txt test-\\\
                        fixtures/errorhandling.txt test-\\\
                        fixtures/frameselided.txt test-\\\
                        fixtures/frameselided_goroutine.txt test-\\\
                        fixtures/lockedm.txt test-\\\
                        fixtures/partial_createdby.txt test-\\\
                        fixtures/partial_stack.txt test-\\\
                        fixtures/waitsince.txt

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package gostackparse parses goroutines stack traces as produced by panic() or debug

# Upstream license specification: Apache-2.0 and BSD-3-Clause
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in test-fixtures; do
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
%license LICENSE-3rdparty.csv LICENSE-APACHE LICENSE-BSD3 LICENSE
%doc example CONTRIBUTING.md README.md test-fixtures/cgo.txt
%doc test-fixtures/empty_input.txt test-fixtures/empty_stack.txt
%doc test-fixtures/errorhandling.txt test-fixtures/frameselided.txt
%doc test-fixtures/frameselided_goroutine.txt test-fixtures/lockedm.txt
%doc test-fixtures/partial_createdby.txt test-fixtures/partial_stack.txt
%doc test-fixtures/waitsince.txt
%{_bindir}/*

%gopkgfiles

%changelog

