# For a more simplified version using the Bonsai URL directly(which is common for Bonsai - hosted OpenSearch):

```python
from opensearchpy import OpenSearch
import urllib3

# Disable warnings for self-signed certificates if needed
urllib3.disable_warnings()


def get_opensearch_field_counts(
        bonsai_url="https://username:password@your-bonsai-cluster-url",
        index_name="your_index",
        field_name="your_field",
        size=100
):
    # Create OpenSearch client from Bonsai URL
    client = OpenSearch(
        hosts=[bonsai_url],
        use_ssl=True,
        verify_certs=True,
        ssl_show_warn=False
    )

    # Execute aggregation query
    response = client.search(
        index=index_name,
        body={
            "size": 0,
            "aggs": {
                "value_counts": {
                    "terms": {
                        "field": field_name,
                        "size": size
                    }
                }
            }
        }
    )

    # Process results
    buckets = response["aggregations"]["value_counts"]["buckets"]
    return {bucket["key"]: bucket["doc_count"] for bucket in buckets}


# Example usage
counts = get_opensearch_field_counts(
    bonsai_url="https://user:pass@opensearch-cluster.us-east-1.bonsaisearch.net:443",
    index_name="my_index",
    field_name="category"
)

for value, count in counts.items():
    print(f"{value}: {count}")
```

Make
sure
to:
1.
Install
the
opensearchpy
package: `pip
install
opensearchpy
`
2.
Replace
the
placeholder
values
with your actual Bonsai URL or connection details
3.
Use
the
correct
index
name and field
name
you
want
to
count

Would
you
like
me
to
explain
any
specific
aspect
of
this
implementation?