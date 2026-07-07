---
name: trace-crispr
category: analysis
description: Trace-CRISPR - Tool for tracing CRISPR-Cas9 editing outcomes.
tags: [trace-crispr, crispr, gene-editing, editing-outcomes, genome-editing]
author: oxo-call-community
source_url: "https://github.com/compbio/trace-crispr"
---

## Concepts

- **Tool Overview**: Trace-CRISPR - A tool for analyzing and tracing CRISPR-Cas9 genome editing outcomes.
- **Core Function**: Identifies and characterizes CRISPR-induced mutations and editing events.
- **Input**: Sequencing reads (FASTQ/BAM), guide RNA sequences, reference genome.
- **Output**: Editing outcomes, mutation types, indel sizes, efficiency metrics.
- **Installation**: `pip install trace-crispr` or `conda install -c bioconda trace-crispr`
- **Use Case**: CRISPR editing validation, mutation analysis, gene knockout screening.

## Pitfalls

- **Guide RNA**: Requires accurate guide RNA sequences for analysis.
- **Alignment**: Requires properly aligned sequencing data.

## Examples

### Analyze CRISPR edits
**Args:** `trace-crispr -i edited.bam -g guide_rna.txt -o editing_results/`
**Explanation:** Analyze CRISPR-Cas9 editing outcomes from sequencing data.

### With FASTQ
**Args:** `trace-crispr -f reads.fastq -g guides.txt -r genome.fasta -o results/`
**Explanation:** Analyze editing outcomes directly from FASTQ reads.
