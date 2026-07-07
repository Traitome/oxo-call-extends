---
name: ped_parser
category: formatting
description: ped_parser parses PED format pedigree files.
tags: [ped_parser, formatting, pedigree, parser]
author: oxo-call-community
source_url: "https://github.com/moonso/ped_parser"
---

## Concepts

- **Tool Overview**: ped_parser parses PED files.
- **Core Function**: Reads and processes pedigree data.
- **Algorithm**: Uses PED format parsing.
- **Input Format**: Accepts PED format files.
- **Output**: Produces parsed pedigree data.
- **Use Case**: Pedigree analysis, family data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large pedigrees require memory.
- **PED Format**: Requires proper PED format.
- **Family Structure**: Complex families may need care.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ped_parser --help`
**Explanation:** Shows available options and usage instructions.

### Parse PED file
**Args:** `ped_parser -i family.ped -o parsed.json`
**Explanation:** Parses PED file to JSON.

### Validate PED
**Args:** `ped_parser validate -i family.ped -o validation.txt`
**Explanation:** Validates PED file structure.

### Verbose mode
**Args:** `ped_parser -v -i family.ped -o parsed.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ped_parser -t 4 -i family.ped -o parsed.json`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `ped_parser -i family.ped -o parsed.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `ped_parser -i family.ped -o parsed.json --report report.html`
**Explanation:** Generates HTML report.