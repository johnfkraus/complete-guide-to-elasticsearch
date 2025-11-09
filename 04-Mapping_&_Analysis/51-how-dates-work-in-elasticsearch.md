## Lesson 51 - How dates work in Elasticsearch

https://en.wikipedia.org/wiki/ISO_8601

Three ways to specify dates:

- Specially-formatted strings
- milliseconds since the epoch (1/1/1970) (long)
- seconds since the epoch (integer)

- Custom date formats are supported.

Three supported formats:
- Date without time.
  - Time is optional.
  - ES assumes midnight when converting to ms.
- Date with time.
  - If no TZ is specified, it is assumed to be in the UTC time zone.
- ms since epoch (long)

Dates are stored as a long using UTC.

_source shows how the date was supplied when doc was created, not how the date is stored for searching.

### Index a document Supplying only a date
```
PUT /reviews/_doc/2
{
  "rating": 4.5,
  "content": "Not bad. Not bad at all!",
  "product_id": 123,
  "created_at": "2015-03-27",
  "author": {
    "first_name": "Average",
    "last_name": "Joe",
    "email": "avgjoe@example.com"
  }
}
```

## Supplying both a date and time
```
PUT /reviews/_doc/3
{
  "rating": 3.5,
  "content": "Could be better",
  "product_id": 123,
  "created_at": "2015-04-15T13:07:41Z",
  "author": {
    "first_name": "Spencer",
    "last_name": "Pearson",
    "email": "spearson@example.com"
  }
}
```

## Specifying the UTC offset
```
PUT /reviews/_doc/4
{
  "rating": 5.0,
  "content": "Incredible!",
  "product_id": 123,
  "created_at": "2015-01-28T09:21:51+01:00",
  "author": {
    "first_name": "Adam",
    "last_name": "Jones",
    "email": "adam.jones@example.com"
  }
}
```

## Supplying a timestamp (milliseconds since the epoch)

- Don't supply UNIX timestamps for default date field.
- Multiply unix seconds by 1,000.
- Don't attach a time zone.

```
# Equivalent to 2015-07-04T12:01:24Z
PUT /reviews/_doc/5
{
  "rating": 4.5,
  "content": "Very useful",
  "product_id": 123,
  "created_at": 1436011284000,
  "author": {
    "first_name": "Taylor",
    "last_name": "West",
    "email": "twest@example.com"
  }
}
```

## Retrieving documents
```
GET /reviews/_search
{
  "query": {
    "match_all": {}
  }
}
```

## Testing the `standard` analyzer on a date
```
POST /_analyze
{
  "text": "2015-03-27",
  "analyzer": "standard"
}
POST /_analyze
{
  "text": "2015-04-15T13:07:41Z",
  "analyzer": "standard"
}
POST /_analyze
{
  "text": "2015-01-28T09:21:51+01:00",
  "analyzer": "standard"
}
POST /_analyze
{
  "text": 1436011284000,
  "analyzer": "standard"
}

```

GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "track_total_hits": true
}

PUT my-date-index
{
  "mappings": {
    "properties": {
      "date": {
        "type":   "date",
        "format": "yyyy-MM-dd"
      }
    }
  }
}
GET /_cat/indices
GET /my-date-index/_mapping
POST /my-date-index/_doc
{
  "name": "Coffee Maker",
  "price": 64,
  "in_stock": 10,
  "date": "2015-01-01"
}
POST /my-date-index/_doc
{
  "name": "Ice Cream Maker",
  "price": 44,
  "in_stock": 3,
  "date": "2015-04-15T13:07:41Z"
}

