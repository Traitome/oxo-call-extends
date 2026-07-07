---
name: jq
category: utility
description: jq is a lightweight and flexible command-line JSON processor.
tags: [jq, utility, JSON, command-line, parsing]
author: oxo-call-community
source_url: "https://stedolan.github.io/jq/"
---

## Concepts

- **Tool Overview**: jq (v1.5) - A lightweight and flexible command-line JSON processor for parsing and manipulating JSON data.
- **JSON Processing**: Parses, filters, and transforms JSON data.
- **Command-line Tool**: Operates directly from the command line.
- **Pipeline Integration**: Integrates with Unix pipelines.
- **Expression Language**: Uses powerful filter expressions for data manipulation.
- **Data Extraction**: Extracts specific fields and values from JSON documents.

## Pitfalls

- **JSON Validity**: Requires valid JSON input.
- **Complex Queries**: Complex queries can be difficult to write.
- **Performance**: Very large JSON files can be slow to process.
- **Memory Usage**: Large JSON documents require significant memory.
- **Version Differences**: Syntax may vary between versions.
- **Encoding Issues**: Character encoding can affect parsing.

## Examples

### Extract specific field
**Args:** `jq '.name' data.json`
**Explanation:** Extracts the 'name' field from JSON data.

### Filter objects
**Args:** `jq '.items[] | select(.type == "protein")' data.json`
**Explanation:** Filters items where type equals "protein".

### Transform JSON
**Args:** `jq '{id: .accession, name: .description}' data.json`
**Explanation:** Transforms JSON structure to new format.

### Extract nested fields
**Args:** `jq '.results[].annotations[].term' data.json`
**Explanation:** Extracts nested annotation terms.

### Pretty print JSON
**Args:** `jq '.' data.json`
**Explanation:** Formats JSON output with indentation.

### Count items
**Args:** `jq '.items | length' data.json`
**Explanation:** Counts the number of items in an array.