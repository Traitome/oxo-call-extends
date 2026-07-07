---
name: metacarp
category: metagenomics
description: MetaCARP (Metagenomic Contamination-Assessment-of-Retail-Products) is a workflow to screen shotgun metagenomic sequencing data.
tags: [metacarp, metagenomics, contamination, screening]
author: oxo-call-community
source_url: "https://github.com/BioinformaticsPlatformWIV-ISP/MetaCARP"
---

## Concepts

- **Tool Overview**: MetaCARP v1.0.0 is a comprehensive workflow designed for screening shotgun metagenomic sequencing data from retail products for contamination assessment.
- **Core Function**: Identifies and quantifies microbial contaminants in metagenomic samples, particularly focusing on food and retail product safety.
- **Quality Control**: Includes integrated quality control steps to ensure reliable contaminant detection.
- **Taxonomic Profiling**: Provides detailed taxonomic profiling of detected contaminants at multiple levels.
- **Input/Output**: Accepts raw sequencing reads in FASTQ format; outputs comprehensive reports including contamination levels and taxonomic classifications.
- **Workflow Integration**: Designed as a Snakemake workflow for reproducibility and scalability.

## Pitfalls

- **Reference Database**: Contamination detection relies on the quality and completeness of reference databases.
- **Host DNA Removal**: Incomplete host DNA removal can interfere with contamination detection.
- **Low Abundance Contaminants**: May miss contaminants present at very low abundance levels.
- **False Positives**: Stringent filtering is required to avoid false positive contamination calls.
- **Computational Resources**: Large datasets may require significant computational resources.
- **Sample Preparation**: Contamination during sample preparation can affect results.

## Examples

### Run complete workflow
**Args:** `snakemake --snakefile metacarp.smk --config input=reads.fastq output=results/`
**Explanation:** Runs the complete MetaCARP workflow on input reads.

### Run with paired-end reads
**Args:** `snakemake --snakefile metacarp.smk --config r1=reads_1.fastq r2=reads_2.fastq output=results/`
**Explanation:** Processes paired-end sequencing data.

### Specify custom database
**Args:** `snakemake --snakefile metacarp.smk --config input=reads.fastq db=custom_db/ output=results/`
**Explanation:** Uses a custom reference database for contamination detection.

### Generate report
**Args:** `snakemake --snakefile metacarp.smk --config input=reads.fastq output=results/ --report report.html`
**Explanation:** Generates an HTML report summarizing contamination findings.

### Run with increased threads
**Args:** `snakemake --snakefile metacarp.smk --config input=reads.fastq output=results/ --cores 16`
**Explanation:** Uses 16 CPU cores for parallel processing.