# Complete Guide to Elasticsearch - Udemy

This repository contains all of the queries used within the [Complete Guide to Elasticsearch course](https://l.codingexplained.com/r/elasticsearch-course?src=github).


https://dedicated-laurel-1hfqmn7b.apps.bonsaisearch.net/app/dev_tools#/console

https://www.geeksforgeeks.org/cloud-computing/elasticsearch-concept-of-painless/

https://alexmarquardt.com/category/painless/

https://search-guard.com/blog/elasticsearch-painless-alerting-primer/

## Lecture 9 -- Hosting Elasticsearch and Kibana on Elastic Cloud

https://l.codingexplained.com/r/elastic-cloud-trial?src=es-getting-started

Authenticating API requests, use header:
Authorization: ApiKey ZXZWN2g1b0….



### Lecture 10 - Installing ES and Kibana on MacOS and Linux

Download the archives.  

ES contains Java.  Kibana contains Node.js.

#### Elasticsearch

Extract the archive.  Rename the directory to get rid of version number.  cd into the directory.

From the elasticsearch directory:

bin/elasticsearch

ES starts and is set up with a superuser 'elastic' and password, found in the stdout from startup.

Save the password.

Resetting elastic user's password:

bin/elasticsearch-reset-password -u elastic

TLS certs are also created.  Data is encrypted during transfer.

Enrollment token is also created for Kibana.  Valid for 30 minutes.

Generate a new Kibana enrollment token:

bin/elasticsearch-create-enrollment-token --scope kibana

#### Kibana

If MacOS, disable gatekeeper for the Kibana directory.  

From the parent directory of the kibana directory:

elastic-stack xattr -d -r com.apple.quarantine kibana

cd kibana

bin/kibana

Browse to the URL + token output in the terminal.

Paste the enrollment token into the web input box.

In the Welcome to Elastic login page, login as elastic user with password from terminal.

### Set up ES and Kibana on Windows

Unzip.  Circumvent "filepath too long" error with 7zip or other program.

Run:

bin\elasticsearch.bat

bin\kibana.bat

Open the url+token from the kibana start terminal.

Paste enrollment token.

(Or click button configure manually)

Login to kibana as elastic user.

### Lecture 12 - Understanding the basic architecture

Cluster-a group of one or more Elasticsearch nodes instances that are connected together.  A cluster is a collection of nodes that work together to store data and provide search and indexing capabilities. It provides horizontal scalability, allowing you to add or remove nodes easily to accommodate changing requirements.

node-an instance of Elasticsearch. Nodes can be deployed on separate machines or run on a single machine for development purposes. 

Index-a collection of documents.  Each index is divided into multiple primary and replica shards.
An index is a collection of documents sharing similar characteristics. It serves as the primary unit for organizing and managing data within Elasticsearch. Each document within an index is uniquely identified by a document ID. Indices are analogous to tables in a relational database.


### Shard

In Elasticsearch, a shard is a basic unit of data storage and search. Elasticsearch uses a distributed architecture to handle large amounts of data and provide scalable and efficient search capabilities. Sharding is the process of breaking down the index into smaller, more manageable pieces called shards. Understanding shards is crucial for designing and optimizing Elasticsearch clusters.

Elastic is able to distribute your data across nodes by subdividing an index into shards. Each index in Elasticsearch is a grouping of one or more physical shards, where each shard is a self-contained Lucene index containing a subset of the documents in the index. By distributing the documents in an index across multiple shards, and distributing those shards across multiple nodes, Elasticsearch increases indexing and query capacity.

Types of Shards
Primary Shards: Primary shards contain the main data and handle all write operations. The number of primary shards is set when creating an index and cannot be changed later.

Replica Shards: Replica shards are copies of the primary shards, serving as failover mechanisms. They improve system resilience and enable parallel search and retrieval operations.

### Lecture 13 - Inspect the cluster

In the console:

GET /_cluster/health

```json
{
  "cluster_name": "opensearch_2.19.2_omc_bonsai_us-east-1_common_opensearch-8466",
  "status": "green",
  "timed_out": false,
  "number_of_nodes": 3,
  "number_of_data_nodes": 3,
  "discovered_master": true,
  "discovered_cluster_manager": true,
  "active_primary_shards": 1,
  "active_shards": 2,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 0,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks": 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 100
}
```

Config file:

$ES_HOME/config/elasticsearch.yml

### CAT API-Compact and Aligned Text

GET /_cat/nodes?v

GET /_cat/indices?v

GET /_cat/indices?v&expand_wildcards=all

GET /[API]/[command]

## Lesson 14 - Sending Queries with Curl

Kibana automatically sets Content-Type and authentication headers.

Download curl from here: https://curl.se/download.html

Conda or cygwin may already have curl.





```bash
curl https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net
{
  "name" : "opensearch_172-31-155-75_2.19.2_omc_bonsai_us-east-1_common_opensearch-8466_manager-data-ingest-2617_",
  "cluster_name" : "opensearch_2.19.2_omc_bonsai_us-east-1_common_opensearch-8466",
  "cluster_uuid" : "lyr-L1ImSoyHujHXhaNpvA",
  "version" : {
    "distribution" : "opensearch",
    "number" : "2.19.2",
    "build_type" : "tar",
    "build_hash" : "e0ba5eebfa3f060fc76e4e2b5b61193a19470d4f",
    "build_date" : "2025-04-29T20:06:33.471315233Z",
    "build_snapshot" : false,
    "lucene_version" : "9.12.1",
    "minimum_wire_compatibility_version" : "7.10.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "The OpenSearch Project: https://opensearch.org/"
}

(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock/workspaces/complete-guide-to-elasticsearch [master]
%

 blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock/workspaces/complete-guide-to-elasticsearch [master]
 
% curl https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   704  100   704    0     0  10524      0 --:--:-- --:--:-- --:--:-- 10666
{
  "name": "opensearch_172-31-155-75_2.19.2_omc_bonsai_us-east-1_common_opensearch-8466_manager-data-ingest-2617_",
  "cluster_name": "opensearch_2.19.2_omc_bonsai_us-east-1_common_opensearch-8466",
  "cluster_uuid": "lyr-L1ImSoyHujHXhaNpvA",
  "version": {
    "distribution": "opensearch",
    "number": "2.19.2",
    "build_type": "tar",
    "build_hash": "e0ba5eebfa3f060fc76e4e2b5b61193a19470d4f",
    "build_date": "2025-04-29T20:06:33.471315233Z",
    "build_snapshot": false,
    "lucene_version": "9.12.1",
    "minimum_wire_compatibility_version": "7.10.0",
    "minimum_index_compatibility_version": "7.0.0"
  },
  "tagline": "The OpenSearch Project: https://opensearch.org/"
}
(base) blauerbock@Johns-MacBook-Pro-2.local /Users/blauerbock/workspaces/complete-guide-to-elasticsearch [master]
```

curl $ESHOST | jq .


### Sending requests to Elasticsearch with curl

You can run queries with cURL or other HTTP clients as well, such as Postman.

You should already have cURL installed with the exception being for some old versions of Windows

Anyway, let’s type out the simplest possible cURL command by simply specifying the endpoint of our Elasticsearch cluster.

If you are using Elastic Cloud, be sure to use the Elasticsearch endpoint from the deployment page and not the Kibana endpoint.

The GET HTTP verb is implicitly assumed if none is specific, but we can also specify it with the -X argument as follows.

Let’s send the request.

curl http://localhost:9200

With explicit HTTP verb:

curl -X GET http://localhost:9200

curl https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net

As you can see, we get an empty response back from Elasticsearch.

That’s because from version 8 and onwards, we need to use the TLS endpoint instead of plaintext, so let’s change that.

curl -X GET https://localhost:9200

Now we get a certificate error.

The reason is that Elasticsearch generates a self signed certificate by default, which is not trusted by HTTP clients for security reasons.

Note that this only applies to local setups, so if you created a cloud deployment, you will not face this issue.

The easiest way to get around that is to simply use cURL’s --insecure flag as follows.

curl --unsecure -X GET https://localhost:9200

This flag instructs cURL to ignore the certificate error, and if you look closely, you can see that we now get a different error.

This was an easy solution and it works just fine for local development, but the more correct approach is to provide cURL with the CA certificate with the "cacert" argument.

From the elasticsearch root directory (or use absolute path):

curl --cacert config/certs/http_cs.crt -X GET https://localhost:9200

The CA certificate is located within the config/certs directory as you can see.

If your working directory is the Elasticsearch root directory, you can specify the relative path just like I did.

Otherwise you can use an absolute path as well.

Running the command, you can see that the certificate error went away with this approach as well.

Alright, so far so good.

We still get an error, because we need to authenticate with our Elasticsearch cluster.

This also applies if you have created a cloud deployment instead of a local one.

Doing so is simple with cURL’s -u argument.

The value should simply be the username for your deployment.

For local deployments, the password is the one that was generated the first time Elasticsearch started up.

curl --cacert config/certs/http_cs.crt -u elastic -X GET https://localhost:9200

When running the command, cURL will prompt us to enter our password.

Perfect, that worked as intended.

For the endpoint we defined, Elasticsearch returns basic information about our cluster.

As an alternative, you can supply your password for the -u argument as well.

Simply add a colon after the username followed by the password.

With this approach, cURL will not prompt us to enter the password when running the command.

curl --cacert config/certs/http_cs.crt -u elastic:password -X GET https://localhost:9200

The password will, however, be exposed within your terminal, so this is not ideal from a security perspective - especially when communicating with a production cluster.

Anyway, that was the most basic request we could send.

Oftentimes we need to send some data along with our request, such as when searching for data.

Let’s update our request path to use Elasticsearch’s Search API for a products index.

This index doesn’t exist yet, but we will create it later.

The Search API requires us to send a JSON object specifying constraints for our query.

We will get back to searching for data later, so I will just use the simplest possible query which matches all documents.

To specify the data, we can use cURL’s -d argument.

curl --cacert config/certs/http_cs.crt -u elastic:password -X GET https://localhost:9200/products/_search -d '{ "query": { "match_all": {} } }'

curl --cacert config/certs/http_cs.crt -u elastic:password -X GET "${ESHOST}/products/_search" -d '{ "query": { "match_all": {} } }'

curl --cacert config/certs/http_cs.crt -u elastic:password -X GET "${ESHOST}/products/_search" -d '{ "query": { "match_all": {} } }'

curl -X GET -H "Content-Type:application/json" "${ESHOST}/products/_search" -d '{ "query": { "match_all": {} } }'

Don’t worry about the JSON object, but here is a formatted version of it anyway.

Notice how I enclosed it within single quotes to avoid having to escape all of the double quotes with backslashes.

**That approach doesn’t work on Windows because it doesn’t like single quotes.

Instead, you need to wrap the argument within double quotes and then escape each double quote within the JSON object.**

You can see an example on your screen, and you can copy it from within the GitHub repository to save some typing.

curl [...] -d "{ \"query\": { \"match_all\": {} }  }"

curl "${ESHOST}" | jq .

Anyway, let’s hit Enter and see what we get.

We get an error back saying that the provided Content-Type header is not supported.

When adding data with the -d argument, cURL just assumes that we are mimicking a form submission.

Because Elasticsearch expects to receive JSON, we need to explicitly define which kind of data we are sending.

That’s done by specifying a Content-Type header with a value of application/json.

That can be done with the -H argument as follows.
```json
curl --cacert config/certs/http_cs.crt -u elastic:password -X GET -H "Content-Type:application/json"  https://localhost:9200/products/_search -d '{ "query": { "match_all": {} } }'

curl -X GET "${ESHOST}/products/_search" -H "Content-Type:application/json" -d '{ "query": { "match_all": {} } }'
```


That should fix the error, so let’s send the request again.
```json

curl -X GET "${ESHOST}/products/_search" -H "Content-Type:application/json" -d '{ "query": { "match_all": {} } }'

{"error":{"root_cause":[{"type":"index_not_found_exception","reason":"no such index [products]","index":"products","resource.id":"products","resource.type":"index_or_alias","index_uuid":"_na_"}],"type":"index_not_found_exception","reason":"no such index [products]","index":"products","resource.id":"products","resource.type":"index_or_alias","index_uuid":"_na_"},"status":404}%
```

Indeed the header error went away.

We now get a different error stating that the products index doesn’t exist.

That’s to be expected since we haven’t created it yet, so everything is good.

So that’s how to send requests to Elasticsearch with cURL.

If you encounter any problems, try checking the order of the arguments, as cURL is quite sensitive in that regard.

If you prefer to use other HTTP clients, it should be fairly easy to replicate this in Postman or something like that.

Alright, I’ll see you in the next lecture.

## Lesson 17 - Add more nodes to the cluster


## Lesson 20-Creating and Deleting Indexes

DELETE /pages

PUT /products

DELETE /pages

PUT /products
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
}

