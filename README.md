# Django api

## 1. ElasticSearch
### Install
[Installation](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-18-04-ru)

### 1.1 HTTP Request
- ```curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>' ```

This example uses the following variables:

- ```<VERB>```
The appropriate HTTP method or verb. For example, GET, POST, PUT, HEAD, or DELETE.
- ```<PROTOCOL>```
Either http or https. Use the latter if you have an HTTPS proxy in front of Elasticsearch or you use Elasticsearch security features to encrypt HTTP communications.
- ```<HOST>```
The hostname of any node in your Elasticsearch cluster. Alternatively, use localhost for a node on your local machine.
- ```<PORT>```
The port running the Elasticsearch HTTP service, which defaults to 9200.
- ```<PATH>```
The API endpoint, which can contain multiple components, such as _cluster/stats or _nodes/stats/jvm.
- ```<QUERY_STRING>```
Any optional query-string parameters. For example, ?pretty will pretty-print the JSON response to make it easier to read.
- ```<BODY>```
A JSON-encoded request body (if necessary).

### 1.2 Testing ElasticSearch after installation
```export ES_URL=localhost:9200```
```curl -X GET $ES_URL```

> We've the got answer such this:
```
{
  "name" : "o6NBGHA",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "xUMUAsMRRbqXdywxu0wXDg",
  "version" : {
    "number" : "6.8.13",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "be13c69",
    "build_date" : "2020-10-16T09:09:46.555371Z",
    "build_snapshot" : false,
    "lucene_version" : "7.7.3",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

### 1.3 Post request. Create an index. Create a type.
```
   curl -X PUT "$ES_URL/blog/post/1?pretty" -H 'Content-Type: application/json' -d '{"field_1": "value_1", "fields_array_1": ["value_1", "value_2"]}'
```
> Answer:
```
{
  "_index" : "blog",
  "_type" : "post",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}

```

> Elasticsearch automatically have created index blog and type post.
> Index it's a database. Type it's a table in this database.
> Mapping - schema of type(table).
> Mapping is generated automatically when a document is indexed.

### 1.4 Get request. Get mapping.
#### 1.4.1 Get mapping
```
curl -XGET "$ES_URL/blog/_mapping?pretty"
```
> Answer:
```
{
  "blog" : {
    "mappings" : {
      "post" : {
        "properties" : {
          "field_1" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          },
          "fields_array_1" : {
            "type" : "text",
            "fields" : {
              "keyword" : {
                "type" : "keyword",
                "ignore_above" : 256
              }
            }
          }
        }
      }
    }
  }
}
```

#### 1.4.2 Get the element by id
```
curl -XGET "$ES_URL/blog/post/1?pretty"
```
> Answer:
```
{
  "_index" : "blog",
  "_type" : "post",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "field_1" : "value_1",
    "fields_array_1" : [
      "value_1",
      "value_2"
    ]
  }
}
```

#### 1.4.3 Get only the document
```
curl -XGET "$ES_URL/blog/post/1/_source?pretty"
```
> Answer:

```

{
  "field_1" : "value_1",
  "fields_array_1" : [
    "value_1",
    "value_2"
  ]
}
```

