# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/nicolai86/scaleway-sdk
%global goipath         github.com/nicolai86/scaleway-sdk
Version:                1.11.1

%gometa

%global common_description %{expand:
Minimal Scaleway API SDK.}

%global golicenses      LICENSE.md
%global godocs          examples README.md README-dist.md README-pkg-api.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Minimal Scaleway API SDK

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/docker/docker/pkg/archive)
BuildRequires:  golang(github.com/docker/docker/pkg/mflag)
BuildRequires:  golang(github.com/docker/docker/pkg/namesgenerator)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/hashicorp/go-version)
BuildRequires:  golang(github.com/kardianos/osext)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/moul/anonuuid)
BuildRequires:  golang(github.com/moul/gotty-client)
BuildRequires:  golang(github.com/moul/http2curl)
BuildRequires:  golang(github.com/renstrom/fuzzysearch/fuzzy)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/api)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/cli)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/clilogger)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/commands)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/config)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/pricing)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/scwversion)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/sshcommand)
BuildRequires:  golang(github.com/scaleway/scaleway-cli/pkg/utils)
BuildRequires:  golang(github.com/Sirupsen/logrus)
BuildRequires:  golang(github.com/skratchdot/open-golang/open)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/sync/errgroup)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv dist/README.md README-dist.md
mv pkg/api/README.md README-pkg-api.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc examples README.md README-dist.md README-pkg-api.md

%gopkgfiles

%changelog

