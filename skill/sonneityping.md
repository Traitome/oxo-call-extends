---
name: sonneityping
category: annotation
description: Sonneityping - Shigella sonnei typing from mykrobe output
tags: [sonneityping, annotation, typing, shigella, mykrobe]
author: oxo-call-community
source_url: "https://github.com/katholt/sonneityping"
---

## Concepts

- **Tool Overview**: sonneityping (v20210201) - A Shigella sonnei typing tool
- **Core Function**: Parses mykrobe output for Shigella sonnei typing
- **Input/Output**: Accepts mykrobe output; outputs typing results
- **Algorithm**: Parses and interprets mykrobe predictions
- **Installation**: `conda install -c bioconda sonneityping`
- **Key Features**: Shigella typing, mykrobe integration, lineage identification

## Pitfalls

- **Input Requirements**: Requires properly formatted mykrobe output
- **Species Specific**: Designed specifically for Shigella sonnei
- **Version Compatibility**: Must use compatible mykrobe version
- **Database**: Requires proper typing database
- **Output Format**: Output format depends on configuration
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `sonneityping --help`
**Explanation:** Shows available options and usage information.

### Basic typing
**Args:** `sonneityping -i mykrobe_output.txt -o typing_results.txt`
**Explanation:** Parse mykrobe output for typing.

### With lineage info
**Args:** `sonneityping -i mykrobe_output.txt -o typing_results.txt --lineage`
**Explanation:** Output lineage information.

### With detailed output
**Args:** `sonneityping -i mykrobe_output.txt -o typing_results.txt --detailed`
**Explanation:** Output detailed typing results.

### Multiple samples
**Args:** `sonneityping -i mykrobe1.txt mykrobe2.txt -o typing_results.txt`
**Explanation:** Process multiple samples.

### Output statistics
**Args:** `sonneityping -i mykrobe_output.txt -o typing_results.txt --stats`
**Explanation:** Output typing statistics.

### Generate report
**Args:** `sonneityping -i mykrobe_output.txt -o typing_results.txt --report`
**Explanation:** Generate typing report.

### With validation
**Args:** `sonneityping -i mykrobe_output.txt -o typing_results.txt --validate`
**Explanation:** Validate typing results.