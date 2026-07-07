---
name: metaphlan2
category: alignment
description: Metagenomic Phylogenetic Analysis
tags: [metaphlan2, alignment, metagenomics, profiling]
author: oxo-call-community
source_url: "https://bitbucket.org/biobakery/metaphlan2"
---

## Concepts

- **Tool Overview**: MetaPhlAn2 v2.96.1 is a computational tool for profiling the composition of microbial communities from metagenomic shotgun sequencing data with species-level resolution.
- **Core Function**: Profiles microbial communities by identifying and quantifying taxa present in metagenomic samples.
- **Species-level Resolution**: Provides taxonomic classification down to the species level.
- **Strain Tracking**: Capable of identifying specific strains and tracking them across samples.
- **Input/Output**: Accepts FASTQ sequencing reads or pre-computed alignments; outputs taxonomic profiles with abundance estimates.
- **Database Integration**: Uses a comprehensive marker gene database for accurate taxonomic assignments.

## Pitfalls

- **Database Completeness**: Profiling accuracy depends on reference database completeness.
- **Host Contamination**: High host DNA content can affect profiling results.
- **Low Abundance Detection**: May miss organisms present at very low abundance.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **False Positives**: May produce false positive identifications with closely related species.
- **Memory Requirements**: Memory usage can be high for large input datasets.

## Examples

### Profile metagenomic sample
**Args:** `metaphlan2.py input.fastq -o profile.txt`
**Explanation:** Profiles microbial community composition from metagenomic reads.

### Paired-end analysis
**Args:** `metaphlan2.py input_1.fastq,input_2.fastq -o profile.txt`
**Explanation:** Processes paired-end sequencing data.

### Use pre-computed alignment
**Args:** `metaphlan2.py --input_type bowtie2out alignment.sam -o profile.txt`
**Explanation:** Uses pre-computed Bowtie2 alignments as input.

### Output biom format
**Args:** `metaphlan2.py input.fastq -o profile.biom --biom`
**Explanation:** Outputs profile in BIOM format for downstream analysis.

### Strain-level analysis
**Args:** `metaphlan2.py input.fastq -o profile.txt --strain_profiling`
**Explanation:** Enables strain-level profiling for species identification.