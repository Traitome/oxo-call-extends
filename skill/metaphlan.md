---
name: metaphlan
category: alignment
description: Metagenomic Phylogenetic Analysis.
tags: [metaphlan, alignment, metagenomics, profiling]
author: oxo-call-community
source_url: "https://github.com/biobakery/metaphlan"
---

## Concepts

- **Tool Overview**: MetaPhlAn v4.2.4 is the latest version of the computational tool for profiling microbial community composition from metagenomic shotgun sequencing data with species-level resolution.
- **Core Function**: Profiles microbial communities by identifying and quantifying taxa present in metagenomic samples using marker genes.
- **Species-level Resolution**: Provides taxonomic classification down to the species level with improved accuracy.
- **Strain Tracking**: Capable of identifying specific strains and tracking them across samples for all species.
- **Input/Output**: Accepts FASTQ sequencing reads or pre-computed alignments; outputs taxonomic profiles with abundance estimates.
- **Enhanced Database**: Uses an expanded marker gene database with improved taxonomic coverage.

## Pitfalls

- **Database Completeness**: Profiling accuracy depends on reference database completeness.
- **Host Contamination**: High host DNA content can affect profiling results.
- **Low Abundance Detection**: May miss organisms present at very low abundance.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **False Positives**: May produce false positive identifications with closely related species.
- **Memory Requirements**: Memory usage can be high for large input datasets.

## Examples

### Profile metagenomic sample
**Args:** `metaphlan input.fastq -o profile.txt`
**Explanation:** Profiles microbial community composition from metagenomic reads.

### Paired-end analysis
**Args:** `metaphlan input_1.fastq,input_2.fastq -o profile.txt`
**Explanation:** Processes paired-end sequencing data.

### Use pre-computed alignment
**Args:** `metaphlan --input_type bowtie2out alignment.sam -o profile.txt`
**Explanation:** Uses pre-computed Bowtie2 alignments as input.

### Output biom format
**Args:** `metaphlan input.fastq -o profile.biom --biom`
**Explanation:** Outputs profile in BIOM format for downstream analysis.

### Strain-level analysis
**Args:** `metaphlan input.fastq -o profile.txt --strain_profiling`
**Explanation:** Enables strain-level profiling for species identification.