# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/docker/docker
%global goipath         github.com/docker/docker
Version:                20.10.7

%gometa

%global common_description %{expand:
Moby Project - a collaborative project for the container ecosystem to assemble
container-based systems.}

%global golicenses      LICENSE NOTICE LICENSE-contrib-busybox
%global godocs          docs AUTHORS CHANGELOG.md CONTRIBUTING.md README.md\\\
                        ROADMAP.md SECURITY.md TESTING.md VENDORING.md\\\
                        README-api.md README-api-types-versions.md\\\
                        README-cmd-dockerd.md README-contrib.md\\\
                        README-contrib-docker-device-tool.md\\\
                        README-contrib-syntax-nano.md\\\
                        README-contrib-syntax-textmate.md\\\
                        README-contrib-syntax-vim.md\\\
                        README-daemon-graphdriver-devmapper.md\\\
                        README-hack.md README-hack-make.md\\\
                        changelog-date-descending-hack-validate\\\
                        changelog-well-formed-hack-validate\\\
                        README-image-spec.md v1.1-image-spec.md\\\
                        v1.2-image-spec.md v1-image-spec.md README-pkg.md\\\
                        README-pkg-archive.md README-pkg-discovery.md\\\
                        README-pkg-plugins-pluginrpc-gen.md\\\
                        README-pkg-reexec.md README-pkg-signal.md\\\
                        README-pkg-stringid.md README-pkg-sysinfo.md\\\
                        tarsum_spec-pkg-tarsum.md README-pkg-useragent.md\\\
                        BRANCHES-AND-TAGS-project.md\\\
                        PATCH-RELEASES-project.md PRINCIPLES-project.md\\\
                        GOVERNANCE-project.md ISSUE-TRIAGE-project.md\\\
                        PACKAGERS-project.md README-project.md\\\
                        RELEASE-PROCESS-project.md REVIEWING-project.md\\\
                        README-client.md 2017-05-01-reports.md\\\
                        2017-05-08-reports.md 2017-05-15-reports.md\\\
                        2017-06-05-reports.md 2017-06-12-reports.md\\\
                        2017-06-26-reports.md 2017-05-01-reports-builder.md\\\
                        2017-05-08-reports-builder.md\\\
                        2017-05-15-reports-builder.md\\\
                        2017-05-22-reports-builder.md\\\
                        2017-05-29-reports-builder.md\\\
                        2017-06-05-reports-builder.md\\\
                        2017-06-12-reports-builder.md\\\
                        2017-06-26-reports-builder.md\\\
                        2017-07-10-reports-builder.md\\\
                        2017-07-17-reports-builder.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Moby Project - a collaborative project for the container ecosystem to assemble container-based systems

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(cloud.google.com/go/logging)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/endpointcreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/cloudwatchlogs)
BuildRequires:  golang(github.com/bsphere/le_go)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/containerd/cgroups)
BuildRequires:  golang(github.com/containerd/cgroups/stats/v1)
BuildRequires:  golang(github.com/containerd/cgroups/v2)
BuildRequires:  golang(github.com/containerd/cgroups/v2/stats)
BuildRequires:  golang(github.com/containerd/containerd)
BuildRequires:  golang(github.com/containerd/containerd/api/events)
BuildRequires:  golang(github.com/containerd/containerd/api/types)
BuildRequires:  golang(github.com/containerd/containerd/archive)
BuildRequires:  golang(github.com/containerd/containerd/cio)
BuildRequires:  golang(github.com/containerd/containerd/containers)
BuildRequires:  golang(github.com/containerd/containerd/content)
BuildRequires:  golang(github.com/containerd/containerd/content/local)
BuildRequires:  golang(github.com/containerd/containerd/contrib/nvidia)
BuildRequires:  golang(github.com/containerd/containerd/defaults)
BuildRequires:  golang(github.com/containerd/containerd/errdefs)
BuildRequires:  golang(github.com/containerd/containerd/events)
BuildRequires:  golang(github.com/containerd/containerd/gc)
BuildRequires:  golang(github.com/containerd/containerd/images)
BuildRequires:  golang(github.com/containerd/containerd/leases)
BuildRequires:  golang(github.com/containerd/containerd/log)
BuildRequires:  golang(github.com/containerd/containerd/metadata)
BuildRequires:  golang(github.com/containerd/containerd/mount)
BuildRequires:  golang(github.com/containerd/containerd/namespaces)
BuildRequires:  golang(github.com/containerd/containerd/oci)
BuildRequires:  golang(github.com/containerd/containerd/pkg/dialer)
BuildRequires:  golang(github.com/containerd/containerd/platforms)
BuildRequires:  golang(github.com/containerd/containerd/reference)
BuildRequires:  golang(github.com/containerd/containerd/remotes)
BuildRequires:  golang(github.com/containerd/containerd/remotes/docker)
BuildRequires:  golang(github.com/containerd/containerd/remotes/docker/schema1)
BuildRequires:  golang(github.com/containerd/containerd/rootfs)
BuildRequires:  golang(github.com/containerd/containerd/runtime/linux/runctypes)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v1/linux)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v2/runc/options)
BuildRequires:  golang(github.com/containerd/containerd/services/server/config)
BuildRequires:  golang(github.com/containerd/containerd/snapshots)
BuildRequires:  golang(github.com/containerd/containerd/sys)
BuildRequires:  golang(github.com/containerd/continuity/driver)
BuildRequires:  golang(github.com/containerd/continuity/fs)
BuildRequires:  golang(github.com/containerd/continuity/pathdriver)
BuildRequires:  golang(github.com/containerd/fifo)
BuildRequires:  golang(github.com/containerd/typeurl)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/activation)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/daemon)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/journal)
BuildRequires:  golang(github.com/docker/distribution)
BuildRequires:  golang(github.com/docker/distribution/digestset)
BuildRequires:  golang(github.com/docker/distribution/manifest/manifestlist)
BuildRequires:  golang(github.com/docker/distribution/manifest/ocischema)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema1)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema2)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/docker/distribution/registry/api/errcode)
BuildRequires:  golang(github.com/docker/distribution/registry/api/v2)
BuildRequires:  golang(github.com/docker/distribution/registry/client)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth/challenge)
BuildRequires:  golang(github.com/docker/distribution/registry/client/transport)
BuildRequires:  golang(github.com/docker/go-connections/nat)
BuildRequires:  golang(github.com/docker/go-connections/sockets)
BuildRequires:  golang(github.com/docker/go-connections/tlsconfig)
BuildRequires:  golang(github.com/docker/go-metrics)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/docker/libkv)
BuildRequires:  golang(github.com/docker/libkv/store)
BuildRequires:  golang(github.com/docker/libkv/store/consul)
BuildRequires:  golang(github.com/docker/libkv/store/etcd)
BuildRequires:  golang(github.com/docker/libkv/store/zookeeper)
BuildRequires:  golang(github.com/docker/libnetwork)
BuildRequires:  golang(github.com/docker/libnetwork/cluster)
BuildRequires:  golang(github.com/docker/libnetwork/config)
BuildRequires:  golang(github.com/docker/libnetwork/datastore)
BuildRequires:  golang(github.com/docker/libnetwork/driverapi)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/bridge)
BuildRequires:  golang(github.com/docker/libnetwork/ipamapi)
BuildRequires:  golang(github.com/docker/libnetwork/ipamutils)
BuildRequires:  golang(github.com/docker/libnetwork/netlabel)
BuildRequires:  golang(github.com/docker/libnetwork/netutils)
BuildRequires:  golang(github.com/docker/libnetwork/networkdb)
BuildRequires:  golang(github.com/docker/libnetwork/options)
BuildRequires:  golang(github.com/docker/libnetwork/portallocator)
BuildRequires:  golang(github.com/docker/libnetwork/resolvconf)
BuildRequires:  golang(github.com/docker/libnetwork/types)
BuildRequires:  golang(github.com/docker/libtrust)
BuildRequires:  golang(github.com/docker/swarmkit/agent)
BuildRequires:  golang(github.com/docker/swarmkit/agent/exec)
BuildRequires:  golang(github.com/docker/swarmkit/api)
BuildRequires:  golang(github.com/docker/swarmkit/api/genericresource)
BuildRequires:  golang(github.com/docker/swarmkit/api/naming)
BuildRequires:  golang(github.com/docker/swarmkit/ca)
BuildRequires:  golang(github.com/docker/swarmkit/log)
BuildRequires:  golang(github.com/docker/swarmkit/manager/allocator/cnmallocator)
BuildRequires:  golang(github.com/docker/swarmkit/manager/encryption)
BuildRequires:  golang(github.com/docker/swarmkit/node)
BuildRequires:  golang(github.com/docker/swarmkit/template)
BuildRequires:  golang(github.com/fluent/fluent-logger-golang/fluent)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/gddo/httputil)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/Graylog2/go-gelf/gelf)
BuildRequires:  golang(github.com/hashicorp/go-immutable-radix)
BuildRequires:  golang(github.com/hashicorp/go-memdb)
BuildRequires:  golang(github.com/imdario/mergo)
BuildRequires:  golang(github.com/mistifyio/go-zfs)
BuildRequires:  golang(github.com/moby/buildkit/api/services/control)
BuildRequires:  golang(github.com/moby/buildkit/cache)
BuildRequires:  golang(github.com/moby/buildkit/cache/metadata)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/inline)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/local)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/registry)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/v1)
BuildRequires:  golang(github.com/moby/buildkit/client)
BuildRequires:  golang(github.com/moby/buildkit/client/llb)
BuildRequires:  golang(github.com/moby/buildkit/cmd/buildkitd/config)
BuildRequires:  golang(github.com/moby/buildkit/control)
BuildRequires:  golang(github.com/moby/buildkit/executor)
BuildRequires:  golang(github.com/moby/buildkit/executor/oci)
BuildRequires:  golang(github.com/moby/buildkit/executor/runcexecutor)
BuildRequires:  golang(github.com/moby/buildkit/exporter)
BuildRequires:  golang(github.com/moby/buildkit/exporter/containerimage/exptypes)
BuildRequires:  golang(github.com/moby/buildkit/exporter/local)
BuildRequires:  golang(github.com/moby/buildkit/exporter/tar)
BuildRequires:  golang(github.com/moby/buildkit/frontend)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/builder)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/dockerignore)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/instructions)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/parser)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/shell)
BuildRequires:  golang(github.com/moby/buildkit/frontend/gateway)
BuildRequires:  golang(github.com/moby/buildkit/frontend/gateway/forwarder)
BuildRequires:  golang(github.com/moby/buildkit/identity)
BuildRequires:  golang(github.com/moby/buildkit/session)
BuildRequires:  golang(github.com/moby/buildkit/snapshot)
BuildRequires:  golang(github.com/moby/buildkit/snapshot/containerd)
BuildRequires:  golang(github.com/moby/buildkit/solver)
BuildRequires:  golang(github.com/moby/buildkit/solver/bboltcachestorage)
BuildRequires:  golang(github.com/moby/buildkit/solver/llbsolver/mounts)
BuildRequires:  golang(github.com/moby/buildkit/solver/llbsolver/ops)
BuildRequires:  golang(github.com/moby/buildkit/solver/pb)
BuildRequires:  golang(github.com/moby/buildkit/source)
BuildRequires:  golang(github.com/moby/buildkit/source/git)
BuildRequires:  golang(github.com/moby/buildkit/source/http)
BuildRequires:  golang(github.com/moby/buildkit/source/local)
BuildRequires:  golang(github.com/moby/buildkit/util/apicaps)
BuildRequires:  golang(github.com/moby/buildkit/util/archutil)
BuildRequires:  golang(github.com/moby/buildkit/util/compression)
BuildRequires:  golang(github.com/moby/buildkit/util/contentutil)
BuildRequires:  golang(github.com/moby/buildkit/util/entitlements)
BuildRequires:  golang(github.com/moby/buildkit/util/flightcontrol)
BuildRequires:  golang(github.com/moby/buildkit/util/imageutil)
BuildRequires:  golang(github.com/moby/buildkit/util/leaseutil)
BuildRequires:  golang(github.com/moby/buildkit/util/network)
BuildRequires:  golang(github.com/moby/buildkit/util/progress)
BuildRequires:  golang(github.com/moby/buildkit/util/resolver)
BuildRequires:  golang(github.com/moby/buildkit/util/system)
BuildRequires:  golang(github.com/moby/buildkit/util/tracing)
BuildRequires:  golang(github.com/moby/buildkit/worker)
BuildRequires:  golang(github.com/moby/locker)
BuildRequires:  golang(github.com/moby/sys/mount)
BuildRequires:  golang(github.com/moby/sys/mountinfo)
BuildRequires:  golang(github.com/moby/sys/symlink)
BuildRequires:  golang(github.com/moby/term)
BuildRequires:  golang(github.com/morikuni/aec)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/image-spec/identity)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/apparmor)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/cgroups)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/configs)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/devices)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux/label)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/RackSec/srslog)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  golang(github.com/tchap/go-patricia/patricia)
BuildRequires:  golang(github.com/tonistiigi/fsutil)
BuildRequires:  golang(github.com/vbatts/tar-split/tar/asm)
BuildRequires:  golang(github.com/vbatts/tar-split/tar/storage)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/sync/syncmap)
BuildRequires:  golang(golang.org/x/sys/execabs)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/backoff)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gotest.tools/v3/assert)
BuildRequires:  golang(gotest.tools/v3/assert/cmp)
BuildRequires:  golang(gotest.tools/v3/fs)
BuildRequires:  golang(gotest.tools/v3/icmd)
BuildRequires:  golang(gotest.tools/v3/poll)
BuildRequires:  golang(gotest.tools/v3/skip)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/gogo/protobuf/io)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(gotest.tools/v3/env)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv contrib/busybox/LICENSE LICENSE-contrib-busybox
mv api/README.md README-api.md
mv api/types/versions/README.md README-api-types-versions.md
mv cmd/dockerd/README.md README-cmd-dockerd.md
mv contrib/README.md README-contrib.md
mv contrib/docker-device-tool/README.md README-contrib-docker-device-tool.md
mv contrib/syntax/nano/README.md README-contrib-syntax-nano.md
mv contrib/syntax/textmate/README.md README-contrib-syntax-textmate.md
mv contrib/syntax/vim/README.md README-contrib-syntax-vim.md
mv daemon/graphdriver/devmapper/README.md README-daemon-graphdriver-devmapper.md
mv hack/README.md README-hack.md
mv hack/make/README.md README-hack-make.md
mv hack/validate/changelog-date-descending changelog-date-descending-hack-validate
mv hack/validate/changelog-well-formed changelog-well-formed-hack-validate
mv image/spec/README.md README-image-spec.md
mv image/spec/v1.1.md v1.1-image-spec.md
mv image/spec/v1.2.md v1.2-image-spec.md
mv image/spec/v1.md v1-image-spec.md
mv pkg/README.md README-pkg.md
mv pkg/archive/README.md README-pkg-archive.md
mv pkg/discovery/README.md README-pkg-discovery.md
mv pkg/plugins/pluginrpc-gen/README.md README-pkg-plugins-pluginrpc-gen.md
mv pkg/reexec/README.md README-pkg-reexec.md
mv pkg/signal/README.md README-pkg-signal.md
mv pkg/stringid/README.md README-pkg-stringid.md
mv pkg/sysinfo/README.md README-pkg-sysinfo.md
mv pkg/tarsum/tarsum_spec.md tarsum_spec-pkg-tarsum.md
mv pkg/useragent/README.md README-pkg-useragent.md
mv project/BRANCHES-AND-TAGS.md BRANCHES-AND-TAGS-project.md
mv project/PATCH-RELEASES.md PATCH-RELEASES-project.md
mv project/PRINCIPLES.md PRINCIPLES-project.md
mv project/GOVERNANCE.md GOVERNANCE-project.md
mv project/ISSUE-TRIAGE.md ISSUE-TRIAGE-project.md
mv project/PACKAGERS.md PACKAGERS-project.md
mv project/README.md README-project.md
mv project/RELEASE-PROCESS.md RELEASE-PROCESS-project.md
mv project/REVIEWING.md REVIEWING-project.md
mv client/README.md README-client.md
mv reports/2017-05-01.md 2017-05-01-reports.md
mv reports/2017-05-08.md 2017-05-08-reports.md
mv reports/2017-05-15.md 2017-05-15-reports.md
mv reports/2017-06-05.md 2017-06-05-reports.md
mv reports/2017-06-12.md 2017-06-12-reports.md
mv reports/2017-06-26.md 2017-06-26-reports.md
mv reports/builder/2017-05-01.md 2017-05-01-reports-builder.md
mv reports/builder/2017-05-08.md 2017-05-08-reports-builder.md
mv reports/builder/2017-05-15.md 2017-05-15-reports-builder.md
mv reports/builder/2017-05-22.md 2017-05-22-reports-builder.md
mv reports/builder/2017-05-29.md 2017-05-29-reports-builder.md
mv reports/builder/2017-06-05.md 2017-06-05-reports-builder.md
mv reports/builder/2017-06-12.md 2017-06-12-reports-builder.md
mv reports/builder/2017-06-26.md 2017-06-26-reports-builder.md
mv reports/builder/2017-07-10.md 2017-07-10-reports-builder.md
mv reports/builder/2017-07-17.md 2017-07-17-reports-builder.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE NOTICE LICENSE-contrib-busybox
%doc docs AUTHORS CHANGELOG.md CONTRIBUTING.md README.md ROADMAP.md SECURITY.md
%doc TESTING.md VENDORING.md README-api.md README-api-types-versions.md
%doc README-cmd-dockerd.md README-contrib.md
%doc README-contrib-docker-device-tool.md README-contrib-syntax-nano.md
%doc README-contrib-syntax-textmate.md README-contrib-syntax-vim.md
%doc README-daemon-graphdriver-devmapper.md README-hack.md README-hack-make.md
%doc changelog-date-descending-hack-validate changelog-well-formed-hack-validate
%doc README-image-spec.md v1.1-image-spec.md v1.2-image-spec.md v1-image-spec.md
%doc README-pkg.md README-pkg-archive.md README-pkg-discovery.md
%doc README-pkg-plugins-pluginrpc-gen.md README-pkg-reexec.md
%doc README-pkg-signal.md README-pkg-stringid.md README-pkg-sysinfo.md
%doc tarsum_spec-pkg-tarsum.md README-pkg-useragent.md
%doc BRANCHES-AND-TAGS-project.md PATCH-RELEASES-project.md
%doc PRINCIPLES-project.md GOVERNANCE-project.md ISSUE-TRIAGE-project.md
%doc PACKAGERS-project.md README-project.md RELEASE-PROCESS-project.md
%doc REVIEWING-project.md README-client.md 2017-05-01-reports.md
%doc 2017-05-08-reports.md 2017-05-15-reports.md 2017-06-05-reports.md
%doc 2017-06-12-reports.md 2017-06-26-reports.md 2017-05-01-reports-builder.md
%doc 2017-05-08-reports-builder.md 2017-05-15-reports-builder.md
%doc 2017-05-22-reports-builder.md 2017-05-29-reports-builder.md
%doc 2017-06-05-reports-builder.md 2017-06-12-reports-builder.md
%doc 2017-06-26-reports-builder.md 2017-07-10-reports-builder.md
%doc 2017-07-17-reports-builder.md

%gopkgfiles

%changelog

