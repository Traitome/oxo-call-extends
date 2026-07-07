---
name: metamobilepicker
category: alignment
description: "MetaMobilePicker: identification of MGEs and ARGs based in metagenomic samples"
tags: [metamobilepicker, alignment, MGE, ARGs, metagenomics]
author: oxo-call-community
source_url: "https://gitlab.com/jkerkvliet/metamobilepicker"
---
## Concepts

- **Tool Overview**: MetaMobilePicker v0.7.3 is a tool for identifying Mobile Genetic Elements (MGEs) and Antibiotic Resistance Genes (ARGs) in metagenomic samples.
- **Core Function**: Detects and annotates MGEs and ARGs from metagenomic sequencing data.
- **MGE Detection**: Identifies mobile genetic elements including plasmids, transposons, and integrons.
- **ARG Detection**: Identifies antibiotic resistance genes and their variants.
- **Input/Output**: Accepts FASTA/Q sequence files; outputs annotated MGEs and ARGs with functional annotations.
- **Comprehensive Analysis**: Provides detailed information about detected elements including their type, location, and potential impact.

## Pitfalls

- **Database Completeness**: Detection accuracy depends on reference database completeness.
- **Sequence Quality**: Poor quality sequences may affect detection accuracy.
- **False Positives**: May detect false positive MGEs or ARGs.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Low Abundance**: May miss elements present at very low abundance.
- **Database Updates**: Requires regular database updates for optimal performance.

## Examples

### Identify MGEs and ARGs
**Args:** `metamobilepicker -i reads.fastq -o results/`
**Explanation:** Identifies MGEs and ARGs in metagenomic reads.

### With custom database
**Args:** `metamobilepicker -i reads.fastq -d custom_db/ -o results/`
**Explanation:** Uses a custom database for detection.

### Focus on ARGs only
**Args:** `metamobilepicker -i reads.fastq -o results/ --args-only`
**Explanation:** Focuses detection on antibiotic resistance genes only.

### Generate visualization
**Args:** `metamobilepicker -i reads.fastq -o results/ -v`
**Explanation:** Generates visualizations of detected elements.

### Batch processing
**Args:** `metamobilepicker -i fastq/ -o results/`
**Explanation:** Processes multiple FASTQ files in batch.