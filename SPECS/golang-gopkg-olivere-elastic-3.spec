# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/olivere/elastic
%global goipath         gopkg.in/olivere/elastic.v3
%global forgeurl        https://github.com/olivere/elastic
Version:                3.0.75

%gometa

%global common_description %{expand:
Package elastic provides an interface to the Elasticsearch server
(http://www.elasticsearch.org/). The first thing you do is to create a Client.
If you have Elasticsearch}

%global golicenses      LICENSE backoff/LICENSE uritemplates/LICENSE
%global godocs          CHANGELOG-3.0.md CODE_OF_CONDUCT.md ISSUE_TEMPLATE.md\\\
                        README.md CONTRIBUTING.md CONTRIBUTORS cluster-\\\
                        test/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package elastic provides an interface to the Elasticsearch server (http://www

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/fortytw2/leaktest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cluster-test; do
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
%license LICENSE backoff/LICENSE uritemplates/LICENSE
%doc CHANGELOG-3.0.md CODE_OF_CONDUCT.md ISSUE_TEMPLATE.md README.md
%doc CONTRIBUTING.md CONTRIBUTORS cluster-test/README.md
%{_bindir}/*

%gopkgfiles

%changelog

