---
name: cmat
category: alignment
description: ClinVar Mapping and Annotation Toolkit.
tags: [cmat, alignment]
author: oxo-call-community
source_url: "https://github.com/EBIvariation/CMAT/blob/v3.4.3/README.md"
---

## Concepts

- **Tool Overview**: cmat (v3.4.3) - ClinVar Mapping and Annotation Toolkit.
- **Core Function**: ClinVar Mapping and Annotation Toolkit.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cmat`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
