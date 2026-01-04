Below is a simple, self‑contained example of using the Builder pattern (with method chaining) to construct an Elasticsearch query JSON in Python.[1][2][3]

## Query builder class

```python
class ESQueryBuilder:
    def __init__(self):
        self._must = []
        self._filter = []
        self._should = []
        self._must_not = []
        self._sort = []
        self._from = 0
        self._size = 10

    def must_match(self, field, value):
        self._must.append({"match": {field: value}})
        return self

    def filter_term(self, field, value):
        self._filter.append({"term": {field: value}})
        return self

    def should_match(self, field, value):
        self._should.append({"match": {field: value}})
        return self

    def must_not_term(self, field, value):
        self._must_not.append({"term": {field: value}})
        return self

    def sort(self, field, order="asc"):
        self._sort.append({field: {"order": order}})
        return self

    def paginate(self, from_, size):
        self._from = from_
        self._size = size
        return self

    def build(self):
        bool_query = {}
        if self._must:
            bool_query["must"] = self._must
        if self._filter:
            bool_query["filter"] = self._filter
        if self._should:
            bool_query["should"] = self._should
        if self._must_not:
            bool_query["must_not"] = self._must_not

        query = {"query": {"bool": bool_query}}
        if self._sort:
            query["sort"] = self._sort
        query["from"] = self._from
        query["size"] = self._size
        return query
```

## Using the builder

```python
builder = (
    ESQueryBuilder()
    .must_match("title", "python")
    .filter_term("status", "published")
    .should_match("tags", "elasticsearch")
    .paginate(from_=0, size=20)
    .sort("published_at", "desc")
)

es_query = builder.build()
print(es_query)
```

`es_query` will be a dict ready to send as the body of an Elasticsearch `_search` request, and you can extend the builder with more methods for ranges, aggregations, etc. as needed.[4][1]

[1](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-query-bool/)
[2](https://refactoring.guru/design-patterns/builder/python/example)
[3](https://softwarepatterns.com/python/builder-software-pattern-python-example)
[4](https://opendistro.github.io/for-elasticsearch-docs/docs/elasticsearch/bool/)
[5](https://pypi.org/project/elasticsearch-query-builder/)
[6](https://www.linkedin.com/pulse/designing-robust-reusable-code-builder-pattern-python-abhay-singh)
[7](https://sergiiblog.com/python-flask-elasticsearch-builder-pattern-and-dto-search-criteria-object/)
[8](https://www.elastic.co/guide/en/elasticsearch/client/net-api/7.17/bool-queries.html)
[9](https://www.elastic.co/docs/reference/elasticsearch/clients/python/esql-query-builder)
[10](https://sergiiblog.com/python-flask-elasticsearch-search-service-and-query-builder/)