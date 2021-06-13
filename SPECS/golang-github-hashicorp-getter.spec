# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/hashicorp/go-getter
%global goipath         github.com/hashicorp/go-getter
Version:                1.5.3

%gometa

%global common_description %{expand:
Package for downloading things from a string URL using a variety of protocols.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package for downloading things from a string URL using a variety of protocols

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/bgentry/go-netrc/netrc)
BuildRequires:  golang(github.com/cheggaaa/pb)
BuildRequires:  golang(github.com/hashicorp/go-cleanhttp)
BuildRequires:  golang(github.com/hashicorp/go-safetemp)
BuildRequires:  golang(github.com/hashicorp/go-version)
BuildRequires:  golang(github.com/klauspost/compress/zstd)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/mitchellh/go-testing-interface)
BuildRequires:  golang(github.com/ulikunitz/xz)
BuildRequires:  golang(google.golang.org/api/iterator)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
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
%gocheck -r .*go-getter.*
%endif

%files
%license LICENSE
%doc README.md

%gopkgfiles

%changelog

