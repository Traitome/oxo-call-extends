---
name: afwdist
category: population-genomics
description: Lightweight tool for calculating pairwise distance metrics based on fixed and non-fixed allele frequencies
tags: [allele-frequency, distance, pairwise, population-genetics, vipera]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/afwdist"
---

## Concepts

- **Tool Overview**: afwdist calculates pairwise distance metrics based on fixed and non-fixed allele frequencies, useful for comparing genetic variation between samples.
- **Core Function**: Computes a distance metric that accounts for both fixed and non-fixed alleles, providing nuanced comparison of genetic variation patterns.
- **Input/Output**: Input: CSV file with columns (sample, position, sequence, frequency) and FASTA reference. Output: CSV with pairwise distances between all sample pairs.
- **Mathematical Basis**: Implements the distance metric from Álvarez-Herrera & Sevilla et al. (2024), weighting fixed and non-fixed allele contributions differently.
- **Installation**: Install via bioconda: `conda install -c bioconda afwdist`

## Pitfalls

- **CSV Format**: Input CSV must have exact column names: 'sample', 'position', 'sequence', 'frequency'.
- **Reference Required**: FASTA reference file is mandatory - distances are computed relative to the reference.
- **Memory Scaling**: Pairwise distance calculation scales quadratically with sample count - large datasets may need significant memory.
- **Frequency Encoding**: Allele frequencies must be properly encoded as decimal values between 0 and 1.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available options and required parameters.

### Calculate pairwise distances
**Args:** `-i variants.csv -r reference.fasta -o distances.csv`
**Explanation:** Computes pairwise distance matrix from allele frequency data.

### Include reference as sample
**Args:** `-i variants.csv -r reference.fasta -o distances.csv -s`
**Explanation:** Includes reference sequence as a sample with 100% fixed alleles in the distance matrix.

### Verbose output for debugging
**Args:** `-i variants.csv -r reference.fasta -o distances.csv -v`
**Explanation:** Enables debug messages to track processing progress.

### Display version
**Args:** `-V`
**Explanation:** Shows the installed version of afwdist.

### Process large dataset
**Args:** `-i large_variants.csv -r ref.fasta -o dist.csv`
**Explanation:** Calculates distances for larger datasets; ensure sufficient memory for O(n²) pairwise computation.
