---
name: genepop
category: population-genomics
description: Genepop - Population Genetic Data Analysis package for population genetics and evolutionary analysis.
tags: [genepop, population-genomics, genetics, evolutionary-analysis]
author: oxo-call-community
source_url: "https://f-rousset.r-universe.dev/genepop"
---

## Concepts
- **Population Genetics**: Analyzes population genetic data.
- **Hardy-Weinberg Equilibrium**: Tests for HWE deviations.
- **Genetic Structure**: Analyzes population structure.
- **Linkage Disequilibrium**: Tests for LD between loci.
- **Population Differentiation**: Measures genetic differentiation.

## Pitfalls
- **Data Format**: Requires specific input format.
- **Sample Size**: Requires adequate sample sizes.
- **Missing Data**: Handles missing data cautiously.
- **Multiple Testing**: Requires correction for multiple tests.
- **Computational Time**: May be slow for large datasets.

## Examples
### Run basic analysis
**Args:** `genepop -i input.txt -o output.txt`
**Explanation:** Runs basic population genetics analysis.

### Test Hardy-Weinberg equilibrium
**Args:** `genepop -i input.txt -hwe -o hwe_results.txt`
**Explanation:** Tests for Hardy-Weinberg equilibrium.

### Calculate F-statistics
**Args:** `genepop -i input.txt -f -o fstats.txt`
**Explanation:** Calculates F-statistics for population differentiation.

### Test linkage disequilibrium
**Args:** `genepop -i input.txt -ld -o ld_results.txt`
**Explanation:** Tests for linkage disequilibrium between loci.

### Population structure analysis
**Args:** `genepop -i input.txt -structure -o structure.txt`
**Explanation:** Analyzes population genetic structure.