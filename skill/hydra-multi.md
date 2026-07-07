---
name: hydra-multi
category: variant_calling
description: Hydra-Multi detects structural variation breakpoints in both unique and duplicated genomic regions.
tags: [hydra-multi, structural variation, SV detection]
author: oxo-call-community
source_url: "https://github.com/arq5x/Hydra"
---

## Concepts

- **Tool Overview**: Hydra-Multi is a paired-end read structural variant discovery tool capable of integrating signals from hundreds of samples simultaneously.
- **Multi-sample Integration**: Designed to detect structural variation breakpoints by clustering discordant paired-end alignments across multiple samples.
- **Duplicated Region Support**: Specifically designed to detect variation in both unique and duplicated genomic regions, examining reads with multiple discordant alignments.
- **Scalability**: Capable of analyzing hundreds to thousands of human genomes using commodity hardware.
- **Breakpoint Detection**: Detects all classes of structural variation including deletions, tandem duplications, inversions, and translocations.
- **Installation**: `conda install -c bioconda hydra-multi`

## Pitfalls

- **Input Format**: Requires properly aligned BAM files with appropriate read groups and mate information.
- **Memory Requirements**: Analyzing large cohorts may require significant memory resources.
- **Alignment Quality**: SV detection accuracy depends heavily on the quality of input alignments.
- **Insert Size Variability**: Library insert size variability can affect breakpoint detection sensitivity.
- **Reference Genome**: Ensure reference genome assembly matches the sequencing data.
- **False Positives**: Discordant read pairs can arise from mapping artifacts, requiring careful filtering.

## Examples

### Run Hydra-Multi on multiple samples
**Args:** `hydra-multi -bam_list bam_files.txt -out sv_results/`
**Explanation:** Runs multi-sample structural variant detection on BAM files listed in bam_files.txt.

### Basic SV detection
**Args:** `hydra -bam sample.bam -out sv_calls.vcf`
**Explanation:** Detects structural variants from a single BAM file and outputs VCF.

### Cluster discordant reads
**Args:** `hydra-cluster -bam cohort.bam -out clustered_breakpoints.txt`
**Explanation:** Clusters discordant read pairs to identify shared breakpoints across samples.

### Filter breakpoints by quality
**Args:** `hydra-filter -in sv_calls.vcf -qual 30 -out filtered.vcf`
**Explanation:** Filters SV calls to retain only those with quality score >= 30.

### Annotate SV breakpoints
**Args:** `hydra-annotate -in sv_calls.vcf -ref hg38 -out annotated.vcf`
**Explanation:** Annotates structural variant breakpoints with gene and functional information.