---
name: metawepp
category: alignment
description: "metaWEPP: Improving resolution of metagenomic analysis using WEPP"
tags: [metawepp, alignment, metagenomics, haplotype]
author: oxo-call-community
source_url: "https://github.com/TurakhiaLab/metaWEPP"
---
## Concepts

- **Tool Overview**: metaWEPP v0.1.0 extends species-level resolution of metagenomic tools by providing near-haplotype detection and abundance estimation for multi-species samples.
- **Core Function**: Improves metagenomic analysis resolution using the WEPP (Wastewater-Based Epidemiology using Phylogenetic Placements) pipeline.
- **Haplotype Detection**: Identifies near-haplotype level variants within metagenomic samples.
- **Phylogenetic Placement**: Performs parsimonious read placement on species-specific mutation-annotated trees (MATs).
- **Unaccounted Alleles**: Flags mutations observed in samples but unexplained by known haplotypes, potentially indicating novel variants.
- **Interactive Dashboard**: Includes visualization tools for exploring identified haplotypes within global phylogenies.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Analysis of complex metagenomes can be time-consuming.
- **Reference Database**: Analysis quality depends on reference database completeness.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis accuracy depends on input read quality.

## Examples

### Run haplotype detection
**Args:** `metawepp -i reads.fastq -o results/`
**Explanation:** Detects haplotypes and estimates abundance in metagenomic reads.

### With reference database
**Args:** `metawepp -i reads.fastq -d reference/ -o results/`
**Explanation:** Uses custom reference database for analysis.

### Generate visualization
**Args:** `metawepp -i reads.fastq -o results/ --visualize`
**Explanation:** Generates interactive visualization dashboard.

### Flag unaccounted alleles
**Args:** `metawepp -i reads.fastq -o results/ --flag-alleles`
**Explanation:** Identifies unaccounted alleles potentially indicating novel variants.

### Batch processing
**Args:** `metawepp -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.