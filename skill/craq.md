---
name: craq
category: qc
description: Reference-free genome assembly evaluator that detects assembly errors (CREs/CSEs) and calculates AQI quality metrics using clipped read alignment analysis
tags: [craq, assembly, quality-assessment, genome-assembly, CRE, CSE, AQI, misassembly-detection]
author: oxo-call-community
source_url: "https://github.com/JiaoLaboratory/CRAQ"
---

## Concepts

- **Tool Overview**: CRAQ (Clipping Reveals Assembly Quality) v1.10 - A reference-free genome assembly evaluator that detects assembly errors at single-base pair resolution and calculates quality metrics.
- **Core Function**: Analyzes clipped read alignment patterns from both NGS short-reads and SMS long-reads to identify: (1) Clip-based Regional Errors (CREs) - small-scale assembly errors, (2) Clip-based Structural Errors (CSEs) - large-scale structural breakpoints, (3) Regional Heterozygous variants (CRHs), and (4) Structural Heterozygous variants (CSHs). Reports Assembly Quality Index (AQI) metrics for assembly classification.
- **Algorithm**: Maps reads to assembly using minimap2 (with -ax sr for Illumina, -ax map-hifi for PacBio HiFi, -ax map-pb for PacBio CLR, -ax map-ont for ONT), analyzes clipping signals and coverage ratios at each position to detect error breakpoints and heterozygous variants.
- **Input**: Assembled genome in FASTA format, plus either: (1) pre-aligned BAM files for both SMS and NGS reads, or (2) raw FASTQ files (SMS as single file, NGS as R1,R2 pair).
- **Output**: Quality reports (R-AQI, S-AQI metrics), BED files for error coordinates (CRE/CSE/CRH/CSH), corrected FASTA if --break enabled, Circos visualization plots.
- **Application**: Assembly quality assessment for genome projects, identifying error locations for manual correction, comparing assemblies from different assemblers, haploid vs diploid assembly discrimination.
- **Installation**: `conda install -c bioconda craq` or `git clone https://github.com/JiaoLaboratory/CRAQ.git`

## Pitfalls

- **Dependency Requirements**: Requires samtools (1.3.1+), minimap2 (2.17+), perl (5+), and pycircos (for plotting). Ensure all dependencies are in PATH before running.
- **Input Format Strictness**: Assembly must be in FASTA (.fa) format, not FASTQ. Pre-aligned BAM files must be sorted and indexed.
- **Single-Dataset Limitation**: Running with only NGS or SMS data reduces detection capability - CSE/CSH won't be detected with NGS-only, and CRE/CRH detection is reduced with SMS-only.
- **Resource Consumption**: `--report_SNV` option is computationally expensive; only enable when detailed SNV reporting is needed.
- **Quality Threshold**: Default `--mapq` of 20 may need adjustment for low-quality assemblies or highly repetitive genomes.
- **Parallelization**: Reads mapping is the bottleneck; use multi-threaded execution via `--thread` parameter (default 10).

## Examples

### Display help message
**Args:** `-h`
**Explanation:** Shows all available parameters including required inputs (--genome, --sms_input, --ngs_input), filter parameters (clipping thresholds), and output options.

### Basic usage with pre-aligned BAM files
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam`
**Explanation:** Run CRAQ with pre-aligned sorted BAM files for both long-read SMS and short-read NGS data. This is the recommended input mode for efficiency when alignments already exist.

### Basic usage with raw sequencing files
**Args:** `-g assembly.fa -sms SMS.fa.gz -ngs NGS_R1.fa.gz,NGS_R2.fa.gz -x map-hifi`
**Explanation:** Run CRAQ directly with raw FASTQ files. The `-x map-hifi` specifies PacBio HiFi read mapping mode. For Illumina short-reads, CRAQ uses minimap2 -ax sr mode by default.

### Run with PacBio CLR instead of HiFi
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -x map-pb`
**Explanation:** Use map-pb option for PacBio CLR reads instead of map-hifi. Other valid options: map-ont for Oxford Nanopore reads.

### Generate corrected assembly
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -b T`
**Explanation:** Enable chimera fragment breaking with `-b T`. CRAQ will detect chimeric contigs and break them at conflict breakpoints, outputting corrected sequences to out_correct.fa.

### Enable Circos visualization
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -pl T`
**Explanation:** Generate Circos plots for visual inspection of genomic quality metrics. Requires pycircos (python 3.7+) to be installed.

### Run with custom thread count
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -t 20`
**Explanation:** Increase thread count to 20 for faster read mapping. Default is 10 threads.

### Adjust quality threshold
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -q 30`
**Explanation:** Increase minimum mapping quality threshold to 30 for higher stringency in read alignment filtering.

### Run with only SMS long-read data
**Args:** `-g assembly.fa -sms SMS_sort.bam`
**Explanation:** Run CRAQ with long-read data only (no NGS). CSE and CSH detection will be limited. More regions may be classified as low_confidence.

### Run with only NGS short-read data
**Args:** `-g assembly.fa -ngs NGS_sort.bam`
**Explanation:** Run CRAQ with short-read data only (no SMS). CRE and CRH detection will be reduced, especially for ONT-based assemblies.

### Search for errors near breakpoints
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -ser T`
**Explanation:** Enable noisy error region searching nearby CRE/CSE breakpoints for more comprehensive error detection.

### Report SNV-level variants
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam -snv T`
**Explanation:** Enable SNV and heterozygous variant reporting. Note: This is computationally expensive and may significantly increase runtime.

### Inspect results in IGV
**Args:** `-g assembly.fa -sms SMS_sort.bam -ngs NGS_sort.bam`
**Explanation:** After CRAQ completes, load the BAM files from ./LRout/ and ./SRout/ directories into IGV for visual inspection of alignment coverage and clipping patterns.