{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "products"
}

## Lesson 21 - Indexing documents

POST /products/_doc
{
  "name": "Coffee Maker",
  "price": 64,
  "in_stock": 10
}
{
  "_index": "products",
  "_id": "Aodt2ZkBa2Q2SW-AFCPx",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 3,
    "successful": 3,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}

POST /


## Lesson 23 - Updating documents

PUT /products/_doc/100
{
  "name": "Toaster",
  "price": 39,
  "in_stock": 4
}
GET /products/_doc/100

POST /products/_update/100
{
  "doc": {
    "in_stock": 3
  }
}
GET /products/_doc/100
POST /products/_update/100
{
  "doc": {
    "tags": ["electronics"]    
  }
}


## Lesson 24 - Scripted updates

Managing Documents/scripted-updates.md

GET /products/_doc/100

POST /products/_update/100
{
  "script": {
    "source": "ctx._source.in_stock--"
  }
}
GET /products/_doc/100

GET /products/_doc/100

POST /products/_update/100
{
  "script": {
    "source": "ctx._source.in_stock=10"
  }
}
GET /products/_doc/100
POST /products/_update/100
{
  "script": {
    "source": "ctx._source.in_stock -= params.quantity",
    "params": {
      "quantity": 4
    }
  }
}



## Lesson 31 - Understanding document versioning

