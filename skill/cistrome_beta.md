---
name: cistrome_beta
category: expression
description: Binding and Expression Target Analysis of ChIP-seq TF with differential gene expression
tags: [cistrome_beta, chip-seq, transcription-factor, gene-expression, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hanfeisun/BETA"
---

## Concepts

- **Tool Overview**: Cistrome BETA is a comprehensive tool for integrating ChIP-seq transcription factor binding data with differential gene expression analysis.
- **Core Function**: Identifies potential target genes of transcription factors by combining binding site information with gene expression changes.
- **Algorithm**: Integrates ChIP-seq peaks with RNA-seq differential expression data to predict functional TF targets.
- **Input**: ChIP-seq peak files (BED/BAM) and differential expression results.
- **Output**: Predicted TF target genes with regulatory potential scores.
- **Application**: Transcription factor target identification, gene regulatory network analysis, and functional genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cistrome_beta`

## Pitfalls

- **Data Quality**: Requires high-quality ChIP-seq and RNA-seq data.
- **Peak Calling**: Depends on accurate peak calling from ChIP-seq data.
- **Reference Genome**: Must use the same reference genome for both datasets.
- **Statistical Thresholds**: Appropriate thresholds must be set for significance.
- **False Positives**: May identify false targets from indirect effects.

## Examples

### Analyze TF targets
**Args:** `beta -i peaks.bed -d diff_expr.txt -g genome.fasta -o targets.txt`
**Explanation:** Identifies transcription factor target genes by integrating ChIP-seq peaks with differential expression data.

### With promoter regions
**Args:** `beta -i peaks.bed -d diff_expr.txt -p 2000 -o targets.txt`
**Explanation:** Limits analysis to promoter regions within 2000bp of TSS.

### Generate regulatory network
**Args:** `beta -i peaks.bed -d diff_expr.txt --network -o network.txt`
**Explanation:** Generates regulatory network from TF-target interactions.

### Display help
**Args:** `beta --help`
**Explanation:** Shows all available options and usage information.