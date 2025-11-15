# Multi-field mappings

A field may be mapped in multiple ways.  
- Allows you to query a field in different ways (querying the text mapping OR the keyword mapping, for example.)
- A text field may also be mapped as a keyword field at the same time.
  - Add ingredients:fields:keyword:type:keyword to the mapping (see below).
    - Terms will not be lowercased in a keyword mapping.
  - This adds another inverted index for the ingredients field.
- We can't run aggregations on text fields.
  - Aggregations can be run on keyword, date and number fields.

### Add `keyword` mapping to a `text` field
```
PUT /multi_field_test
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text"
      },
      "ingredients": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword"
          }
        }
      }
    }
  }
}
```

### Index a test document
```
POST /multi_field_test/_doc
{
  "description": "To make this spaghetti carbonara, you first need to...",
  "ingredients": ["Spaghetti", "Bacon", "Eggs"]
}
```

### Retrieve documents
```
GET /multi_field_test/_search
{
  "query": {
    "match_all": {}
  }
}
```

### Querying the `text` mapping

The "match" query is the main query used for full text searches.

```
GET /multi_field_test/_search
{
  "query": {
    "match": {
      "ingredients": "Spaghetti"
    }
  }
}
```

## Querying the `keyword` mapping

To search for exact matches, we use a "term" level query.

A term query requires an exact match for the target field.

The following will query the inverted index that contains the raw string values supplied at index time (i.e., values that were not analyzed.)

```
GET /multi_field_test/_search
{
  "query": {
    "term": {
      "ingredients.keyword": "Spaghetti"
    }
  }
}
```

## Clean up
```
DELETE /multi_field_test
```