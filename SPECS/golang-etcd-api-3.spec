# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/etcd-io/etcd
%global goipath         go.etcd.io/etcd/api/v3
%global forgeurl        https://github.com/etcd-io/etcd
Version:                3.5.0~rc.1

%gometa
%global extractdir      etcd-3.5.0-rc.1

%global goaltipaths     github.com/etcd-io/etcd/api/v3

%global common_description %{expand:
Distributed reliable key-value store for the most critical data of a
distributed system.}

%global golicenses      LICENSE LICENSE-api LICENSE-client-pkg\\\
                        LICENSE-client-v2 LICENSE-client-v3 LICENSE-etcdctl\\\
                        LICENSE-etcdutl LICENSE-pkg LICENSE-raft\\\
                        LICENSE-server
%global godocs          CONTRIBUTING.md GOVERNANCE.md README.md ROADMAP.md\\\
                        code-of-conduct.md README-Documentation.md\\\
                        README-client-v2.md README-client-v3.md\\\
                        README-contrib.md README-contrib-lock.md\\\
                        README-contrib-mixin.md\\\
                        README-contrib-raftexample.md\\\
                        README-contrib-systemd-etcd3-multinode.md doc\\\
                        README-etcdctl.md READMEv2-etcdctl.md\\\
                        README-etcdutl.md README-hack.md\\\
                        README-hack-benchmark.md\\\
                        README-hack-insta-discovery.md\\\
                        README-hack-kubernetes-deploy.md\\\
                        README-hack-patch.md README-hack-tls-setup.md\\\
                        README-pkg.md README-pkg-adt.md README-raft.md\\\
                        design-raft.md README-scripts README-security.md\\\
                        email-templates-security.md\\\
                        security-release-process-security.md\\\
                        README-tools-benchmark.md\\\
                        README-tools-etcd-dump-db.md\\\
                        README-tools-etcd-dump-logs.md\\\
                        README-tools-etcd-dump-metrics\\\
                        README-tools-local-tester.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Distributed reliable key-value store for the most critical data of a distributed system

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
BuildRequires:  golang(go.etcd.io/etcd/raft/v3)
BuildRequires:  golang(go.etcd.io/etcd/raft/v3/confchange)
BuildRequires:  golang(go.etcd.io/etcd/raft/v3/quorum)
BuildRequires:  golang(go.etcd.io/etcd/raft/v3/raftpb)
BuildRequires:  golang(go.etcd.io/etcd/raft/v3/tracker)
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
mv api/LICENSE LICENSE-api
mv client/pkg/LICENSE LICENSE-client-pkg
mv client/v2/LICENSE LICENSE-client-v2
mv client/v3/LICENSE LICENSE-client-v3
mv etcdctl/LICENSE LICENSE-etcdctl
mv etcdutl/LICENSE LICENSE-etcdutl
mv pkg/LICENSE LICENSE-pkg
mv raft/LICENSE LICENSE-raft
mv server/LICENSE LICENSE-server
mv Documentation/README.md README-Documentation.md
mv client/v2/README.md README-client-v2.md
mv client/v3/README.md README-client-v3.md
mv contrib/README.md README-contrib.md
mv contrib/lock/README.md README-contrib-lock.md
mv contrib/mixin/README.md README-contrib-mixin.md
mv contrib/raftexample/README.md README-contrib-raftexample.md
mv contrib/systemd/etcd3-multinode/README.md README-contrib-systemd-etcd3-multinode.md
mv etcdctl/README.md README-etcdctl.md
mv etcdctl/READMEv2.md READMEv2-etcdctl.md
mv etcdutl/README.md README-etcdutl.md
mv hack/README.md README-hack.md
mv hack/benchmark/README.md README-hack-benchmark.md
mv hack/insta-discovery/README.md README-hack-insta-discovery.md
mv hack/kubernetes-deploy/README.md README-hack-kubernetes-deploy.md
mv hack/patch/README.md README-hack-patch.md
mv hack/tls-setup/README.md README-hack-tls-setup.md
mv pkg/README.md README-pkg.md
mv pkg/adt/README.md README-pkg-adt.md
mv raft/README.md README-raft.md
mv raft/design.md design-raft.md
mv scripts/README README-scripts
mv security/README.md README-security.md
mv security/email-templates.md email-templates-security.md
mv security/security-release-process.md security-release-process-security.md
mv tools/benchmark/README.md README-tools-benchmark.md
mv tools/etcd-dump-db/README.md README-tools-etcd-dump-db.md
mv tools/etcd-dump-logs/README.md README-tools-etcd-dump-logs.md
mv tools/etcd-dump-metrics/README README-tools-etcd-dump-metrics
mv tools/local-tester/README.md README-tools-local-tester.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE LICENSE-api LICENSE-client-pkg LICENSE-client-v2
%license LICENSE-client-v3 LICENSE-etcdctl LICENSE-etcdutl LICENSE-pkg
%license LICENSE-raft LICENSE-server
%doc CONTRIBUTING.md GOVERNANCE.md README.md ROADMAP.md code-of-conduct.md
%doc README-Documentation.md README-client-v2.md README-client-v3.md
%doc README-contrib.md README-contrib-lock.md README-contrib-mixin.md
%doc README-contrib-raftexample.md README-contrib-systemd-etcd3-multinode.md doc
%doc README-etcdctl.md READMEv2-etcdctl.md README-etcdutl.md README-hack.md
%doc README-hack-benchmark.md README-hack-insta-discovery.md
%doc README-hack-kubernetes-deploy.md README-hack-patch.md
%doc README-hack-tls-setup.md README-pkg.md README-pkg-adt.md README-raft.md
%doc design-raft.md README-scripts README-security.md
%doc email-templates-security.md security-release-process-security.md
%doc README-tools-benchmark.md README-tools-etcd-dump-db.md
%doc README-tools-etcd-dump-logs.md README-tools-etcd-dump-metrics
%doc README-tools-local-tester.md

%gopkgfiles

%changelog

