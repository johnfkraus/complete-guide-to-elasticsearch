### Date filtering

https://stackoverflow.com/questions/15643414/filtering-by-date-in-elasticsearch

```json

curl -XPUT localhost:9200/test -d '{
    "settings": {
        "index.number_of_shards": 1,
        "index.number_of_replicas": 0
    },
    "mappings": {
        "doc": {
            "_timestamp": {
                "enabled": "true"
            },
            "properties": {
                "cards": {
                    "type": "integer"
                },
                "last_updated": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss"
                }
            }
        }
    }
}
'
curl -XPOST localhost:9200/test/doc/1 -d '{
    "last_updated": "2012-01-01 12:13:14"
}
'
curl -XPOST localhost:9200/test/doc/2 -d '{
    "last_updated": "2013-02-02 01:02:03"
}
'
curl -X POST 'http://localhost:9200/test/_refresh'
echo
curl -X GET 'http://localhost:9200/test/doc/_search?pretty' -d '{
    "query": {
        "filtered": {
            "query": {
                "match_all": {}
            },
            "filter": {
                "range": {
                    "last_updated": {
                        "gte": "2013-01-01 00:00:00"
                    }
                }
            }
        }
    }
}
'
```
   
