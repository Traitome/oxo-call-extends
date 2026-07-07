---
name: itbins
category: metagenomics
description: Superfast CLI tool for automated refinement of metagenome-assembled genomes (MAGs).
tags: [itbins, metagenomics, MAGs, binning]
author: oxo-call-community
source_url: "https://codeberg.org/JMK/itBins"
---

## Concepts

- **MAG Refinement**: Automatically refines metagenome-assembled genomes.
- **Contig Binning**: Groups contigs into genome bins based on composition and coverage.
- **Quality Improvement**: Improves the quality of existing genome bins.
- **Taxonomic Classification**: Assigns taxonomic labels to genome bins.
- **Fast Processing**: Optimized for rapid processing of large metagenomic datasets.
- **Multi-sample Support**: Handles multiple metagenomic samples simultaneously.

## Pitfalls

- **Assembly Quality**: Poor quality assemblies affect binning accuracy.
- **Coverage Bias**: Uneven coverage can lead to incorrect bin assignments.
- **Computational Resources**: Processing large datasets requires significant resources.
- **Memory Requirements**: Memory usage increases with dataset complexity.
- **Parameter Tuning**: Optimal parameters may vary between datasets.
- **Contig Length**: Very short contigs may be incorrectly binned.

## Examples

### Basic MAG refinement
**Args:** `itbins --contigs contigs.fasta --coverage coverage.txt --output refined_bins/`
**Explanation:** Refines metagenome-assembled genomes from contigs.

### With taxonomy
**Args:** `itbins --contigs contigs.fasta --coverage coverage.txt --taxonomy --output refined_bins/`
**Explanation:** Adds taxonomic classification to refined bins.

### Multiple samples
**Args:** `itbins --contigs contigs.fasta --coverage sample1.txt sample2.txt --output refined_bins/`
**Explanation:** Processes multiple samples for co-assembly binning.

### Quality filtering
**Args:** `itbins --contigs contigs.fasta --coverage coverage.txt --min-quality 50 --output refined_bins/`
**Explanation:** Filters bins based on quality metrics.

### Batch processing
**Args:** `itbins --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple datasets in batch mode.

### Generate statistics
**Args:** `itbins --contigs contigs.fasta --coverage coverage.txt --stats --output refined_bins/`
**Explanation:** Generates statistics about the binning process.