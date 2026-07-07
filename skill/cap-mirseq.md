---
name: cap-mirseq
category: rna-seq
description: miRNA sequencing data analysis pipeline
tags: [cap-mirseq, mirna, sequencing, small-rna, rna-seq]
author: oxo-call-community
source_url: "https://github.com/PMBio/cap-miRSeq"
---

## Concepts

- **Tool Overview**: cap-miRSeq is a comprehensive pipeline for miRNA sequencing data analysis.
- **Core Function**: Processes small RNA sequencing data to identify and quantify miRNAs.
- **Workflow**: Quality trimming → Adapter removal → miRNA mapping → Quantification.
- **Input**: FASTQ files from small RNA sequencing experiments.
- **Output**: miRNA expression profiles and annotations.
- **Application**: miRNA expression analysis and biomarker discovery.
- **Installation**: Install via bioconda: `conda install -c bioconda cap-mirseq`

## Pitfalls

- **Adapter Sequences**: Must provide correct adapter sequences for trimming.
- **Reference Database**: Requires miRNA reference database (miRBase).
- **Quality Control**: Poor quality reads can affect mapping accuracy.
- **Mapping Parameters**: Adjust mapping stringency based on data quality.

## Examples

### Process miRNA sequencing data
**Args:** `cap-mirseq -i reads.fq -a adapter.fa -d mirbase/ -o results/`
**Explanation:** Processes small RNA sequencing data for miRNA analysis.

### Set trimming parameters
**Args:** `cap-mirseq -i reads.fq -a adapter.fa -q 20 -l 18 -o results/`
**Explanation:** Uses quality cutoff 20 and minimum length 18 for trimming.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.