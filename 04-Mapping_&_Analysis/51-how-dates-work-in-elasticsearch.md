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
GET /


