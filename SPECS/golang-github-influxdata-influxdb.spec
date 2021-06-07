# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/influxdata/influxdb
%global goipath         github.com/influxdata/influxdb
Version:                1.9.1

%gometa

%global common_description %{expand:
Package influxdb is the root package of InfluxDB, the scalable datastore for
metrics, events, and real-time analytics. If you're looking for the Go HTTP
client for InfluxDB,}

%global golicenses      LICENSE
%global godocs          CODING_GUIDELINES.md QUERIES.md TODO.md\\\
                        CONTRIBUTING.md DEPENDENCIES.md CHANGELOG.md\\\
                        README.md errors-kit-platform-errors.md\\\
                        README-monitor.md README-releng.md\\\
                        style_guide-logger.md README-cmd-influx_inspect.md\\\
                        README-cmd-influx_tsm.md\\\
                        README-cmd-influx_tools-export.md\\\
                        README-cmd-influx_tools-importer.md README-man.md\\\
                        footer-man.txt influx-man.txt influx_inspect-man.txt\\\
                        influx_tsm-man.txt influxd-backup-man.txt\\\
                        influxd-config-man.txt influxd-restore-man.txt\\\
                        influxd-run-man.txt influxd-version-man.txt\\\
                        influxd-man.txt README-services-collectd.md\\\
                        README-services-collectd-test_client.md\\\
                        continuous_queries-services-continuous_querier.md\\\
                        README-services-graphite.md\\\
                        README-services-opentsdb.md\\\
                        README-services-precreator.md README-services-udp.md\\\
                        README-pkg.md README-pkg-snowflake.md\\\
                        README-client.md README-importer.md README-tsdb.md\\\
                        DESIGN-tsdb-engine-tsm1.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Package influxdb is the root package of InfluxDB, the scalable datastore for metrics, events, and real-time analytics

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(collectd.org/api)
BuildRequires:  golang(collectd.org/network)
BuildRequires:  golang(github.com/apache/arrow/go/arrow)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/array)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/memory)
BuildRequires:  golang(github.com/bmizerany/pat)
BuildRequires:  golang(github.com/boltdb/bolt)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cespare/xxhash)
BuildRequires:  golang(github.com/dgrijalva/jwt-go/v4)
BuildRequires:  golang(github.com/dgryski/go-bitstream)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/influxdata/flux)
BuildRequires:  golang(github.com/influxdata/flux/arrow)
BuildRequires:  golang(github.com/influxdata/flux/ast)
BuildRequires:  golang(github.com/influxdata/flux/cmd/flux/cmd)
BuildRequires:  golang(github.com/influxdata/flux/codes)
BuildRequires:  golang(github.com/influxdata/flux/compiler)
BuildRequires:  golang(github.com/influxdata/flux/csv)
BuildRequires:  golang(github.com/influxdata/flux/dependencies/testing)
BuildRequires:  golang(github.com/influxdata/flux/execute)
BuildRequires:  golang(github.com/influxdata/flux/execute/table)
BuildRequires:  golang(github.com/influxdata/flux/interpreter)
BuildRequires:  golang(github.com/influxdata/flux/interval)
BuildRequires:  golang(github.com/influxdata/flux/lang)
BuildRequires:  golang(github.com/influxdata/flux/memory)
BuildRequires:  golang(github.com/influxdata/flux/metadata)
BuildRequires:  golang(github.com/influxdata/flux/parser)
BuildRequires:  golang(github.com/influxdata/flux/plan)
BuildRequires:  golang(github.com/influxdata/flux/runtime)
BuildRequires:  golang(github.com/influxdata/flux/semantic)
BuildRequires:  golang(github.com/influxdata/flux/stdlib)
BuildRequires:  golang(github.com/influxdata/flux/stdlib/influxdata/influxdb)
BuildRequires:  golang(github.com/influxdata/flux/stdlib/universe)
BuildRequires:  golang(github.com/influxdata/flux/values)
BuildRequires:  golang(github.com/influxdata/httprouter)
BuildRequires:  golang(github.com/influxdata/influxql)
BuildRequires:  golang(github.com/influxdata/roaring)
BuildRequires:  golang(github.com/influxdata/usage-client/v1)
BuildRequires:  golang(github.com/jsternberg/zap-logfmt)
BuildRequires:  golang(github.com/jwilder/encoding/simple8b)
BuildRequires:  golang(github.com/klauspost/pgzip)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mileusna/useragent)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/peterh/liner)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/prometheus/prompb)
BuildRequires:  golang(github.com/retailnext/hllpp)
BuildRequires:  golang(github.com/spf13/cast)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/tinylib/msgp/msgp)
BuildRequires:  golang(github.com/uber/jaeger-client-go)
BuildRequires:  golang(github.com/xlab/treeprint)
BuildRequires:  golang(go.uber.org/multierr)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/text/encoding/unicode)
BuildRequires:  golang(golang.org/x/text/transform)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/opentracing/opentracing-go/mocktracer)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.uber.org/zap/zaptest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv kit/platform/errors/errors.md errors-kit-platform-errors.md
mv monitor/README.md README-monitor.md
mv releng/README.md README-releng.md
mv logger/style_guide.md style_guide-logger.md
mv cmd/influx_inspect/README.md README-cmd-influx_inspect.md
mv cmd/influx_tsm/README.md README-cmd-influx_tsm.md
mv cmd/influx_tools/export/README.md README-cmd-influx_tools-export.md
mv cmd/influx_tools/importer/README.md README-cmd-influx_tools-importer.md
mv man/README.md README-man.md
mv man/footer.txt footer-man.txt
mv man/influx.txt influx-man.txt
mv man/influx_inspect.txt influx_inspect-man.txt
mv man/influx_tsm.txt influx_tsm-man.txt
mv man/influxd-backup.txt influxd-backup-man.txt
mv man/influxd-config.txt influxd-config-man.txt
mv man/influxd-restore.txt influxd-restore-man.txt
mv man/influxd-run.txt influxd-run-man.txt
mv man/influxd-version.txt influxd-version-man.txt
mv man/influxd.txt influxd-man.txt
mv services/collectd/README.md README-services-collectd.md
mv services/collectd/test_client/README.md README-services-collectd-test_client.md
mv services/continuous_querier/continuous_queries.md continuous_queries-services-continuous_querier.md
mv services/graphite/README.md README-services-graphite.md
mv services/opentsdb/README.md README-services-opentsdb.md
mv services/precreator/README.md README-services-precreator.md
mv services/udp/README.md README-services-udp.md
mv pkg/README.md README-pkg.md
mv pkg/snowflake/README.md README-pkg-snowflake.md
mv client/README.md README-client.md
mv importer/README.md README-importer.md
mv tsdb/README.md README-tsdb.md
mv tsdb/engine/tsm1/DESIGN.md DESIGN-tsdb-engine-tsm1.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CODING_GUIDELINES.md QUERIES.md TODO.md CONTRIBUTING.md DEPENDENCIES.md
%doc CHANGELOG.md README.md errors-kit-platform-errors.md README-monitor.md
%doc README-releng.md style_guide-logger.md README-cmd-influx_inspect.md
%doc README-cmd-influx_tsm.md README-cmd-influx_tools-export.md
%doc README-cmd-influx_tools-importer.md README-man.md footer-man.txt
%doc influx-man.txt influx_inspect-man.txt influx_tsm-man.txt
%doc influxd-backup-man.txt influxd-config-man.txt influxd-restore-man.txt
%doc influxd-run-man.txt influxd-version-man.txt influxd-man.txt
%doc README-services-collectd.md README-services-collectd-test_client.md
%doc continuous_queries-services-continuous_querier.md
%doc README-services-graphite.md README-services-opentsdb.md
%doc README-services-precreator.md README-services-udp.md README-pkg.md
%doc README-pkg-snowflake.md README-client.md README-importer.md README-tsdb.md
%doc DESIGN-tsdb-engine-tsm1.md

%gopkgfiles

%changelog

