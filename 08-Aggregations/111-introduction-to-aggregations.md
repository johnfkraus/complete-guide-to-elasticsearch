## Lesson 111 - Introduction to aggregations

### Adding `orders` index with field mappings

```
PUT /orders
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "purchased_at": {
        "type": "date"
      },
      "lines": {
        "type": "nested",
        "properties": {
          "product_id": {
            "type": "integer"
          },
          "amount": {
            "type": "double"
          },
          "quantity": {
            "type": "short"
          }
        }
      },
      "total_amount": {
        "type": "double"
      },
      "status": {
        "type": "keyword"
      },
      "sales_channel": {
        "type": "keyword"
      },
      "salesman": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "text"
          }
        }
      }
    }
  }
}
```

### Populating the `orders` index with test data

If you are using a cloud hosted Elasticsearch deployment, remove the `--cacert` argument.

```
# macOS & Linux
curl --cacert config/certs/http_ca.crt -u elastic -H "Content-Type:application/x-ndjson" -X POST https://localhost:9200/orders/_bulk --data-binary "@orders-bulk.json"

curl -H "Content-Type: application/x-ndjson" -XPOST https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/orders/_bulk --data-binary "@orders-bulk.json"

GET /orders/_search
{
  "query": {
    "match_all": {}
  }
}


# Windows
curl --cacert config\certs\http_ca.crt -u elastic -H "Content-Type:application/x-ndjson" -X POST https://localhost:9200/orders/_bulk --data-binary "@orders-bulk.json"
```

GET /orders/default/_mapping