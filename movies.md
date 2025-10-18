## Movies

https://medium.com/@animeshblog/elasticsearch-the-beginners-cookbook-1cf30f98218


Fire a PUT request from Postman http://localhost:9200/movies or you can use the cURL command curl -X PUT “http://localhost:9200/movies/”

Create index:

PUT /movies
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}

Insert record:

POST /movies/_doc 
{
  "name":"Justice League", 
  "genre":"Action",
  "summary":"Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy",
  "yearofrelease":201, 
  "metascore":45, 
  "votes":275122, 
  "rating":6.5
}

Update record; change the JSON and repeat above action:

POST /movies/_doc 
{
  "name":"Justice League", 
  "genre":"Action",
  "summary":"Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face an even greater enemy",
  "yearofrelease":201, 
  "metascore":45, 
  "votes":275122, 
  "rating":7.5
}

DELETE /movies/_doc/1

Movie data for bulk ingest:

```json
{ "index" : { } }
{  "name":"Thor Ragnarok",  "genre":"Action", "summary":"Thor is imprisoned on the planet Sakaar, and must race  against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela", "yearofrelease":2017, "metascore":74, "votes":374270, "rating":7.9 }
{ "index" : {} }
{  "name":"Infinity War",  "genre":"Sci-Fi",   "summary":"The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe", "yearofrelease":2018, "metascore":68, "votes":450856, "rating":8.6 }
{ "index" : {} }
{  "name":"Christopher Robin",  "genre":"Comedy", "summary":"A working-class family man, Christopher Robin, encounters his childhood friend Winnie-the-Pooh, who helps him to  rediscover the joys of life", "yearofrelease":2018, "metascore":60, "votes":9648, "rating":7.9}

```
Make sure there is a newline at the end of the bulk json file.


curl -H "Content-Type: application/x-ndjson" -XPOST https://bcec8e0e4c:0122727a305d76ffd8ce@dedicated-laurel-1hfqmn7b.us-east-1.bonsaisearch.net/movies/_bulk --data-binary "@movies-bulk.json"