DELETE /my-date-index
PUT my-date-index
{
  "mappings": {
    "properties": {
      "created": {
        "type": "date"
      },
      "expires": {
        "type": "date"
      },
      "date_text": {
        "type": "text"
      }
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "track_total_hits": true
}


GET /_cat/indices
GET /my-date-index/_mapping
POST /my-date-index/_doc
{
  "name": "Coffee Maker",
  "price": 64,
  "in_stock": 10,
  "created": 1744722461000,
  "expires": "2025-04-15T13:07:41Z",
  "date_text": "2026-04-15T13:07:41Z",
  "date_implicit": "2028-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Ice Cream Maker",
  "price": 44,
  "in_stock": 3,
  "created": 1420074021000,
  "expires": "2015-01-01T01:00:21Z",
  "date_text": "2016-04-15T13:07:41Z",
  "date_implicit": "2017-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Dog food",
  "price": 23,
  "in_stock": 5,
  "date": "2007-04-15T13:07:41"
}
POST /my-date-index/_doc
{
  "name": "Bed",
  "price": 144,
  "in_stock": 11,
  "created": 1176642461000,
  "expires": "2007-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Chair 2",
  "price": 101,
  "in_stock": 7,
  "created": 1744722461000,
  "date": "2025-04-15T13:07:41Z"
}
GET /my-date-index/_search
{
  "query": {
    "date_text": "2016"
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 100
      }
    } 
  }
}

GET /my-date-index/_search
{
  "query": {
    "range": {
      "date": {
        "gt": "2015-03-01"
      }
    } 
  }
}
GET /my-date-index/_search
{
  "query": {
    "term": {
      "date_text": "2015"
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "created": {
        "gt": "2020-01-01"
      }
    } 
  }
}



DELETE /my-date-index
PUT my-date-index
{
  "mappings": {
    "properties": {
      "epoch": {
        "type": "date"
      },
      "expires": {
        "type": "date"
      },
      "date_text": {
        "type": "text"
      }
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "track_total_hits": true
}


GET /_cat/indices
GET /my-date-index/_mapping
POST /my-date-index/_doc
{
  "name": "Coffee Maker",
  "price": 64,
  "in_stock": 10,
  "epoch": 1744722461000,
  "expires": "2025-04-15T13:07:41Z",
  "date_text": "2026-04-15T13:07:41Z",
  "date_implicit": "2028-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Ice Cream Maker",
  "price": 44,
  "in_stock": 3,
  "epoch": 1420074021000,
  "expires": "2015-01-01T01:00:21Z",
  "date_text": "2016-04-15T13:07:41Z",
  "date_implicit": "2017-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Dog food",
  "price": 23,
  "in_stock": 5,
  "date": "2007-04-15T13:07:41"
}
POST /my-date-index/_doc
{
  "name": "Bed",
  "price": 144,
  "in_stock": 11,
  "epoch": 1176642461000,
  "expires": "2007-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Chair 2",
  "price": 101,
  "in_stock": 7,
  "epoch": 1744722461000,
  "date": "2025-04-15T13:07:41Z"
}
GET /my-date-index/_search
{
  "query": {
    "date_text": "2016"
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 100
      }
    } 
  }
}

GET /my-date-index/_search
{
  "query": {
    "range": {
      "date": {
        "gt": "2015-03-01"
      }
    } 
  }
}
GET /my-date-index/_search
{
  "query": {
    "term": {
      "date_text": "2015"
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "epoch": {
        "gt": "2020-01-01"
      }
    } 
  }
}



DELETE /my-date-index
PUT my-date-index
{
  "mappings": {
    "properties": {
      "epoch": {
        "type": "date"
      },
      "explicit": {
        "type": "date"
      },
      "date_text": {
        "type": "text"
      }
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "track_total_hits": true
}


GET /_cat/indices
GET /my-date-index/_mapping
POST /my-date-index/_doc
{
  "name": "Coffee Maker 2",
  "price": 64,
  "in_stock": 10,
  "epoch": 1744722461000,
  "explicit": "2025-04-15T13:07:41Z",
  "date_text": "2026-04-15T13:07:41Z",
  "date_implicit": "2028-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Ice Cream Maker 2",
  "price": 44,
  "in_stock": 3,
  "epoch": 1420074021000,
  "explicit": "2015-01-01T01:00:21Z",
  "date_text": "2016-04-15T13:07:41Z",
  "date_implicit": "2017-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Dog food",
  "price": 23,
  "in_stock": 5,
  "date": "2007-04-15T13:07:41"
}
POST /my-date-index/_doc
{
  "name": "Bed",
  "price": 144,
  "in_stock": 11,
  "epoch": 1176642461000,
  "explicit": "2007-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Chair 2",
  "price": 101,
  "in_stock": 7,
  "epoch": 1744722461000,
  "explicit": "2025-04-15T13:07:41Z"
}
GET /my-date-index/_search
{
  "query": {
    "date_text": "2016"
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 100
      }
    } 
  }
}

