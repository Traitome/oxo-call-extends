---
name: cgat-scripts
category: genomics
description: Collection of scripts from the Computational Genomics Analysis Toolkit
tags: [cgat-scripts, genomics, toolkit, bioinformatics, scripts]
author: oxo-call-community
source_url: "https://www.cgat.org/downloads/public/cgat/documentation"
---

## Concepts

- **Tool Overview**: CGAT-Scripts is a collection of utility scripts from the Computational Genomics Analysis Toolkit.
- **Core Function**: Provides command-line scripts for various genomics analysis tasks.
- **Scripts**: Includes scripts for sequence manipulation, statistics, file conversion, and data analysis.
- **Input**: Various bioinformatics data formats.
- **Output**: Processed data and analysis results.
- **Application**: Genomics data processing and analysis pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda cgat-scripts`

## Pitfalls

- **Script Availability**: Not all scripts may be installed by default.
- **Dependency Management**: Some scripts may require additional dependencies.
- **Documentation**: Individual script documentation may vary.
- **Version Compatibility**: Script behavior may change between versions.

## Examples

### List available scripts
**Args:** `cgat-scripts --list`
**Explanation:** Lists all available CGAT scripts.

### Run specific script
**Args:** `cgat fastq2fasta --input reads.fastq --output reads.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Filter BAM file
**Args:** `cgat bam2bam --input alignments.bam --output filtered.bam --filter unmapped`
**Explanation:** Filters unmapped reads from BAM file.

### Display script help
**Args:** `cgat fastq2fasta --help`
**Explanation:** Shows help for specific script.