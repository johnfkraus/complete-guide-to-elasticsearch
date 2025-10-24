# Defining field aliases

Field aliases CAN be update, but only its target field.

Perform a mapping update with a new path value.

Alias is a query level construct; not used for indexing.

ES also supports index aliases.  Typically used for large data volumes.


## Add `comment` alias pointing to the `content` field
```
PUT /reviews/_mapping
{
  "properties": {
    "comment": {
      "type": "alias",
      "path": "content"
    }
  }
}
```
Mapping before:
{
  "reviews": {
    "mappings": {
      "properties": {
        "author": {
          "properties": {
            "email": {
              "type": "keyword"
            },
            "first_name": {
              "type": "text"
            },
            "last_name": {
              "type": "text"
            }
          }
        },
        "content": {
          "type": "text"
        },
        "created_at": {
          "type": "date"
        },
        "product_id": {
          "type": "integer"
        },
        "rating": {
          "type": "float"
        }
      }
    }
  }
}

Mapping after:
{
  "reviews": {
    "mappings": {
      "properties": {
        "author": {
          "properties": {
            "email": {
              "type": "keyword"
            },
            "first_name": {
              "type": "text"
            },
            "last_name": {
              "type": "text"
            }
          }
        },
        "comment": {
          "type": "alias",
          "path": "content"
        },
        "content": {
          "type": "text"
        },
        "created_at": {
          "type": "date"
        },
        "product_id": {
          "type": "integer"
        },
        "rating": {
          "type": "float"
        }
      }
    }
  }
}




## Using the field alias
```
GET /reviews/_search
{
  "query": {
    "match": {
      "comment": "outstanding"
    }
  }
}
```

## Using the "original" field name still works
```
GET /reviews/_search
{
  "query": {
    "match": {
      "content": "outstanding"
    }
  }
}
```