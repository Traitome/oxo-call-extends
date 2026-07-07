---
name: pyquery
category: programming
description: PyQuery is a jQuery-like library for Python that allows DOM manipulation and HTML parsing.
tags: [pyquery, programming, html, parsing]
author: oxo-call-community
source_url: "https://github.com/gawel/pyquery"
---

## Concepts

- **Tool Overview**: pyquery parses HTML.
- **Core Function**: DOM manipulation.
- **Algorithm**: Uses CSS selectors.
- **Input Format**: Accepts HTML/XML.
- **Output**: Produces parsed data.
- **Use Case**: Web scraping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large documents require memory.
- **HTML Structure**: Must be well-formed.
- **Selector Syntax**: Must be correct.
- **Runtime**: Parsing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyquery --help`
**Explanation:** Shows available options and usage instructions.

### Parse HTML
**Args:** `pyquery parse -i page.html -o data.json`
**Explanation:** Extracts data from HTML.

### With parameters
**Args:** `pyquery parse -i page.html -p params.yaml -o data.json`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyquery -v parse -i page.html -o data.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyquery -t 4 parse -i page.html -o data.json`
**Explanation:** Uses 4 threads for parallel processing.

### Extract table
**Args:** `pyquery extract -i page.html -s "table.data" -o table.csv`
**Explanation:** Extracts specific element.

### Generate report
**Args:** `pyquery parse -i page.html -o data.json --report report.html`
**Explanation:** Generates HTML report.