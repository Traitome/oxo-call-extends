---
name: hmftools-wisp
category: expression
description: WISP performs tumor fraction estimation for longitudinal samples such as ctDNA, using SNV, CNA, and LOH methods.
tags: [hmftools-wisp, tumor-fraction, ctDNA, MRD, longitudinal, cfDNA, minimal-residual-disease, cancer]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/wisp"
---

## Concepts

- **Tool Overview**: WISP (v1.2) estimates tumor fraction in longitudinal samples (typically ctDNA) guided by biomarkers identified in a primary tumor biopsy from the same patient. It uses three independent methods—SNV/allele frequency, copy number alteration (CNA), and loss of heterozygosity (LOH)—to provide a comprehensive tumor fraction estimate for minimal residual disease (MRD) detection.

- **SNV-Based Tumor Fraction Estimation**: WISP filters somatic SNVs from the primary tumor biopsy and evaluates their variant allele frequencies (VAF) in the cfDNA sample. It applies strict filters: mappability ≥0.5, repeat count <4, not subclonal, adequate depth, and sufficient base quality. The tumor fraction is calculated using the formula: TF = 2×adjVAF / (WA_VCN + 2×adjVAF - WA_CN×adjVAF), where adjVAF accounts for sequencing noise.

- **Clonality Adjustment Methods**: WISP uses two methods to adjust for clonality differences between primary tumor and cfDNA. The VAF_PEAK method uses kernel density estimation to find a TF peak higher than the raw estimate when depth >20 and sufficient fragment support exists. The LOW_COUNT method estimates dropout rate when depth is limited by analyzing the ratio of 1-fragment vs >1-fragment support sites.

- **CNA-Based Tumor Fraction (WGS only)**: For WGS cfDNA samples, WISP compares tumor GC ratios from cfDNA to copy number segments in the primary tumor. It filters for segments with integer copy numbers (0-6) and performs weighted regression to find the purity that best fits the observed pattern. The CNA method has a limit of detection based on aneuploidy score and clonal proportion.

- **LOH-Based Tumor Fraction (WGS only)**: WISP uses high-confidence heterozygous BAF sites in LOH regions from the primary tumor. It calculates allele frequencies at LOH sites in cfDNA and derives implied tumor fraction. The method detects whether a subset of LOH regions has significantly higher TF, indicating subclonal LOH in the primary.

- **Minimal Residual Disease Detection**: WISP reports MRD status (TRUE/FALSE) for both SNV and LOH methods based on whether the observed tumor fraction exceeds the limit of detection (LOD) at 99% confidence. MRD detection sensitivity depends on sequencing depth, number of informative variants, and tumor aneuploidy.

## Pitfalls

- **Primary Tumor Dependency**: WISP requires prior analysis of the primary tumor sample through the HMF pipeline (PURPLE, AMBER, COBALT, SAGE). Without these outputs, WISP cannot estimate tumor fraction. Ensure all primary tumor pipeline outputs are available before running WISP.

- **Targeted vs WGS Limitations**: The CNA and LOH methods only work with WGS data, not targeted sequencing. For targeted panels, only the SNV-based TF estimation is available. Choose the appropriate sample type for your analysis goals.

- **Low Tumor Purity Samples**: Samples with very low tumor fraction (<0.5%) may be below the limit of detection for all methods. The LOD_CNA formula is: 0.4% / sqrt(aneuploidy_score) / clonalProportion^3, which can be quite high for low-aneuploidy tumors.

- **Subclonal Copy Number Changes**: The CNA method excludes non-integer copy numbers and high-copy regions (like ecDNA) as these are volatile during tumor evolution. This can reduce the number of informative segments and increase uncertainty in the estimate.

- ** CHIP Contamination**: Clonal hematopoiesis of indeterminate potential (CHIP) can cause false-positive MRD signals. WISP attempts to filter outliers but CHIP variants may still affect accuracy, especially in older patients.

- **Multiple Longitudinal Samples**: WISP accepts multiple sample IDs separated by semicolons, but all samples share the same primary tumor. For studies with multiple timepoints from different primaries, run WISP separately for each primary-sample pair.

