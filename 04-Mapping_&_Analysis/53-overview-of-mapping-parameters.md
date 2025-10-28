## Lesson 53 - Overview of mapping parameters

Slides are [here](./../elasticsearch-slides-udemy/Mapping_and_Analysis/53-Overview_of_mapping_parameters.pdf)

### format

[Date format documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-date-format.html)

- To customize date field formats using Java DateFormatter syntax.

Instructor recommends using the default format.  ISO-8601

### properties

### coerce (enabled by default)

### Introduction to doc_values

- Set doc_values to false to save disk space.
  - Only disable if you won't use aggregations, sorting or scripting.
  - cannot be changed without re-indexing the documents into a new index.

### norms

Normalization factors used for relevance scoring.  Disabling saves disk space.  If you don't need relevance scoring.

- Filtering and aggregation don't involve relevance scoring.

### index

Set to false to prevent indexing of a parameter.

### null_value

By default, in ES, NULL values cannot be indexed or searched.  They are ignored.

Use this parameter to replace null values with another values.

Only works for explicit null values.  Not [].

Replacement values must be the same data type as the field.

Does not affect values stored in _source.

### copy_to

Used to copy multiple fields into a group field.

Specify the name of the target field as the value.

E.g., first_name and last_name -> full_name.

The target value is not part of _source (unless you were to specify a full_name field as part of the mapping).





