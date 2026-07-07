---
name: validictory
category: utility
description: validictory - JSON schema validation library.
tags: [validictory, json-validation, python, utility]
author: oxo-call-community
source_url: "https://github.com/jamesturk/validictory"
---

## Concepts

- **Tool Overview**: validictory - A JSON schema validation library.
- **Core Function**: Validates JSON data against schemas.
- **Input**: JSON data, schema.
- **Output**: Validation result.
- **Installation**: Install via pip
- **Use Case**: JSON validation, API development, bioinformatics.

## Pitfalls

- **Schema Complexity**: Requires well-defined schemas.
- **Performance**: May be slow for complex schemas.

## Examples

### Validate JSON
**Args:** `python -c "import validictory; validictory.validate({'name': 'test'}, {'type': 'object', 'properties': {'name': {'type': 'string'}}})"`
**Explanation:** Validate JSON against schema.

### With options
**Args:** `python -c "import validictory; validictory.validate(data, schema, required=True)"`
**Explanation:** Require all properties.
