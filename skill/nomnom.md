---
name: nomnom
category: formatting
description: NomNom converts genomic data tables into hierarchical YAML files for structured data representation.
tags: [nomnom, formatting, yaml, genomics]
author: oxo-call-community
source_url: "https://github.com/diegomics/NomNom"
---

## Concepts

- **Tool Overview**: NomNom transforms tabular genomic data into hierarchical YAML format.
- **Core Function**: Converts flat tables to structured YAML representation.
- **Algorithm**: Parses tabular data and organizes into nested YAML structure.
- **Input Format**: Accepts CSV, TSV, and other tabular formats.
- **Output**: Produces hierarchical YAML files.
- **Use Case**: Data organization, configuration management, and interoperability.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Structure**: Requires well-structured input data.
- **YAML Compatibility**: Output must be valid YAML.
- **Memory Usage**: Large tables require memory.
- **Dependency**: Requires proper YAML handling.
- **Documentation**: Limited documentation.

## Examples

### Display help
**Args:** `nomnom --help`
**Explanation:** Shows available options and usage instructions.

### Basic conversion
**Args:** `nomnom -i data.tsv -o output.yaml`
**Explanation:** Converts TSV to YAML format.

### CSV input
**Args:** `nomnom -i data.csv -o output.yaml --csv`
**Explanation:** Converts CSV to YAML format.

### Custom delimiter
**Args:** `nomnom -i data.txt -o output.yaml -d ";"`
**Explanation:** Uses custom delimiter.

### Nested output
**Args:** `nomnom -i data.tsv -o output.yaml -n`
**Explanation:** Creates nested YAML structure.

### Include header
**Args:** `nomnom -i data.tsv -o output.yaml -H`
**Explanation:** Uses first row as header.

### Verbose mode
**Args:** `nomnom -i data.tsv -o output.yaml -v`
**Explanation:** Runs with verbose output.