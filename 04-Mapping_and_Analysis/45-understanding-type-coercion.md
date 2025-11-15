## Lesson 45 - Understanding type coercion

- The _source object contains the values supplied at index time, not the values that are indexed.

- Search queries use indexed values, not _source.
- Supplying a floating point for an integer will truncate it to an integer.
- Coercion is NOT used for dynamic mapping.

- Type coercion can be disabled.

PUT /coercion_test
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}

## Supplying a floating point
```
PUT /coercion_test/_doc/1
{
  "price": 7.4
}

GET /coercion_test/_mapping
```

## Supplying a floating point within a string
```
PUT /coercion_test/_doc/2
{
  "price": "7.4"
}
```

## Supplying an invalid value
```
PUT /coercion_test/_doc/3
{
  "price": "7.4m"
}
```

## Retrieve document
```
GET /coercion_test/_doc/2
```

## Clean up
```
DELETE /coercion_test
```