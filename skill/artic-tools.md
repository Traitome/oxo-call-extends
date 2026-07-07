---
name: artic-tools
category: formatting
description: Artic-tools - Utility tools for working with ARTIC bioinformatics pipeline
tags: [artic-tools, formatting, artic, nanopore, viral-genomics, primer-schemes]
author: oxo-call-community
source_url: "https://github.com/will-rowe/artic-tools"
---

## Concepts

- **Tool Overview**: Artic-tools provides a collection of utility tools for working with the ARTIC bioinformatics pipeline for viral nanopore sequencing. Version 0.3.1.
- **Core Function**: Offers helper tools for primer scheme validation, read filtering, and data manipulation in ARTIC workflows.
- **Primer Scheme Tools**: Validates and manipulates ARTIC primer schemes for different pathogens.
- **Read Filtering**: Filters and processes nanopore reads for improved assembly quality.
- **Format Conversion**: Converts between different file formats used in ARTIC pipeline.
- **Quality Control**: Provides QC metrics and filtering options for nanopore data.
- **Input/Output**: Supports FASTQ, FASTA, BED, and other formats used in ARTIC workflows.
- **Installation**: `conda install -c bioconda artic-tools` or install from GitHub.

## Pitfalls

- **ARTIC Dependency**: Designed specifically for ARTIC pipeline. May not work with other pipelines.
- **Primer Scheme Format**: Requires ARTIC-formatted primer schemes. Other formats need conversion.
- **Read Quality**: Filtering thresholds must be adjusted based on data quality. Too strict filtering removes too many reads.
- **Version Compatibility**: Artic-tools version should match ARTIC pipeline version for compatibility.
- **Nanopore Specific**: Optimized for nanopore data. May not work with Illumina or other sequencing platforms.

## Examples

### Display help
**Args:** `artic-tools --help`
**Explanation:** Shows all available command-line options and usage information.

### Validate primer scheme
**Args:** `artic-tools validate-scheme --scheme scheme.bed --reference genome.fasta`
**Explanation:** Validates primer scheme against reference genome. Checks for primer binding sites and overlaps.

### Filter reads by length
**Args:** `artic-tools filter-length --input reads.fastq --min 400 --max 700 --output filtered.fastq`
**Explanation:** Filters reads to specified length range (400-700bp). Appropriate for SARS-CoV-2 amplicons.

### Remove primer sequences
**Args:** `artic-tools remove-primers --input reads.fastq --scheme scheme.bed --output trimmed.fastq`
**Explanation:** Removes primer sequences from reads using specified primer scheme.

### Check amplicon coverage
**Args:** `artic-tools amplicon-coverage --input aligned.bam --scheme scheme.bed --output coverage.txt`
**Explanation:** Calculates coverage per amplicon from aligned reads. Identifies amplicon dropouts.

### Convert primer scheme format
**Args:** `artic-tools convert-scheme --input primers.csv --output scheme.bed --format bed`
**Explanation:** Converts primer scheme from CSV to BED format used by ARTIC pipeline.

### Generate primer statistics
**Args:** `artic-tools primer-stats --scheme scheme.bed --reference genome.fasta --output stats.txt`
**Explanation:** Generates statistics for primer scheme including primer positions, Tm, and GC content.

### Filter by quality score
**Args:** `artic-tools filter-quality --input reads.fastq --min-quality 10 --output filtered.fastq`
**Explanation:** Filters reads by minimum average quality score. Removes low-quality reads.