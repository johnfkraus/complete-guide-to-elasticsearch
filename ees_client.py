from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search, Q
from elasticsearch_dsl import Document, Text, Keyword, Integer, Response, Boolean, Date
import json
from apikey import API_KEY

my_index = "products"

ES_URL = "https://my-elasticsearch-project-fc4715.es.us-central1.gcp.elastic.cloud"

def get_connection():

    # Create underlying client
    client = Elasticsearch(
        ES_URL,
        api_key=API_KEY,
    )

    # Register this client with elasticsearch-dsl
    connections.add_connection("default", client)

    return client

    # Now all `elasticsearch_dsl` objects will use this connection.

# You can supply queries as:
# * Python dicts
# * JSON strings
# * elasticsearch-dsl DSL objects (optional)
#
# Here are all three ways.

## **A. Python dict query**

def search_error_messages():
    client = get_connection()
    s = Search(index=my_index).query({
        "match": {
            "message": "error"
        }
    })

    response = s.execute()
    return response


## **B. Using JSON string query**

def execute_json_query(_my_index):
    get_connection()
    json_query = """
    {
      "match": {
        "message": "error"
      }
    }
    """

    s = Search(index=_my_index).query(json.loads(json_query))
    response = s.execute()
    return response

## **C. Using DSL query syntax (optional)**

def search_error_messages_dsl():
    q = Q("range", timestamp={"gte": "now-1d"})
    s = Search(index=my_index).query(q)
    response = s.execute()
    return response

# ✅ 4. Pretty-printing responses

# Elasticsearch responses behave like dictionaries but also allow object-style access.

### ✔ Pretty print as JSON:

def pretty_print_as_json(response):
    if isinstance(response, ObjectApiResponse):
        response = response.body
        print(json.dumps(response, indent=2))
    if not isinstance(response, dict):
        print(json.dumps(response.to_dict(), indent=2))
    else:
        print(json.dumps(response, indent=2))

### ✔ Iterate through hits:

def iterate_through_hits(response):
    for hit in response:
        print(json.dumps(hit.to_dict(), indent=2))

    ### ✔ Print total hits and timing:
    
    print(f"Total hits: {response.hits.total.value}")
    print(f"Took: {response.took} ms")

# ✅ 5. Full Working Example (everything together)

def full_example() -> Response:
    # ES_URL = "https://your-endpoint.elastic.cloud"
    # API_KEY = "YOUR_API_KEY"
    client = Elasticsearch(
        ES_URL,
        api_key=API_KEY,
    )
    connections.add_connection("default", client)

    # ----- Run Query -----
    query = {
        "query": {
            "range": {
                "in_stock": {
                    "gt": 49
                }
            }
        }
    }
    # s = Search(index="logs-*").update_from_dict(query)
    s = Search(index=my_index).update_from_dict(query)
    response = s.execute()

    return response

    # ----- Pretty Print Full Response -----
    # print("\n=== RAW RESPONSE ===")
    # print(json.dumps(response.to_dict(), indent=2))
    #
    # # ----- Pretty Print Each Document -----
    # print("\n=== DOCUMENTS ===")
    # for hit in response:
    #     print(json.dumps(hit.to_dict(), indent=2))


class Product(Document):
    name = Text()
    price = Integer()
    in_stock = Integer()
    sold = Integer()
    tags = Keyword(multi=True)
    description = Text()
    is_active = Boolean()
    created = Date(format="yyyy/MM/dd")

    class Index:
        name = "products"


def get_client():
    client = Elasticsearch(
        ES_URL,
        api_key=API_KEY,
    )
    return client


def another_example():
    # Create underlying client
    client = get_client()

    Product.init(using=client)

    p = Product(
        meta={'id': 'product-1'},
        name="Hand Sanitizer",
        price=7,
        in_stock=50,
        sold=59,
        tags=[],
        description="Ideal for keeping hands clean.",
        is_active=False,
        created="2001/01/02"
    )
    p.save(using=client)


def pretty_print_response(response):
    print(f"{type(response)=}")
    # ----- Pretty Print Full Response -----
    print("\n=== RAW RESPONSE ===")
    print(json.dumps(response.to_dict(), indent=2))

    # ----- Pretty Print Each Document -----
    print("\n=== DOCUMENTS ===")
    for hit in response:
        print(json.dumps(hit.to_dict(), indent=2))


def get_field_caps(_my_index:str) -> ObjectApiResponse:  # -> ObjectApiResponse:
    client = get_client()
    field_caps_resp = client.field_caps(index=_my_index, fields="*")
    return field_caps_resp

def main():
    func_num = 1
    match func_num:
        case 1:
            response = full_example()
            print("full example response:")
            pretty_print_response(response)
        case 2:
            field_caps_resp = get_field_caps(my_index)
            print(f"{type(field_caps_resp)=}")
            pretty_print_as_json(field_caps_resp)
        case 3:
            search_error_messages()
        case 4:
            print(execute_json_query(my_index))
        case _:
            print("Invalid function number")


if __name__ == "__main__":
    main()


"""
# ❗️ Notes about Serverless

# Serverless does **not** support some legacy features (like types or custom analyzers), but `elasticsearch-dsl` works fine for:
#
# * search queries
# * aggregations
# * parsing results
# * pagination
# * request building
#
# Everything above is fully compatible.


# If you want, I can provide examples for:
#
# ✅ Aggregations
# ✅ Index creation / document insertion
# ✅ Async queries
# ✅ Creating models with `elasticsearch-dsl` `Document` classes
"""

