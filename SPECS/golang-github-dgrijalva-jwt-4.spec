# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/dgrijalva/jwt-go
%global goipath         github.com/dgrijalva/jwt-go/v4
%global forgeurl        https://github.com/dgrijalva/jwt-go
Version:                4.0.0~preview1

%gometa

%global goaltipaths     github.com/dgrijalva/jwt-go

%global common_description %{expand:
Golang implementation of JSON Web Tokens (JWT).}

%global golicenses      LICENSE
%global godocs          MIGRATION_GUIDE.md README.md VERSION_HISTORY.md\\\
                        README-cmd-jwt.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang implementation of JSON Web Tokens (JWT)

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
mv cmd/jwt/README.md README-cmd-jwt.md

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
%doc MIGRATION_GUIDE.md README.md VERSION_HISTORY.md README-cmd-jwt.md
%{_bindir}/*

%gopkgfiles

%changelog

