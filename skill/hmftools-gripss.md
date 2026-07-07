---
name: hmftools-gripss
category: qc
description: Filter and post-process GRIDSS somatic structural variant calls to produce high-confidence SV sets.
tags: [hmftools-gripss, structural variants, GRIDSS, somatic mutation, filtering, cancer]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/gripss"
---

## Concepts

- **Tool Overview**: hmftools-gripss (v2.4) applies filtering and post-processing steps to GRIDSS paired tumor-normal structural variant output to produce high-confidence somatic SV calls.
- **GRIDSS Foundation**: Built on GRIDSS (Genomic Rearrangement IDentification Software Suite) which uses breakend assembly and split-read evidence for SV detection.
- **Somatic Filtering Strategy**: Filters germline variants, artifacts, and low-confidence calls using multiple evidence metrics including read support, allelic fraction, and breakpoint characteristics.
- **Paired Tumor-Normal Design**: Requires both tumor and matched normal BAM files to distinguish somatic variants from inherited structural variants.
- **Confidence Classification**: Classifies SVs into high-confidence and low-confidence sets based on breakend coverage (>8 fragments in normal) and allelic fraction (>0.01) thresholds.
- **Clinical Application**: Produces actionable somatic SV calls for cancer genomics including gene fusions, deletions, and translocations relevant for therapy selection.

## Pitfalls

- **CRITICAL: GRIDSS Prerequisite**: Must run GRIDSS first to generate raw SV calls; GRIPSS will fail without proper GRIDSS output files.
- **Normal Contamination Threshold**: Variants with >3% normal read support are hard-filtered; low-purity tumors may have borderline calls.
- **Breakpoint Size Limitations**: Deletions/duplications under 1000bp with split read support in normal are filtered; small SVs may be missed.
- **Reference Genome Consistency**: GRIDSS and GRIPSS must use the same reference genome version; mixed versions cause coordinate mismatches.
- **BAM Coordinate Sorting**: Both tumor and normal BAMs must be coordinate-sorted; query-name sorted BAMs produce incorrect results.

## Examples

### Run GRIPSS on GRIDSS output
**Args:** `gripss -sample_id tumor1 -tumor tumor.bam -normal normal.bam -gridss_vcf gridss_output.vcf -ref_genome GRCh37_hmf -output_dir ./gripss/`
**Explanation:** Runs GRIPSS filtering on GRIDSS VCF output. Produces high-confidence somatic SV VCF and low-confidence VCF for review.

### Standard GRIPSS with paired tumor-normal
**Args:** `gripss -sample_id sample1 -tumor tumor.bam -normal normal.bam -ref_genome GRCh38 -output_dir ./gripss_output`
**Explanation:** Standard GRIPSS workflow requiring tumor-normal BAM pair and GRIDSS VCF. Outputs somatic SV calls with annotation.

### Generate GRIPSS visualization files
**Args:** `gripss -sample_id test -tumor tumor.bam -normal normal.bam -gridss_vcf gridss.vcf -ref_genome GRCh37 -output_dir ./gripss -write_plot`
**Explanation:** Produces visualization plots showing SV distribution, size profiles, and gene annotations for manual review.

### Batch process multiple samples
**Args:** `for vcf in gridss_results/*.vcf; do sample=$(basename $vcf .vcf); gripss -sample_id $sample -tumor ${sample}.bam -normal normal.bam -gridss_vcf $vcf -ref_genome GRCh37_hmf -output_dir ./gripss/$sample; done`
**Explanation:** Iterates through GRIDSS VCF files and runs GRIPSS for each sample. Assumes matching BAM files exist.

### GRIPSS with custom filter parameters
**Args:** `gripss -sample_id custom -tumor tumor.bam -normal normal.bam -gridss_vcf gridss.vcf -ref_genome GRCh38 -output_dir ./output -min_breakend_support 10 -min_allelic_fraction 0.02`
**Explanation:** Runs GRIPSS with stricter filtering thresholds (10 reads minimum breakend support, 2% minimum allelic fraction) for high-stringency analysis.

### Combine GRIPSS with LINX for annotation
**Args:** `gripss -sample_id patient1 -tumor tumor.bam -normal normal.bam -gridss_vcf gridss.vcf -ref_genome GRCh37_hmf -output_dir ./gripss && linx -sample_id patient1 -gripss_dir ./gripss -ref_genome GRCh37_hmf -output_dir ./linx`
**Explanation:** Runs GRIPSS followed by LINX to annotate and visualize the filtered somatic SVs with gene fusion and breakpoint information.
