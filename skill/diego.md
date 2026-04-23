---
name: diego
category: expression
description: Detection of differential alternative splicing using Aitchison's geometry.
tags: [diego, expression, splicing, differential, compositional-data]
author: oxo-call-community
source_url: "http://www.bioinf.uni-leipzig.de/Software/DIEGO"
---

## Concepts

- **Tool Overview**: DIEGO v0.1.2 - Tool for detecting differential alternative splicing events using Aitchison's compositional data geometry.
- **Core Function**: Identifies differential splicing events by treating splice isoform counts as compositional data.
- **Input/Output**: Expects read counts per splice isoform; outputs differential splicing events with statistics.
- **Installation**: `conda install -c bioconda diego`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires isoform-level read count data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diego --counts counts.tsv --groups groups.tsv --output diff_splicing.tsv`
**Explanation:** Detects differential alternative splicing between conditions.
