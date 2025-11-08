

curl -XGET "https://dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net:443/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}'