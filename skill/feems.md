---
name: feems
category: population-genomics
description: "Fast Estimation of Effective Migration Surfaces (FEEMS) + admixture (FEEMSmix)"
tags: [feems, population-genomics, migration, spatial-genetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/NovembreLab/feems"
---

## Concepts

- **Tool Overview**: FEEMS is a python package for inferring and visualizing gene-flow patterns in spatial population genetic data using effective migration surfaces.
- **Core Function**: Estimates effective migration rates across geographic space from genetic data.
- **Input/Output**: Input: Genetic data (VCF/plink), coordinates. Output: Migration surfaces, visualizations.
- **Algorithm**: Uses spatial statistical methods for migration estimation.
- **Key Features**: Fast migration estimation, spatial visualization, admixture analysis (FEEMSmix), geographic visualization, population genetics.
- **Installation**: `conda install -c bioconda feems`

## Pitfalls

- **Sample Density**: Requires sufficient geographic sampling.
- **Genetic Data Quality**: Requires high-quality genetic data.
- **Coordinate Data**: Requires accurate coordinate information.
- **Computational Complexity**: Large datasets may require significant resources.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic migration estimation
**Args:** `feems -i genotypes.vcf --coords coords.txt -o migration_results/`
**Explanation:** Estimates effective migration surface.

### With visualization
**Args:** `feems -i genotypes.vcf --coords coords.txt -o results/ --plot`
**Explanation:** Generates migration surface visualization.

### Admixture analysis
**Args:** `feemsmix -i genotypes.vcf --coords coords.txt -o admixture_results/`
**Explanation:** Performs admixture analysis.

### Multiple populations
**Args:** `feems -i genotypes.vcf --coords coords.txt -o results/ --pop popfile.txt`
**Explanation:** Analyzes multiple populations.

### Grid resolution
**Args:** `feems -i genotypes.vcf --coords coords.txt -o results/ --resolution 50`
**Explanation:** Sets migration surface grid resolution.