## Lesson 82 - Phrase searches

A phrase search matches if the query words in order are found in the field.  Partial matches = true.

Word order matters in a phrase.

To match, no other words are allowed in between words in the phrase.

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