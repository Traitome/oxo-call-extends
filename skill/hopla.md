---
name: hopla
category: variant_analysis
description: Hopla enables classic genomic single, duo, trio, etc., analysis, by studying a single (multisample) vcf-file
tags: [hopla, vcf, genotype, phasing, trio]
author: oxo-call-community
source_url: "https://github.com/CenterForMedicalGeneticsGhent/Hopla"
---

## Concepts

- **Trio Analysis**: Hopla specializes in analyzing genomic relationships within family trios (proband, father, mother), enabling accurate genotype phasing and inheritance pattern detection
- **PED File Integration**: Requires pedigree information in PED format for proper family relationship definition
- **Merlin Integration**: Leverages the Merlin tool for robust genotype inference and haplotype phasing
- **Multi-sample VCF Processing**: Capable of handling complex multi-sample VCF files with hundreds of samples
- **Haplotype Inference**: Uses statistical methods to determine phase information for heterozygous variants
- **Visualization Support**: Generates HTML reports with Plotly-based visualizations for result interpretation

## Pitfalls

- **PED File Format**: Incorrect PED file format can lead to misinterpretation of family relationships
- **VCF Requirements**: Requires properly formatted VCF with correct sample identifiers matching PED file
- **Memory Usage**: Large multi-sample VCF files may require significant memory resources
- **Reference Genome Consistency**: Must use consistent reference genome across all input files
- **Phasing Limitations**: Cannot phase sites where all trio members are heterozygous (~20% of variants)
- **Dependency Availability**: Requires R packages (DNAcopy, GenomicRanges, kinship2) and Merlin tool

## Examples

### Basic trio analysis
**Args:** `hopla -v input.vcf -p pedigree.ped -o output_dir/`
**Explanation:** Performs trio analysis on a VCF file using pedigree information from PED file.

### Generate HTML report
**Args:** `hopla -v input.vcf -p pedigree.ped -o output_dir/ --html`
**Explanation:** Generates an interactive HTML report with visualizations of genotype distributions and inheritance patterns.

### Single sample analysis
**Args:** `hopla -v input.vcf -p pedigree.ped -o output_dir/ --single`
**Explanation:** Runs analysis in single-sample mode, useful for quality control and variant filtering.

### Duo analysis (parent-child)
**Args:** `hopla -v input.vcf -p pedigree.ped -o output_dir/ --duo`
**Explanation:** Performs duo analysis for parent-child pairs when full trio data is unavailable.

### Custom phasing parameters
**Args:** `hopla -v input.vcf -p pedigree.ped -o output_dir/ --phase-threshold 0.95`
**Explanation:** Sets a higher confidence threshold (0.95) for phasing calls, reducing false positive phasing assignments.