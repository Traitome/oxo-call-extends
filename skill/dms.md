---
name: dms
category: annotation
description: DMS - Deep Mutational Scanning analysis tools.
tags: [dms, annotation, deep-mutational-scanning, variant, protein]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DMS - Tools for analyzing deep mutational scanning experiments.
- **Core Function**: Analyzes high-throughput mutagenesis data to assess variant effects.
- **Input/Output**: Expects sequencing counts from DMS experiments; outputs variant fitness scores.
- **Installation**: `conda install -c bioconda dms`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires deep mutational scanning count data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dms analyze --counts counts.tsv --output fitness.tsv`
**Explanation:** Analyzes deep mutational scanning data.
