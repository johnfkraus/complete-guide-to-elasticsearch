## Lesson 128 -- Adding synonyms

### Creating index with custom analyzer

The same custom analyzer will be used on indexed documents and queries.

Sample synonym configured in the index mapping: "awful => terrible"

A query for either "awful" and "terrible" will both be a match.

Term-level queries are not analyzed, so don't try to combine terms and synonyms.
If we were to search for the term "awful" with a term-level query, it wouldn't match anything, because "awful" has been replaced with "terrible" in the inverted index.

```
PUT /synonyms
{
  "settings": {
    "analysis": {
      "filter": {
        "synonym_test": {
          "type": "synonym", 
          "synonyms": [
            "awful => terrible",
            "awesome => great, super",
            "elasticsearch, logstash, kibana => elk",
            "weird, strange"
          ]
        }
      },
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "synonym_test"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "my_analyzer"
      }
    }
  }
}
```

## Testing the analyzer (with synonyms)

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "awesome"
}
```

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "Elasticsearch"
}
```

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "weird"
}
```

```
POST /synonyms/_analyze
{
  "analyzer": "my_analyzer",
  "text": "Elasticsearch is awesome, but can also seem weird sometimes."
}
```

## Adding a test document

```
POST /synonyms/_doc
{
  "description": "Elasticsearch is awesome, but can also seem weird sometimes."
}
```

## Searching the index for synonyms

```
GET /synonyms/_search
{
  "query": {
    "match": {
      "description": "great"
    }
  }
}
```

```
GET /synonyms/_search
{
  "query": {
    "match": {
      "description": "awesome"
    }
  }
}
```