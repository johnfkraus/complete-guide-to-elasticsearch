# Value counts:
GET /products/_search
{
  "size": 0,
  "aggs": {
    "value_counts": {
      "terms": {
        "field": "is_active",
        "size": 100
      }
    }
  }
}

# value counts for keyword
GET /products/_search
{
  "size": 0,
  "aggs": {
    "value_counts": {
      "terms": {
        "field": "tags.keyword",
        "size": 100
      }
    }
  }
}

# min/max date field
GET /products/_search
{
  "size": 0,
  "aggs": {
    "min_date": {
      "min": {
        "field": "created"
      }
    },
    "max_date": {
      "max": {
        "field": "created"
      }
    }
  }
}
