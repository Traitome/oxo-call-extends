---
name: muse
category: variant-calling
description: An accurate and ultra-fast somatic point mutation calling tool for whole-genome sequencing (WGS) and whole-exome sequencing (WES) data from heterogeneous tumor samples.
tags: [muse, variant-calling, somatic-mutation, tumor, wgs, wes, bam, vcf]
author: oxo-call-community
source_url: "https://bioinformatics.mdanderson.org/public-software/muse"
---

## Concepts

- **Tool Overview**: MuSe v2.1.2 is a somatic point mutation caller that uses a Markov chain model to capture tumor mutation heterogeneity. It takes aligned reads (BAM/CRAM) and identifies somatic point mutations by distinguishing tumor from normal sequencing evidence.
- **Core Function**: Employs a Markov chain-based likelihood approach to model allelic heterogeneity in tumors. Handles subclonal populations and contamination from normal cells, making it robust for heterogeneous tumor samples.
- **Algorithm**: Uses a two-state (somatic vs germline) model with Markov chain Monte Carlo (MCMC) sampling to estimate the probability of each mutation being somatic. Incorporates base call quality, mapping quality, and allelic fraction information.
- **Input Format**: Requires tumor BAM/CRAM file (aligned to reference), matched normal BAM/CRAM, and reference genome (FASTA). Both tumor and normal must be from the same patient.
- **Output**: Outputs VCF format with somatic mutation calls, including allele frequencies, variant quality scores, and MCMC convergence statistics. Also generates a summary report.
- **Workflow**: Three main steps: `muse call` (generates candidate variants), `muse sump` (combines and filters), `muse purge` (removes artifacts). Must run call before sump; purge is optional.

## Pitfalls

- **Paired Tumor-Normal Required**: MuSe requires matched tumor-normal BAM pairs. It cannot call somatic mutations from tumor-only data. For tumor-only analysis, use other callers like Mutect2.
- **Input BAM Requirements**: BAM files must be coordinate-sorted and indexed. MuSe relies on proper chromosome ordering and indexing for efficient access.
- **MCMC Convergence**: MuSe uses MCMC sampling which requires sufficient iterations to converge. For quick tests, results may be unreliable. Default settings are usually adequate for production runs.
- **Memory Usage**: Large WGS files can require significant memory during MCMC sampling. Consider chromosome-by-chromosome processing for very large files.
- **Base Quality Recalibration**: MuSe does not perform realignment or recalibration. Pre-process BAMs with GATK BaseRecalibrator for best results.
- **Filtering is Critical**: The `muse sump` step applies filtering thresholds. Default thresholds may not suit all use cases. Adjust based on sequencing depth and tumor purity.

## Examples

### Step 1: Call somatic variants
**Args:** `muse call -r reference.fa -f tumor.bam -n normal.bam -o calls`
**Explanation:** First step generates candidate somatic variant calls from tumor BAM using matched normal. Creates calls.vcf file with all candidates before filtering.

### Step 2: Summarize and filter variants
**Args:** `muse sump -I calls -O filtered -t 0.05 -E`
**Explanation:** Combines and filters variant calls. `-t` sets p-value threshold (0.05 default), `-E` applies additional error modeling. Produces filtered.vcf with high-confidence somatic calls.

### Purge artifact variants
**Args:** `muse purge -I filtered.vcf -O purged -C 0.6`
**Explanation:** Optional third step removes alignment artifacts. `-C` sets maximum contamination threshold (0.6 = 60% normal contamination). Useful for low-purity tumors.

### Run complete workflow with multiple chromosomes
**Args:** `muse call -r ref.fa -f tumor.bam -n normal.bam -o chr1 -L chr1`
**Explanation:** Use `-L` to restrict to specific chromosome. Run separately for each chromosome then combine with `muse sump` for large genomes to manage memory.

### Specify threads for faster processing
**Args:** `muse call -r ref.fa -f tumor.bam -n normal.bam -o calls -T 8`
**Explanation:** Use `-T` to specify thread count for parallel processing. Helpful for large WGS files. Default is single-threaded.
