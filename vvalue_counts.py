# Thanks for providing the OpenSearch information! I see you're using OpenSearch 2.19.2, which is a fork of Elasticsearch. I'll update the code to work specifically with your OpenSearch instance.

# Here's code that will connect to your OpenSearch instance and retrieve value counts for a specified field:

from opensearchpy import OpenSearch
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_field_value_counts(
        host="opensearch_172-31-155-75_2.19.2_omc_bonsai_us-east-1_common_opensearch-8466_manager-data-ingest-2617_",
        port=443,
        index_name="your_index",
        field_name="your_field",
        size=100,
        username=None,
        password=None,
        use_ssl=True
):
    """
    Get value counts for a specific field in an OpenSearch index.

    Args:
        host: OpenSearch host
        port: OpenSearch port (usually 443 for Bonsai)
        index_name: The name of the index to query
        field_name: The field to count values for
        size: Number of unique values to return
        username: Username for authentication
        password: Password for authentication
        use_ssl: Whether to use SSL/TLS

    Returns:
        Dictionary of field values and their counts
    """
    try:
        # Connection settings
        client_config = {
            "hosts": [{"host": host, "port": port}],
            "use_ssl": use_ssl,
            "verify_certs": True,
            "connection_class": None,  # Will be automatically determined
        }

        # Add authentication if provided
        if username and password:
            client_config["http_auth"] = (username, password)

        # Connect to OpenSearch
        client = OpenSearch(**client_config)

        # Check connection
        info = client.info()
        logger.info(f"Connected to OpenSearch: {info['version']['number']}")

        # Build and execute the query
        query = {
            "size": 0,  # Don't return documents
            "aggs": {
                "value_counts": {
                    "terms": {
                        "field": field_name,
                        "size": size,
                        "order": {"_count": "desc"}
                    }
                }
            }
        }

        # Execute search
        response = client.search(index=index_name, body=query)

        # Extract and return results
        buckets = response["aggregations"]["value_counts"]["buckets"]
        results = {bucket["key"]: bucket["doc_count"] for bucket in buckets}

        return results

    except Exception as e:
        logger.error(f"Error querying OpenSearch: {str(e)}")
        raise


# Example usage
if __name__ == "__main__":
    # Configure these parameters for your OpenSearch instance
    # For Bonsai, the host would typically be your cluster URL
    # and the port would be 443
    os_host = "your-bonsai-host.region.bonsaisearch.net"
    os_port = 443
    os_username = "your_username"  # Set to None if not using auth
    os_password = "your_password"  # Set to None if not using auth
    index = "your_index_name"
    field = "your_field_name"

    # Get the value counts
    value_counts = get_field_value_counts(
        host=os_host,
        port=os_port,
        index_name=index,
        field_name=field,
        username=os_username,
        password=os_password
    )

    # Print results
    if value_counts:
        print(f"Value counts for field '{field}' in index '{index}':")
        for value, count in sorted(value_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{value}: {count}")
    else:
        print("Failed to retrieve value counts")


