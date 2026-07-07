---
name: pedagree
category: programming
description: pedagree provides Pythonic pedigree manipulation.
tags: [pedagree, programming, pedigree, python]
author: oxo-call-community
source_url: "https://github.com/brentp/pedagree"
---

## Concepts

- **Tool Overview**: pedagree manipulates pedigree files.
- **Core Function**: Provides pedigree analysis and manipulation.
- **Algorithm**: Uses Python-based pedigree processing.
- **Input Format**: Accepts PED format files.
- **Output**: Produces modified pedigree files.
- **Use Case**: Family analysis, pedigree management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large pedigrees require memory.
- **Pedigree Format**: Requires proper PED format.
- **Family Structure**: Complex families may need care.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pedagree --help`
**Explanation:** Shows available options and usage instructions.

### Parse pedigree
**Args:** `pedagree -i family.ped -o parsed.json`
**Explanation:** Parses pedigree file.

### Validate pedigree
**Args:** `pedagree validate -i family.ped -o validation.txt`
**Explanation:** Validates pedigree structure.

### Verbose mode
**Args:** `pedagree -v -i family.ped -o parsed.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pedagree -t 4 -i family.ped -o parsed.json`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pedagree -i family.ped -o parsed.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pedagree -i family.ped -o parsed.json --report report.html`
**Explanation:** Generates HTML report.