# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/vmware/go-nfs-client
%global goipath         github.com/vmware/go-nfs-client
%global commit          d43b92724c1b2cc50338f1a030442a405a49abe6

%gometa

%global common_description %{expand:
NFS client implementation for Golang.}

%global golicenses      LICENSE_BSD-2.txt NOTICE.txt
%global godocs          README.md example

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        NFS client implementation for Golang

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/rasky/go-xdr/xdr2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog

