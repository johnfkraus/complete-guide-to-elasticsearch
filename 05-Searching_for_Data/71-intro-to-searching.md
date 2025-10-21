## Lesson 71 - Intro to searching

### URI Searches

GET /products/_search?q=name:sauvignon AND tags:wine

### Query DSL

GET /products/_search
{
  "query": {
    "match_all": {}
  }
}
