---
name: alder
category: population-genomics
description: Computes weighted linkage disequilibrium statistics for inferring population admixture history
tags: [admixture, linkage-disequilibrium, population-genetics, ld, ancestry]
author: oxo-call-community
source_url: "http://cb.csail.mit.edu/cb/alder/"
---

## Concepts

- **Tool Overview**: ALDER computes weighted linkage disequilibrium (LD) statistics to detect and date population admixture events.
- **Core Function**: Analyzes LD decay as a function of genetic distance to infer admixture timing and mixture proportions between populations.
- **Input/Output**: Input: Genotype data in EIGENSTRAT format. Output: Admixture date estimates, mixture proportions, and LD decay curves.
- **Method**: Uses weighted LD to distinguish admixture LD from background LD, providing robust admixture inference.
- **Installation**: Install via bioconda: `conda install -c bioconda alder`

## Pitfalls

- **Reference Populations**: Requires appropriate reference populations for accurate admixture inference.
- **SNP Ascertainment**: Results sensitive to SNP ascertainment bias - use consistent SNP sets.
- **Genetic Map**: Requires genetic map for accurate distance-based LD decay analysis.
- **Single Admixture Model**: Assumes single admixture event - complex histories may not be captured.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and input format requirements.

### Basic admixture analysis
**Args:** `alder parfile.txt`
**Explanation:** Runs ALDER with parameters specified in parameter file.

### Analyze with specific test population
**Args:** `alder -p test_pop:ref1:ref2 parfile.txt`
**Explanation:** Tests admixture in test_pop using ref1 and ref2 as source populations.

### Set minimum genetic distance
**Args:** `alder -d 0.5cM parfile.txt`
**Explanation:** Uses minimum genetic distance of 0.5cM for LD curve fitting.

### Output LD decay curve
**Args:** `alder -o ld_curve.txt parfile.txt`
**Explanation:** Outputs LD decay curve data for visualization.

### Specify number of Jackknife blocks
**Args:** `alder -j 100 parfile.txt`
**Explanation:** Uses 100 blocks for Jackknife standard error estimation.

### Run with custom genetic map
**Args:** `alder -m genetic_map.txt parfile.txt`
**Explanation:** Uses custom genetic map for distance calculations.
