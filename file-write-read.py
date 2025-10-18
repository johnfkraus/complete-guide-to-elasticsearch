Here's how to work with JSON files in Python:

## Writing JSON to a File

```python

import json

# Your data (dictionary, list, etc.)
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking", "photography"]
}

# Write to file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 makes it readable
```

## Reading JSON from a File

```python
import json

# Read from file into a dictionary
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)  # {'name': 'Alice', 'age': 30, ...}
print(data['name'])  # Alice
```

## Key Points

- **`json.dump()`** - writes Python object to a file
- **`json.load()`** - reads JSON file into Python object (usually a dict or list)
- **`indent=4`** - optional parameter that formats the JSON nicely with indentation
- **`with open()`** - automatically closes the file when done

If you're working with JSON strings instead of files, you can use:
- `json.dumps()` - converts Python object to JSON string
- `json.loads()` - converts JSON string to Python object