---
name: singlem
category: metagenomics
description: SingleM - Shotgun metagenome profiling
tags: ["singlem", "metagenomics", "profiling", "taxonomy"]
author: oxo-call-community
source_url: "https://wwood.github.io/singlem"
---

## Concepts

- **Tool Overview**: SingleM (v0.20.3) profiles shotgun metagenomes for bacterial/archaeal taxa.
- **Core Function**: Determines relative abundance of taxa in metagenomic samples.
- **Algorithm**: Uses single marker gene analysis for taxonomic profiling.
- **Input/Output**: Accepts FASTQ reads and produces abundance profiles.
- **Metagenomic Profiling**: Specialized for novel lineage detection.
- **Applications**: Microbiome analysis, metagenomics, contamination assessment.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Database Requirements**: Requires marker gene database.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Profile metagenome
**Args:** `singlem pipe -i reads.fastq -o profile.tsv`
**Explanation:** `-i` input FASTQ; `-o` output profile.

### With database
**Args:** `singlem pipe -i reads.fastq -d database/ -o profile.tsv`
**Explanation:** `-d` marker gene database.

### Merge profiles
**Args:** `singlem merge -i profiles/ -o merged_profile.tsv`
**Explanation:** Merges multiple profiles.

### Help command
**Args:** `singlem --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `singlem --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `singlem -v pipe -i reads.fastq -o profile.tsv`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `singlem -t 8 pipe -i reads.fastq -o profile.tsv`
**Explanation:** `-t 8` uses 8 threads.