PUT /products/_doc/123?version=521&version_type=external
{
  "name": "Kuerig Machine",
  "price": 49,
  "in_stock": 10
}

## Lesson 33 - Update by Query

[Slides](/Users/blauerbock/workspaces/complete-guide-to-elasticsearch/elasticsearch-slides-udemy/Managing_Documents/33-Update_by_query.pdf)

We need to use a script:

POST /products/_update_by_query
{
  "conflicts": "proceed",
  "script": {
    "source": "ctx._source.in_stock--"
  },
  "query": {
    "match_all": {}
  }
}

"bonsai_exception",
"reason": "Update by query is for business+ only"

Steps in Update by Query:

1. POST /products/_update_by_query
2. Take snapshot of the index.
- Snapshot prevents overwriting changes made after the snapshot was taken.
- Query can take some time.
- Each document's primary term and sequence number is used.  
  - A doc is only updated if the values match from the snapshot.
  - "Optimistic concurrency control"
  - # of conflicts is returned under the "version_conflicts" key.
  - Avoid aborting the query using "conflicts": "proceed".
    - Version conflicts will be counted but query will not be aborted.
3. Search query is sent to each of the shards to find all matching documents. 
4. When a match is found, a bulk request is sent to update those documents.  Uses scroll api internally.  Each pair of search and bulk requests are sent sequentially (one at a time).
5. Should there be an error in the search query or bulk update, ES will try up to 10 times.  If the affected query is still not successful, the whole query is aborted.  The failures will then be specified in the results under the failures key.  The query is aborted and NOT rolled back.  Docs that were updated will remain updated even if the request failed.  The query is not run within a transaction, as with RDBMS.  If the query can partially succeed or fail, it will return information you can use to deal with it.



