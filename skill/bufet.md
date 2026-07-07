---
name: bufet
category: expression
description: Unbiased miRNA functional enrichment analysis tool with fast execution
tags: [bufet, mirna, enrichment, functional-analysis]
author: oxo-call-community
source_url: "https://github.com/diwis/BUFET/"
---

## Concepts

- **Tool Overview**: BUFET performs unbiased miRNA functional enrichment analysis efficiently.
- **Core Function**: Identifies enriched biological functions associated with miRNA targets.
- **Algorithm**: Implements the Bleazard et al. method with optimized execution.
- **Input**: miRNA target predictions and gene annotation data.
- **Output**: Functional enrichment results with statistical significance.
- **Performance**: Processes 1 million iterations in less than 10 minutes.
- **Installation**: Install via bioconda: `conda install -c bioconda bufet`

## Pitfalls

- **Target Data**: Requires high-quality miRNA target predictions.
- **Annotation Version**: Ensure annotation databases are current.
- **Multiple Testing**: Apply appropriate multiple testing correction.
- **Input Format**: Follow required input format for miRNA targets.

## Examples

### Run enrichment analysis
**Args:** `bufet -i mirna_targets.txt -a annotations.gmt -o enrichment_results.tsv`
**Explanation:** Performs unbiased miRNA functional enrichment analysis.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.