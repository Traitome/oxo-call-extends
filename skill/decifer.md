---
name: decifer
category: expression
description: DeCiFer simultaneously selects mutation multiplicities and clusters SNVs by their corresponding descendant cell fractions (DCF).
tags: [decifer, expression, SAM]
author: oxo-call-community
source_url: "https://github.com/raphael-group/decifer"
---

## Concepts

- **Tool Overview**: decifer (v2.1.4) - DeCiFer simultaneously selects mutation multiplicities and clusters SNVs by their corresponding descendant cell fractions (DCF).
- **Core Function**: DeCiFer is an algorithm that simultaneously selects mutation multiplicities and clusters SNVs by their corresponding descendant cell fractions (DCF), a statistic that quantifies the proportion of cell...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda decifer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
