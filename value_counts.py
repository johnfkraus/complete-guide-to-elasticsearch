"""
# Value counts:
GET /products/_search
{
  "size": 0,
  "aggs": {
    "value_counts": {
      "terms": {
        "field": "is_active",
        "size": 100
      }
    }
  }
}
"""


# To obtain value counts for an Elasticsearch index field in Python, you can use the Elasticsearch Python client with aggregations. Here's how to do it:

from elasticsearch import Elasticsearch

# Connect to your Elasticsearch instance
host = 'https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net'
es = Elasticsearch([host])  # Replace with your ES host

# Create an aggregation query to count field values
response = es.search(
    index="products",  # Replace with your index name
    body={
        "size": 0,  # Don't return documents, just aggregation results
        "aggs": {
            "value_counts": {
                "terms": {
                    "field": "is_active",  # Replace with your field name
                    "size": 100  # Number of top values to return
                }
            }
        }
    }
)

# Process and display the results
buckets = response['aggregations']['value_counts']['buckets']
for bucket in buckets:
    print(f"{bucket['key']}: {bucket['doc_count']}")


# If you're using the newer Elasticsearch client API (v8+):


from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")  # Replace with your ES host

# Perform aggregation
response = es.search(
    index="your_index_name",
    size=0,
    aggs={
        "value_counts": {
            "terms": {
                "field": "your_field_name",
                "size": 100
            }
        }
    }
)

# Process results
buckets = response["aggregations"]["value_counts"]["buckets"]
for bucket in buckets:
    print(f"{bucket['key']}: {bucket['doc_count']}")


# Would you like me to explain how these examples work?