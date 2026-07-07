---
name: hmftools-cuppa
category: utility
description: Predict tissue of origin for tumor samples using DNA and RNA sequencing data from WGTS analysis.
tags: [hmftools-cuppa, tissue of origin, cancer of unknown primary, CUP, machine learning, WGTS]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/cuppa/README.md"
---

## Concepts

- **Tool Overview**: hmftools-cuppa (v2.4) is a machine learning-based tissue of origin (TOO) prediction tool that classifies tumors into 36 defined cancer classes using whole genome and transcriptome sequencing (WGTS) data.
- **Multi-modal Classification**: CUPPA combines DNA-based features (mutational signatures, driver mutations) with RNA expression data for independent and combined DNA+RNA predictions.
- **Cancer of Unknown Primary (CUP)**: Designed for CUP cases where metastatic tumors cannot be identified through standard pathology, providing molecular classification to guide treatment decisions.
- **Machine Learning Approach**: Uses orthogonal DNA features from WGS to train classifiers that recognize cancer-type specific mutational patterns across the genome.
- **Clinical Utility**: Shows 77% TOO prediction accuracy in CUP patients using WGTS, significantly improving over panel testing (62%) and informing treatment options in 79% of cases.
- **WiGiTS Integration**: Part of Hartwig Medical Foundation's WiGiTS pipeline, used alongside other tools for comprehensive tumor molecular profiling.

## Pitfalls

- **Input Data Quality**: Requires high-quality WGS and RNA-seq data; low coverage or degraded samples (e.g., FFPE) may reduce prediction accuracy.
- **Cancer Type Limitations**: Some cancer types share similar mutational profiles and may be difficult to distinguish; prediction confidence varies by cancer class.
- **Reference Data Dependency**: Performance depends on having representative training data for all cancer types; rare tumors may have lower accuracy.
- **Ambiguous Predictions**: When multiple cancer types have similar probabilities, the tool may report low-confidence predictions requiring clinical interpretation.
- **WGTS Requirement**: Optimal performance requires both WGS and RNA-seq (WGTS mode); DNA-only predictions are less accurate than combined DNA+RNA.

## Examples

### Run CUPPA with DNA and RNA combined prediction
**Args:** `cuppa -sample_id patient1 -dna_dir ./wgs_results -rna_dir ./rnaseq_results -output_dir ./cuppa/ -ref_genome GRCh37_hmf`
**Explanation:** Runs CUPPA with both DNA and RNA-seq data for combined tissue of origin prediction. The DNA directory should contain SAGE variant calls and CHORD HRD scores.

### Run DNA-only CUPPA prediction
**Args:** `cuppa -sample_id tumor1 -dna_dir ./wgs_output -output_dir ./cuppa_dna -ref_genome GRCh38_hmf -dna_only`
**Explanation:** Performs tissue prediction using only DNA features when RNA-seq is not available. DNA-only mode relies on mutational signatures and driver mutations.

### Generate CUPPA visualization plot
**Args:** `cuppa -sample_id sample1 -dna_dir ./dna -rna_dir ./rna -output_dir ./output -plot -ref_genome GRCh37`
**Explanation:** Produces a visualization showing prediction probabilities for each cancer class. The plot helps interpret the confidence of each prediction.

### Process multiple CUP samples in batch
**Args:** `for dir in cup_samples/*/; do sample=$(basename $dir); cuppa -sample_id $sample -dna_dir $dir/dna -output_dir ./cuppa_results/$sample -ref_genome GRCh37_hmf; done`
**Explanation:** Iterates through multiple CUP sample directories and runs CUPPA for each. Useful for cohort analysis.

### CUPPA with explicit cancer class list
**Args:** `cuppa -sample_id test -dna_dir ./dna -output_dir ./output -ref_genome GRCh37 -cancer_classes breast,lung,colorectal,prostate`
**Explanation:** Restricts prediction to specific cancer classes of interest. Useful when clinical evidence suggests certain tissue origins.

### Run CUPPA with PURPLE and LINX integration
**Args:** `cuppa -sample_id patient1 -dna_dir ./wgs -purple_dir ./purple -linx_dir ./linx -output_dir ./cuppa -ref_genome GRCh38_hmf`
**Explanation:** Uses PURPLE (purity/ploidy) and LINX (SV annotations) outputs as additional features for improved tissue prediction. These provide copy number context.
