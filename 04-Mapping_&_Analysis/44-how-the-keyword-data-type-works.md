## Lesson 44 - How the `keyword` data type works

- Keyword fields are analyzed with the 'keyword' analyzer.

- The keyword analyzer is a no-op analyzer, outputting the unmodified string as a single token which is placed in the inverted index.
- Keyword fields are used for exact matching, aggregations, and sorting.


## Testing the `keyword` analyzer
```
POST /_analyze
{
  "text": "2 guys walk into   a bar, but the third... DUCKS! :-)",
  "analyzer": "keyword"
}
```