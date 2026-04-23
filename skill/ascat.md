---
name: ascat
category: variant-calling
description: ASCAT - Allele-specific copy number analysis of tumor samples accounting for purity and ploidy
tags: [copy-number, cnv, tumor-purity, ploidy, cancer, allele-specific]
author: oxo-call-community
source_url: "https://github.com/VanLoo-lab/ascat"
---

## Concepts

- **Tool Overview**: ASCAT (Allele-Specific Copy Number Analysis of Tumors) derives copy number profiles of tumor cells, accounting for normal cell admixture and tumor aneuploidy. Version 3.2.0.
- **Purity and Ploidy**: Simultaneously estimates tumor purity (fraction of tumor cells) and ploidy (average DNA content per cell). Critical for accurate copy number calling.
- **Allele-Specific CN**: Reports copy number for both parental alleles separately. Distinguishes copy-neutral LOH from true deletions.
- **Input Types**: Accepts SNP array data (Affymetrix, Illumina) or massively parallel sequencing data (WGS, WES). Different pipelines for each input type.
- **Normal Contamination**: Corrects for normal cell contamination in tumor samples. Essential for accurate copy number estimation in heterogeneous tumors.
- **Segmentation**: Identifies copy number segments across genome. Breakpoints indicate structural variants or copy number changes.
- **R Package**: Implemented as R package with comprehensive visualization and reporting functions.

## Pitfalls

- **Paired Samples**: Requires matched normal sample for best results. Tumor-only mode available but less accurate.
- **Purity Threshold**: Low purity tumors (<30%) may fail to converge or produce unreliable results. Check purity estimates carefully.
- **Complex Genomes**: Highly aneuploid tumors with multiple subclones may be difficult to resolve. Multiple solutions possible.
- **GC Correction**: Proper GC bias correction essential for sequencing data. Incorrect correction produces false CNVs.
- **SNP Density**: Low SNP density (e.g., WES vs WGS) reduces resolution. May miss small CNVs.
- **Reference Selection**: Germline SNP positions must match reference genome build. Mismatched builds cause errors.

## Examples

### Basic ASCAT run from sequencing data
**Args:** `ascat.runASCAT(Tumor_LogR_file="tumor_logR.txt", Tumor_BAF_file="tumor_BAF.txt", Germline_LogR_file="normal_logR.txt", Germline_BAF_file="normal_BAF.txt", gender="XX")`
**Explanation:** Standard ASCAT analysis from LogR and BAF files. Gender specified for sex chromosome analysis. Outputs purity, ploidy, and copy number segments.

### Run with tumor-only data
**Args:** `ascat.runASCAT(Tumor_LogR_file="tumor_logR.txt", Tumor_BAF_file="tumor_BAF.txt", isMale=FALSE, tumorOnly=TRUE)`
**Explanation:** Tumor-only mode when matched normal unavailable. Uses population reference for BAF estimation. Less accurate than paired mode.

### Set purity and ploidy manually
**Args:** `ascat.runASCAT(Tumor_LogR_file="tumor_logR.txt", Tumor_BAF_file="tumor_BAF.txt", Germline_LogR_file="normal_logR.txt", Germline_BAF_file="normal_BAF.txt", ploidy=3.5, rho=0.7)`
**Explanation:** Manually specifies ploidy (3.5n) and purity (70%). Useful when automatic estimation fails or for validation with known values.

### Process SNP array data
**Args:** `ascat.loadData(Tumor_LogR_file="tumor.txt", Tumor_BAF_file="tumor_BAF.txt", Germline_LogR_file="normal.txt", Germline_BAF_file="normal_BAF.txt", chrs=c(1:22,"X"))`
**Explanation:** Loads SNP array data for ASCAT analysis. Specify chromosomes to analyze. Works with Affymetrix or Illumina array formats.

### Generate ASCAT plots
**Args:** `ascat.plotASCAT(output_file="ascat_results.pdf")`
**Explanation:** Generates comprehensive PDF plots showing copy number profiles, purity/ploidy estimates, and segmentation. Essential for quality assessment.

### Export copy number segments
**Args:** `ascat.writeSegments(output_file="segments.txt")`
**Explanation:** Exports copy number segments in tab-delimited format. Includes chromosome, start, end, copy number, and allele-specific copy numbers.

### Adjust segmentation parameters
**Args:** `ascat.runASCAT(Tumor_LogR_file="tumor_logR.txt", Tumor_BAF_file="tumor_BAF.txt", Germline_LogR_file="normal_logR.txt", Germline_BAF_file="normal_BAF.txt", gamma=1.0, penalty=25)`
**Explanation:** Adjusts segmentation parameters: gamma (LogR scaling) and penalty (segmentation penalty). Tune for specific data types or quality levels.