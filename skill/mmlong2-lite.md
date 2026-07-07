---
name: mmlong2-lite
category: utility
description: Lightweight workflow for microbial genome recovery using either Nanopore or PacBio HiFi reads
tags: [mmlong2-lite, utility, assembly]
author: oxo-call-community
source_url: "https://github.com/Serka-M/mmlong2-lite"
---

## Concepts

- **Tool Overview**: mmlong2-lite v1.2.1 is a lightweight workflow for microbial genome recovery.
- **Core Function**: Recovers microbial genomes from long-read sequencing data.
- **Long-read Support**: Works with Nanopore and PacBio HiFi reads.
- **Lightweight Design**: Optimized for efficiency.
- **Input/Output**: Accepts raw reads; outputs assembled genomes.
- **Microbial Genomics**: Focused on microbial genome assembly.

## Pitfalls

- **Long-read Specific**: Designed for long-read sequencing data.
- **Computational Resources**: Assembly may require significant resources.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Results depend on read quality.
- **Microbial Focus**: Optimized for microbial genomes.

## Examples

### Run genome recovery
**Args:** `mmlong2-lite -i reads.fastq -o assembly/`
**Explanation:** Runs microbial genome recovery workflow.

### With Nanopore reads
**Args:** `mmlong2-lite -i reads.fastq -t nanopore -o assembly/`
**Explanation:** Optimized for Nanopore data.

### With PacBio HiFi reads
**Args:** `mmlong2-lite -i reads.fastq -t pacbio-hifi -o assembly/`
**Explanation:** Optimized for PacBio HiFi data.

### With quality filtering
**Args:** `mmlong2-lite -i reads.fastq -q -o assembly/`
**Explanation:** Applies quality filtering.

### Batch processing
**Args:** `mmlong2-lite -i fastq/ -o assemblies/`
**Explanation:** Processes multiple read files.