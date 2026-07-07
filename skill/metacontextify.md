---
name: metacontextify
category: alignment
description: Automated environmental annotation of marine metagenomic samples
tags: [metacontextify, alignment, metagenomics, marine, annotation]
author: oxo-call-community
source_url: "https://github.com/MaartenLangen/metacontextify"
---

## Concepts

- **Tool Overview**: metacontextify v0.1.0 is a tool for automated environmental annotation of marine metagenomic samples, providing contextual information about sample origin.
- **Core Function**: Annotates metagenomic sequences with environmental metadata including location, depth, temperature, and other environmental parameters.
- **Marine Focus**: Specifically designed for marine metagenomic data analysis and environmental characterization.
- **Metadata Integration**: Integrates environmental metadata with sequence data for comprehensive annotation.
- **Input/Output**: Accepts FASTA/Q sequence files with associated metadata; outputs annotated sequences with environmental context.
- **Taxonomic Context**: Provides taxonomic classification along with environmental annotation.

## Pitfalls

- **Metadata Quality**: Annotation quality depends on the quality and completeness of input metadata.
- **Sample Origin**: Requires accurate sample origin information for meaningful environmental annotation.
- **Database Coverage**: Environmental databases may have limited coverage for certain marine environments.
- **Sequence Quality**: Poor quality sequences may produce incorrect annotations.
- **Geographic Bias**: Reference databases may have geographic biases affecting annotation.
- **Environmental Variability**: Dynamic marine environments may affect annotation consistency.

## Examples

### Annotate marine metagenome
**Args:** `metacontextify -i reads.fastq -m metadata.csv -o annotated.fasta`
**Explanation:** Annotates metagenomic reads with environmental metadata.

### With custom database
**Args:** `metacontextify -i reads.fastq -m metadata.csv -d custom_db/ -o annotated.fasta`
**Explanation:** Uses a custom environmental database for annotation.

### Generate summary report
**Args:** `metacontextify -i reads.fastq -m metadata.csv -o annotated.fasta -r report.txt`
**Explanation:** Generates a summary report of environmental annotations.

### Filter by environment type
**Args:** `metacontextify -i reads.fastq -m metadata.csv -e pelagic -o annotated.fasta`
**Explanation:** Filters annotations to specific environment types.

### Output in JSON format
**Args:** `metacontextify -i reads.fastq -m metadata.csv -o annotations.json -f json`
**Explanation:** Outputs annotations in JSON format for programmatic access.