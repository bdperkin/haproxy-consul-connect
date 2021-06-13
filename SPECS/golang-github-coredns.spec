# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/coredns/coredns
%global goipath         github.com/coredns/coredns
Version:                1.8.4

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE
%global godocs          ADOPTERS.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        GOVERNANCE.md README.md SECURITY.md corefile.5.md\\\
                        plugin.md coredns.1.md coredns-0.9.10-notes.md\\\
                        coredns-0.9.9-notes.md coredns-001-notes.md\\\
                        coredns-002-notes.md coredns-003-notes.md\\\
                        coredns-004-notes.md coredns-005-notes.md\\\
                        coredns-006-notes.md coredns-007-notes.md\\\
                        coredns-008-notes.md coredns-009-notes.md\\\
                        coredns-010-notes.md coredns-011-notes.md\\\
                        coredns-1.0.0-notes.md coredns-1.0.1-notes.md\\\
                        coredns-1.0.2-notes.md coredns-1.0.3-notes.md\\\
                        coredns-1.0.4-notes.md coredns-1.0.5-notes.md\\\
                        coredns-1.0.6-notes.md coredns-1.1.0-notes.md\\\
                        coredns-1.1.1-notes.md coredns-1.1.2-notes.md\\\
                        coredns-1.1.3-notes.md coredns-1.1.4-notes.md\\\
                        coredns-1.2.0-notes.md coredns-1.2.1-notes.md\\\
                        coredns-1.2.2-notes.md coredns-1.2.3-notes.md\\\
                        coredns-1.2.4-notes.md coredns-1.2.5-notes.md\\\
                        coredns-1.2.6-notes.md coredns-1.3.0-notes.md\\\
                        coredns-1.3.1-notes.md coredns-1.4.0-notes.md\\\
                        coredns-1.5.0-notes.md coredns-1.5.1-notes.md\\\
                        coredns-1.5.2-notes.md coredns-1.6.0-notes.md\\\
                        coredns-1.6.1-notes.md coredns-1.6.2-notes.md\\\
                        coredns-1.6.3-notes.md coredns-1.6.4-notes.md\\\
                        coredns-1.6.5-notes.md coredns-1.6.6-notes.md\\\
                        coredns-1.6.7-notes.md coredns-1.6.8-notes.md\\\
                        coredns-1.6.9-notes.md coredns-1.7.0-notes.md\\\
                        coredns-1.7.1-notes.md coredns-1.8.0-notes.md\\\
                        coredns-1.8.1-notes.md coredns-1.8.2-notes.md\\\
                        coredns-1.8.3-notes.md coredns-1.8.4-notes.md\\\
                        README-plugin-acl.md README-plugin-any.md\\\
                        README-plugin-auto.md README-plugin-autopath.md\\\
                        README-plugin-azure.md README-plugin-bind.md\\\
                        README-plugin-bufsize.md README-plugin-cache.md\\\
                        README-plugin-cancel.md README-plugin-chaos.md\\\
                        README-plugin-clouddns.md README-plugin-debug.md\\\
                        README-plugin-dns64.md README-plugin-dnssec.md\\\
                        README-plugin-dnstap.md README-plugin-erratic.md\\\
                        README-plugin-errors.md README-plugin-etcd.md\\\
                        README-plugin-file.md README-plugin-forward.md\\\
                        README-plugin-grpc.md README-plugin-health.md\\\
                        README-plugin-hosts.md README-plugin-import.md\\\
                        README-plugin-k8s_external.md\\\
                        README-plugin-kubernetes.md\\\
                        README-plugin-loadbalance.md README-plugin-local.md\\\
                        README-plugin-log.md README-plugin-loop.md\\\
                        README-plugin-metadata.md README-plugin-metrics.md\\\
                        README-plugin-minimal.md README-plugin-nsid.md\\\
                        README-plugin-pprof.md README-plugin-ready.md\\\
                        README-plugin-reload.md README-plugin-rewrite.md\\\
                        README-plugin-root.md README-plugin-route53.md\\\
                        README-plugin-secondary.md README-plugin-sign.md\\\
                        README-plugin-template.md README-plugin-tls.md\\\
                        README-plugin-trace.md README-plugin-transfer.md\\\
                        README-plugin-whoami.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/apparentlymart/go-cidr/cidr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/route53)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/route53/route53iface)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/profiles/latest/dns/mgmt/dns)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/profiles/latest/privatedns/mgmt/privatedns)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure/auth)
