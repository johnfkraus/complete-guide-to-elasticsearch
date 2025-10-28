## Lesson 88 - Querying nested objects

### Importing test data

Follow [these instructions](/Managing%20Documents/importing-data-with-curl.md) and specify `recipes-bulk.json` as the file name.

curl -H "Content-Type: application/x-ndjson" -XPOST https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/recipes/_bulk --data-binary "@recipes-bulk.json"

curl -XPOST $ESHOST/recipes/_search
{
  "query": {
    "match_all": {}
  }
}

### Searching arrays of objects (the wrong way)

```
GET /recipes/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "ingredients.name": "parmesan"
          }
        },
        {
          "range": {
            "ingredients.amount": {
              "gte": 100
            }
          }
        }
      ]
    }
  }
}
```

## Create the correct mapping (using the `nested` data type)

```
DELETE /recipes
```

```
PUT /recipes
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "title": { "type": "text" },
      "description": { "type": "text" },
      "preparation_time_minutes": { "type": "integer" },
      "steps": { "type": "text" },
      "created": { "type": "date" },
      "ratings": { "type": "float" },
      "servings": {
        "properties": {
          "min": { "type": "integer" },
          "max": { "type": "integer" }
        }
      },
      "ingredients": {
        "type": "nested",
        "properties": {
          "name": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword"
              }
            }
          },
          "amount": { "type": "integer" },
          "unit": { "type": "keyword" }
        }
      }
    }
  }
}
```

[Import the test data again](#importing-test-data).

## Using the `nested` query

```
GET /recipes/_search
{
  "query": {
    "nested": {
      "path": "ingredients",
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "ingredients.name": "parmesan"
              }
            },
            {
              "range": {
                "ingredients.amount": {
                  "gte": 100
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

PUT /my-index-000001
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 2
  }
}

GET /recipes/_search
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
  "query": {
    "nested": {
      "path": "ingredients",
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "ingredients.name": "parmesan"
              }
            },
            {
              "range": {
                "ingredients.amount": {
                  "gte": 100
                }
              }
            }
          ]
        }
      }
    }
  }
}
