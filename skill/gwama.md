---
name: gwama
category: bioinformatics
description: GWAMA (Genome-Wide Association Meta Analysis) performs meta-analysis of GWAS summary statistics.
tags: [gwama, GWAS, meta-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://www.geenivaramu.ee/en/tools/gwama"
---

## Concepts

- **GWAS Meta-Analysis**: GWAMA combines results from multiple GWAS studies.

- **Summary Statistics**: Analyzes summary statistics from genome-wide association studies.

- **Fixed Effects**: Supports fixed-effects meta-analysis models.

- **Random Effects**: Supports random-effects meta-analysis models.

- **Heterogeneity Testing**: Tests for heterogeneity across studies.

- **Publication Bias**: Evaluates potential publication bias.

## Pitfalls

- **Study Quality**: Results depend on the quality of input studies.

- **Population Stratification**: Account for population differences.

- **Sample Overlap**: Be cautious of sample overlap between studies.

- **Effect Size Heterogeneity**: Heterogeneous effects may complicate interpretation.

- **Multiple Testing**: Correct for multiple hypothesis testing.

## Examples

### Run meta-analysis
**Args:** `gwama -input input.txt -output results.txt`
**Explanation:** Performs GWAS meta-analysis.

### Fixed effects model
**Args:** `gwama -input input.txt -model fixed -output results.txt`
**Explanation:** Uses fixed-effects meta-analysis model.

### Random effects model
**Args:** `gwama -input input.txt -model random -output results.txt`
**Explanation:** Uses random-effects meta-analysis model.

### Include heterogeneity test
**Args:** `gwama -input input.txt -heterogeneity -output results.txt`
**Explanation:** Performs heterogeneity testing.

### Forest plot
**Args:** `gwama -input input.txt -forest -o forest.pdf`
**Explanation:** Generates forest plot of results.

### Publication bias test
**Args:** `gwama -input input.txt -egger -output results.txt`
**Explanation:** Performs Egger's test for publication bias.

### Help command
**Args:** `gwama --help`
**Explanation:** Shows available options and usage information.