# Run Elasticsearch and Kibana on local machine using Docker

How to use podman

Run podman help in the terminal for a list of commands to interact with Podman. For example, try the 'Create' button within the Containers tab of Podman Desktop and view your containers with podman:

$ podman ps

docker network create elastic-network

docker network ls

NETWORK ID     NAME                          DRIVER    SCOPE
8cc6e85f0918   bridge                        bridge    local
961bfa0fa5ca   elastic-network               bridge    local
1cce1b923fb9   elastic-start-local_default   bridge    local
5e791a850cc4   host                          host      local
0a500897ed94   none                          null      local

 # docker run -d --name elasticsearch \
podman run -d --name elasticsearch-arm64 \
  --net elastic-network \
  -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=true" \
  -e "xpack.security.authc.api_key.enabled=true" \
  -e "xpack.security.enrollment.enabled=true" \
  docker.elastic.co/elasticsearch/elasticsearch:9.2.1-arm64


ERROR: [xpack.security.enrollment.enabled] must be set to `true` to create an enrollment token, with exit code 78

podman exec -it elasticsearch-arm64 ./bin/elasticsearch-setup-passwords auto

12/28/2025

% podman exec -it elasticsearch-arm64 ./bin/elasticsearch-setup-passwords auto
******************************************************************************
Note: The 'elasticsearch-setup-passwords' tool has been deprecated. This       command will be removed in a future release.
******************************************************************************

Initiating the setup of passwords for reserved users elastic,apm_system,kibana,kibana_system,logstash_system,beats_system,remote_monitoring_user.
The passwords will be randomly generated and printed to the console.
Please confirm that you would like to continue [y/N]y


Changed password for user apm_system
PASSWORD apm_system = JmhqFZ5k1Nu829LOMrFB

Changed password for user kibana_system
PASSWORD kibana_system = 6BzsjGvfvtYTHtWvodKY

Changed password for user kibana
PASSWORD kibana = 6BzsjGvfvtYTHtWvodKY

Changed password for user logstash_system
PASSWORD logstash_system = 13wnvIMPr0W8b3qcxgXq

Changed password for user beats_system
PASSWORD beats_system = 4Aa4vZkB0KhMsSzvU8Jv

Changed password for user remote_monitoring_user
PASSWORD remote_monitoring_user = 0juIQXgtNm3MakPokWZE

Changed password for user elastic
PASSWORD elastic = KpOpmDm7mkiLocPScRMd


% docker exec -it elasticsearch ./bin/elasticsearch-setup-passwords auto
******************************************************************************
Note: The 'elasticsearch-setup-passwords' tool has been deprecated. This       command will be removed in a future release.
******************************************************************************

Initiating the setup of passwords for reserved users elastic,apm_system,kibana,kibana_system,logstash_system,beats_system,remote_monitoring_user.

The passwords will be randomly generated and printed to the console.

Please confirm that you would like to continue [y/N]y
...


Insert the Kibana system_user password in the following command and run it:

podman run -d --name kibana-arm64 \
  --net elastic-network \
  -p 5601:5601 \
  -e "ELASTICSEARCH_HOSTS=http://elasticsearch:9200" \
  -e "ELASTICSEARCH_USERNAME=kibana_system" \
  -e "ELASTICSEARCH_PASSWORD=6BzsjGvfvtYTHtWvodKY" \
  docker.elastic.co/kibana/kibana:9.2.1-arm64

Browse to localhost:5601

Log in with the "elastic" user and password from above.

Changed password to "giraffe"

Load some bulk data:

Did not work:

curl -k -u elastic:wCb3HLmy9lXZyfBajxIc -H "Content-Type:application/x-ndjson" -XPOST https://localhost:9200/products/_bulk --data-binary "@ds160_100_bulk.ndjson"

curl: (35) LibreSSL/3.3.6: error:1404B42E:SSL routines:ST_CONNECT:tlsv1 alert protocol version

curl -k -u elastic:giraffe -H "Content-Type:application/x-ndjson" -XPOST https://localhost:9200/products/_bulk --data-binary "@ds160_100_bulk.ndjson"

curl -k -u elastic:giraffe -H "Content-Type:application/x-ndjson" -XGET https://localhost:9200/_cat/indices