BuildRequires:  golang(github.com/coredns/caddy)
BuildRequires:  golang(github.com/coredns/caddy/caddyfile)
BuildRequires:  golang(github.com/coredns/caddy/onevent)
BuildRequires:  golang(github.com/dnstap/golang-dnstap)
BuildRequires:  golang(github.com/farsightsec/golang-framestream)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/grpc-ecosystem/grpc-opentracing/go/otgrpc)
BuildRequires:  golang(github.com/infobloxopen/go-trees/iptree)
BuildRequires:  golang(github.com/matttproud/golang_protobuf_extensions/pbutil)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/openzipkin-contrib/zipkin-go-opentracing)
BuildRequires:  golang(github.com/openzipkin/zipkin-go)
BuildRequires:  golang(github.com/openzipkin/zipkin-go/reporter/http)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promauto)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/mvccpb)
BuildRequires:  golang(go.etcd.io/etcd/client/v3)
BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/api/dns/v1)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/DataDog/dd-trace-go.v1/ddtrace/ext)
BuildRequires:  golang(gopkg.in/DataDog/dd-trace-go.v1/ddtrace/opentracer)
BuildRequires:  golang(gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/discovery/v1)
BuildRequires:  golang(k8s.io/api/discovery/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth/gcp)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth/oidc)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth/openstack)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  golang(k8s.io/klog)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/opentracing/opentracing-go/mocktracer)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/testutil/promlint)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv notes/coredns-0.9.10.md coredns-0.9.10-notes.md
mv notes/coredns-0.9.9.md coredns-0.9.9-notes.md
mv notes/coredns-001.md coredns-001-notes.md
mv notes/coredns-002.md coredns-002-notes.md
mv notes/coredns-003.md coredns-003-notes.md
mv notes/coredns-004.md coredns-004-notes.md
mv notes/coredns-005.md coredns-005-notes.md
mv notes/coredns-006.md coredns-006-notes.md
mv notes/coredns-007.md coredns-007-notes.md
mv notes/coredns-008.md coredns-008-notes.md
mv notes/coredns-009.md coredns-009-notes.md
mv notes/coredns-010.md coredns-010-notes.md
mv notes/coredns-011.md coredns-011-notes.md
mv notes/coredns-1.0.0.md coredns-1.0.0-notes.md
mv notes/coredns-1.0.1.md coredns-1.0.1-notes.md
mv notes/coredns-1.0.2.md coredns-1.0.2-notes.md
mv notes/coredns-1.0.3.md coredns-1.0.3-notes.md
mv notes/coredns-1.0.4.md coredns-1.0.4-notes.md
mv notes/coredns-1.0.5.md coredns-1.0.5-notes.md
mv notes/coredns-1.0.6.md coredns-1.0.6-notes.md
mv notes/coredns-1.1.0.md coredns-1.1.0-notes.md
mv notes/coredns-1.1.1.md coredns-1.1.1-notes.md
mv notes/coredns-1.1.2.md coredns-1.1.2-notes.md
mv notes/coredns-1.1.3.md coredns-1.1.3-notes.md
mv notes/coredns-1.1.4.md coredns-1.1.4-notes.md
mv notes/coredns-1.2.0.md coredns-1.2.0-notes.md
mv notes/coredns-1.2.1.md coredns-1.2.1-notes.md
mv notes/coredns-1.2.2.md coredns-1.2.2-notes.md
mv notes/coredns-1.2.3.md coredns-1.2.3-notes.md
mv notes/coredns-1.2.4.md coredns-1.2.4-notes.md
mv notes/coredns-1.2.5.md coredns-1.2.5-notes.md
mv notes/coredns-1.2.6.md coredns-1.2.6-notes.md
mv notes/coredns-1.3.0.md coredns-1.3.0-notes.md
mv notes/coredns-1.3.1.md coredns-1.3.1-notes.md
mv notes/coredns-1.4.0.md coredns-1.4.0-notes.md
mv notes/coredns-1.5.0.md coredns-1.5.0-notes.md
mv notes/coredns-1.5.1.md coredns-1.5.1-notes.md
mv notes/coredns-1.5.2.md coredns-1.5.2-notes.md
mv notes/coredns-1.6.0.md coredns-1.6.0-notes.md
mv notes/coredns-1.6.1.md coredns-1.6.1-notes.md
mv notes/coredns-1.6.2.md coredns-1.6.2-notes.md
mv notes/coredns-1.6.3.md coredns-1.6.3-notes.md
mv notes/coredns-1.6.4.md coredns-1.6.4-notes.md
mv notes/coredns-1.6.5.md coredns-1.6.5-notes.md
mv notes/coredns-1.6.6.md coredns-1.6.6-notes.md
mv notes/coredns-1.6.7.md coredns-1.6.7-notes.md
mv notes/coredns-1.6.8.md coredns-1.6.8-notes.md
mv notes/coredns-1.6.9.md coredns-1.6.9-notes.md
mv notes/coredns-1.7.0.md coredns-1.7.0-notes.md
mv notes/coredns-1.7.1.md coredns-1.7.1-notes.md
mv notes/coredns-1.8.0.md coredns-1.8.0-notes.md
mv notes/coredns-1.8.1.md coredns-1.8.1-notes.md
mv notes/coredns-1.8.2.md coredns-1.8.2-notes.md
mv notes/coredns-1.8.3.md coredns-1.8.3-notes.md
mv notes/coredns-1.8.4.md coredns-1.8.4-notes.md
mv plugin/acl/README.md README-plugin-acl.md
mv plugin/any/README.md README-plugin-any.md
mv plugin/auto/README.md README-plugin-auto.md
mv plugin/autopath/README.md README-plugin-autopath.md
mv plugin/azure/README.md README-plugin-azure.md
mv plugin/bind/README.md README-plugin-bind.md
mv plugin/bufsize/README.md README-plugin-bufsize.md
mv plugin/cache/README.md README-plugin-cache.md
mv plugin/cancel/README.md README-plugin-cancel.md
mv plugin/chaos/README.md README-plugin-chaos.md
mv plugin/clouddns/README.md README-plugin-clouddns.md
mv plugin/debug/README.md README-plugin-debug.md
mv plugin/dns64/README.md README-plugin-dns64.md
mv plugin/dnssec/README.md README-plugin-dnssec.md
mv plugin/dnstap/README.md README-plugin-dnstap.md
mv plugin/erratic/README.md README-plugin-erratic.md
mv plugin/errors/README.md README-plugin-errors.md
mv plugin/etcd/README.md README-plugin-etcd.md
mv plugin/file/README.md README-plugin-file.md
mv plugin/forward/README.md README-plugin-forward.md
mv plugin/grpc/README.md README-plugin-grpc.md
mv plugin/health/README.md README-plugin-health.md
mv plugin/hosts/README.md README-plugin-hosts.md
mv plugin/import/README.md README-plugin-import.md
mv plugin/k8s_external/README.md README-plugin-k8s_external.md
mv plugin/kubernetes/README.md README-plugin-kubernetes.md
mv plugin/loadbalance/README.md README-plugin-loadbalance.md
mv plugin/local/README.md README-plugin-local.md
mv plugin/log/README.md README-plugin-log.md
mv plugin/loop/README.md README-plugin-loop.md
mv plugin/metadata/README.md README-plugin-metadata.md
mv plugin/metrics/README.md README-plugin-metrics.md
mv plugin/minimal/README.md README-plugin-minimal.md
mv plugin/nsid/README.md README-plugin-nsid.md
mv plugin/pprof/README.md README-plugin-pprof.md
mv plugin/ready/README.md README-plugin-ready.md
mv plugin/reload/README.md README-plugin-reload.md
mv plugin/rewrite/README.md README-plugin-rewrite.md
mv plugin/root/README.md README-plugin-root.md
mv plugin/route53/README.md README-plugin-route53.md
mv plugin/secondary/README.md README-plugin-secondary.md
mv plugin/sign/README.md README-plugin-sign.md
mv plugin/template/README.md README-plugin-template.md
mv plugin/tls/README.md README-plugin-tls.md
mv plugin/trace/README.md README-plugin-trace.md
mv plugin/transfer/README.md README-plugin-transfer.md
mv plugin/whoami/README.md README-plugin-whoami.md

