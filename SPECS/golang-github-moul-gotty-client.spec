# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/moul/gotty-client
%global goipath         github.com/moul/gotty-client
Version:                1.10.0

%gometa

%global common_description %{expand:
:wrench: terminal client for GoTTY.}

%global golicenses      LICENSE
%global godocs          README.md AUTHORS

Name:           %{goname}
Release:        1%{?dist}
Summary:        :wrench: terminal client for GoTTY

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/creack/goselect)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
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
%doc README.md AUTHORS
%{_bindir}/*

%gopkgfiles

%changelog

