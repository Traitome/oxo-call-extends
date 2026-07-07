---
name: crispector2
category: utility
description: Allele-specific CRISPR off-target editing activity quantification using de novo SNV detection and statistical allele calling
tags: [crispector2, CRISPR, allele-specific, off-target, SNV, genome-editing, NGS, Bayesian]
author: oxo-call-community
source_url: "https://github.com/theAguy/crispector2"
---

## Concepts

- **Tool Overview**: crispector2 (v2.1.2) / CRISPECTOR2.0 - An advanced tool for allele-specific quantification of CRISPR off-target editing activity from comparative NGS data.
- **Core Function**: Enables reference-free, allele-aware quantification of on- and off-target activity by using de novo sample-specific single nucleotide variant (SNV) detection and statistical-based allele-calling algorithms. Detects how genetic variants affect CRISPR editing outcomes in different alleles.
- **Algorithm**: (1) Performs multiplex PCR/NGS on edited and control samples. (2) Maps reads and assigns them to alleles based on SNVs. (3) Uses entropy-based SNV detection to identify allele-specific positions. (4) Applies statistical allele-calling with phasing. (5) Quantifies INDELs per allele to measure allele-specific editing activity.
- **Input**: FASTQ files from multiplex rhAmpSeq PCR of edited and mock samples, sgRNA sequences, amplicon sequences.
- **Output**: Allele-specific editing frequencies, off-target activity per allele, SNV positions, statistical confidence values.
- **Application**: Personal genome editing analysis, therapeutic CRISPR target validation, allele-specific off-target assessment, population genomics in gene editing.
- **Installation**: `pip install crispector2` or `conda install -c bioconda crispector2`

## Pitfalls

- **Complex Sample Requirements**: Works best with samples containing multiple alleles (heterozygous or mixed populations).
- **Deep Sequencing Required**: Requires high sequencing depth for accurate allele frequency estimation, especially for low-abundance alleles.
- **SNV Detection Sensitivity**: Entropy threshold for SNV detection may need tuning based on sequencing error rates.
- **Computational Resources**: Allele phasing and statistical calling can be memory-intensive for large datasets.
- **Reference Allele Assumption**: May have reduced accuracy when allele frequencies deviate significantly from expected heterozygosity.

## Examples

### Basic allele-specific analysis
**Args:** `crispector2 analyze -i edited.fastq -c control.fastq -g guide_seq -a amplicon -o results/`
**Explanation:** Perform standard allele-aware analysis comparing edited and control samples.

### Enable allele deconvolution
**Args:** `crispector2 analyze -i edited.fastq -c control.fastq -g guide_seq -a amplicon --allele_deconvolution -o results/`
**Explanation:** Enable automatic allele deconvolution to quantify editing per haplotype.

### Adjust SNV detection threshold
**Args:** `crispector2 analyze -i edited.fastq -c control.fastq -g guide_seq -a amplicon --entropy_threshold 0.1 -o results/`
**Explanation:** Set entropy threshold for SNV detection (lower = more sensitive).

### Specify multiple amplicons
**Args:** `crispector2 batch -i samples.txt -o batch_results/`
**Explanation:** Process multiple amplicons/samples from a batch input file.

### Off-target site analysis
**Args:** `crispector2 offtarget -i edited.fastq -c control.fastq -bed offtargets.bed -o offtarget_results/`
**Explanation:** Analyze off-target sites from candidate BED file with allele-specific quantification.

### Export allele table
**Args:** `crispector2 export -i results/ -f tsv -o allele_table.tsv`
**Explanation:** Export detailed allele frequencies and editing outcomes to TSV format.

### Compare multiple samples
**Args:** `crispector2 compare -s sample1/,sample2/,sample3/ -o comparison/`
**Explanation:** Compare allele-specific editing across multiple samples.

### Display version
**Args:** `crispector2 --version`
**Explanation:** Display installed version.

### Show help
**Args:** `crispector2 --help`
**Explanation:** Show all available commands and options.
