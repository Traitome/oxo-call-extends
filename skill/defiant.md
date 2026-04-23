---
name: defiant
category: epigenomics
description: Differential methylation, Easy, Fast, Identification and ANnoTation.
tags: [defiant, epigenomics, methylation, differential-analysis]
author: oxo-call-community
source_url: "https://github.com/hhg7/defiant"
---

## Concepts

- **Tool Overview**: Defiant v1.1.4 - Tool for fast differential methylation analysis with annotation capabilities.
- **Core Function**: Identifies differentially methylated regions (DMRs) between conditions and annotates them with genomic features.
- **Input/Output**: Expects methylation calls (BED/Bismark output); outputs DMRs with annotations.
- **Installation**: `conda install -c bioconda defiant`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires methylation data in compatible format from bisulfite sequencing.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `defiant --control control.bed --treatment treatment.bed --output dmrs.tsv`
**Explanation:** Finds differentially methylated regions between conditions.
