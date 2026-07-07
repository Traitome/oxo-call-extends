---
name: colorid_bv
category: qc
description: BIGSI data structure for metagenomic and QC applications
tags: [colorid_bv, bigsi, metagenomics, indexing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hcdenbakker/colorid_bv"
---

## Concepts

- **Tool Overview**: colorid_bv is an experimental tool using the BIGSI (Bloom Filter-based Index for Sequence Search) data structure for metagenomic analysis and quality control applications.
- **Core Function**: Implements colored de Bruijn graph indexing for efficient sequence search and metagenomic classification.
- **Algorithm**: Uses Bloom filter-based indexing with color information to enable fast k-mer queries across multiple samples.
- **Input**: Sequencing reads or assembled contigs in FASTA/FASTQ format.
- **Output**: Query results, presence/absence matrices, or QC metrics.
- **Application**: Metagenomic analysis, contamination detection, and sequence database querying.
- **Installation**: Install via bioconda: `conda install -c bioconda colorid_bv`

## Pitfalls

- **Memory Usage**: BIGSI indexes can require significant memory.
- **False Positives**: Bloom filter-based approach may produce false positives.
- **k-mer Size**: Results depend on appropriate k-mer size selection.
- **Index Construction**: Building indexes can be computationally intensive.
- **Experimental Status**: Tool is experimental and may have limited documentation.

## Examples

### Build BIGSI index
**Args:** `colorid_bv build -i sequences.fasta -o index.bigsi`
**Explanation:** Builds BIGSI index from sequence data.

### Query index
**Args:** `colorid_bv query -i index.bigsi -q query.fasta -o results.txt`
**Explanation:** Queries BIGSI index with sequence queries.

### Quality control analysis
**Args:** `colorid_bv qc -i reads.fastq -r reference.bigsi -o qc_report.txt`
**Explanation:** Performs QC analysis using BIGSI reference index.

### Display help
**Args:** `colorid_bv --help`
**Explanation:** Shows all available options and usage information.