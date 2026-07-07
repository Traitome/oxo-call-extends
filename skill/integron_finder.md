---
name: integron_finder
category: annotation
description: Integron Finder detects integrons in DNA sequences using covariance models for attC sites and HMM profiles for integron-integrases.
tags: [integron_finder, annotation, integron-detection, antibiotic-resistance]
author: oxo-call-community
source_url: "https://integronfinder.readthedocs.io/en/latest"
---

## Concepts

- **Integron Detection**: Identifies integrons in bacterial genomes using multiple computational approaches.
- **attC Site Detection**: Uses covariance models to detect attC recombination sites.
- **Integrase Detection**: Uses HMM profiles to identify integron-integrase genes (intI).
- **Cassette Arrays**: Identifies gene cassette arrays within integrons.
- **Promoter and attI Site Detection**: Uses pattern matching for promoter and attI site identification.

## Pitfalls

- **False Positives**: May detect partial integrons or degenerated attC sites.
- **Sequence Quality**: Requires high-quality sequence data for reliable detection.
- **Computational Time**: Comprehensive analysis can be time-consuming for large genomes.
- **Parameter Sensitivity**: Detection thresholds may need adjustment for specific organisms.
- **Output Interpretation**: Results require biological interpretation of integron structures.

## Examples

### Basic integron detection
**Args:** `integron_finder my_sequences.fasta -o Results_Integron_Finder`
**Explanation:** Detects integrons in input sequences with default parameters.

### Detect CALIN elements
**Args:** `integron_finder sequences.fasta -o calin_results --calin`
**Explanation:** Enables detection of CALIN (Clusters of AttC sites Lacking INtegrase) elements.

### Search for promoter and attI sites
**Args:** `integron_finder genome.fasta -o detailed_results --promoter --atti`
**Explanation:** Searches for promoter sequences and attI integration sites.

### Parallel processing
**Args:** `integron_finder multi_fasta.fasta -o parallel_results --cpu 4`
**Explanation:** Uses 4 CPU cores for parallel processing.

### Keep intermediate results
**Args:** `integron_finder sequences.fasta -o full_results --keep-tmp`
**Explanation:** Retains intermediate files for debugging and further analysis.

### Custom attC evalue threshold
**Args:** `integron_finder sequences.fasta -o custom_results --attc-evalue 1e-5`
**Explanation:** Sets custom E-value threshold for attC site detection.