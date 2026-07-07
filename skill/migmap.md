---
name: migmap
category: alignment
description: A wrapper for IgBlast V-(D)-J mapping tool designed to facilitate analysis immune receptor libraries profiled using high-throughput sequencing.
tags: [migmap, alignment, immunology]
author: oxo-call-community
source_url: "https://github.com/mikessh/migmap"
---

## Concepts

- **Tool Overview**: MigMap v1.0.3 is a wrapper for IgBlast V-(D)-J mapping tool.
- **Core Function**: Maps immune receptor sequences to V-(D)-J germline genes.
- **IgBlast Integration**: Wraps IgBlast for V-(D)-J alignment.
- **Immune Repertoire**: Analyzes high-throughput immune receptor sequencing data.
- **Input/Output**: Accepts sequencing reads; outputs V-(D)-J assignments.
- **Adaptive Immunity**: Supports analysis of B-cell and T-cell receptor repertoires.

## Pitfalls

- **Immune Receptor Specific**: Designed for immune receptor analysis.
- **IgBlast Dependency**: Requires IgBlast for mapping.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal mapping.
- **Data Quality**: Mapping accuracy depends on input sequence quality.
- **Germline Database**: Requires appropriate germline gene database.

## Examples

### Map V(D)J sequences
**Args:** `migmap -i reads.fastq -o results.txt`
**Explanation:** Maps immune receptor sequences to germline genes.

### With custom database
**Args:** `migmap -i reads.fastq -d germline_db/ -o results.txt`
**Explanation:** Uses custom germline gene database.

### Detailed output
**Args:** `migmap -i reads.fastq -o results.txt -v`
**Explanation:** Generates detailed mapping report.

### Batch processing
**Args:** `migmap -i fastq/ -o results/`
**Explanation:** Processes multiple read files in batch mode.

### Filter results
**Args:** `migmap -i reads.fastq -o results.txt -f high`
**Explanation:** Filters results by mapping quality.