## Lesson 35 - Batch processing

The create action will fail if the document already exists.

The index action will add the document if it doesn't already exist; if the document exists, it will be replaced.

## Lesson 36 - Importing data with CURL

curl https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net | jq .

curl -H "Content-Type: application/x-ndjson" -XPOST http://localhost:9200/products/_bulk --data-binary "@products-bulk.json"

curl https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net | jq .

curl -H "Content-Type: application/x-ndjson" -XPOST https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/products/_bulk --data-binary "@products-bulk.json"

GET /products/_search
{
  "query": {
    "match_all": {}
  }
}


curl -X GET -H "Content-Type:application/json" "${ESHOST}/products/_search" -d '{ "query": { "match_all": {} } }'

## Lesson 42 - Intro to mapping

/Users/blauerbock/workspaces/complete-guide-to-elasticsearch/elasticsearch-slides-udemy/04-Mapping_and_Analysis/42-Introduction_to_mapping.pdf

GET /_mapping

GET products/_mapping

GET /reviews/_mapping

GET /reviews/_mapping/field/content

## Lesson 43 - Overview of data types

Slides:
/Users/blauerbock/workspaces/complete-guide-to-elasticsearch/elasticsearch-slides-udemy/04-Mapping_and_Analysis/43-Overview_of_data_types.pdf

Link:
https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/field-data-types

 


nested data type-similar to object but maintains object relationship.
- Allows querying object independently.

keyword-used for exact matching of values.
- used for filtering, aggregating and sorting.

For full-text searches, use the text data type instead.

An inverted index is created for each text field.  Each text field has a dedicated inverted index.

An inverted index is a sorted mapping between terms and the documents that contain them.

Other data types use different data types.

Numeric, dates, and geospatial fields are stored as BKD trees.  Dates are stored as long values internally.

A BKD tree, or Balanced K-Dimensional tree, is an I/O-efficient dynamic data structure designed for indexing large-scale numeric and multi-dimensional data, particularly in systems like Elasticsearch and Apache Lucene.


## Lesson 48 - Retrieving mappings

GET products/_mapping

GET /reviews/_mapping

GET /reviews/_mapping/field/content

## Lesson 58 - Introduction to Dynamic Mapping

No pdf?  No code?

Does not require you to define explicit field mappings before indexing documents.

The first time ES encounters a field, it will automatically create a field mapping for it using "sensible" defaults.

Example:

```curl
POST /my-index/_doc
{
  "tags": ["computer","electronics"],
  "in_stock": 4,
  "created_at": "2020/01/01 00:00:00"  
}
```
We specified the date as a string because there is no date datatype in JSON.

ES uses "date detection".  

ES always chooses the long data type, since it can't know how large the numbers will be.

ES adds two mappings for "tags", since it doesn't know how you intend to use the tags field.  
- text mapping for full text searches
- keyword for exact matches, sorting and aggregations.
  - "ignore_above": 256, because it almost never makes sense to use such long values for sorting and aggregations.  Reduces unnecessary duplicative use of disk space.

Rules for dynamic mapping:

https://www.udemy.com/course/elasticsearch-complete-guide/learn/lecture/18848584#overview

Elasticsearch Dynamic Mapping

Elasticsearch dynamically maps new fields in incoming documents by default, using predefined rules to infer data types based on the field's content  When a new field is detected and contains a non-null value, Elasticsearch adds it to the mapping using these rules: null values do not create a field, boolean values map to the boolean type, numeric values (float or long) are mapped based on detection, and strings are classified as date, numeric, or text/keyword depending on pattern matching  Specifically, strings that match date patterns are mapped as date fields, those that pass numeric detection are mapped as float or long, and others are mapped as text with a .keyword sub-field 

Dynamic mapping can be controlled using the `dynamic` parameter in index mappings. Setting it to `true` enables dynamic field creation, while `runtime` creates fields that are loaded from `_source` at query time without being indexed  Setting `dynamic` to `false` ignores new fields, and `strict` rejects documents containing unknown fields  The default behavior is `true`, enabling dynamic mapping 

Date detection is enabled by default and checks string fields against patterns defined in `dynamic_date_formats`, which by default includes "strict_date_optional_time" and "yyyy/MM/dd HH:mm:ss Z||yyyy/MM/dd Z"  

Date detection can be disabled by setting `date_detection` to `false`, causing new string fields to be mapped as text instead of date.  

Custom date formats can be defined by modifying `dynamic_date_formats` to support specific patterns, either as an array (where the first matching pattern determines the mapping) or as a string with `||` to allow multiple formats 

Numeric detection is disabled by default but can be enabled via `numeric_detection` to automatically map string representations of numbers to float or long types  This is useful when applications or languages output numbers as strings.

For greater control, dynamic templates can be defined using the `dynamic_templates` parameter in index mappings. These templates allow custom rules based on field name patterns (`match`, `path_match`), data types (`match_mapping_type`), or other conditions, enabling specific mappings for new fields  Templates are processed in order, with the first matching template taking precedence  For example, a template can map all string fields with a "user_" prefix as keyword fields  Dynamic templates can also be used to map fields as runtime fields, which are not indexed but loaded from `_source` during queries 

