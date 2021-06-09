# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/dominikh/go-tools
%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
Version:                0.2.0

%gometa

%global goaltipaths     github.com/dominikh/go-tools

%global common_description %{expand:
Staticcheck - The advanced Go linter.}

%global golicenses      LICENSE LICENSE-THIRD-PARTY LICENSE-go-gcsizes\\\
                        LICENSE-go-ir
%global godocs          doc README.md README-cmd-keyify.md\\\
                        README-cmd-staticcheck.md README-cmd-structlayout.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Staticcheck - The advanced Go linter

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
mv go/gcsizes/LICENSE LICENSE-go-gcsizes
mv go/ir/LICENSE LICENSE-go-ir
mv cmd/keyify/README.md README-cmd-keyify.md
mv cmd/staticcheck/README.md README-cmd-staticcheck.md
mv cmd/structlayout/README.md README-cmd-structlayout.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE LICENSE-THIRD-PARTY LICENSE-go-gcsizes LICENSE-go-ir
%doc doc README.md README-cmd-keyify.md README-cmd-staticcheck.md
%doc README-cmd-structlayout.md

%gopkgfiles

%changelog

