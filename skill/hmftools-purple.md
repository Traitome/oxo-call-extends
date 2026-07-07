---
name: hmftools-purple
category: variant-calling
description: PURPLE combines BAF, read depth, small variants and structural variants to estimate tumor purity and copy number profiles.
tags: [hmftools-purple, copy-number, purity, ploidy, tumor, CNV, BAF, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/purple"
---

## Concepts

- **Tool Overview**: PURPLE (v4.3) is a purity ploidy estimator that combines B-allele frequency (BAF), read depth ratios, small variants, and structural variants to estimate the purity and copy number profile of a tumor sample. It produces allele-specific copy number profiles adjusted for tumor purity.

- **Copy Number Profiling**: Generates segment-level copy number calls showing the absolute copy number of each genomic region adjusted for tumor purity and ploidy. Handles diploid, amplified, and deleted regions across the genome.

- **Purity Estimation**: Estimates the fraction of tumor cells in the sample by combining BAF deviation from 0.5 with depth ratios. Outputs a continuous purity score (0.0-1.0) used for downstream analysis and sample QC.

- **Ploidy Calculation**: Calculates the weighted average ploidy of the tumor genome. Diploid tumors have ploidy ~2.0, while highly aneuploid tumors may have ploidy >3.0.

- **Somatic CNV Identification**: Distinguishes somatic copy number alterations from germline variation by comparing tumor and matched normal BAF patterns. Identifies focal amplifications, deletions, and loss of heterozygosity (LOH).

- **Driver Event Catalog**: Annotates copy number profiles with known cancer driver genes, distinguishing oncogene amplifications from tumor suppressor gene deletions. Maps alterations to canonical cancer pathways.

## Pitfalls

- **AMBER and COBALT Dependency**: PURPLE requires AMBER (BAF generation) and COBALT (gc-content normalization) outputs as inputs. Running PURPLE before completing AMBER/COBALT will fail.

- **Reference Genome Version**: PURPLE requires consistent reference genome (GRCh37 or GRCh38) across all inputs. GRCh37 uses chr prefix convention, GRCh38 may or may not. Mixing conventions causes parsing failures.

- **Structural Variant Integration**: For accurate copy number at breakpoint regions, PURPLE integrates GRIPSS structural variant calls. Without SV input, breakpoints are inferred from BAF/depth transitions which may be less precise.

- **Low Purity Samples**: Samples with purity <20% may produce unreliable copy number calls due to weak BAF deviation. Consider filtering samples with insufficient tumor fraction.

- **Complex Genome Regions**: Copy number estimation in regions with repetitive sequences, segmental duplications, or HLA loci may be unreliable. These regions are flagged in the output.

- **Memory for WGS**: Whole genome samples with millions of BAF windows require 8GB+ heap memory. Use `-Xmx16G` for large cohort processing.

## Examples

### Run PURPLE with AMBER and COBALT
**Args:** `purple -sample tumor1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -ref_genome GRCh37_hmf -output_dir ./purple/`
**Explanation:** Standard PURPLE run using AMBER BAF files and COBALT GC-content normalization. Produces somatic CNV calls, purity/ploidy estimates, and driver event catalog.

### Tumor-normal paired analysis
**Args:** `purple -sample tumor1 -reference_sample normal1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -ref_genome GRCh37_hmf -output_dir ./purple/`
**Explanation:** Uses matched normal sample to distinguish somatic from germline copy number alterations. The reference sample improves accuracy of BAF-based copy number estimation.

### Include structural variant data
**Args:** `purple -sample tumor1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -gripss_dir ./gripss/ -ref_genome GRCh37_hmf -output_dir ./purple/`
**Explanation:** Integrates GRIPSS structural variant calls for improved copy number estimation at breakpoints. SV support is indicated in the SegSupport column of output.

### Run on GRCh38 reference
**Args:** `purple -sample tumor1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -ref_genome GRCh38_hmf -output_dir ./purple/`
**Explanation:** Uses GRCh38 reference genome. All input files must be aligned to GRCh38. Requires corresponding GRCh38 AMBER and COBALT outputs.

### High-memory mode for cohort analysis
**Args:** `purple -sample tumor1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -ref_genome GRCh37_hmf -output_dir ./purple/ -Xmx16G`
**Explanation:** Allocates 16GB heap memory for processing large cohorts or whole genome samples. Prevents out-of-memory errors during BAF window enumeration.

### Specify output target regions
**Args:** `purple -sample tumor1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -target_regions capture_regions.bed -ref_genome GRCh37_hmf -output_dir ./purple/`
**Explanation:** Limits copy number analysis to target regions from a BED file. Useful for targeted panel sequencing where whole-genome analysis is unnecessary.

### Run with somatic variant input
**Args:** `purple -sample tumor1 -amber_dir ./amber/ -cobalt_dir ./cobalt/ -sage_vcf somatic_variants.vcf -ref_genome GRCh37_hmf -output_dir ./purple/`
**Explanation:** Provides somatic SNV/indel calls from SAGE for allelic copy number analysis. Variants in regions with copy number alteration are flagged for allele-specific interpretation.
