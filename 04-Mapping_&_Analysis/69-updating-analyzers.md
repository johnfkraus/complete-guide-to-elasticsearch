## Lesson 69 -- Updating analyzers

elasticsearch-slides-udemy/04-Mapping_and_Analysis/69-Updating_analyzers.pdf

### Add `description` mapping using `my_custom_analyzer`
```
PUT /analyzer_test/_mapping
{
  "properties": {
    "description": {
      "type": "text",
      "analyzer": "my_custom_analyzer"
    }
  }
}
```

### Index a test document
```
POST /analyzer_test/_doc
{
  "description": "Is that Peter's cute-looking dog?"
}
```

### Search query using `keyword` analyzer
```
GET /analyzer_test/_search
{
  "query": {
    "match": {
      "description": {
        "query": "that",
        "analyzer": "keyword"
      }
    }
  }
}
```

### Close `analyzer_test` index
```
POST /analyzer_test/_close
```

## Update `my_custom_analyzer` (remove `stop` token filter)

Specify the analyzer as if it didn't already exist.

```
PUT /analyzer_test/_settings
{
  "analysis": {
    "analyzer": {
      "my_custom_analyzer": {
        "type": "custom",
        "tokenizer": "standard",
        "char_filter": ["html_strip"],
        "filter": [
          "lowercase",
          "asciifolding"
        ]
      }
    }
  }
}
```

## Open `analyzer_test` index
```
POST /analyzer_test/_open
```

## Retrieve index settings
```
GET /analyzer_test/_settings
```

## Reindex documents
```
POST /analyzer_test/_update_by_query?conflicts=proceed
```

{
  "error": {
    "root_cause": [
      {
        "type": "bonsai_exception",
        "reason": "Update by query is for business+ only"
      }
    ],
    "type": "bonsai_exception",
    "reason": "Update by query is for business+ only"
  },
  "status": 403
}