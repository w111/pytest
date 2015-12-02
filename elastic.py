from datetime import datetime
from elasticsearch import Elasticsearch

# by default we connect to localhost:9200
es = Elasticsearch(['http://logs.garpun.lan:9200'])

# datetimes will be serialized
# es.index(index="logstash-2015.12.02", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

# but not deserialized
e = es.search_shards()

c = [item[0]["index"] for item in e["shards"] if len(item)>0]
c = list(set(c))
c.sort(reverse=True)
shards = c[0:2]
# shards = set(c[0:2])
print(shards)
body={
  "facets": {
    "terms": {
      "terms": {
        "field": "extra.md5Msg",
        "size": 40,
        "order": "count",
        "exclude": []
      },
      "facet_filter": {
        "fquery": {
          "query": {
            "filtered": {
              "query": {
                "bool": {
                  "should": [
                    {
                      "query_string": {
                        "query": "level_name:\"ERROR\""
                      }
                    },
                    {
                      "query_string": {
                        "query": "level_name:\"CRITICAL\""
                      }
                    },
                    {
                      "query_string": {
                        "query": "level_name:\"ALERT\""
                      }
                    },
                    {
                      "query_string": {
                        "query": "level_name:\"EMERGENCY\""
                      }
                    }
                  ]
                }
              },
              "filter": {
                "bool": {
                  "must": [
                    {
                      "range": {
                        "@timestamp": {
                          "from": 1449003317910,
                          "to": 1449089717910
                        }
                      }
                    },
                    {
                      "fquery": {
                        "query": {
                          "query_string": {
                            "query": "channel='es.amp.garpun.com'"
                          }
                        },
                        "_cache": True
                      }
                    }
                  ],
                  "must_not": [
                    {
                      "fquery": {
                        "query": {
                          "query_string": {
                            "query": "context.agency:(381)"
                          }
                        },
                        "_cache": True
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      }
    }
  },
  "size": 0
}
e = es.search(index=shards, body=body)
for item in e["facets"]["terms"]["terms"]:
    print(item)