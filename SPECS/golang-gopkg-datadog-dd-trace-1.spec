# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/DataDog/dd-trace-go
%global goipath         gopkg.in/DataDog/dd-trace-go.v1
%global forgeurl        https://github.com/DataDog/dd-trace-go
Version:                1.31.1

%gometa

%global common_description %{expand:
A Go tracing package for Datadog APM.}

%global golicenses      LICENSE LICENSE-3rdparty.csv LICENSE-APACHE LICENSE-\\\
                        BSD3 NOTICE
%global godocs          CONTRIBUTING.md MIGRATING.md README.md\\\
                        contrib/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go tracing package for Datadog APM

# Upstream license specification: Apache-2.0 and BSD-3-Clause
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/pubsub)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/confluentinc/confluent-kafka-go/kafka)
BuildRequires:  golang(github.com/DataDog/datadog-go/statsd)
BuildRequires:  golang(github.com/DataDog/gostackparse)
BuildRequires:  golang(github.com/DataDog/sketches-go/ddsketch)
BuildRequires:  golang(github.com/emicklei/go-restful)
BuildRequires:  golang(github.com/garyburd/redigo/redis)
BuildRequires:  golang(github.com/gin-gonic/gin)
BuildRequires:  golang(github.com/globalsign/mgo)
BuildRequires:  golang(github.com/globalsign/mgo/bson)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/go-chi/chi/middleware)
BuildRequires:  golang(github.com/go-chi/chi/v5)
BuildRequires:  golang(github.com/go-chi/chi/v5/middleware)
BuildRequires:  golang(github.com/go-pg/pg/v10)
BuildRequires:  golang(github.com/go-redis/redis)
BuildRequires:  golang(github.com/go-redis/redis/v7)
BuildRequires:  golang(github.com/go-redis/redis/v8)
BuildRequires:  golang(github.com/gocql/gocql)
BuildRequires:  golang(github.com/gofiber/fiber/v2)
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/gomodule/redigo/redis)
BuildRequires:  golang(github.com/google/pprof/profile)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/errors)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/introspection)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/trace)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hashicorp/vault/api)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/consts)
BuildRequires:  golang(github.com/jinzhu/gorm)
BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/julienschmidt/httprouter)
BuildRequires:  golang(github.com/labstack/echo)
BuildRequires:  golang(github.com/labstack/echo/v4)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/Shopify/sarama)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/iterator)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/opt)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/storage)
BuildRequires:  golang(github.com/syndtr/goleveldb/leveldb/util)
BuildRequires:  golang(github.com/tidwall/buntdb)
BuildRequires:  golang(github.com/tinylib/msgp/msgp)
BuildRequires:  golang(github.com/twitchtv/twirp)
BuildRequires:  golang(github.com/zenazn/goji/web)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson)
BuildRequires:  golang(go.mongodb.org/mongo-driver/event)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(golang.org/x/xerrors)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/stats)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(gopkg.in/jinzhu/gorm.v1)
BuildRequires:  golang(gorm.io/gorm)

%if %{with check}
# Tests
BuildRequires:  golang(cloud.google.com/go/pubsub/pstest)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/graph-gophers/graphql-go)
BuildRequires:  golang(github.com/graph-gophers/graphql-go/relay)
BuildRequires:  golang(github.com/jackc/pgx/v4/stdlib)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/twitchtv/twirp/ctxsetters)
BuildRequires:  golang(github.com/twitchtv/twirp/example)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo/options)
BuildRequires:  golang(google.golang.org/api/books/v1)
BuildRequires:  golang(google.golang.org/api/civicinfo/v2)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/api/urlshortener/v1)
BuildRequires:  golang(gopkg.in/olivere/elastic.v3)
BuildRequires:  golang(gopkg.in/olivere/elastic.v5)
BuildRequires:  golang(gorm.io/driver/mysql)
BuildRequires:  golang(gorm.io/driver/postgres)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/dd-trace-go.v1 %{goipath}
for cmd in contrib/google.golang.org/api; do
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
%license LICENSE LICENSE-3rdparty.csv LICENSE-APACHE LICENSE-BSD3 NOTICE
%doc CONTRIBUTING.md MIGRATING.md README.md contrib/README.md
%{_bindir}/*

%gopkgfiles

%changelog

