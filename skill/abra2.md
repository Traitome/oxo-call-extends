---
name: abra2
category: variant-calling
description: ABRA2 is an updated implementation of ABRA - Assembly Based ReAligner for indel realignment.
tags: [abra2, variant-calling, realignment, indel, bam, dna, rna]
author: oxo-call-community
source_url: "https://github.com/mozack/abra2"
---

## Concepts

- **Tool Overview**: Assembly-based realigner for next-generation sequencing data that improves indel detection through localized assembly and global realignment. Version 2.24.
- **Core Function**: Realigns reads around indels using localized de novo assembly to produce more accurate alignments, especially for complex indels and splice junctions.
- **Input/Output**: Input is coordinate-sorted, indexed BAM files; output is realigned BAM files. Supports both DNA and RNA-seq data.
- **Installation**: Install via bioconda: `conda install -c bioconda abra2`
- **Platform Support**: Linux (x86_64, ARM64)
- **Java-Based**: Requires Java 8 runtime. Run via `java -jar abra2.jar`.
- **Multi-Sample Support**: Can process multiple BAM files simultaneously (e.g., normal + tumor pairs).
- **RNA-Seq Support**: Supports RNA-seq realignment with splice junction awareness using STAR junction files or GTF annotations.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Requirements**: Input BAM must be coordinate-sorted and indexed (.bai file required).
- **Temporary Space**: Requires substantial temporary disk space (at least equal to input file size). Use `--tmpdir` to specify location.
- **Memory Allocation**: Requires sufficient Java heap space. Use `-Xmx` flag (e.g., `-Xmx16G` for 16GB).
- **RNA Junctions**: For RNA-seq, use both `--junctions bam` and `--gtf` for best results. Only tested with STAR output.
- **Targets BED**: Optional but recommended for targeted sequencing. Omit to process entire genome (slower).

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and parameters.

### Realign single DNA BAM file
**Args:** `--in input.bam --out realigned.bam --ref reference.fa --threads 8`
**Explanation:** Realigns a single BAM file using 8 threads. Processes entire genome if no targets BED is specified.

### Realign tumor-normal pair
**Args:** `--in normal.bam,tumor.bam --out normal.abra.bam,tumor.abra.bam --ref hg38.fa --threads 8 --targets regions.bed`
**Explanation:** Realigns both BAM files simultaneously within specified target regions. Joint processing improves consistency.

### Realign RNA-seq BAM with junction information
**Args:** `--in star_aligned.bam --out realigned.bam --ref hg38.fa --junctions bam --gtf annotation.gtf --threads 8 --dist 500000 --sua`
**Explanation:** Realigns RNA-seq data using splice junction information from the BAM itself and GTF annotation. The `--sua` flag enables splice-aware realignment.

### Realign with known indels
**Args:** `--in input.bam --out realigned.bam --ref reference.fa --in-vcf known_indels.vcf --threads 8`
**Explanation:** Incorporates known indels from a VCF file to guide realignment. Avoid using large databases like dbSNP.

### Realign with custom temporary directory
**Args:** `--in input.bam --out realigned.bam --ref reference.fa --tmpdir /scratch/tmp --threads 12`
**Explanation:** Specifies a custom temporary directory with sufficient space. Important when default /tmp is limited.
