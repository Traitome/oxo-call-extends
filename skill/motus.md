---
name: motus
category: metagenomics
description: Marker gene-based OTU (mOTU) profiling
tags: [motus, metagenomics, profiling]
author: oxo-call-community
source_url: "http://motus-tool.org/"
---

## Concepts

- **Tool Overview**: mOTUs v4.0.4 performs marker gene-based OTU profiling.
- **Core Function**: Profiles microbial communities using marker genes.
- **Marker Genes**: Uses conserved single-copy marker genes.
- **Taxonomic Profiling**: Assigns taxonomy to sequencing reads.
- **Quantification**: Estimates relative abundance of taxa.
- **Input/Output**: Accepts sequencing reads; outputs taxonomic profiles.

## Pitfalls

- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for profiling.
- **Data Quality**: Results depend on sequencing quality.
- **Reference Database**: Requires marker gene database.
- **Computational Resources**: Large datasets may require significant resources.
- **Version Compatibility**: Some options may vary between versions.

## Examples

### Profile metagenome
**Args:** `motus profile -i reads.fastq -o profile.txt`
**Explanation:** Performs mOTU profiling on metagenomic reads.

### With paired-end reads
**Args:** `motus profile -i reads_1.fastq reads_2.fastq -o profile.txt`
**Explanation:** Processes paired-end sequencing data.

### Build database
**Args:** `motus build -d database/ -o custom_db`
**Explanation:** Builds custom marker gene database.

### Update database
**Args:** `motus update`
**Explanation:** Updates mOTU database.

### Merge profiles
**Args:** `motus merge -i profiles/ -o merged_profile.txt`
**Explanation:** Merges multiple profiles into one.