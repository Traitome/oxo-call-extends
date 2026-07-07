---
name: metacache
category: alignment
description: MetaCache is a classification system for mapping genomic sequences (short reads, long reads, contigs, ...) from metagenomic samples to their most likely taxon of origin.
tags: [metacache, alignment, metagenomics, classification]
author: oxo-call-community
source_url: "https://github.com/muellan/metacache"
---

## Concepts

- **Tool Overview**: MetaCache v2.6.0 is a fast and memory-efficient classification system designed for mapping genomic sequences from metagenomic samples to their most likely taxonomic origin. It supports short reads, long reads, and contigs.
- **Core Function**: Uses a k-mer based indexing approach to quickly classify sequences by comparing them against a reference database.
- **Index Building**: MetaCache builds an index from reference genomes, allowing for rapid sequence classification during analysis.
- **Multi-level Classification**: Supports classification at multiple taxonomic levels (species, genus, family, etc.) depending on the confidence of matches.
- **Input/Output**: Accepts FASTA/Q formatted sequence files; outputs classification results in various formats including SAM, BAM, and custom report formats.
- **Performance**: Optimized for large metagenomic datasets with efficient memory usage and fast classification speeds.

## Pitfalls

- **Database Completeness**: Classification accuracy depends heavily on the completeness and quality of the reference database.
- **k-mer Size Selection**: Choosing inappropriate k-mer sizes can affect classification sensitivity and specificity.
- **Memory Requirements**: Building large indexes can require significant memory resources.
- **Ambiguous Reads**: Reads mapping to multiple taxa may produce ambiguous classification results.
- **Long Read Support**: While supported, long reads may require parameter adjustments for optimal performance.
- **Taxonomic Bias**: Reference databases may have inherent taxonomic biases that affect classification results.

## Examples

### Build index from reference database
**Args:** `metacache build -d ref_db/ -o index/`
**Explanation:** Builds an index from the reference database directory containing FASTA files.

### Classify short reads
**Args:** `metacache classify -i reads.fastq -x index/ -o results.sam`
**Explanation:** Classifies short reads against the built index and outputs results in SAM format.

### Classify long reads
**Args:** `metacache classify -i long_reads.fastq -x index/ -m long -o results.sam`
**Explanation:** Uses long read mode for optimal classification of long sequencing reads.

### Generate classification report
**Args:** `metacache report -i results.sam -o report.txt`
**Explanation:** Generates a human-readable classification report from SAM output.

### Classify with custom k-mer size
**Args:** `metacache classify -i reads.fastq -x index/ -k 25 -o results.sam`
**Explanation:** Uses a custom k-mer size of 25 for classification.