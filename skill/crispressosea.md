---
name: crispressosea
category: genome-editing
description: CRISPRessoSea processes multiple pooled amplicon sequencing experiments for CRISPR genome editing analysis with high throughput and standardized output
tags: [crispressosea, CRISPR, pooled-amplicon, genome-editing, NGS, demultiplex]
author: oxo-call-community
source_url: "https://github.com/clementlab/CRISPRessoSea"
---

## Concepts

- **Tool Overview**: CRISPRessoSea (v0.1.5+) is designed for processing multiple pooled amplicon CRISPR sequencing experiments in a standardized manner.
- **Core Function**: Analyzes pooled amplicon sequencing data where multiple CRISPR target sites are multiplexed in a single sequencing reaction. Automatically demultiplexes reads by amplicon sequence and quantifies editing outcomes at each target site.
- **Algorithm**: (1) Reads are assigned to amplicons based on sequence similarity. (2) For each amplicon, the tool aligns reads and quantifies insertions, deletions, and substitutions relative to the reference. (3) Guides are identified and allele frequencies calculated. (4) Summary statistics across all amplicons are aggregated.
- **Input/Output**: Accepts FASTQ/FASTQ.gz input; outputs per-amplicon CRISPResso reports plus aggregated summary
- **Installation**: `pip install crispressosea` or `conda install -c bioconda crispressosea`

## Pitfalls

- **Amplicon Assignment**: Reads with equal homology to multiple amplicons are assigned to the first matching amplicon by default. Use `--assign_ambiguous_alignments_to_first_reference` to control this behavior.
- **Mismatched Amplicons**: Ensure all amplicon sequences in the amplicon list exactly match the experimental design; even single base differences cause demultiplexing failure.
- **Guide Sequence**: The sgRNA sequence must be provided without the PAM sequence for accurate cut-site analysis.

## Examples

### Demultiplex pooled amplicons with amplicon list file
**Args:** `--fastq_r1 pooled_reads.fastq.gz --amplicon_list amplicons.txt --output_folder sea_results/`
**Explanation:** Provide a tab-separated file with amplicon sequences and names to demultiplex pooled reads. Each amplicon gets analyzed separately.

### Paired-end pooled amplicon sequencing
**Args:** `--fastq_r1 reads_R1.fastq.gz --fastq_r2 reads_R2.fastq.gz --amplicon_list amplicons.txt --output_folder sea_results/`
**Explanation:** Analyze paired-end sequencing data from pooled amplicon library. Both read files are used for more accurate alignment.

### Custom mismatch threshold for amplicon assignment
**Args:** `--fastq_r1 reads.fastq.gz --amplicon_list amplicons.txt --mismatch_threshold 0.1 --output_folder sea_results/`
**Explanation:** Set maximum allowed mismatch rate (10%) for amplicon assignment during demultiplexing. Higher values allow more divergent sequences to be assigned.

### Analyze with guide sequences
**Args:** `--fastq_r1 reads.fastq.gz --amplicon_list amplicons.txt --guide_list guides.txt --output_folder sea_results/`
**Explanation:** Provide guide RNA sequences for each amplicon to enable cut-site analysis and HDR quantification.

### Specify minimum alignment score
**Args:** `--fastq_r1 reads.fastq.gz --amplicon_list amplicons.txt --default_min_aln_score 80 --output_folder sea_results/`
**Explanation:** Set minimum alignment score (0-100) for read assignment. Higher values require more exact matching to amplicons.
