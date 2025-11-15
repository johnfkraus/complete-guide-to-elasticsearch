## Lesson 127 -- `fuzzy` query

The match query is a full-text query, and is analyzed.

Fuzzy query is term level query, and is not analyzed.

Since we're searching a field which is analyzed using the lower-case token filter, the following query does not match within the inverted index.

```
GET /products/_search
{
  "query": {
    "fuzzy": {
      "name": {
        "value": "LOBSTER",
        "fuzziness": "auto"
      }
    }
  }
}
```

When the value is lowercased, we find lobster AND oyster.


```
GET /products/_search
{
  "query": {
    "fuzzy": {
      "name": {
        "value": "lobster",
        "fuzziness": "auto"
      }
    }
  }
}
```


The use of /default in an Elasticsearch query URL, such as /&lt;index&gt;/default/_search, indicates the document type within an index. 
Explanation: 

• Document Types (Legacy): In older versions of Elasticsearch (before 7.0), an index could contain multiple "types" of documents. For example, an orders index might have a customer type and a product type. The /default part of the URL would specify which document type you were querying within that index. 
• Removal of Document Types: Starting with Elasticsearch 7.0, the concept of multiple document types within a single index was removed. The recommendation now is to have "one type per index," meaning all documents in an index should have a similar structure. [1]  
• Current Behavior: If you are using a modern version of Elasticsearch (7.x or later) and still see /default in your queries, it's likely a remnant from an older indexing process or a default behavior where documents were indexed with a type named "default." In these cases, the _type field for documents might still show default or _doc. 
• Modern Approach: In current Elasticsearch versions, you would typically omit the document type from the URL and simply query the index directly, like /&lt;index&gt;/_search. The _doc type is the default when no specific type is provided. 

In summary: While /default was used to specify document types in older Elasticsearch versions, its presence in modern queries usually reflects a legacy indexing pattern or a default type designation rather than a functional requirement for querying. The current best practice is to have one document type per index and query the index directly without specifying a document type in the URL. 

AI responses may include mistakes.

[1] https://stackoverflow.com/questions/64040651/what-is-the-use-of-default-in-elastic-search

