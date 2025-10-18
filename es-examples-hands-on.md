## ES Examples Hands-On Tutorial

https://coralogix.com/blog/42-elasticsearch-query-examples-hands-on-tutorial/


PUT /employees
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}

PUT employees/_mapping
{
  "properties": {
    "date_of_birth": {
      "type": "date",
      "format": "dd/MM/yyyy"
    }
  }
}

POST _bulk
{ "index" : { "_index" : "employees", "_id" : "1" } }
{"id":1,"name":"Huntlee Dargavel","email":"hdargavel0@japanpost.jp","gender":"male","ip_address":"58.11.89.193","date_of_birth":"11/09/1990","company":"Talane","position":"Research Associate","experience":7,"country":"China","phrase":"Multi-channelled coherent leverage","salary":180025}
{ "index" : { "_index" : "employees", "_id" : "2" } }
{"id":2,"name":"Othilia Cathel","email":"ocathel1@senate.gov","gender":"female","ip_address":"3.164.153.228","date_of_birth":"22/07/1987","company":"Edgepulse","position":"Structural Engineer","experience":11,"country":"China","phrase":"Grass-roots heuristic help-desk","salary":193530}
{ "index" : { "_index" : "employees", "_id" : "3" } }
{"id":3,"name":"Winston Waren","email":"wwaren2@4shared.com","gender":"male","ip_address":"202.37.210.94","date_of_birth":"10/11/1985","company":"Yozio","position":"Human Resources Manager","experience":12,"country":"China","phrase":"Versatile object-oriented emulation","salary":50616}
{ "index" : { "_index" : "employees", "_id" : "4" } }
{"id" : 4,"name" : "Alan Thomas","email" : "athomas2@example.com","gender" : "male","ip_address" : "200.47.210.95","date_of_birth" : "11/12/1985","company" : "Yamaha","position" : "Resources Manager","experience" : 12,"country" : "China","phrase" : "Emulation of roots heuristic coherent systems","salary" : 300000}

POST employees/_search
{
  "query": {
    "match": {
      "phrase": {
        "query" : "heuristic"
      }
    }
  }
}

POST employees/_search
{
  "query": {
    "match": {
      "phrase": {
        "query" : "heuristic roots help"
      }
    }
  }
}

POST employees/_search
{
  "query": {
    "match": {
      "phrase": {
        "query" : "heuristic roots help",
        "operator" : "AND"
      }
    }
  }
}

POST employees/_search
{
  "query": {
    "match": {
      "phrase": {
        "query" : "heuristic roots help",
        "minimum_should_match": 3
      }
    }
  }
}


POST employees/_search
{
  "query": {
    "multi_match": {
        "query" : "research help", "fields": ["position","phrase"]
    }
  }
}

GET employees/_search
{
  "query": {
    "match_phrase": {
      "phrase": {
        "query": "roots coherent",
        "slop": 1
      }
    }
  }
}