## Examples

### Run WISP with all HMF pipeline outputs
**Args:** `java -jar wisp.jar -patient_id P001 -tumor_id TUMOR1 -samples TUMOR1_BLOOD1 -purple_dir ./purple/ -amber_dir ./amber/ -cobalt_dir ./cobalt/ -somatic_vcf ./sage/TUMOR1.purple.somatic.vcf.gz -bqr_dir ./sage/ -ref_genome /reference/GRCh37_hmf.fa -ref_genome_version 37 -output_dir ./wisp/`
**Explanation:** Standard WISP run with complete HMF pipeline outputs. Estimates tumor fraction in a cfDNA sample using SNV, CNA, and LOH methods. Produces summary output with MRD status and confidence intervals.

### Process multiple longitudinal samples
**Args:** `java -jar wisp.jar -patient_id P001 -tumor_id TUMOR1 -samples "TUMOR1_BLOOD1;TUMOR1_BLOOD2;TUMOR1_BLOOD3" -purple_dir ./purple/ -amber_dir ./amber/ -cobalt_dir ./cobalt/ -somatic_vcf ./sage/TUMOR1.purple.somatic.vcf.gz -bqr_dir ./sage/ -ref_genome /reference/GRCh37_hmf.fa -ref_genome_version 37 -output_dir ./wisp_multi/`
**Explanation:** Processes three longitudinal ctDNA samples from the same patient in a single run. All samples are compared against the same primary tumor. Useful for tracking tumor fraction changes over time during treatment.

### Targeted panel mode (SNV only)
**Args:** `java -jar wisp.jar -patient_id P001 -tumor_id TUMOR1 -samples TUMOR1_CTDNA -purple_dir ./purple/ -amber_dir ./amber/ -cobalt_dir ./cobalt/ -somatic_vcf ./sage/TUMOR1.purple.somatic.vcf.gz -bqr_dir ./sage/ -ref_genome /reference/GRCh37_hmf.fa -ref_genome_version 37 -output_dir ./wisp_panel/`
**Explanation:** Runs WISP in targeted sequencing mode. Only SNV-based TF estimation will be available since CNA and LOH methods require WGS data. Uses the same somatic VCF from the primary tumor panel analysis.

### GRCh38 reference
**Args:** `java -jar wisp.jar -patient_id P001 -tumor_id TUMOR1 -samples TUMOR1_BLOOD1 -purple_dir ./purple_grch38/ -amber_dir ./amber_grch38/ -cobalt_dir ./cobalt_grch38/ -somatic_vcf ./sage/TUMOR1.purple.somatic.vcf.gz -bqr_dir ./sage_grch38/ -ref_genome /reference/GRCh38.fa -ref_genome_version 38 -output_dir ./wisp_grch38/`
**Explanation:** Runs WISP with GRCh38 reference build. Ensure all input directories (purple, amber, cobalt, sage) were generated from GRCh38-aligned data for consistent coordinates.

### Interpret WISP summary output
**Args:** `cat ./wisp_multi/wisp_summary.tsv | grep -E "SampleId|SNVPurity|LOHPurity|SNV_MRD|LOH_MRD"`
**Explanation:** Extracts key fields from WISP summary for multiple samples. Shows SNV and LOH tumor fraction estimates along with MRD detection status for longitudinal monitoring.

### Calculate tumor fraction change between timepoints
**Args:** `python3 -c "tf1=0.023; tf2=0.012; change=(tf1-tf2)/tf1*100; print(f'Tumor fraction change: {change:.1f}% (decreased)')"`
**Explanation:** Example calculation showing how to compute relative change in tumor fraction between two timepoints. A decrease indicates treatment response; an increase suggests disease progression.

### Check MRD status from output
**Args:** `awk -F'\t' 'NR==1 || $13=="TRUE"' ./wisp/wisp_summary.tsv | head -10`
**Explanation:** Filters summary output for samples with MRD detected (SNV_MRD = TRUE). The 13th column corresponds to SNV_MRD status. TRUE indicates tumor-derived DNA detected above the limit of detection.
