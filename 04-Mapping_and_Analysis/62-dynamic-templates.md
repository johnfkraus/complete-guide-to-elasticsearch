# Dynamic templates

elasticsearch-slides-udemy/04-Mapping_and_Analysis/62-Dynamic_templates.pdf

JSON Data Types

JSON supports six primary data types: string, number, boolean, null, object, and array  Strings are sequences of Unicode characters enclosed in double quotes and can include backslash-escaped characters such as \\, \", \/, \n, \r, \t, and \u followed by four hexadecimal digits  Numbers are represented in base 10 using decimal notation, with no support for octal or hexadecimal formats, and must not be NaN or Infinity  Boolean values are strictly true or false and are not enclosed in quotes  The null value represents an absence of a value and is written as null without quotes  Objects are unordered collections of key-value pairs enclosed in curly braces, where keys must be strings in double quotes and values can be any valid JSON type  Arrays are ordered sequences of values enclosed in square brackets, where elements can be of any valid JSON type and are separated by commas  These types can be nested arbitrarily to form complex data structures 


## Map whole numbers to `integer` instead of `long`
```
PUT /dynamic_template_test
{
  "mappings": {
    "dynamic_templates": [
      {
        "integers": {
          "match_mapping_type": "long",
          "mapping": {
            "type": "integer"
          }
        }
      }
    ]
  }
}
```

## Test the dynamic template
```
POST /dynamic_template_test/_doc
{
  "in_stock": 123
}
```

## Retrieve mapping (and dynamic template)
```
GET /dynamic_template_test/_mapping
```

## Modify default mapping for strings (set `ignore_above` to 512)
```
PUT /test_index
{
  "mappings": {
    "dynamic_templates": [
      {
        "strings": {
          "match_mapping_type": "string",
          "mapping": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 512
              }
            }
          }
        }
      }
    ]
  }
}
```

## Using `match` and `unmatch`
```
PUT /test_index
{
  "mappings": {
    "dynamic_templates": [
      {
        "strings_only_text": {
          "match_mapping_type": "string",
          "match": "text_*",
          "unmatch": "*_keyword",
          "mapping": {
            "type": "text"
          }
        }
      },
      {
        "strings_only_keyword": {
          "match_mapping_type": "string",
          "match": "*_keyword",
          "mapping": {
            "type": "keyword"
          }
        }
      }
    ]
  }
}

POST /test_index/_doc
{
  "text_product_description": "A description.",
  "text_product_id_keyword": "ABC-123"
}
```

## Setting `match_pattern` to `regex`
```
PUT /test_index
{
  "mappings": {
    "dynamic_templates": [
      {
        "names": {
          "match_mapping_type": "string",
          "match": "^[a-zA-Z]+_name$",
          "match_pattern": "regex",
          "mapping": {
            "type": "text"
          }
        }
      }
    ]
  }
}

POST /test_index/_doc
{
  "first_name": "John",
  "middle_name": "Edward",
  "last_name": "Doe"
}
```

## Using `path_match`
```
PUT /test_index
{
  "mappings": {
    "dynamic_templates": [
      {
        "copy_to_full_name": {
          "match_mapping_type": "string",
          "path_match": "employer.name.*",
          "mapping": {
            "type": "text",
            "copy_to": "full_name"
          }
        }
      }
    ]
  }
}

POST /test_index/_doc
{
  "employer": {
    "name": {
      "first_name": "John",
      "middle_name": "Edward",
      "last_name": "Doe"
    }
  }
}
```

## Using placeholders
```
PUT /test_index
{
  "mappings": {
    "dynamic_templates": [
      {
        "no_doc_values": {
          "match_mapping_type": "*",
          "mapping": {
            "type": "{dynamic_type}",
            "index": false
          }
        }
      }
    ]
  }
}

POST /test_index/_doc
{
  "name": "John Doe",
  "age": 26
}
```