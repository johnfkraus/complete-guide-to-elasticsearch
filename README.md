This repository contains all of the queries used within the [Complete Guide to Elasticsearch course](https://l.codingexplained.com/r/elasticsearch-course?src=github).

## Lecture 13

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

CAT API-Compact and Aligned Text

GET /_cat/nodes?v


GET /_cat/indices?v


GET /_cat/indices?v&expand_wildcards=all


GET /[API]/[command]

## Lesson 14