While dynamic mapping is convenient, explicit mapping is recommended for production environments to ensure precise control over data indexing and to avoid potential type conflicts 

Every field in ES may contain zero or more values.

Elasticsearch dynamically maps fields based on the data type detected in incoming documents. For arrays, the mapping is determined by the first non-null value within the array; if the array contains null values, no field is added until a concrete value is encountered  When a new field is detected, Elasticsearch applies default mapping rules: strings that pass date or numeric detection are mapped as date or numeric types (float or long), while other strings are mapped as text with a .keyword sub-field  Numeric values are mapped as long or double depending on their precision, boolean values as boolean, and objects as object type 

Dynamic mapping behavior can be controlled using the `dynamic` parameter in index mappings, which can be set to `true` (default, automatically adds new fields), `false` (ignores new fields), or `strict` (rejects documents with unknown fields)  To customize the mapping of dynamically added fields, dynamic templates can be defined. These templates are processed in order, and the first matching template applies  For example, a dynamic template can be created to map all string fields as keyword fields instead of the default text type 

For arrays, the dynamic mapping rule depends on the first non-null value, and this behavior is consistent across all data types  If a field contains an array of mixed types, the mapping is determined by the first non-null value in the array. Elasticsearch does not support dynamic mapping for all data types, and fields like geo_point or geo_shape must be explicitly mapped  Additionally, dynamic mapping can be disabled at the index level or within nested objects to prevent unintended field creation

## Lesson 63 -- Mapping Recommendations

elasticsearch-slides-udemy/04-Mapping_and_Analysis/63-Mapping_recommendations.pdf

Use explicit mapping, at least for production clusters.
- Optimized mappings save disk space.
- Set dynamic mapping to "strict", not false.
  - You are always in control.
  - Setting dynamic mapping to false lets you add fields for which there are no mappings. These fields are ignored in terms of indexing. 
  - Strict dynamic mapping avoids surprises and unexpected results.

Don't always map strings as both text and keyword.
- Typically only one is needed.
- Each mapping requires disk space.
  - Add a text mapping if you want to do full-text searches.
  - Add a keyword mapping if you want to do aggregations, sorting or filtering.

Disable coercion.
- Coercion forgives you for not doing the right thing.  Try to do the right thing instead.
- Use the correct data types whenever possible.

Use appropriate numeric data types.
- For whole numbers, the integer data type might be enough.

Mapping parameters.

Set doc_values to false for a field if you don't need sorting, aggregations, and scripting.

Set norms to false if you won't use a field for relevance scoring.

Set index to false if you don't need to filter on values.
- You can still do aggregations, such as for time-series data.

The foregoing parameters make sense for over one million documents.

## Lesson 64 - Stemming and Stop Words

Stop words are filtered out during the analysis process. They provide little or no value for relevance scoring.

There is not much need to remove stop words due to improvements in the relevance algorithm.


## Lesson 65 -- Analyzers and Search Queries

The same analyzer is used for indexing and searching.

## Lesson 66 - Analyzers and search queries

https://www.elastic.co/docs/reference/text-analysis/analyzer-reference

standard_analyzer

- Splits by word.  Splits text at word boundaries and removes punctuation.
  - Done by standard tokenizer.
- Lowercases letters with the lowercase token filter.
- Contains the stop token filter (disabled by default).

simple analyzer

- Split the input text whenever it encounters anything other than a letter.
- Lowercases with the lowercase tokenizer, not a token filter (unusual, a token hack to avoid passing through the input twice).

whitespace analyzer

- Splits text into tokens by whitespace.
- Does NOT lowercase letters.

keyword analyzer

- No-op analyzer that leaves the input intact, outputting it as a single term.
- Used for keyword fields by default.
  - Used for exact matching.

pattern analyzer

- Lets you define a regular expression to match token separators.
- The regex should match whatever should split the text into tokens.
- The default pattern matches all non-word characters (\W+).
- Lowercases letters by default, but this can be disabled.

There are also language-specific analyzers.



## Lesson 67 - Creating custom analyzers

https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis.html

## Lesson 68 -- Adding analyzers to existing indexes




## Lesson 71 - Intro to Searching

GET /products/_search
{
  "query": {
    "match_all": {}
  }
}


## Lesson 72 - Intro to term-level queries

Term queries are used to search structured data for exact values (filtering).
- Term-level queries are not analyzed.
  - the search value is used exactly as for inverted index lookups.
  - can be used with data types such as keyword, numbers, dates.
  - Don't use term level queries for the text data type.
    - results will be unpredictable.
    - there is no explicit error message or failure, but you dont' get the results you should.
- Never use term level queries on text data type field.

## Lesson 73 - Searching for terms

Term level queries are case-sensitive.

### Booleans

GET /products/_search
{
  "query": {
    "term": {
      "is_active": true
    }
  }
}

### Numbers

GET /products/_search
{
  "query": {
    "term": {
      "in_stock": 1
    }
  }
}


### Dates

GET /products/_search
{
  "query": {
    "term": {
      "created": "2007/10/14"
    }
  }
}

### Timestamps

GET /products/_search
{
  "query": {
    "term": {
      "created": "2007/10/14 12:34:56"
    }
  }
}

### Explicit syntax 