%build
%gobuild -o %{gobuilddir}/bin/coredns %{goipath}

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
%doc ADOPTERS.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md README.md
%doc SECURITY.md corefile.5.md plugin.md coredns.1.md coredns-0.9.10-notes.md
%doc coredns-0.9.9-notes.md coredns-001-notes.md coredns-002-notes.md
%doc coredns-003-notes.md coredns-004-notes.md coredns-005-notes.md
%doc coredns-006-notes.md coredns-007-notes.md coredns-008-notes.md
%doc coredns-009-notes.md coredns-010-notes.md coredns-011-notes.md
%doc coredns-1.0.0-notes.md coredns-1.0.1-notes.md coredns-1.0.2-notes.md
%doc coredns-1.0.3-notes.md coredns-1.0.4-notes.md coredns-1.0.5-notes.md
%doc coredns-1.0.6-notes.md coredns-1.1.0-notes.md coredns-1.1.1-notes.md
%doc coredns-1.1.2-notes.md coredns-1.1.3-notes.md coredns-1.1.4-notes.md
%doc coredns-1.2.0-notes.md coredns-1.2.1-notes.md coredns-1.2.2-notes.md
%doc coredns-1.2.3-notes.md coredns-1.2.4-notes.md coredns-1.2.5-notes.md
%doc coredns-1.2.6-notes.md coredns-1.3.0-notes.md coredns-1.3.1-notes.md
%doc coredns-1.4.0-notes.md coredns-1.5.0-notes.md coredns-1.5.1-notes.md
%doc coredns-1.5.2-notes.md coredns-1.6.0-notes.md coredns-1.6.1-notes.md
%doc coredns-1.6.2-notes.md coredns-1.6.3-notes.md coredns-1.6.4-notes.md
%doc coredns-1.6.5-notes.md coredns-1.6.6-notes.md coredns-1.6.7-notes.md
%doc coredns-1.6.8-notes.md coredns-1.6.9-notes.md coredns-1.7.0-notes.md
%doc coredns-1.7.1-notes.md coredns-1.8.0-notes.md coredns-1.8.1-notes.md
%doc coredns-1.8.2-notes.md coredns-1.8.3-notes.md coredns-1.8.4-notes.md
%doc README-plugin-acl.md README-plugin-any.md README-plugin-auto.md
%doc README-plugin-autopath.md README-plugin-azure.md README-plugin-bind.md
%doc README-plugin-bufsize.md README-plugin-cache.md README-plugin-cancel.md
%doc README-plugin-chaos.md README-plugin-clouddns.md README-plugin-debug.md
%doc README-plugin-dns64.md README-plugin-dnssec.md README-plugin-dnstap.md
%doc README-plugin-erratic.md README-plugin-errors.md README-plugin-etcd.md
%doc README-plugin-file.md README-plugin-forward.md README-plugin-grpc.md
%doc README-plugin-health.md README-plugin-hosts.md README-plugin-import.md
%doc README-plugin-k8s_external.md README-plugin-kubernetes.md
%doc README-plugin-loadbalance.md README-plugin-local.md README-plugin-log.md
%doc README-plugin-loop.md README-plugin-metadata.md README-plugin-metrics.md
%doc README-plugin-minimal.md README-plugin-nsid.md README-plugin-pprof.md
%doc README-plugin-ready.md README-plugin-reload.md README-plugin-rewrite.md
%doc README-plugin-root.md README-plugin-route53.md README-plugin-secondary.md
%doc README-plugin-sign.md README-plugin-template.md README-plugin-tls.md
%doc README-plugin-trace.md README-plugin-transfer.md README-plugin-whoami.md
%{_bindir}/*

%gopkgfiles

%changelog

