# Show me some Python code that uses the Builder pattern to create an Elasticsearch query.
import sys
import os
sys.path.append(r"/Users/blauerbock/workspaces/python-workout/logging/logapp")
# print(sys.path)

from logapp.logger import SingletonLogger

# Assuming your package is in a 'my_package' directory located one level up from the current script
package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, package_root)

# Now you can import your package
# import my_package
# # Or a specific module within it
# from my_package import my_module

import json

logger = SingletonLogger.get_logger()

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


builder = (
    ESQueryBuilder()
    .must_match("title", "python")
    .must_match("description", "builder")
    .filter_term("status", "published")
    .should_match("tags", "elasticsearch")
    .should_match("tags", "opensearch")
    .paginate(from_=0, size=20)
    .sort("published_at", "desc")
)

es_query = builder.build()

# print(es_query)
print(json.dumps(es_query, indent=2))