is required if we want to specify parameters for our query.
```
GET /products/_search
{
  "query": {
    "term": {
      "tags.keyword": {
        "value": "Vegetable"
      }
    }
  }
}

GET /products/_search
{
  "query": {
    "term": {
      "tags.keyword": {
        "value": "vegetable",
        "case_insensitive": true
      }
    }
  }
}

# note "terms" vs "term"
GET /products/_search
{
  "query": {
    "terms": {
      "tags.keyword": ["Soup", "Meat"]
    }
  }
}
```
SQL equivalent: tags.keyword CONTAINS "Soup" AND/OR "Meat"

## Lesson 75 - Range searches

GET /products/_search
{
  "query": {
    "range": {
      "in_stock": {
        "gte": 1,
        "lte": 5
      }
    }
  }
}

SQL equivalent: 

WHERE in_stock >= 1 AND in_stock <= 5

### Exclude boundaries

GET /products/_search
{
  "query": {
    "range": {
      "in_stock": {
        "gt": 1,
        "lt": 5
      }
    }
  }
}

### Dates without time
GET /products/_search
{
  "query": {
    "range": {
      "created": {
        "gte": "2007/01/01",
        "lte": "2020/01/31"
      }
    }
  }
}

### Specify date format
GET /products/_search
{
  "query": {
    "range": {
      "created": {
        "format": "dd/MM/yyyy",
        "gte": "01/01/2007",
        "lte": "31/01/2020"
      }
    }
  }
}


### Specify a UTC offset

## Lesson 76 - Prefixes, wildcards & regular expressions

### Searching for a prefix

Prefix must occur at the beginning of the term.

```
GET /products/_search
{
  "query": {
    "prefix": {
      "name.keyword": {
        "value": "Past"
      }
    }
  }
}
```
If we search tags instead of name, we get more hits.

GET /products/_search
{
  "query": {
    "prefix": {
      "tags.keyword": {
        "value": "Past"
      }
    }
  }
}


### Wildcards

#### Single character wildcard (`?`)

```
GET /products/_search
{
  "query": {
    "wildcard": {
      "tags.keyword": {
        "value": "Past?"
      }
    }
  }
}
```

#### Zero or more characters wildcard (`*`)

```
GET /products/_search
{
  "query": {
    "wildcard": {
      "tags.keyword": {
        "value": "Bee*"
      }
    }
  }
}

GET /products/_search
{
  "query": {
    "regexp": {
      "tags.keyword": {
        "value": "Bee(f|r)+"
      }
    }
  }
}
```

### Regexp

```
GET /products/_search
{
  "query": {
    "regexp": {
      "tags.keyword": {
        "value": "Bee(f|r)+"
      }
    }
  }
}
```
ES uses Apache Lucene regex, in which anchor symbols are not supported (^,$).


### Case insensitive searches

All of the above queries can be made case insensitive by adding the `case_insensitive` parameter, e.g.:

```
GET /products/_search
{
  "query": {
    "prefix": {
      "name.keyword": {
        "value": "Past",
        "case_insensitive": true
      }
    }
  }
}
```
## Lesson 77 - Querying by field existence

### Basic usage

```
GET /products/_search
{
  "query": {
    "exists": {
      "field": "tags.keyword"
    }
  }
}
```

**SQL:** `SELECT * FROM products WHERE tags IS NOT NULL`

### Inverting the query

There is no dedicated query for this, so we do it with the `bool` query.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "exists": {
            "field": "tags.keyword"
          }
        }
      ]
    }
  }
}
```

**SQL:** `SELECT * FROM products WHERE tags IS NULL`






## Lesson 79 - The match query

### Basic usage

```
GET /products/_search
{
  "query": {
    "match": {
      "name": "pasta"
    }
  }
}
```

Full text queries are analyzed (and therefore case insensitive), so the below query yields the same results.

```
GET /products/_search
{
  "query": {
    "match": {
      "name": "PASTA"
    }
  }
}
```

### Searching for multiple terms

```
GET /products/_search
{
  "query": {
    "match": {
      "name": "PASTA CHICKEN"
    }
  }
}
```

### Specifying the operator

Defaults to `or`. The below makes both terms required.

```
GET /products/_search
{
  "query": {
    "match": {
      "name": {
        "query": "pasta chicken",
        "operator": "and"
      }
    }
  }
}
```

## Lesson 81 - Searching multiple fields

https://www.elastic.co/docs/api/

### Basic usage

```
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "vegetable",
      "fields": ["name", "tags"]
    }
  }
}
```

### Per-field relevance boosting

```
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "vegetable",
      "fields": ["name^2", "tags"]
    }
  }
}
```

### Specifying a tie breaker

```
GET /products/_search
{
  "query": {
    "multi_match": {
      "query": "vegetable broth",
      "fields": ["name", "description"],
      "tie_breaker": 0.3
    }
  }
}
```
## Lesson 83 - Leaf and compound queries

- Leaf queries search for values and are independent queries.
  - term and match queries
- Compound queries wrap other queries to produce a result.
- 



## Lesson 84 - Querying with boolean logic

https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query

### `must`

Query clauses added within the `must` occurrence type are required to match.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ]
    }
  }
}
```

**SQL:** `SELECT * FROM products  WHERE tags IN ("Alcohol")`

### `must_not`

