
GET /ds160/_search
{
    "_source": {
        "includes": ["submission_date"]
    },
    "query": {
        "range": {
            "submission_date": {
                "gte": "2025-06-08"
            }
        } 
    }
}


POST my_index/_doc
{
  "timestamp_field": "2023-01-01T12:34:56.789Z",
  "some_other_field": "test data"
}
Z indicates

curl -k -u elastic:giraffe -H "Content-Type:application/x-ndjson" -XPOST https://localhost:9200/ds120/_bulk --data-binary "@ds160_1_bulk.ndjson"



/Users/blauerbock/workspaces/complete-guide-to-elasticsearch/ds160-1.json


GET /datetime/_search
{
    "_source": {
        "includes": ["submission_date"]
    },
    "query": {
        "range": {
            "submission_date": {
                "gt": "2023-12-31T00:00:00Z"
            }
        } 
    }
}


No, records with datetimes occurring during 2024-12-31 but before 2025-01-01 are not included when using a gt '2024-12-31' filter. 
When you provide a date string with no time part, such as '2024-12-31', Elasticsearch interprets it as the very beginning of that day: 2024-12-31T00:00:00.000 in UTC. The gt (greater than) operator is strictly exclusive, meaning it only matches records with timestamps after this precise moment. 
A filter with gt '2024-12-31' will match records starting from 2024-12-31T00:00:00.001 (or the first nanosecond after the start of the day, depending on the exact precision).
Any record with a timestamp on 2024-12-31 (from 00:00:00.000 to 23:59:59.999...) is considered less than or equal to the beginning of the next day, and thus will not be returned by the gt filter. 
How to Include the Entire Day of 2024-12-31
To include all records from the entire day of December 31, 2024, you have a few options:
Use gte with the start of the day and lt with the start of the next day: This is generally the most precise method.
json
"range": {
  "your_date_field": {
    "gte": "2024-12-31",
    "lt": "2025-01-01"
  }
}
Use lte with date math: You can explicitly define the upper bound using date math to ensure you include the last millisecond of the day.
json
"range": {
  "your_date_field": {
    "gte": "2024-12-31",
    "lte": "2024-12-31||+1d-1ms"
  }
}
Use lte with a full timestamp: Specify the very end of the day.
json
"range": {
  "your_date_field": {
    "gte": "2024-12-31T00:00:00",
    "lte": "2024-12-31T23:59:59.999"
  }
}
 
For more details on how date range queries and date math work, you can refer to the Elasticsearch Range query reference. 


In Elasticsearch, finding documents that match an exact date requires using a range query that specifies both a start and end time for that single date, or a match query if the field mapping and query string are configured correctly to handle only the date portion. 
Using a Range Query (Recommended)
Since dates in Elasticsearch are internally stored as a long representing milliseconds since the epoch and often include time information, it is safer and more precise to use a range query. This approach ensures you capture all data within the 24-hour period of the specified day, regardless of the time or timezone settings. 
json
GET your_index/_search
{
  "query": {
    "range": {
      "your_date_field": {
        "gte": "2023-01-01",
        "lte": "2023-01-01"
      }
    }
  }
}
You can also use date math for this, by rounding down the gte value to the start of the day and implicitly rounding the lte value to the end of the day. 
json
GET your_index/_search
{
  "query": {
    "range": {
      "your_date_field": {
        "gte": "2023-01-01||/d",
        "lte": "2023-01-01||/d",
        "time_zone": "America/New_York"
      }
    }
  }
}
Using a Match Query
You can use a match query if your date field is consistently formatted and you are searching for a date string that aligns with that format. 
If your field is mapped with a specific format (e.g., "yyyy-MM-dd"), the match query will work as expected:
json
GET your_index/_search
{
  "query": {
    "match": {
      "your_date_field": "2023-01-01"
    }
  }
}
Caution: If your date field includes a time component (e.g., "2023-01-01T12:00:00Z"), a simple match query for "2023-01-01" might not return all documents for that day, or any if the default format does not match the query string's format. For this reason, the range query is generally considered a better practice for date equality. 
For more details on working with date formats and queries, refer to the official Elasticsearch documentation on Range queries. 