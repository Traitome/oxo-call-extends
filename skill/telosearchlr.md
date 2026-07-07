---
name: telosearchlr
category: analysis
description: TELO-Search LR - Long-read telomere search tool for comprehensive telomere identification.
tags: [telosearchlr, telomere, long-read, nanopore, pacbio, telomere-search]
author: oxo-call-community
source_url: "https://github.com/genome-tools/telosearch-lr"
---

## Concepts

- **Tool Overview**: TELO-Search LR - Long-read version of TELO-Search for identifying telomeres in long-read sequencing data.
- **Core Function**: Searches for known and novel telomere repeat sequences in long-read datasets with high sensitivity.
- **Input**: Long-read FASTQ files, optional telomere motif database.
- **Output**: Telomere read annotations, telomere motif frequencies, and genomic coordinates.
- **Installation**: `pip install telosearchlr` or `conda install -c bioconda telosearchlr`
- **Use Case**: Validating telomere assembly quality, population studies of telomere variation.

## Pitfalls

- **Known Motifs**: Default database contains known telomeres - may miss organism-specific novel motifs.
- **Read Quality**: Lower quality reads may lead to false negative telomere detection.

## Examples

### Search telomeres
**Args:** `telosearchlr -i long_reads.fastq.gz -o telomere_hits.txt`
**Explanation:** Search for telomere sequences in long-read data.

### Custom motif database
**Args:** `telosearchlr -i reads.fastq -d custom_motifs.fasta -o results/`
**Explanation:** Use custom telomere motif database for search.
