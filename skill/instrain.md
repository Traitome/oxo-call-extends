---
name: instrain
category: metagenomics
description: Strain-level metagenomics analysis tool that profiles intra-population genetic diversity and compares populations in a microdiversity-aware manner.
tags: [instrain, metagenomics, strain-level, microdiversity, population-genetics]
author: oxo-call-community
source_url: "https://instrain.readthedocs.io/en/latest/"
---

## Concepts

- **Strain-level Analysis**: inStrain performs strain-level metagenomics analysis by mapping reads to reference genomes and calculating microdiversity metrics.
- **Microdiversity Profiling**: Quantifies intra-population genetic diversity including SNPs, nucleotide diversity, and linkage disequilibrium.
- **Population Comparison**: Compares strain profiles between samples to identify shared strains and population differences.
- **Genome-level Metrics**: Provides gene-level and genome-level metrics when provided with gene annotations and scaffold-to-bin mappings.
- **Read Quality Filtering**: Filters reads based on mapping quality, pair status, and ANI thresholds to ensure accurate analysis.

## Pitfalls

- **Reference Genome Selection**: Reference genomes must be closely related to the strains in the sample; distant references reduce mapping accuracy.
- **Mapping Artifacts**: Mismapped reads can produce false positive SNPs; use competitive mapping to multiple genomes.
- **Coverage Requirements**: Requires sufficient coverage (≥10x) for reliable microdiversity estimation.
- **Computational Resources**: Large datasets may require significant memory and processing time.
- **ANI Thresholds**: Minimum read ANI thresholds need adjustment based on expected genetic divergence.

## Examples

### Profile strain microdiversity
**Args:** `instrain profile -i mapped_reads.bam -g genome.fasta -o strain_profile`
**Explanation:** Analyzes microdiversity and generates strain profile metrics from mapped reads.

### Compare strains between samples
**Args:** `instrain compare -i profile1/ profile2/ -o strain_comparison`
**Explanation:** Compares strain profiles between two samples and calculates popANI and conANI.

### Profile with gene-level metrics
**Args:** `instrain profile -i mapped_reads.bam -g genome.fasta -f genes.fna -o gene_level_profile`
**Explanation:** Calculates gene-level microdiversity metrics using predicted genes.

### Genome-wide analysis with scaffold-to-bin
**Args:** `instrain genome_wide -i strain_profile/ -s scaffold_to_bin.tsv -o genome_wide_results`
**Explanation:** Aggregates metrics to genome level using scaffold-to-bin mapping file.

### Adjust minimum read ANI threshold
**Args:** `instrain profile -i mapped_reads.bam -g genome.fasta -o relaxed_profile -l 0.96`
**Explanation:** Uses a relaxed minimum read ANI threshold of 0.96 for more distant references.

### Generate visualization outputs
**Args:** `instrain profile -i mapped_reads.bam -g genome.fasta -o viz_profile --plot`
**Explanation:** Generates visualization plots of strain profiles and microdiversity patterns.