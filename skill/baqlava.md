---
name: baqlava
category: expression
description: BAQLaVa - Bioinformatic Application of Quantification and Labeling of Viral Taxonomy
tags: [baqlava, expression, viral-taxonomy, quantification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/biobakery/baqlava"
---

## Concepts

- **Tool Overview**: BAQLaVa (v0.5) is a bioinformatic application for the quantification and labeling of viral taxonomy from sequencing data.
- **Core Function**: Quantifies viral taxonomy abundance from metagenomic sequencing data.
- **Viral Classification**: Identifies and quantifies viral taxa in metagenomic samples.
- **Abundance Estimation**: Estimates relative abundance of different viral species.
- **Taxonomic Labeling**: Assigns taxonomic labels to viral sequences.
- **Input/Output**: Accepts sequencing reads (FASTQ); outputs taxonomic profiles and abundance tables.
- **Installation**: `conda install -c bioconda baqlava`.

## Pitfalls

- **Reference Database**: Requires viral reference database for classification.
- **Host Contamination**: Host sequences may interfere with viral detection.
- **Low Abundance Viruses**: May miss low abundance viral taxa.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic viral quantification
**Args:** `baqlava -i reads.fastq -o viral_profile.txt`
**Explanation:** Quantifies viral taxonomy from sequencing reads.

### Pair-end reads
**Args:** `baqlava -i reads_1.fastq -i reads_2.fastq -o viral_profile.txt`
**Explanation:** Processes paired-end sequencing reads for viral quantification.

### Specify reference database
**Args:** `baqlava -i reads.fastq -d viral_db/ -o viral_profile.txt`
**Explanation:** Uses custom viral reference database for classification.

### Output in JSON format
**Args:** `baqlava -i reads.fastq -o viral_profile.json --format json`
**Explanation:** Outputs results in JSON format for programmatic processing.

### Filter by abundance
**Args:** `baqlava -i reads.fastq -o viral_profile.txt --min-abundance 0.01`
**Explanation:** Filters out taxa with abundance below threshold.

### Generate visualization
**Args:** `baqlava -i reads.fastq -o viral_profile.txt --plot viral_plot.png`
**Explanation:** Generates visualization of viral taxonomic distribution.

### Display help
**Args:** `baqlava --help`
**Explanation:** Shows all available command-line options and usage information.