"""
I have this cloud elastic cluster:
{
  "name": "serverless",
  "cluster_name": "fc4715a87aaf4d62a9bf28a9434e8a2d",
  "cluster_uuid": "oouVAjVCR-SkoYcgaLwfYA",
  "version": {
    "number": "8.11.0",
    "build_flavor": "serverless",
    "build_type": "docker",
    "build_hash": "00000000",
    "build_date": "2023-10-31",
    "build_snapshot": false,
    "lucene_version": "9.7.0",
    "minimum_wire_compatibility_version": "8.11.0",
    "minimum_index_compatibility_version": "8.11.0"
  },
  "tagline": "You Know, for Search"
}
How can I connect to this using pytho?
I don't know my cloud id.  How do I get it?
"""
from pprint import pprint
from elasticsearch import Elasticsearch  #  7.12.0

# Replace these with your actual details
# cloud_id = "https://my-elasticsearch-project-fc4715.es.us-central1.gcp.elastic.cloud"  # You get this from the Elastic Cloud console
api_key = "ZlBXSmg1b0Iyc1FIMF9yMi1TaHk6ZTNWWHBlQnVrQ2JkcmdmYVJqckxjUQ=="    # The API Key you generated in Elastic Cloud

# https://my-elasticsearch-project-fc4715.es.us-central1.gcp.elastic.cloud

# Create the Elasticsearch client
# es = Elasticsearch(
#     cloud_id=cloud_id,
#     api_key=api_key
# )
#
# # Check if the connection is successful
# if es.ping():
#     print("Successfully connected to Elasticsearch!")
# else:
#     print("Connection failed.")
#
# # Example of a simple query: Search for documents in an index
# index_name = "your_index_name"  # Replace with your index name
# query = {
#     "query": {
#         "match_all": {}  # A simple query to fetch all documents
#     }
# }
#
# # Run the search query
# response = es.search(index=index_name, body=query)
#
# # Print the query response
# print("Search results:")
# print(response)
#
# from elasticsearch import Elasticsearch

# Your serverless endpoint
ES_URL = "https://my-elasticsearch-project-fc4715.es.us-central1.gcp.elastic.cloud"

# Your API key (Base64 string: id:api_key)
API_KEY = "ZlBXSmg1b0Iyc1FIMF9yMi1TaHk6ZTNWWHBlQnVrQ2JkcmdmYVJqckxjUQ=="\

# Create client
es = Elasticsearch(
    ES_URL,
    api_key=API_KEY,
)

# Test connection
print("Connected:", es.info())

# Example query
resp = es.search(
    index="products",
    query={
        "match_all": {}
    }
)

print(f"{resp=}")

hits = resp["hits"]["hits"]
for hit in hits:
    doc_id = hit["_id"]
    source_data = hit["_source"]
    print(f"Document ID: {doc_id}, Source: {source_data}")



#print(resp["raw"])