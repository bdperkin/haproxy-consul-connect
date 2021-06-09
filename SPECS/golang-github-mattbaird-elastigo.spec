# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/mattbaird/elastigo
%global goipath         github.com/mattbaird/elastigo
Version:                1.0
%global commit          2fe47fd29e4b70353f852ede77a196830d2924ec

%gometa

%global common_description %{expand:
Copyright 2012 Matthew Baird Licensed under the Apache License, Version 2.0
(the "License");}

%global golicenses      LICENSE LICENSE-cookbooks-build-essential\\\
                        LICENSE-cookbooks-git LICENSE-cookbooks-mercurial
%global godocs          HACKING.md README.md\\\
                        CHANGELOG-cookbooks-build-essential.md\\\
                        README-cookbooks-build-essential.md\\\
                        CHANGELOG-cookbooks-git.md README-cookbooks-git.md\\\
                        README-cookbooks-golang.md\\\
                        CHANGELOG-cookbooks-mercurial.md\\\
                        README-cookbooks-mercurial.md README-tutorial.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Copyright 2012 Matthew Baird Licensed under the Apache License, Version 2

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/araddon/gou)
BuildRequires:  golang(github.com/bitly/go-hostpool)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/bmizerany/assert)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv cookbooks/build-essential/LICENSE LICENSE-cookbooks-build-essential
mv cookbooks/git/LICENSE LICENSE-cookbooks-git
mv cookbooks/mercurial/LICENSE LICENSE-cookbooks-mercurial
mv cookbooks/build-essential/CHANGELOG.md CHANGELOG-cookbooks-build-essential.md
mv cookbooks/build-essential/README.md README-cookbooks-build-essential.md
mv cookbooks/git/CHANGELOG.md CHANGELOG-cookbooks-git.md
mv cookbooks/git/README.md README-cookbooks-git.md
mv cookbooks/golang/README.md README-cookbooks-golang.md
mv cookbooks/mercurial/CHANGELOG.md CHANGELOG-cookbooks-mercurial.md
mv cookbooks/mercurial/README.md README-cookbooks-mercurial.md
mv tutorial/README.md README-tutorial.md

%build
%gobuild -o %{gobuilddir}/bin/elastigo %{goipath}
for cmd in tutorial; do
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
%license LICENSE LICENSE-cookbooks-build-essential LICENSE-cookbooks-git
%license LICENSE-cookbooks-mercurial
%doc HACKING.md README.md CHANGELOG-cookbooks-build-essential.md
%doc README-cookbooks-build-essential.md CHANGELOG-cookbooks-git.md
%doc README-cookbooks-git.md README-cookbooks-golang.md
%doc CHANGELOG-cookbooks-mercurial.md README-cookbooks-mercurial.md
%doc README-tutorial.md
%{_bindir}/*

%gopkgfiles

%changelog

