# Understanding arrays

Array values should be of the same type.

Coercion only works for fields that are already mapped.

Use the nested data type for arrays of objects if you need to query the objects independently


### Arrays of strings are concatenated when analyzed
```
POST /_analyze
{
  "text": ["Strings are simply", "merged together."],
  "analyzer": "standard"
}
```

Coercion:

POST /_analyze
{
  "text": ["Strings are simply", "merged together.", 5],
  "analyzer": "standard"
}

POST /_analyze
{
  "text": [37, 45, "9", 5],
  "analyzer": "standard"
}

Fails:

POST /_analyze
{
  "text": [ { "name": "Coffee maker" }, { "name": "Toaster" } ],
  "analyzer": "standard"
}