GET /my-date-index/_search
{
  "query": {
    "range": {
      "explicit": {
        "gt": "2015-03-01"
      }
    } 
  }
}
GET /my-date-index/_search
{
  "query": {
    "term": {
      "date_text": "2016"
    }
  }
}
GET /my-date-index/_explain/FUAyZZoBCEGqWRPsVmm5
{
  "query": {
    "term": {
      "date_text": "2016"
    }
  }
}
GET /my-date-index/_explain/FUAyZZoBCEGqWRPsVmm5
{
  "query": {
    "term": {
      "date_text": "2016"
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "epoch": {
        "gt": "2014-01-01"
      }
    } 
  }
}

GET /my-date-index/_search
{
  "query": {
    "range": {
      "epoch": {
        "gt": 1320074021000
      }
    } 
  }
}


DELETE /my-date-index
PUT my-date-index
{
  "mappings": {
    "properties": {
      "epoch": {
        "type": "date",
        "format": "epoch_millis"
      },
      "explicit": {
        "type": "date"
      },
      "date_text": {
        "type": "text"
      }
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  }
}
GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "track_total_hits": true
}

GET /_cat/indices
GET /my-date-index/_mapping
POST /my-date-index/_doc
{
  "name": "Coffee Maker",
  "price": 64,
  "in_stock": 10,
  "epoch": 1744722461000,
  "explicit": "2025-04-15T13:07:41Z",
  "date_text": "2026-04-15T13:07:41Z",
  "date_implicit": "2028-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Ice Cream Maker",
  "price": 44,
  "in_stock": 3,
  "epoch": 1420074021000,
  "explicit": "2015-01-01T01:00:21Z",
  "date_text": "2016-04-15T13:07:41Z",
  "date_implicit": "2017-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Dog food",
  "price": 23,
  "in_stock": 5,
  "date_implicit": "2007-04-15T13:07:41"
}
POST /my-date-index/_doc
{
  "name": "Bed",
  "price": 144,
  "in_stock": 11,
  "epoch": 1176642461000,
  "explicit": "2007-04-15T13:07:41Z"
}
POST /my-date-index/_doc
{
  "name": "Chair",
  "price": 101,
  "in_stock": 7,
  "epoch": 1744722461000,
  "explicit": "2025-04-15T13:07:41Z"
}
GET /my-date-index/_search
{
  "query": {
    "match": {
      "date_text": "2016"      
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 100
      }
    } 
  }
}

GET /my-date-index/_search
{
  "query": {
    "range": {
      "explicit": {
        "gt": "2015-03-01"
      }
    } 
  }
}
GET /my-date-index/_search
{
  "query": {
    "term": {
      "date_text": "2016"
    }
  }
}
GET /my-date-index/_explain/J4xdZZoBa2Q2SW-AUUVc
{
  "query": {
    "term": {
      "date_text": "2016"
    }
  }
}
GET /my-date-index/_explain/FUAyZZoBCEGqWRPsVmm5
{
  "query": {
    "term": {
      "date_text": "2016"
    }
  }
}
GET /my-date-index/_search
{
  "query": {
    "range": {
      "epoch": {
        "gt": "2014-01-01"
      }
    } 
  }
}



GET /my-date-index/_explain/F0BdZZoBCEGqWRPsPGkp
{
  "query": {
    "range": {
      "epoch": {
        "gt": "2014-01-01"
      }
    } 
  }
}

