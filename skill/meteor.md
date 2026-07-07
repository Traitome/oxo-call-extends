---
name: meteor
category: annotation
description: Meteor is a plateform for quantitative metagenomics profiling of complex ecosystems.
tags: [meteor, annotation, metagenomics]
author: oxo-call-community
source_url: "https://github.com/metagenopolis/meteor"
---

## Concepts

- **Tool Overview**: Meteor v2.0.22 is a platform for quantitative metagenomics profiling of complex ecosystems, enabling species-level taxonomic profiling and functional analysis.
- **Core Function**: Performs quantitative metagenomic profiling of complex microbial communities.
- **Taxonomic Profiling**: Provides species-level taxonomic profiling for Bacteria, Archaea, and Eukaryotes.
- **Functional Analysis**: Analyzes functional potential of microbial communities.
- **Strain-level Analysis**: Enables strain-level population structure inference.
- **Input/Output**: Accepts sequencing reads; outputs taxonomic and functional profiles.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Analysis of complex metagenomes can be time-consuming.
- **Database Completeness**: Profiling accuracy depends on gene catalogue completeness.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input read quality.

## Examples

### Run metagenomic profiling
**Args:** `meteor -i reads.fastq -o profile.txt`
**Explanation:** Performs quantitative metagenomic profiling.

### With custom gene catalogue
**Args:** `meteor -i reads.fastq -d catalogue/ -o profile.txt`
**Explanation:** Uses custom gene catalogue for profiling.

### Paired-end analysis
**Args:** `meteor -i reads_1.fastq -r reads_2.fastq -o profile.txt`
**Explanation:** Processes paired-end sequencing data.

### Functional analysis
**Args:** `meteor -i reads.fastq -o profile.txt -f`
**Explanation:** Performs functional analysis alongside taxonomic profiling.

### Batch processing
**Args:** `meteor -i fastq/ -o profiles/`
**Explanation:** Processes multiple samples in batch mode.