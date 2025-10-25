## Elasticsearch cheatsheet

https://coralogix.com/blog/42-elasticsearch-query-examples-hands-on-tutorial/


GET /_cluster/health

GET /_cat/indices?v

GET /_cat

GET /products/_count

GET /_count

### Create index:

Command line:

curl -X PUT “http://localhost:9200/movies/”

Kibana:

PUT /movies
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}

### Insert record:

curl -X POST "${ESHOST}/movies/movie/" -H 'content-type: application/json' -d '{"name":"Justice League", "genre":"Action",
"summary":"Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy","yearofrelease":201, "metascore":45, "votes":275122, "rating":6.6}'

POST /movies/_doc 
{
"name":"Justice League", "genre":"Action", "summary":"Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy", "yearofrelease":201, "metascore":45, "votes":275122, "rating":6.6
}


Bulk load data:

curl -H "Content-Type: application/x-ndjson" -XPOST https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/movies/_bulk --data-binary "@products-bulk.json"


### Search

GET /recipes/_search
{
  "query": {
    "match_all": {}
  }
}

Get by id:

GET /movies/_doc/1

GET /_cat/indices

GET /_count

GET /orders/_search
{
  "size": 0,
  "aggs": {
    "amts_stats": {
      "stats": {
        "field": "total_amount"
      }
    }
  }
}