cd /Users/blauerbock/workspaces/python-workout/recursive_json_parsing/data/visas

curl -k -u elastic:giraffe -H "Content-Type:application/x-ndjson" -XPOST https://localhost:9200/products/_bulk --data-binary "@ds160_100_bulk.ndjson"



Kibana

http://localhost:5601/app/dev_tools#/console/shell

In Kibana:

POST /_bulk
{"index": {"_index": "ds160", "_id": "DS20250001-14936F7B"}}
{"application_id": "DS20250001-14936F7B", "form_type": "DS-160", "submission_date": "2025-06-08", "personal_information": {"surname": "SUR384", "given_names": "Given3547", "sex": "M", "marital_status": "DIVORCED", "date_of_birth": "1993-04-06", "city_of_birth": "New Delhi", "country_of_birth": "India", "nationality": "India", "other_nationalities": []}, "passport_information": {"passport_number": "P23718431", "issuing_country": "India", "issue_date": "2019-04-08", "expiration_date": "2029-04-08", "lost_stolen_passport": false}, "travel_information": {"purpose_of_trip": "BUSINESS", "visa_class": "J1", "intended_date_of_arrival": "2026-06-03", "intended_length_of_stay_days": 90, "address_in_us": {"street": "4334 Main St", "city": "Austin", "state": "PA", "zip_code": "80284"}, "person_paying_for_trip": "SELF"}, "us_contact": {"contact_type": "ORGANIZATION", "name": "ACME Corp", "relationship": "BUSINESS ASSOCIATE", "address": {"street": "850 Contact Way", "city": "New York", "state": "VA", "zip_code": "35203"}, "phone": "+1-921-171-1750"}, "family_information": {"father": {"surname": "FAM94", "given_names": "Father30", "country_of_birth": "Brazil"}, "mother": {"surname": "FAM20", "given_names": "Mother30", "country_of_birth": "India"}, "spouse": null}, "address_and_phone": {"home_address": {"street": "465 Home Rd", "city": "New Delhi", "postal_code": "93320", "country": "India"}, "primary_phone": "+47-266-479-6820", "email": "user4432@example.com"}, "work_education": {"primary_occupation": "Researcher", "present_employer": {"name": "EduWorld", "address": {"street": "960 Corporate Blvd", "city": "London", "postal_code": "89840", "country": "China"}, "job_title": "Technician", "start_date": "2022-11-23", "monthly_income": "2338 EUR"}, "employment_history": [{"employer_name": "TechServe Ltd", "address": {"street": "605 Industrial Ave", "city": "New York", "postal_code": "13905", "country": "United States"}, "job_title": "Student", "start_date": "2008-11-24", "end_date": "2013-11-23"}], "education": [{"degree": "PhD", "institution": "University 70", "graduation_year": 2020}]}, "security_background": {"medical_conditions": false, "drug_use": false, "criminal_history": false, "immigration_violations": false, "terrorist_activities": false, "export_control_violations": false, "additional_info": {"has_prior_denial": false, "prior_denial_reasons": null}}, "previous_us_travel": {"visited_before": true, "visits": [{"arrival_date": "2024-01-18", "length_of_stay_days": 28, "visa_type": "TN", "was_immigration_issue": false}, {"arrival_date": "2022-10-09", "length_of_stay_days": 3, "visa_type": "B1/B2", "was_immigration_issue": false}]}, "testing_nested": {"level1": {"level2": {"level3": {"documents": [{"doc_type": "invitation", "present": false, "meta": {"issued_by": "Innovate Labs", "issued_date": "2025-02-18"}}, {"doc_type": "sponsor_letter", "present": true, "meta": {"sponsor_id": "S6155"}}], "flags": {"flagA": true, "flagB": false}}, "array_test": [{"k": 0, "v": "val_0_83"}, {"k": 1, "v": "val_1_59"}, {"k": 2, "v": "val_2_19"}, {"k": 3, "v": "val_3_34"}]}, "misc": {"notes": null}}}}
{"index": {"_index": "ds160", "_id": 

etc...

GET ds160/_search
{
"query": {
    "match_all": {}
}
}
