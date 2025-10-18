GET /_cat/indices?v

GET products/_mapping

GET /products

GET /products/_count

GET /products/_search
{
  "query": {
    "match_all": {}
  }
}

curl -XGET https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/products/_count
