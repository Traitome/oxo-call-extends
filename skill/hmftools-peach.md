---
name: hmftools-peach
category: variant-calling
description: PEACH infers haplotypes for interpretation in a pharmacogenomic context.
tags: [hmftools-peach, pharmacogenomics, haplotype, diplotype, CYP450, drug-metabolism]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/peach/README.md"
---

## Concepts

- **Tool Overview**: PEACH (v2.0.0) infers pharmacogenomic haplotypes from genetic variants for clinical interpretation of drug metabolism. It identifies star alleles (e.g., CYP2D6*1, CYP2C19*2) and predicts phenotypes for key drug-metabolizing enzymes.

- **Star Allele Nomenclature**: PEACH uses the CPIC standard star allele nomenclature to report haplotypes. Each star allele (e.g., *1, *2, *3) corresponds to specific functional variants that affect enzyme activity.

- **Diplotype-to-Phenotype Prediction**: Converts inferred diplotypes into predicted metabolizer phenotypes using CPIC guidelines: Poor (PM), Intermediate (IM), Normal (NM), and Ultra-Rapid (UM) metabolizers.

- **Haplotype phasing**: Uses probabilistic phasing to determine which variants occur together on the same chromosome. Handles complex regions with homologous genes and copy number variations.

- **Coverage of Key Genes**: Focuses on clinically important pharmacogenes including CYP2D6, CYP2C19, CYP3A5, DPYD, TPMT, and others with established clinical guidelines.

- **Clinical Report Generation**: Produces structured reports linking inferred haplotypes to drug dosing recommendations. Integrates with electronic health records for clinical decision support.

## Pitfalls

- **Reference Haplotype Database**: PEACH requires current haplotype definition files matching the gene being analyzed. Using outdated allele definitions causes incorrect star allele assignment.

- **Copy Number Variation**: Gene duplications and deletions are common in CYP2D6 and other pharmacogenes. PEACH may miscall haplotypes in samples with CNVs without additional validation.

- **Pseudogene Interference**: Genes like CYP2D6 have pseudogene copies (CYP2D7, CYP2D8) that can cause alignment artifacts. Ensure reads map uniquely to the correct gene copy.

- **Novel Variants**: Variants not in the reference haplotype database are reported but may not affect star allele assignment. Novel variants of uncertain significance require manual interpretation.

- **Sample Quality**: Low coverage or high error rates in target regions reduce phasing accuracy. Minimum 50x coverage recommended for confident diplotype calls.

- **Platform-Specific Parameters**: Different sequencing platforms (WGS, targeted panel, SNP array) require different parameter settings. Adjust detection thresholds based on expected coverage.

## Examples

### Run PEACH on pharmacogenomics targets
**Args:** `peach -input variants.vcf -gene_panel pharmacogenomics_targets.tsv -ref_genome GRCh37_hmf -output peach_results.tsv`
**Explanation:** Standard PEACH run on pharmacogenomics gene panel. Infers diplotypes for all panel genes and generates phenotype predictions with drug dosing recommendations.

### Specify custom haplotype database
**Args:** `peach -input variants.vcf -gene_panel pharmacogenomics_targets.tsv -haplotype_db cpic_haplotypes.tsv -ref_genome GRCh37_hmf -output peach_results.tsv`
**Explanation:** Uses custom haplotype definition file instead of default. Useful for updated allele definitions or custom gene panels not in the default database.

### Process with sample-specific parameters
**Args:** `peach -input tumor1_variants.vcf -gene_panel pgx_panel.tsv -ref_genome GRCh37_hmf -min_coverage 30 -min_af 0.1 -output peach_results.tsv`
**Explanation:** Adjusts detection thresholds for lower quality samples. Reduces false positives from low-coverage or low-allelic-fraction variant calls.

### Run on GRCh38 reference
**Args:** `peach -input variants.vcf -gene_panel pharmacogenomics_targets.tsv -ref_genome GRCh38_hmf -output peach_results.tsv`
**Explanation:** Uses GRCh38 reference genome. Input VCF must be aligned to GRCh38. GRCh38 has improved gene annotations for some pharmacogenes.

### Generate clinical report
**Args:** `peach -input variants.vcf -gene_panel pharmacogenomics_targets.tsv -ref_genome GRCh37_hmf -output peach_results.tsv -report clinical`
**Explanation:** Generates enhanced clinical report with CPIC dosing guidelines. Includes specific drug recommendations based on predicted metabolizer phenotype.

### Multi-sample batch processing
**Args:** `peach -input batch_variants.vcf -gene_panel pharmacogenomics_targets.tsv -ref_genome GRCh37_hmf -output_dir ./peach_batch/`
**Explanation:** Processes multiple samples from a batch VCF. Each sample is analyzed independently with results written to separate output files.

### Enable CNV detection
**Args:** `peach -input variants.vcf -gene_panel pharmacogenomics_targets.tsv -ref_genome GRCh37_hmf -output peach_results.tsv -enable_cnv`
**Explanation:** Enables copy number variation detection for genes like CYP2D6. Identifies gene duplications and deletions that affect diplotype interpretation.
