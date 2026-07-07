---
name: fraposa-pgsc
category: population-genomics
description: Tools to perform ancestry projection to a reference dataset within the calculator pipeline (pgsc_calc).
tags: [fraposa-pgsc, ancestry, population genomics, PGSC]
author: oxo-call-community
source_url: "https://github.com/PGScatalog/fraposa_pgsc"
---

## Concepts
- **Ancestry Projection**: Projects sample ancestry onto reference populations.
- **PGSC Integration**: Works within the Polygenic Score Catalog calculator pipeline.
- **Reference Dataset**: Uses predefined reference datasets for ancestry comparison.
- **PCA Analysis**: Uses principal component analysis for ancestry inference.
- **Population Matching**: Matches samples to known population groups.

## Pitfalls
- **Reference Bias**: Results depend on reference dataset composition.
- **Sample Quality**: Requires high-quality genotype data.
- **Computational Requirements**: PCA analysis is computationally intensive.
- **Interpretation**: Requires careful interpretation of ancestry results.
- **Dataset Compatibility**: Requires specific input format.

## Examples
### Project ancestry
**Args:** `fraposa-pgsc project --input genotypes.vcf --reference ref_panel/ --output ancestry.txt`
**Explanation:** Projects sample ancestry onto reference panel.

### Run PCA
**Args:** `fraposa-pgsc pca --input genotypes.vcf --output pca_results.txt`
**Explanation:** Performs PCA analysis on genotype data.

### Match to populations
**Args:** `fraposa-pgsc match --input ancestry.txt --populations populations.txt --output matches.txt`
**Explanation:** Matches samples to predefined population groups.

### Generate report
**Args:** `fraposa-pgsc report --input ancestry.txt --output report.pdf`
**Explanation:** Generates visual report of ancestry results.

### Quality control
**Args:** `fraposa-pgsc qc --input genotypes.vcf --output qc_report.txt`
**Explanation:** Performs quality control on input genotype data.