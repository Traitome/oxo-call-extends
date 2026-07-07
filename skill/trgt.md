---
name: trgt
category: analysis
description: TRGT - Tool for analyzing targeted sequencing data.
tags: [trgt, targeted-sequencing, variant-calling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/compbio/trgt"
---

## Concepts

- **Tool Overview**: TRGT - A tool for analyzing targeted sequencing data from gene panels.
- **Core Function**: Processes targeted sequencing data for variant calling and coverage analysis.
- **Input**: BAM files, target regions (BED), reference genome.
- **Output**: Variant calls (VCF), coverage statistics, quality metrics.
- **Installation**: `pip install trgt` or `conda install -c bioconda trgt`
- **Use Case**: Targeted sequencing analysis, clinical genomics, gene panel analysis.

## Pitfalls

- **Target Definition**: Requires accurate target region definitions.
- **Coverage**: Requires sufficient coverage depth.

## Examples

### Process targeted data
**Args:** `trgt -i alignments.bam -t targets.bed -r genome.fasta -o results/`
**Explanation:** Process targeted sequencing data.

### Coverage analysis
**Args:** `trgt coverage -i bam_files/ -t targets.bed -o coverage/`
**Explanation:** Analyze coverage across target regions.
