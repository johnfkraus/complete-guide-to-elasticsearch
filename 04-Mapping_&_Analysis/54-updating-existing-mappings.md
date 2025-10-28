## Lesson 54 - Updating existing mappings

Slides are [here](./../elasticsearch-slides-udemy/Mapping_and_Analysis/54-Updating_existing_mappings.pdf)

For filtering, the keyword data type is ideal.

### Generally, field mappings cannot be updated

This query won't work.
```
PUT /reviews/_mapping
{
  "properties": {
    "product_id": {
      "type": "keyword"
    }
  }
}
```

## Some mapping parameters can be changed

The `ignore_above` mapping parameter _can_ be updated, for instance.
```
PUT /reviews/_mapping
{
  "properties": {
    "author": {
      "properties": {
        "email": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    }
  }
}
```