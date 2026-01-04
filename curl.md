

curl -XGET "https://dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net:443/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}'

For elastic cloud:
Create products index.

curl -s -X PUT "$EC_URL/products" \
  -H "Authorization: ApiKey $EC_API_KEY" \
  -H "Content-Type: application/json" 


curl -s -X DELETE "$EC_URL/products" -H "Authorization: ApiKey $EC_API_KEY"

curl -s -X GET "$EC_URL/products" -H "Authorization: ApiKey $EC_API_KEY"

curl -s -X GET "$EC_URL/_cat/indices" -H "Authorization: ApiKey $EC_API_KEY"

curl -s -X POST "$EC_URL/products/_bulk" \
  -H "Authorization: ApiKey $EC_API_KEY" \
  -H "Content-Type: application/x-ndjson" \
  --data-binary "@products-bulk.json"

curl -s -X POST "$EC_URL/products/_search?scroll=1m" \
  -H "Authorization: ApiKey $EC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 10000,
    "query": { "match_all": {} }
  }' | jq '.hits.hits[]._source' > products-export.json


SCROLL_OUTPUT="products-export-scroll.json"
rm -f "$SCROLL_OUTPUT"

# 1. Initial request
RESPONSE=$(curl -s -X POST "$EC_URL/products/_search?scroll=1m" \
  -H "Authorization: ApiKey $EC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"size": 5000, "query": {"match_all":{}}}')

SCROLL_ID=$(echo "$RESPONSE" | jq -r '._scroll_id')

echo "[" > "$SCROLL_OUTPUT"
FIRST=1

while true; do
  HITS=$(echo "$RESPONSE" | jq '.hits.hits')
  COUNT=$(echo "$HITS" | jq 'length')

  if [ "$COUNT" -eq 0 ]; then
    break
  fi

  if [ $FIRST -eq 1 ]; then
    echo "$HITS" | jq -c '.[] | ._source' >> "$SCROLL_OUTPUT"
    FIRST=0
  else
    echo "," >> "$SCROLL_OUTPUT"
    echo "$HITS" | jq -c '.[] | ._source' | paste -sd "," - >> "$SCROLL_OUTPUT"
  fi

  RESPONSE=$(curl -s -X POST "$EC_URL/_search/scroll" \
    -H "Authorization: ApiKey $EC_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"scroll\":\"1m\", \"scroll_id\":\"$SCROLL_ID\"}")

  SCROLL_ID=$(echo "$RESPONSE" | jq -r '._scroll_id')
done

echo "]" >> "$SCROLL_OUTPUT"





curl -s -X PUT "$EC_URL/products" \
  -H "Authorization: ApiKey $EC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "mappings": {
      "properties": {
        "name":       { "type": "text" },
        "price":      { "type": "integer" },
        "in_stock":   { "type": "integer" },
        "sold":       { "type": "integer" },
        "tags":       { "type": "keyword" },
        "description":{ "type": "text" },
        "is_active":  { "type": "boolean" },
        "created":    { "type": "date", "format": "yyyy/MM/dd" }
      }
    }
  }'


Return _source only:

curl -s -X GET "$EC_URL/products/_search?filter_path=hits.hits._source" \
  -H "Authorization: ApiKey $EC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "query": {
    "match_all": {}
  }
}