GET /my-date-index/_search
{
  "query": {
    "range": {
      "epoch": {
        "gt": 1320074021000
      }
    } 
  }
}

GET /my-date-index/_explain/F0BdZZoBCEGqWRPsPGkp
{
  "query": {
    "range": {
      "epoch": {
        "gt": 1320074021000
      }
    } 
  }
}

In Elasticsearch, I have an large index in which some date fields were indexed as text, not dates.  I want to be able to execute range queries on these dates.  How can I fix this without having to re-index the entire set of data?

Current records:

GET /my-date-index/_search
{
  "query": {
    "match_all": {}
  }
}

{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "my-date-index",
        "_id": "KYxnZZoBa2Q2SW-AmkWT",
        "_score": 1,
        "_source": {
          "name": "Coffee Maker 2",
          "price": 64,
          "in_stock": 10,
          "epoch": 1744722461000,
          "explicit": "2025-04-15T13:07:41Z",
          "date_text": "2026-04-15T13:07:41Z",
          "date_implicit": "2028-04-15T13:07:41Z"
        }
      },
      {
        "_index": "my-date-index",
        "_id": "GkBnZZoBCEGqWRPssGnD",
        "_score": 1,
        "_source": {
          "name": "Ice Cream Maker 2",
          "price": 44,
          "in_stock": 3,
          "epoch": 1420074021000,
          "explicit": "2015-01-01T01:00:21Z",
          "date_text": "2016-04-15T13:07:41Z",
          "date_implicit": "2017-04-15T13:07:41Z"
        }
      },
      {
        "_index": "my-date-index",
        "_id": "G0BnZZoBCEGqWRPsumlT",
        "_score": 1,
        "_source": {
          "name": "Dog food",
          "price": 23,
          "in_stock": 5,
          "date_implicit": "2007-04-15T13:07:41"
        }
      },
      {
        "_index": "my-date-index",
        "_id": "HEBoZZoBCEGqWRPsRGlH",
        "_score": 1,
        "_source": {
          "name": "Chair 2",
          "price": 101,
          "in_stock": 7,
          "epoch": 1744722461000,
          "explicit": "2025-04-15T13:07:41Z"
        }
      }
    ]
  }
}


Current mapping:

{
  "my-date-index": {
    "mappings": {
      "properties": {
        "date_implicit": {
          "type": "date"
        },
        "date_text": {
          "type": "text"
        },
        "epoch": {
          "type": "date",
          "format": "epoch_millis"
        },
        "explicit": {
          "type": "date"
        },
        "in_stock": {
          "type": "long"
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "price": {
          "type": "long"
        }
      }
    }
  }
}

Try range search on "date_text" field:

GET /my-date-index/_search
{
  "query": {
    "range": {
      "date_text": {
        "gt": "2014-01-01"
      }
    } 
  }
}

GET my-index-/_search
{
  "query": {
    "range": {
      "your_date_field_parsed": {
        "gte": "2024-01-01",
        "lte": "2024-12-31"
      }
    }
  }
}

To enable range queries on date fields currently indexed as text in Elasticsearch without a full reindex, you can use the following approach: Add a new date-typed field.
Modify your index mapping to introduce a new field with a date type. This new field will store the correctly parsed date values. You can specify the format if your date strings follow a specific pattern.

PUT your_index_name/_mapping
{
  "properties": {
    "your_date_field_parsed": {
      "type": "date",
      "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd" // Adjust format to match your data
    }
  }
}

PUT my-date-index/_mapping
  {
    "properties": {
      "your_date_field_parsed": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd" }
    }
  }

POST my-date-index/_update_by_query
{
  "script": {
    "source": "if (ctx._source.date_text != null) { ctx._source.your_date_field_parsed = ctx._source.date_text }",
    "lang": "painless"
  },
  "query": {
    "exists": {
      "field": "date_text"
    }
  }
}

