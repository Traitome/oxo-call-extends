---
name: tb-profiler
category: analysis
description: TB-Profiler - Profiling tool for Mycobacterium tuberculosis to detect drug resistance and strain lineage from WGS data.
tags: [tb-profiler, tuberculosis, mycobacterium, drug-resistance, wgs, lineage, variant-calling, illumina, nanopore]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/TBProfiler"
---

## Concepts

- **Tool Overview**: tb-profiler (v5+) - Command-line tool for profiling M. tuberculosis from WGS data to detect drug resistance mutations and predict strain lineage.
- **Core Function**: Aligns reads to H37Rv reference using bowtie2/BWA/minimap2, calls variants with bcftools/freebayes, and compares against drug-resistance database to predict phenotype.
- **Input**: Illumina FASTQ, Nanopore FASTQ/BAM, or pre-aligned BAM/CRAM files. Also accepts assembled contigs.
- **Output**: JSON and TXT results with drug resistance predictions, lineage calls, and mutation details. CSV format available.
- **Installation**: `conda install -c bioconda tb-profiler` or `pip install git+https://github.com/jodyphelan/TBProfiler.git`
- **Key Feature**: Supports both short-read (Illumina) and long-read (Nanopore) sequencing data with automatic platform detection.

## Pitfalls

- **Database Updates**: Drug resistance database evolves - always use latest version with `tb-profiler update_tbdb`.
- **Platform-Specific**: Different aligners for different platforms (BWA for Illumina, minimap2 for Nanopore).
- **Hetero-resistance**: Reports read support for mutations indicating mixed populations but cannot reliably call from Nanopore data.
- **Missing Drugs**: Not all drugs have known genetic markers - some resistance may be phenotypic only.
- **Lineage Prediction**: Based on phylogenetic markers - may not capture all sublineages in diverse populations.

## Examples

### Standard Illumina analysis
**Args:** `tb-profiler profile -1 reads_1.fastq.gz -2 reads_2.fastq.gz -p sample --txt`
**Explanation:** Typical paired-end Illumina analysis with text output. Creates results/sample.results.txt.

### Nanopore analysis
**Args:** `tb-profiler profile --reads sample.fastq.gz -p sample --platform nanopore`
**Explanation:** Long-read Nanopore analysis with automatic basecaller detection.

### BAM input
**Args:** `tb-profiler profile --bam alignment.bam -p sample`
**Explanation:** Use pre-aligned BAM file as input instead of raw reads.

### CSV output for multiple samples
**Args:** `tb-profiler profile -1 *.fastq.gz -p sample --csv`
**Explanation:** Generate CSV format output suitable for batch processing.

### Reheader BAM
**Args:** `tb-profiler reheader -b sample.bam -p new_prefix -o new_sample.bam`
**Explanation:** Reheader BAM files with standardized sample naming.

### Update database
**Args:** `tb-profiler update_tbdb`
**Explanation:** Update the drug resistance and lineage database to latest version.

### Batch processing
**Args:** `tb-profiler batch -i samples.txt -t 8`
**Explanation:** Process multiple samples listed in input file using 8 threads.

### Collate results
**Args:** `tb-profiler collate -d results_dir/`
**Explanation:** Combine multiple sample results into a single table for comparative analysis.

### List available drugs
**Args:** `tb-profiler list -v`
**Explanation:** Display all drugs in the resistance database with version info.
