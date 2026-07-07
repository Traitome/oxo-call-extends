---
name: pywdl
category: programming
description: PyWDL is a Python implementation of a WDL parser and language bindings.
tags: [pywdl, programming, wdl, workflow]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/pywdl"
---

## Concepts

- **Tool Overview**: pywdl parses WDL workflows.
- **Core Function**: WDL parsing.
- **Algorithm**: Uses parser combinators.
- **Input Format**: Accepts WDL files.
- **Output**: Produces workflow objects.
- **Use Case**: Workflow development.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex workflows require memory.
- **WDL Version**: Must be supported.
- **Syntax Errors**: Must be fixed.
- **Runtime**: Parsing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pywdl --help`
**Explanation:** Shows available options and usage instructions.

### Parse workflow
**Args:** `pywdl parse -i workflow.wdl -o parsed.json`
**Explanation:** Parses WDL workflow.

### With parameters
**Args:** `pywdl parse -i workflow.wdl -p params.yaml -o parsed.json`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pywdl -v parse -i workflow.wdl -o parsed.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pywdl -t 4 parse -i workflow.wdl -o parsed.json`
**Explanation:** Uses 4 threads for parallel processing.

### Validate workflow
**Args:** `pywdl validate -i workflow.wdl`
**Explanation:** Validates WDL syntax.

### Generate report
**Args:** `pywdl parse -i workflow.wdl -o parsed.json --report report.html`
**Explanation:** Generates HTML report.