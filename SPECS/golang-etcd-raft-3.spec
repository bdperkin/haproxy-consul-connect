# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/etcd-io/etcd
%global goipath         go.etcd.io/etcd/raft/v3
%global forgeurl        https://github.com/etcd-io/etcd
Version:                3.5.0~beta.4
%global tag             raft/v3.5.0-beta.4
%global commit          ce9ded489882476895a7a1977b08d4f681a12ae5

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE api/LICENSE client/pkg/LICENSE\\\
                        client/v2/LICENSE client/v3/LICENSE etcdctl/LICENSE\\\
                        etcdutl/LICENSE pkg/LICENSE raft/LICENSE\\\
                        server/LICENSE
%global godocs          CONTRIBUTING.md GOVERNANCE.md README.md ROADMAP.md\\\
                        code-of-conduct.md Documentation/README.md\\\
                        client/v2/README.md client/v3/README.md\\\
                        contrib/README.md contrib/lock/README.md\\\
                        contrib/mixin/README.md contrib/raftexample/README.md\\\
                        contrib/systemd/etcd3-multinode/README.md doc\\\
                        etcdctl/README.md etcdctl/READMEv2.md\\\
                        etcdutl/README.md hack/README.md\\\
                        hack/benchmark/README.md hack/insta-\\\
                        discovery/README.md hack/kubernetes-deploy/README.md\\\
                        hack/patch/README.md hack/tls-setup/README.md\\\
                        pkg/README.md pkg/adt/README.md raft/README.md\\\
                        raft/design.md scripts/README security/README.md\\\
                        security/email-templates.md security/security-\\\
                        release-process.md tools/benchmark/README.md\\\
                        tools/etcd-dump-db/README.md tools/etcd-dump-\\\
                        logs/README.md tools/etcd-dump-metrics/README\\\
                        tools/local-tester/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/bgentry/speakeasy)