Query clauses added within the `must_not` occurrence type are required to _not_ match.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ],
      "must_not": [
        {
          "term": {
            "tags.keyword": "Wine"
          }
        }
      ]
    }
  }
}
```

**SQL:** `SELECT * FROM products WHERE tags IN ("Alcohol") AND tags NOT IN ("Wine")`

### `should`

Matching query clauses within the `should` occurrence type boost a matching document's relevance score.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ],
      "must_not": [
        {
          "term": {
            "tags.keyword": "Wine"
          }
        }
      ],
      "should": [
        {
          "term": {
            "tags.keyword": "Beer"
          }
        }
      ]
    }
  }
}
```

An example with a few more adding more `should` query clauses:

```
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ],
      "must_not": [
        {
          "term": {
            "tags.keyword": "Wine"
          }
        }
      ],
      "should": [
        {
          "term": {
            "tags.keyword": "Beer"
          }
        },
        {
          "match": {
            "name": "beer"
          }
        },
        {
          "match": {
            "description": "beer"
          }
        }
      ]
    }
  }
}
```

### `minimum_should_match`

Since only `should` query clauses are specified, at least one of them must match.

```
GET /products/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "term": {
            "tags.keyword": "Beer"
          }
        },
        {
          "match": {
            "name": "beer"
          }
        }
      ]
    }
  }
}
```

Since a `must` query clause is specified, all of the `should` query clauses are optional. 
They are therefore only used to boost the relevance scores of matching documents.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ], 
      "should": [
        {
          "term": {
            "tags.keyword": "Beer"
          }
        },
        {
          "match": {
            "name": "beer"
          }
        }
      ]
    }
  }
}
```

This behavior can be configured with the `minimum_should_match` parameter as follows.

```
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ], 
      "should": [
        {
          "term": {
            "tags.keyword": "Beer"
          }
        },
        {
          "match": {
            "name": "beer"
          }
        }
      ],
      "minimum_should_match": 1
    }
  }
}
```

### `filter`

Query clauses defined within the `filter` occurrence type must match. 
This is similar to the `must` occurrence type. The difference is that 
`filter` query clauses do not affect relevance scores and may be cached.

```
GET /products/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "tags.keyword": "Alcohol"
          }
        }
      ]
    }
  }
}
```

### Examples

### Example #1

**SQL:** `SELECT * FROM products WHERE (tags IN ("Beer") OR name LIKE '%Beer%') AND in_stock <= 100`

**Variation #1**

```
GET /products/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "in_stock": {
              "lte": 100
            }
          }
        }
      ],
      "must": [
        {
          "bool": {
            "should": [
              { "term": { "tags.keyword": "Beer" } },
              { "match": { "name": "Beer" } }
            ]
          }
        }
      ]
    }
  }
}
```

**Variation #2**

```
GET /products/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "in_stock": {
              "lte": 100
            }
          }
        }
      ],
      "should": [
        { "term": { "tags.keyword": "Beer" } },
        { "match": { "name": "Beer" } }
      ],
      "minimum_should_match": 1
    }
  }
}

