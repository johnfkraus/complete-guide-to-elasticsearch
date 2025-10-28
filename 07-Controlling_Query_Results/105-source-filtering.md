## Lesson 55—Source filtering

By default the entire contents of the _source field are returned.

Removing fields can improve performance.

You can query to find the document id and use it to retrieve information from some other data store.

### Excluding the `_source` field altogether

Set "_source" = false.


```
GET /recipes/_search
{
  "_source": false,
  "query": {
    "match": { "title": "pasta" }
  }
}
```

## Only returning the `created` field

```
GET /recipes/_search
{
  "_source": "created",
  "query": {
    "match": { "title": "pasta" }
  }
}
```

## Only returning an object's key

```
GET /recipes/_search
{
  "_source": "ingredients.name",
  "query": {
    "match": { "title": "pasta" }
  }
}
```

## Returning all of an object's keys

```
GET /recipes/_search
{
  "_source": "ingredients.*",
  "query": {
    "match": { "title": "pasta" }
  }
}
```

## Returning the `ingredients` object with all keys, __and__ the `servings` field

```
GET /recipes/_search
{
  "_source": [ "ingredients.*", "servings" ],
  "query": {
    "match": { "title": "pasta" }
  }
}
```

## From _source, including all of the `ingredients` object's keys, except the `name` key. I.e., exclude one key.

```
GET /recipes/_search
{
  "_source": {
    "includes": "ingredients.*",
    "excludes": "ingredients.name"
  },
  "query": {
    "match": { "title": "pasta" }
  }
}
```
