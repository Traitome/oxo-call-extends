---
name: clair
category: variant-calling
description: Fast and accurate germline small variant calling for single-molecule sequencing data
tags: [clair, variant-calling, long-reads, ont, deep-learning, snp, indel]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/Clair"
---

## Concepts

- **Tool Overview**: Clair is a fast and accurate germline small variant caller for single-molecule sequencing data (ONT/PacBio), succeeding Clairvoyante with improved accuracy and speed.
- **Core Function**: Calls germline SNPs and small indels from aligned long-read sequencing data using deep neural networks.
- **Algorithm**: Uses pileup-based approach with deep learning models trained on ONT and PacBio data for high accuracy.
- **Input**: Aligned BAM/CRAM file and reference genome (FASTA).
- **Output**: VCF file with variant calls and quality scores.
- **Application**: Germline variant calling from long-read sequencing data.
- **Installation**: Install via bioconda: `conda install -c bioconda clair`

## Pitfalls

- **Data Type**: Designed for long-read data (ONT/PacBio), not optimal for Illumina.
- **Reference Genome**: Must match the reference used for alignment.
- **Memory Requirements**: Requires significant RAM for large genomes.
- **BAM Index**: Input BAM must be indexed (.bai file present).
- **Model Selection**: Must use appropriate model for sequencing platform.

## Examples

### Call variants from ONT data
**Args:** `clair callVarBam --bam_fn reads.bam --ref_fn reference.fa --model_path ont_model --output output.vcf`
**Explanation:** Calls variants from ONT-aligned BAM using ONT-specific model.

### Call variants from PacBio data
**Args:** `clair callVarBam --bam_fn reads.bam --ref_fn reference.fa --model_path pb_model --output output.vcf`
**Explanation:** Uses PacBio-specific model for variant calling.

### With GPU acceleration
**Args:** `clair callVarBam --bam_fn reads.bam --ref_fn reference.fa --model_path ont_model --output output.vcf --gpu`
**Explanation:** Uses GPU for faster variant calling.

### Display help
**Args:** `clair --help`
**Explanation:** Shows all available options and usage information.