BuildRequires:  golang(github.com/cockroachdb/datadriven)
BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/daemon)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/journal)
BuildRequires:  golang(github.com/creack/pty)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/etcd-io/gofail/runtime)
BuildRequires:  golang(github.com/form3tech-oss/jwt-go)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/golang/protobuf/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/btree)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-middleware/logging/settable)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  golang(github.com/grpc-ecosystem/grpc-gateway/runtime)
BuildRequires:  golang(github.com/grpc-ecosystem/grpc-gateway/utilities)
BuildRequires:  golang(github.com/jonboulle/clockwork)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/modern-go/reflect2)
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/soheilhy/cmux)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/tmc/grpc-websocket-proxy/wsproxy)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(github.com/xiang90/probing)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/authpb)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/etcdserverpb)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/etcdserverpb/gw)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/membershippb)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/mvccpb)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/v3rpc/rpctypes)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/version)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/fileutil)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/logutil)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/pathutil)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/srv)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/systemd)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/testutil)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/tlsutil)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/transport)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/types)
BuildRequires:  golang(go.etcd.io/etcd/client/v2)
BuildRequires:  golang(go.etcd.io/etcd/client/v3)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/concurrency)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/credentials)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/internal/endpoint)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/internal/resolver)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/leasing)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/mirror)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/namespace)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/naming/endpoints)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/naming/endpoints/internal)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/ordering)
BuildRequires:  golang(go.etcd.io/etcd/client/v3/snapshot)
BuildRequires:  golang(go.etcd.io/etcd/etcdctl/v3/ctlv2)
BuildRequires:  golang(go.etcd.io/etcd/etcdctl/v3/ctlv2/command)
BuildRequires:  golang(go.etcd.io/etcd/etcdctl/v3/ctlv3)
BuildRequires:  golang(go.etcd.io/etcd/etcdctl/v3/ctlv3/command)
BuildRequires:  golang(go.etcd.io/etcd/etcdutl/v3/etcdutl)
BuildRequires:  golang(go.etcd.io/etcd/etcdutl/v3/snapshot)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/adt)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/cobrautl)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/contention)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/cpuutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/crc)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/debugutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/expect)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/flags)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/httputil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/idutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/ioutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/netutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/osutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/pbutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/proxy)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/report)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/runtime)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/schedule)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/stringutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/traceutil)
BuildRequires:  golang(go.etcd.io/etcd/pkg/v3/wait)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/auth)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/config)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/datadir)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/embed)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdmain)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/etcdhttp)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/membership)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/rafthttp)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/snap)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/snap/snappb)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2auth)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2discovery)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2error)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2http)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2http/httptypes)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2stats)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2store)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v2v3)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3alarm)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3client)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3compactor)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3election)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3election/v3electionpb)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3election/v3electionpb/gw)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3lock)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3lock/v3lockpb)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3lock/v3lockpb/gw)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/api/v3rpc)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/etcdserver/cindex)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/lease)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/lease/leasehttp)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/lease/leasepb)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mvcc)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mvcc/backend)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mvcc/buckets)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/proxy/grpcproxy)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/proxy/grpcproxy/adapter)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/proxy/grpcproxy/cache)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/proxy/httpproxy)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/proxy/tcpproxy)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/verify)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/wal)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/wal/walpb)
BuildRequires:  golang(go.etcd.io/etcd/tests/v3/functional/agent)
BuildRequires:  golang(go.etcd.io/etcd/tests/v3/functional/rpcpb)
BuildRequires:  golang(go.etcd.io/etcd/tests/v3/functional/runner)
BuildRequires:  golang(go.etcd.io/etcd/tests/v3/functional/tester)
BuildRequires:  golang(go.etcd.io/etcd/tests/v3/integration)
BuildRequires:  golang(go.etcd.io/etcd/v3/tools/benchmark/cmd)
BuildRequires:  golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp)
BuildRequires:  golang(go.opentelemetry.io/otel/exporters/otlp/otlpgrpc)
BuildRequires:  golang(go.opentelemetry.io/otel/propagation)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/resource)
BuildRequires:  golang(go.opentelemetry.io/otel/sdk/trace)
BuildRequires:  golang(go.opentelemetry.io/otel/semconv)
BuildRequires:  golang(go.uber.org/multierr)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(go.uber.org/zap/zapgrpc)
BuildRequires:  golang(go.uber.org/zap/zaptest)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/trace)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/health)
BuildRequires:  golang(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires:  golang(google.golang.org/grpc/keepalive)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/resolver)
BuildRequires:  golang(google.golang.org/grpc/resolver/manual)
BuildRequires:  golang(google.golang.org/grpc/serviceconfig)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/grpc/test/grpc_testing)
BuildRequires:  golang(gopkg.in/cheggaaa/pb.v1)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mock/mockstorage)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mock/mockstore)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mock/mockwait)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/mvcc/backend/testing)
BuildRequires:  golang(golang.org/x/sync/errgroup)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/v3 %{goipath}
for cmd in contrib/lock/client contrib/lock/storage contrib/raftexample etcdctl etcdutl server tools/benchmark tools/etcd-dump-db tools/etcd-dump-logs tools/etcd-dump-metrics tools/local-tester/bridge; do
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
%license LICENSE api/LICENSE client/pkg/LICENSE client/v2/LICENSE
%license client/v3/LICENSE etcdctl/LICENSE etcdutl/LICENSE pkg/LICENSE
%license raft/LICENSE server/LICENSE
%doc CONTRIBUTING.md GOVERNANCE.md README.md ROADMAP.md code-of-conduct.md
%doc Documentation/README.md client/v2/README.md client/v3/README.md
%doc contrib/README.md contrib/lock/README.md contrib/mixin/README.md
%doc contrib/raftexample/README.md contrib/systemd/etcd3-multinode/README.md doc
%doc etcdctl/README.md etcdctl/READMEv2.md etcdutl/README.md hack/README.md
%doc hack/benchmark/README.md hack/insta-discovery/README.md
%doc hack/kubernetes-deploy/README.md hack/patch/README.md
%doc hack/tls-setup/README.md pkg/README.md pkg/adt/README.md raft/README.md
%doc raft/design.md scripts/README security/README.md
%doc security/email-templates.md security/security-release-process.md
%doc tools/benchmark/README.md tools/etcd-dump-db/README.md
%doc tools/etcd-dump-logs/README.md tools/etcd-dump-metrics/README
%doc tools/local-tester/README.md
%{_bindir}/*

%gopkgfiles

%changelog

