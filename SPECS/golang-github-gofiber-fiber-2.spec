# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/gofiber/fiber
%global goipath         github.com/gofiber/fiber/v2
%global forgeurl        https://github.com/gofiber/fiber
Version:                2.12.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          middleware/basicauth/README.md\\\
                        middleware/cache/README.md\\\
                        middleware/compress/README.md\\\
                        middleware/cors/README.md middleware/csrf/README.md\\\
                        middleware/etag/README.md middleware/expvar/README.md\\\
                        middleware/favicon/README.md\\\
                        middleware/filesystem/README.md\\\
                        middleware/limiter/README.md\\\
                        middleware/logger/README.md\\\
                        middleware/monitor/README.md\\\
                        middleware/pprof/README.md middleware/proxy/README.md\\\
                        middleware/recover/README.md\\\
                        middleware/requestid/README.md\\\
                        middleware/session/README.md\\\
                        middleware/timeout/README.md utils/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: BSD-3-Clause and MIT
License:        BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/valyala/fasthttp)
BuildRequires:  golang(github.com/valyala/fasthttp/expvarhandler)
BuildRequires:  golang(github.com/valyala/fasthttp/fasthttpadaptor)
BuildRequires:  golang(github.com/valyala/fasthttp/reuseport)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/valyala/fasthttp/fasthttputil)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -r .*cache.*
%endif

%gopkgfiles

%changelog

