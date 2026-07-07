---
name: rcsbsearch
category: programming
description: RCSBSearch provides access to the RCSB Protein Data Bank Search API for structural biology queries.
tags: [rcsbsearch, programming, protein-structure, rcsb-pdb]
author: oxo-call-community
source_url: "https://rcsbsearch.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: rcsbsearch searches structures.
- **Core Function**: PDB search API.
- **Algorithm**: Uses query methods.
- **Input Format**: Accepts search queries.
- **Output**: Produces structure data.
- **Use Case**: Structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large queries require memory.
- **API Limits**: Affects search.
- **Parameters**: Must be configured.
- **Runtime**: Search may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rcsbsearch --help`
**Explanation:** Shows available options and usage instructions.

### Search structures
**Args:** `rcsbsearch search -q "lysozyme" -o results.json`
**Explanation:** Searches PDB database.

### With parameters
**Args:** `rcsbsearch search -q "lysozyme" -p params.yaml -o results.json`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rcsbsearch -v search -q "lysozyme" -o results.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rcsbsearch -t 4 search -q "lysozyme" -o results.json`
**Explanation:** Uses 4 threads for parallel processing.

### With filters
**Args:** `rcsbsearch search -q "lysozyme" -f "resolution<2.0" -o results.json`
**Explanation:** Uses search filters.

### Generate report
**Args:** `rcsbsearch search -q "lysozyme" -o results.json --report report.html`
**Explanation:** Generates HTML report.