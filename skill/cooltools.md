---
name: cooltools
category: epigenomics
description: Analysis tools for genomic interaction data in .cool format (Hi-C)
tags: [cooltools, hi-c, genomics, interaction, 3d, chromatin, tad, loops]
author: oxo-call-community
source_url: "https://github.com/open2c/cooltools"
---

## Concepts

- **Tool Overview**: Cooltools provides a suite of command-line tools for analyzing Hi-C and other genomic interaction data stored in .cool format.
- **Core Function**: Computes key Hi-C features including insulation scores, eigenvectors (compartments), expected contact frequencies, saddle plots, and pile-up analysis.
- **Input/Output**: Input: .cool or .mcool files (from cooler). Output: Various analysis results in TSV, NPZ, or image formats.
- **Key Analyses**: Insulation score (TAD boundaries), eigenvectors (A/B compartments), expected contacts, dots (loops), and saddle plots.
- **Integration**: Works seamlessly with cooler format. Part of the Open2C ecosystem for Hi-C analysis.
- **Genome Assembly**: Requires chromosome sizes file for the reference genome used in Hi-C mapping.

## Pitfalls

- **Balanced Data Required**: Most analyses require balanced (normalized) cool files. Run `cooler balance` first.
- **Resolution Selection**: Different analyses work best at different resolutions. TADs at 10kb, compartments at 100kb.
- **Memory Usage**: Whole-genome analyses at fine resolution can be memory-intensive. Use region-based queries for large genomes.
- **Expected Contacts**: Computing expected contacts is a prerequisite for many other analyses (dots, saddles).

## Examples

### Compute insulation score for TAD boundaries
**Args:** `insulation -r 10000 input.mcool::resolutions/10000 -o insulation.tsv`
**Explanation:** Computes insulation score at 10kb resolution to identify TAD boundaries.

### Compute eigenvectors for compartments
**Args:** `eigs-cis -r 100000 input.mcool::resolutions/100000 -o eigs.npz`
**Explanation:** Computes first eigenvectors (A/B compartment signal) at 100kb resolution.

### Compute expected contact frequency
**Args:** `expected-cis -r 10000 input.mcool::resolutions/10000 -o expected.tsv`
**Explanation:** Computes distance-dependent expected contact frequency for cis interactions.

### Call dots (loop calls)
**Args:** `dots -r 10000 input.mcool::resolutions/10000 -p 4 -o dots.tsv`
**Explanation:** Identifies significant looping interactions using 4 threads.

### Generate saddle plot
**Args:** `saddle -r 100000 input.mcool::resolutions/100000 eigs.npz -o saddle.npz`
**Explanation:** Generates saddle plot data for compartment analysis using pre-computed eigenvectors.

### Compute pile-up at specific regions
**Args:** `pileup -r 10000 input.mcool::resolutions/10000 features.bed -o pileup.npz`
**Explanation:** Computes average contact profile (pile-up) around specified genomic features.

### Compute coverage
**Args:** `coverage input.mcool::resolutions/10000 -o coverage.tsv`
**Explanation:** Computes coverage statistics for each chromosome in the cool file.

### Genome-wide contact statistics
**Args:** `info input.mcool::resolutions/10000`
**Explanation:** Displays statistics about the contact matrix including total reads, coverage, and balance weights.
