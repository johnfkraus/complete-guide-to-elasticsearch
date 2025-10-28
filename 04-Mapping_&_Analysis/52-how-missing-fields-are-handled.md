## Lesson 52 - How missing fields are handled

All fields in ES are optional.

You can leave out a field when indexing documents.

(Unlike RDBs, where you need to allow null values.)

Some integrity checks have to be done at the application level, such as checking for required fields.

Adding a field mapping does not make a field required.

Searches automatically handle missing fields.

