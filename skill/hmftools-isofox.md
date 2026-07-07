---
name: hmftools-isofox
category: alignment
description: Count fragment support for identifying and quantifying gene and transcript features from genome-aligned RNA-seq data.
tags: [hmftools-isofox, RNA-seq, expression, transcript quantification, gene expression, tumor]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/isofox"
---

## Concepts

- **Tool Overview**: hmftools-isofox (v1.7.2) identifies and quantifies gene and transcript features using fragment counting from genome-aligned RNA-seq data in tumor samples.
- **Fragment-based Quantification**: Uses read pairs spanning transcript features rather than simple read counts, providing more accurate expression estimates.
- **Transcript Feature Analysis**: Enables identification and quantification of alternatively spliced transcripts, allele-specific expression, and novel transcript discovery.
- **Tumor Expression Profiling**: Designed specifically for tumor samples, accounting for aneuploidy and copy number alterations that affect expression normalization.
- **WiGiTS Integration**: Part of the Hartwig Medical Foundation's WiGiTS pipeline for combined DNA/RNA analysis in cancer genomics.
- **Gene/transcript Resolution**: Provides expression estimates at both gene-level and transcript-level resolution for comprehensive alternative splicing analysis.

## Pitfalls

- **RNA-seq Data Requirement**: Requires high-quality genome-aligned RNA-seq data; pre-aligned BAM files from STAR or similar aligners are the expected input.
- **Reference Genome Consistency**: The reference genome version must match between RNA-seq alignment and isofox analysis for accurate coordinate-based counting.
- **Paired-end Preference**: Works best with paired-end RNA-seq data; single-end data may have reduced quantification accuracy for transcripts.
- **Strand-specific Protocols**: Some sequencing protocols are strand-specific; incorrect library type settings may cause feature counting errors.
- **Copy Number Influence**: In highly aneuploid tumors, expression normalization should account for copy number alterations affecting gene dosage.

## Examples

### Run Isofox on tumor RNA-seq BAM
**Args:** `isofox -sample_id tumor1 -bam tumor_rnaseq.bam -ref_genome GRCh38_hmf -output_dir ./isofox/`
**Explanation:** Performs standard Isofox analysis on tumor RNA-seq data. Generates gene expression counts and transcript features for downstream analysis.

### Isofox with allele-specific expression analysis
**Args:** `isofox -sample_id test -bam rnaseq.bam -ref_genome GRCh37 -output_dir ./output -allele_specific`
**Explanation:** Enables allele-specific expression analysis using heterozygous variants to distinguish parental expression. Useful for imprinted gene studies.

### Generate transcript expression profile
**Args:** `isofox -sample_id sample1 -bam rnaseq.bam -ref_genome GRCh38_hmf -output_dir ./isofox -features transcript`
**Explanation:** Produces transcript-level expression quantification in addition to gene-level counts. Essential for alternative splicing analysis.

### Isofox with matched normal for comparison
**Args:** `isofox -sample_id patient1 -tumor_bam tumor_rna.bam -normal_bam normal_rna.bam -ref_genome GRCh37 -output_dir ./isofox`
**Explanation:** Analyzes tumor RNA with matched normal comparison to identify tumor-specific expression changes and expressed variants.

### Batch process multiple RNA samples
**Args:** `for bam in tumor_rna_*.bam; do sample=$(basename $bam .bam); isofox -sample_id $sample -bam $bam -ref_genome GRCh38_hmf -output_dir ./isofox/$sample; done`
**Explanation:** Iterates through multiple tumor RNA-seq BAM files and runs Isofox for each. Each sample gets its own output directory with expression data.

### Isofox for fusion gene detection support
**Args:** `isofox -sample_id fusion_test -bam rnaseq.bam -ref_genome GRCh38 -output_dir ./output -fusion_support`
**Explanation:** Identifies reads supporting gene fusions by detecting junction-spanning fragments. Results can guide fusion validation with dedicated fusion callers.
