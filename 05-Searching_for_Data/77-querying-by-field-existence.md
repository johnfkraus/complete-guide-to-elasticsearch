## Lesson 77 - Querying by field existence

The exists query searches indexed values, not source values.


How empty values are indexed:

- Field Value: NULL
- Indexed Value: N/A

- Field Value: []
- Indexed Value: N/A

- Field Value: ""
- Indexed Value: ""
An empty string is not considered an empty value.  Documents with "" will be matched by the exists query.



### Basic usage

This query matches all documents that have an indexed value for the field ("tags.keyword").

```
GET /products/_search
{
  "query": {
    "exists": {
      "field": "tags.keyword"
    }
  }
}
```

**SQL:** `SELECT * FROM products WHERE tags IS NOT NULL`

### Inverting the query

There is no dedicated query for this, so we do it with the `bool` query.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "exists": {
            "field": "tags.keyword"
          }
        }
      ]
    }
  }
}
```

**SQL:** `SELECT * FROM products WHERE tags IS NULL`


