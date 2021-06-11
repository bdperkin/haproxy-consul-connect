# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/hashicorp/consul-template
%global goipath         github.com/hashicorp/consul-template
Version:                0.26.0

%gometa

%global common_description %{expand:
Template rendering, notifier, and supervisor for @HashiCorp Consul and Vault
data.}

%global golicenses      LICENSE
%global godocs          docs examples CHANGELOG.md README.md\\\
                        readme-toc-scripts.sh

Name:           %{goname}
Release:        1%{?dist}
Summary:        Template rendering, notifier, and supervisor for @HashiCorp Consul and Vault data

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hashicorp/consul/sdk/testutil)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/hashicorp/go-rootcerts)
BuildRequires:  golang(github.com/hashicorp/go-sockaddr/template)
BuildRequires:  golang(github.com/hashicorp/go-syslog)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/hashicorp/logutils)
BuildRequires:  golang(github.com/hashicorp/vault/api)
BuildRequires:  golang(github.com/mattn/go-shellwords)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/mitchellh/hashstructure)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/hashicorp/go-gatedio)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv scripts/readme-toc.sh readme-toc-scripts.sh

%build
%gobuild -o %{gobuilddir}/bin/consul-template %{goipath}

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
%doc docs examples CHANGELOG.md README.md readme-toc-scripts.sh
%{_bindir}/*

%gopkgfiles

%changelog

