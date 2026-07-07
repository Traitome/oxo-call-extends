---
name: mutopia
category: variant-calling
description: Topographic modeling of mutational signatures across the cancer genome
tags: [mutopia, variant-calling, mutational-signatures, cancer, topographic, shap]
author: oxo-call-community
source_url: "https://github.com/sigscape/MuTopia"
---

## Concepts

- **Tool Overview**: MuTopia v1.0.6 (Mutational Topography) is a computational framework for analyzing mutational signatures across the cancer genome. It combines mutational signature decomposition with topographic modeling to understand how local genomic context influences signature activity.
- **Core Function**: Decomposes somatic mutations into constituent signatures (like those in the COSMIC database) and models how each signature's activity varies across genomic regions (topography). Uses SHAP (SHapley Additive exPlanations) values for interpretability.
- **Algorithm**: Employs non-negative matrix factorization (NMF) variants for signature extraction, combined with gradient boosting models to capture context-dependent signature activity. SHAP values provide per-mutation attribution to signatures.
- **Input Format**: Accepts somatic mutation VCF files (annotated with genomic context), pre-computed mutation matrices, or catalog files. Requires reference genome for context extraction.
- **Output**: Produces signature exposure profiles per sample, per-mutation VCF annotations with signature contributions, and topographic maps showing signature activity across genomic features.
- **Use Case**: Cancer genomics research, understanding mutational processes, identifying exposure sources (e.g., tobacco, UV, APOBEC), and studying how chromatin environment affects mutation rates.

## Pitfalls

- **Mutation Context**: MuTopia requires accurate mutation context (typically 96-channel context: 6 substitution types × 4 flanking bases each side). Ensure VCFs have proper annotation.
- **Reference Genome**: Uses reference genome for context extraction. Ensure consistency between VCF and reference build (GRCh37 vs GRCh38).
- **COSMIC Signatures**: While it can extract de novo signatures, comparing to COSMIC v3 signatures requires COSMIC database access.
- **Sample Size**: Signature decomposition works better with multiple samples. Single-sample analysis has limited statistical power.
- **Computational Resources**: NMF decomposition and SHAP calculations are computationally intensive for large mutation sets.
- **Interpretation**: SHAP values indicate signature contribution but don't directly reveal biological mechanisms. Further analysis needed for mechanistic insights.

## Examples

### Basic topographic modeling
**Args:** `-i mutations.vcf -g genome_dir -o output_dir`
**Explanation:** Runs MuTopia with mutation VCF and genome directory for context. Outputs signature decomposition and topographic analysis.

### Specify mutation context
**Args:** `-i variants.vcf -g hg38/ -o results/ -c 96`
**Explanation:** Sets mutation context size to 96 (6 substitution types × 4 flanking bases). The context is extracted from the genome using flanking bases.

### Analyze with known signatures
**Args:** `-i mutations.vcf --signatures COSMIC_v3 -o output/`
**Explanation:** Constrains decomposition to known COSMIC v3 signatures instead of de novo extraction. Produces exposures to established signatures.

### Generate per-mutation annotations
**Args:** `-i variants.vcf -g genome/ -o annotated/ --annotate`
**Explanation:** Outputs a new VCF with each mutation annotated by its signature contributions (SHAP values).

### Set SHAP background
**Args:** `-i mutations.vcf -g genome/ -o results/ --shap-background random`
**Explanation:** Uses random permutations as background for SHAP calculations. Default may be sufficient for most cases.
