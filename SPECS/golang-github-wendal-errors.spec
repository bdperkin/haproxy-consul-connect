# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/wendal/errors
%global goipath         github.com/wendal/errors
%global commit          7f31f4b264ec95ca86f90649fe4dca4a2a690f4a

%gometa

%global common_description %{expand:
增强型errors包(for golang).}

%global godocs          License.txt README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        增强型errors包(for golang)

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

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

