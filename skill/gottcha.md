---
name: gottcha
category: bioinformatics
description: GOTTCHA (Genomic Origin Through Taxonomic CHAllenge) is a taxonomic classification tool for metagenomic sequencing data.
tags: [gottcha, metagenomics, taxonomic-classification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/LANL-Bioinformatics/GOTTCHA"
---

## Concepts

- **Metagenomic Classification**: GOTTCHA identifies the taxonomic origin of metagenomic sequencing reads using clade-specific marker genes.

- **Unique Marker Identification**: Uses unique clade-specific oligonucleotide markers for taxonomic assignment.

- **Database Construction**: Builds databases of taxonomic markers from reference sequences for classification.

- **Read Mapping**: Maps sequencing reads to marker databases to determine taxonomic origin.

- **Abundance Profiling**: Generates taxonomic abundance profiles from classification results.

- **Phylogenetic Resolution**: Provides classification at multiple taxonomic levels (species, genus, family, etc.).

## Pitfalls

- **Database Coverage**: Limited database coverage can lead to unclassified reads. Ensure comprehensive reference sequences.

- **Marker Specificity**: Markers may not be perfectly specific. Cross-validation with other methods is recommended.

- **Read Quality**: Low-quality reads can produce incorrect classifications. Preprocess reads with quality filtering.

- **Computational Requirements**: Building large databases or processing many samples requires significant resources.

- **False Discovery**: Random matches can occur. Use appropriate significance thresholds.

## Examples

### Build reference database
**Args:** `gottcha build -i reference.fasta -o database/`
**Explanation:** Builds a taxonomic marker database from reference sequences.

### Classify metagenomic reads
**Args:** `gottcha classify -i reads.fastq -d database/ -o results.txt`
**Explanation:** Classifies metagenomic reads using the built database.

### Generate abundance profile
**Args:** `gottcha abundance -i results.txt -o profile.txt`
**Explanation:** Generates a taxonomic abundance profile from classification results.

### Specify taxonomic level
**Args:** `gottcha classify -i reads.fastq -d database/ -l genus -o results.txt`
**Explanation:** Classifies reads at the genus level instead of the default species level.

### Filter by confidence
**Args:** `gottcha classify -i reads.fastq -d database/ -c 0.8 -o filtered.txt`
**Explanation:** Only reports classifications with confidence scores above 0.8.

### Batch process samples
**Args:** `gottcha classify -d samples/ -d database/ -o output/`
**Explanation:** Processes all samples in a directory and saves individual results.

### Generate summary report
**Args:** `gottcha report -i results.txt -o summary.html`
**Explanation:** Generates a comprehensive HTML report with classification statistics.