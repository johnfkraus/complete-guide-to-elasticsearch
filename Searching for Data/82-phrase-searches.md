## Lesson 82 - Phrase searches

Word order matters in a phrase.

No other words in between words in the phrase.

Hyphens and parentheses are dropped during the analysis process.

### Basic usage

```

GET /products/_search
{
  "query": {
    "match_phrase": {
      "description": "Complete Guide to Elasticsearch"
    }
  }
}

GET /products/_search
{
  "query": {
    "match_phrase": {
      "name": "mango juice"
    }
  }
}
```

### More examples

```
GET /products/_search
{
  "query": {
    "match_phrase": {
      "name": "juice mango"
    }
  }
}
```

```
GET /products/_search
{
  "query": {
    "match_phrase": {
      "name": "Juice (mango)"
    }
  }
}
```

```
GET /products/_search
{
  "query": {
    "match_phrase": {
      "description": "browse the internet"
    }
  }
}
```