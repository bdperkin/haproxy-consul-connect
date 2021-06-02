# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/dominikh/go-tools
%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
Version:                0.2.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE LICENSE-THIRD-PARTY go/gcsizes/LICENSE\\\
                        go/ir/LICENSE
%global godocs          doc README.md cmd/keyify/README.md\\\
                        cmd/staticcheck/README.md cmd/structlayout/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: BSD-3-Clause and MIT
License:        BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(golang.org/x/tools/go/analysis)
BuildRequires:  golang(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  golang(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/go/ast/inspector)
BuildRequires:  golang(golang.org/x/tools/go/buildutil)
BuildRequires:  golang(golang.org/x/tools/go/loader)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/tools/go/types/objectpath)
BuildRequires:  golang(golang.org/x/tools/go/types/typeutil)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in go/ir; do
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
%license LICENSE LICENSE-THIRD-PARTY go/gcsizes/LICENSE go/ir/LICENSE
%doc doc README.md cmd/keyify/README.md cmd/staticcheck/README.md
%doc cmd/structlayout/README.md
%{_bindir}/*

%gopkgfiles

%changelog

