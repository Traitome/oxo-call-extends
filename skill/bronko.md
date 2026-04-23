---
name: bronko
category: variant-calling
description: Ultra-rapid mapping free variant caller for viral amplicon sequencing
tags: [bronko, viral, amplicon, variant-calling, mapping-free]
author: oxo-call-community
source_url: "https://github.com/treangenlab/bronko"
---

## Concepts

- **Tool Overview**: BRONKO is an ultra-rapid mapping-free variant caller for viral amplicon sequencing.
- **Core Function**: Calls variants from viral amplicon data without traditional read mapping.
- **Algorithm**: K-mer based approach for rapid variant detection.
- **Input**: FASTQ reads and reference sequence.
- **Output**: Variant calls with frequency estimates.
- **Application**: Rapid viral variant calling for surveillance.
- **Installation**: Install via bioconda: `conda install -c bioconda bronko`

## Pitfalls

- **Amplicon Data**: Designed for amplicon sequencing; not for whole-genome data.
- **Viral Genomes**: Optimized for small viral genomes.
- **Reference Required**: Must provide reference sequence for variant calling.

## Examples

### Call viral variants
**Args:** `bronko -r reference.fa -i reads.fq -o variants.vcf`
**Explanation:** Calls variants from viral amplicon sequencing data.

### Set minimum frequency
**Args:** `bronko -r reference.fa -i reads.fq -f 0.01 -o variants.vcf`
**Explanation:** Reports variants with minimum 1% frequency.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