```

### Example #2

**SQL:** `SELECT * FROM products WHERE tags IN ("Beer") AND (name LIKE '%Beer%' OR description LIKE '%Beer%') AND in_stock <= 100`

**Variation #1**

```
GET /products/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "in_stock": {
              "lte": 100
            }
          }
        },
        {
          "term": {
            "tags.keyword": "Beer"
          }
        }
      ],
      "should": [
        { "match": { "name": "Beer" } },
        { "match": { "description": "Beer" } }
      ],
      "minimum_should_match": 1
    }
  }
}
```

**Variation #2**

```
GET /products/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "in_stock": {
              "lte": 100
            }
          }
        },
        {
          "term": {
            "tags.keyword": "Beer"
          }
        }
      ],
      "must": [
        {
          "multi_match": {
            "query": "Beer",
            "fields": ["name", "description"]
          }
        }
      ]
    }
  }
}
```
## Lesson 85 - Query execution contexts

- Filter execution context
  - No relevance scores are calculated.
  - Match or no match.
  - ES doesn't spend resources on calculating relevance scores.




## Lesson 86 - Boosting query

### Matching juice products

```
GET /products/_search
{
  "size": 20,
  "query": {
    "match": {
      "name": "juice"
    }
  }
}
```

### Match juice products, but deprioritize apple juice

```
GET /products/_search
{
  "size": 20,
  "query": {
    "boosting": {
      "positive": {
        "match": {
          "name": "juice"
        }
      },
      "negative": {
        "match": {
          "name": "apple"
        }
      },
      "negative_boost": 0.5
    }
  }
}
```

### Without filtering (deprioritize everything apples)

```
GET /products/_search
{
  "query": {
    "boosting": {
      "positive": {
        "match_all": {}
      },
      "negative": {
        "match": {
          "name": "apple"
        }
      },
      "negative_boost": 0.5
    }
  }
}
```

### More examples

#### "I like pasta"

Boost the relevance scores for pasta products.

```
GET /recipes/_search
{
  "query": {
    "bool": {
      "must": [
        { "match_all": {} }
      ], 
      "should": [
        {
          "term": {
            "ingredients.name.keyword": "Pasta"
          }
        }
      ]
    }
  }
}
```

#### "I don't like bacon"

Reduce the relevance scores for bacon products.

```
GET /recipes/_search
{
  "query": {
    "boosting": {
      "positive": {
        "match_all": {}
      },
      "negative": {
        "term": {
          "ingredients.name.keyword": "Bacon"
        }
      },
      "negative_boost": 0.5
    }
  }
}
```

#### Pasta products, preferably without bacon

```
GET /recipes/_search
{
  "query": {
    "boosting": {
      "positive": {
        "term": {
          "ingredients.name.keyword": "Pasta"
        }
      },
      "negative": {
        "term": {
          "ingredients.name.keyword": "Bacon"
        }
      },
      "negative_boost": 0.5
    }
  }
}
```

#### "I like pasta, but not bacon"

```
GET /recipes/_search
{
  "query": {
    "boosting": {
      "positive": {
        "bool": {
          "must": [
            { "match_all": {} }
          ],
          "should": [
            {
              "term": {
                "ingredients.name.keyword": "Pasta"
              }
            }
          ]
        }
      },
      "negative": {
        "term": {
          "ingredients.name.keyword": "Bacon"
        }
      },
      "negative_boost": 0.5
    }
  }
}
```


## Lesson 87 - Disjunction max (`dis_max`)

### Basic usage

```
GET /products/_search
{
  "query": {
    "dis_max": {
      "queries": [
        { "match": { "name": "vegetable" } },
        { "match": { "tags": "vegetable" } }
      ]
    }
  }
}
```

### Specifying a tie breaker

```
GET /products/_search
{
  "query": {
    "dis_max": {
      "queries": [
        { "match": { "name": "vegetable" } },
        { "match": { "tags": "vegetable" } }
      ],
      "tie_breaker": 0.3
    }
  }
}
```


GET /recipes/_search
{
  "query": {
    "match_all": {}
  }
}

## Lesson 88 - Querying nested objects

### Importing test data

Follow [these instructions](/Managing%20Documents/importing-data-with-curl.md) and specify `recipes-bulk.json` as the file name.

recipes-bulk.json

curl -H "Content-Type: application/x-ndjson" -XPOST https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/recipes/_bulk --data-binary "@recipes-bulk.json"

curl -X GET -H "Content-Type:application/json" "${ESHOST}/products/_search" -d '{ "query": { "match_all": {} } }'

### Searching arrays of objects (the wrong way)

```
GET /recipes/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "ingredients.name": "parmesan"
          }
        },
        {
          "range": {
            "ingredients.amount": {
              "gte": 100
            }
          }
        }
      ]
    }
  }
}
```

### Create the correct mapping (using the `nested` data type)

```
DELETE /recipes
```

```
PUT /recipes
{
  "mappings": {
    "properties": {
      "title": { "type": "text" },
      "description": { "type": "text" },
      "preparation_time_minutes": { "type": "integer" },
      "steps": { "type": "text" },
      "created": { "type": "date" },
      "ratings": { "type": "float" },
      "servings": {
        "properties": {
          "min": { "type": "integer" },
          "max": { "type": "integer" }
        }
      },
      "ingredients": {
        "type": "nested",
        "properties": {
          "name": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword"
              }
            }
          },
          "amount": { "type": "integer" },
          "unit": { "type": "keyword" }
        }
      }
    }
  }
}
```

[Import the test data again](#importing-test-data).

### Using the `nested` query

```
GET /recipes/_search
{
  "query": {
    "nested": {
      "path": "ingredients",
      "query": {
        "bool": {
          "must": [
            {
              "match": {
                "ingredients.name": "parmesan"
              }
            },
            {
              "range": {
                "ingredients.amount": {
                  "gte": 100
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

The usage for your Bonsai cluster has exceeded the limits for its Sandbox plan.  Shard Overage: 12 / 10

PUT /products
{
  "products": {
    "aliases": {},
    "mappings": {
      "properties": {
        "created": {
          "type": "date",
          "format": "yyyy/MM/dd HH:mm:ss||yyyy/MM/dd||epoch_millis",
          "print_format": "yyyy/MM/dd HH:mm:ss"
        },
        "description": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "doc": {
          "properties": {
            "in_stock": {
              "type": "long"
            }
          }
        },
        "in_stock": {
          "type": "long"
        },
        "is_active": {
          "type": "boolean"
        },
        "name": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "price": {
          "type": "long"
        },
        "sold": {
          "type": "long"
        },
        "tags": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        }
      }
    },
    "settings": {
      "index": {
        "replication": {
          "type": "DOCUMENT"
        },
        "number_of_shards": "1",
        "auto_expand_replicas": null,
        "provided_name": "products",
        "priority": "0",
        "number_of_replicas": "1"
      }
    }
  }
}

PUT /_all/_settings?preserve_existing=true'{
"index.number_of_shards" : "1",
"index.number_of_replicas" : "1"
}

From lesson 20:

PUT /products
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  }
}

curl -XGET https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/products/_count

https://elasticsearch-cheatsheet.jolicode.com/




## Lesson 108 - Pagination

total_pages = ceil(total_hits/page_size)

from = (page_size * (page_number - 1))

Limited to 10,000 results.

Queries are stateless.


# Section 8 - Aggregations

Elasticsearch organizes aggregations into three categories:

https://www.elastic.co/docs/reference/aggregations/

Metric aggregations that calculate metrics, such as a sum or average, from field values.

Bucket aggregations that group documents into buckets, also called bins, based on field values, ranges, or other criteria.

Pipeline aggregations that take input from other aggregations instead of documents or fields.

## Lesson 111 - Intro to aggregations



