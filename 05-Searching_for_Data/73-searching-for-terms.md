## Lesson 73 - Searching for terms

### Basic usage

```
GET /products/_search
{
  "query": {
    "term": {
      "tags.keyword": "Vegetable"
    }
  }
}
```

## Explicit syntax

A more explicit syntax than the above. Use this if you need to add parameters to the query.

```
GET /products/_search
{
  "query": {
    "term": {
      "tags.keyword": {
        "value": "Vegetable"
      }
    }
  }
}
```

## Case insensitive search

```
GET /products/_search
{
  "query": {
    "term": {
      "tags.keyword": {
        "value": "Vegetable",
        "case_insensitive": true
      }
    }
  }
}
```

## Searching for multiple terms

Use the "terms" query.

```
GET /products/_search
{
  "query": {
    "terms": {
      "tags.keyword": ["Soup", "Meat"]
    }
  }
}
```

## Searching for booleans

```
GET /products/_search
{
  "query": {
    "term": {
      "is_active": true
    }
  }
}
```

## Searching for numbers

```
GET /products/_search
{
  "query": {
    "term": {
      "in_stock": 1
    }
  }
}
```

## Searching for dates

```
GET /products/_search
{
  "query": {
    "term": {
      "created": "2007/10/14"
    }
  }
}
```

## Searching for timestamps

```
GET /products/_search
{
  "query": {
    "term": {
      "created": "2007/10/14 12:34:56"
    }
  }
}
```

Elasticsearch term-level queries are designed for searching structured data based on exact values, unlike full-text queries which analyze text and consider relevancy. They operate on the precise terms stored in the inverted index, making them suitable for fields mapped as keyword or for numerical, boolean, or date fields. 
Here are some common term-level queries: 

- Term query: Finds documents where a specific field contains an exact, unanalyzed term. This is case-sensitive by default but can be made case-insensitive with the case_insensitive parameter. 

    GET /_search
    {
      "query": {
        "term": {
          "status.keyword": "published"
        }
      }
    }

- Terms query: Finds documents where a specific field contains any of the exact terms provided in a list. 

    GET /_search
    {
      "query": {
        "terms": {
          "tag.keyword": ["tech", "programming"]
        }
      }
    }

- Range query: Finds documents where a field's value falls within a specified range (e.g., dates, numbers, or strings). 

    GET /_search
    {
      "query": {
        "range": {
          "price": {
            "gte": 10,
            "lte": 50
          }
        }
      }
    }

- Exists query: Finds documents where a specific field has any non-null indexed value. 

    GET /_search
    {
      "query": {
        "exists": {
          "field": "description"
        }
      }
    }

- Prefix query: Finds documents where a field contains terms that begin with a specified exact prefix. 

    GET /_search
    {
      "query": {
        "prefix": {
          "product_code.keyword": "XYZ-"
        }
      }
    }

- Wildcard query: Finds documents where a field contains terms matching a wildcard pattern, using ? for single characters and * for multiple characters. 

    GET /_search
    {
      "query": {
        "wildcard": {
          "filename.keyword": "report*.pdf"
        }
      }
    }

- Fuzzy query: Finds documents containing terms similar to the search term, based on the Damerau–Levenshtein edit distance. 

    GET /_search
    {
      "query": {
        "fuzzy": {
          "city.keyword": "Londn"
        }
      }
    }

- Term-level queries are generally not recommended for full-text fields (analyzed text) unless used with a keyword subfield, as they will search for the exact, unanalyzed form of the input, which may not match what was indexed after analysis. 
- They are well-suited for filtering and exact matching on structured data types. 
