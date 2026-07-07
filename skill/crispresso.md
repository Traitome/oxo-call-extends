---
name: crispresso
category: genome-editing
description: Software pipeline for analyzing CRISPR-Cas9 targeted amplicon sequencing data with allele quantification
tags: [crispresso, CRISPR, genome-editing, amplicon, NGS, indel, HDR, NHEJ, base-editor, Cas9, Cpf1]
author: oxo-call-community
source_url: "https://github.com/lucapinello/CRISPResso"
---

## Concepts

- **Tool Overview**: CRISPResso (v1.0.13) / CRISPResso2 - A software pipeline designed for rapid and intuitive analysis and interpretation of genome editing experiments from amplicon sequencing data.
- **Core Function**: Aligns sequencing reads to reference amplicon sequences, quantifies insertions, deletions, and substitutions to determine editing outcomes. Supports both cleaving nucleases (Cas9, Cpf1) and non-cleaving nucleases (base editors).
- **Algorithm**: (1) Filters low-quality reads. (2) Trims adapters. (3) Merges paired-end reads. (4) Aligns to reference using Needleman-Wunsch with biologically-informed scoring. (5) Quantifies HDR/NHEJ outcomes. (6) Generates visualization plots.
- **Input**: FASTQ files (paired-end, single-end, or interleaved), amplicon sequence, sgRNA sequence, optional HDR template.
- **Output**: Editing efficiency percentages, allele frequency tables, indel distribution plots, quantification of frameshift/inframe mutations, splice site affected.
- **Application**: Genome editing validation, HDR efficiency measurement, base editor analysis, pooled amplicon sequencing, allele deconvolution.
- **Installation**: `pip install CRISPResso` or `conda install -c bioconda crispresso`

## Pitfalls

- **Paired-end Recommended**: Best results with paired-end sequencing; single-end may have lower accuracy.
- **Quality Filtering**: Default quality filtering is strict - may discard many reads if quality is low.
- **Amplicon Length**: Works best with amplicons 100-500bp; very short or long amplicons may have issues.
- **Multiple Alleles**: For heterozygous samples, provide all allele sequences to correctly assign reads.
- **Base Editor Specifics**: When analyzing base editors, provide the base editor mode and target base to get accurate editing window quantification.
- **Guide Sequence**: Must provide sgRNA without PAM sequence.

## Examples

### Basic Cas9 editing analysis
**Args:** `CRISPResso --fastq_r1 R1.fastq.gz --fastq_r2 R2.fastq.gz --amplicon_seq ACGCAT... --guide_seq GTTTAGA... -o output/`
**Explanation:** Analyze Cas9 editing with paired-end reads and single guide RNA.

### Base editor analysis
**Args:** `CRISPResso --fastq_r1 base_editor.fastq.gz --amplicon_seq ACGCAT... --guide_seq GTTTAGA... --base_editor_output -o base_editor_output/`
**Explanation:** Analyze base editor data with specific base conversion tracking (C to T by default).

### Allele-specific quantification
**Args:** `CRISPResso --fastq_r1 sample.fastq.gz --amplicon_seq WT_SEQ,ALT_SEQ --guide_seq GTTTAGA... -o allele_output/`
**Explanation:** Provide multiple amplicon sequences to deconvolute alleles and quantify editing per allele.

### Batch analysis
**Args:** `CRISPRessoBatch -f batch_file.txt -o batch_output/`
**Explanation:** Process multiple samples from a batch file with one command.

### Pooled amplicon sequencing
**Args:** `CRISPRessoPooled --fastq sample.fastq.gz --amplicon_gb amplicons.bed --guide_seqs guides.txt -o pooled_output/`
**Explanation:** Analyze multiplexed amplicon sequencing from pooled experiments.

### WGS targeted sites
**Args:** `CRISPRessoWGS -b sample.bam --regions regions.bed -o wgs_output/`
**Explanation:** Analyze specific sites in whole-genome sequencing data.

### Compare samples
**Args:** `CRISPRessoCompare -n treated -n control -o compare_output/`
**Explanation:** Compare editing outcomes between treated and control samples.

### HDR analysis
**Args:** `CRISPResso --fastq_r1 HDR.fastq.gz --amplicon_seq TARGET... --guide_seq GTTTAGA... --expected_hdr_amplicon_seq HDR_TEMPLATE... -o hdr_output/`
**Explanation:** Quantify homology-directed repair (HDR) outcomes using a donor template sequence.

### Adjust quantification window
**Args:** `CRISPResso --fastq_r1 sample.fastq.gz --amplicon_seq TARGET... --guide_seq GTTTAGA... --quantification_window_center -10 --quantification_window_size 20 -o output/`
**Explanation:** Set custom quantification window around the cut site for base editors.

### Exclude bp from edges
**Args:** `CRISPResso --fastq_r1 sample.fastq.gz --amplicon_seq TARGET... --guide_seq GTTTAGA... --exclude_bp_from_left 10 --exclude_bp_from_right 10 -o output/`
**Explanation:** Exclude end positions from analysis to avoid edge artifacts.
