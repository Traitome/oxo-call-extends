---
name: savont
category: variant-calling
description: Amplicon sequencing variants (ASVs) and taxonomic profiling from long-read amplicon sequencing
tags: ["savont", "variant-calling", "amplicon", "long-read", "taxonomic-profiling"]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/savont"
---

## Concepts

- **Tool Overview**: Savont (v0.3.2) is a tool for amplicon sequencing variants (ASVs) and taxonomic profiling from modern long-read (nanopore + PacBio) amplicon sequencing with >98% accuracy.
- **Core Function**: Processes long-read amplicon data to identify ASVs and perform taxonomic classification.
- **Algorithm**: Uses error correction and clustering algorithms optimized for long amplicon reads.
- **Input/Output**: Accepts FASTQ reads from amplicon sequencing and produces ASV tables with taxonomic assignments.
- **Accuracy**: Achieves >98% accuracy for ASV identification from noisy long-read data.
- **Applications**: Microbiome analysis, 16S/18S rRNA sequencing, and amplicon-based biodiversity studies.

## Pitfalls

- **Amplicon Specific**: Designed specifically for amplicon sequencing data.
- **Reference Database**: Requires up-to-date reference databases for taxonomic classification.
- **Read Length**: Performance depends on read length and quality.
- **PCR Bias**: May be affected by PCR amplification biases.
- **Memory Usage**: High memory requirements for large datasets.
- **Database Updates**: Regular database updates required for accurate taxonomic assignments.

## Examples

### Basic ASV calling
**Args:** `savont -i reads.fastq -o asv_table.tsv`
**Explanation:** `-i` input FASTQ; `-o` output ASV table in TSV format.

### With taxonomic classification
**Args:** `savont -i reads.fastq -d silva -o asv_table.tsv`
**Explanation:** `-d silva` uses SILVA database for taxonomic classification.

### Quality filtering
**Args:** `savont -i reads.fastq -q 10 -o asv_table.tsv`
**Explanation:** `-q 10` filters reads with average quality below 10.

### Cluster threshold
**Args:** `savont -i reads.fastq -c 0.99 -o asv_table.tsv`
**Explanation:** `-c 0.99` sets clustering identity threshold to 99%.

### Output FASTA
**Args:** `savont -i reads.fastq -f asvs.fasta -o asv_table.tsv`
**Explanation:** `-f` outputs representative sequences in FASTA format.

### Batch processing
**Args:** `savont -i ./samples/ -o ./results/ -b`
**Explanation:** `-b` batch mode for processing multiple samples.

### Verbose mode
**Args:** `savont -i reads.fastq -v -o asv_table.tsv`
**Explanation:** `-v` enables verbose output for debugging.