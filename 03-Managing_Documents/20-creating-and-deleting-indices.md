## Lesson 20 - Creating & Deleting Indices

### Deleting an index

```
DELETE /pages
```

### Creating an index (with settings)

```
PUT /products
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 2
  }
}

PUT /products
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}

# Change the number of replicas:

PUT /products/_settings
{
  "index": {
    "number_of_replicas": 0
  }
}


```