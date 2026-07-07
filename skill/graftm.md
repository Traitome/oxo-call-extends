---
name: graftm
category: bioinformatics
description: GraftM is a pipeline for identifying and classifying marker gene reads from metagenomic datasets using phylogenetic placement.
tags: [graftm, metagenomics, marker-genes, phylogenetic-placement, bioinformatics]
author: oxo-call-community
source_url: "http://geronimp.github.io/graftM"
---

## Concepts

- **Marker Gene Identification**: GraftM identifies marker gene reads from metagenomic sequencing data.

- **Phylogenetic Placement**: Places marker gene sequences onto reference phylogenies for taxonomic classification.

- **Database Construction**: Builds custom databases of marker genes for specific taxonomic groups.

- **Abundance Estimation**: Estimates relative abundance of different taxa based on marker gene coverage.

- **Quality Control**: Provides metrics for assessing classification quality and confidence.

- **Multi-marker Support**: Supports analysis of multiple marker genes simultaneously.

## Pitfalls

- **Reference Database**: Classification accuracy depends on database coverage. Ensure comprehensive reference sequences.

- **Marker Selection**: Choose appropriate marker genes for your research question. Different markers have different resolution.

- **Read Quality**: Low-quality reads can produce incorrect classifications. Preprocess reads carefully.

- **Computational Requirements**: Building large databases or processing many samples requires significant resources.

- **Horizontal Gene Transfer**: Marker genes may be horizontally transferred, affecting taxonomic assignment.

## Examples

### Build marker database
**Args:** `graftm build -i reference_sequences.fasta -o marker_db/`
**Explanation:** Builds a marker gene database from reference sequences.

### Classify metagenomic reads
**Args:** `graftm graft -i reads.fastq -d marker_db/ -o results.txt`
**Explanation:** Identifies and classifies marker gene reads from metagenomic data.

### Estimate abundance
**Args:** `graftm abundance -i results.txt -o abundance.txt`
**Explanation:** Estimates relative abundance of taxa from classification results.

### Specify multiple markers
**Args:** `graftm graft -i reads.fastq -d marker_db1/ marker_db2/ -o results.txt`
**Explanation:** Analyzes multiple marker genes simultaneously.

### Generate report
**Args:** `graftm report -i results.txt -o report.html`
**Explanation:** Generates a comprehensive HTML report with classification statistics.

### Batch processing
**Args:** `graftm batch -d samples/ -d marker_db/ -o results/`
**Explanation:** Processes multiple metagenomic samples in a directory.

### Filter low-confidence hits
**Args:** `graftm graft -i reads.fastq -d marker_db/ -c 0.9 -o filtered.txt`
**Explanation:** Only keeps classifications with confidence scores above 0.9.