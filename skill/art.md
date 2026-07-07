---
name: art
category: qc
description: ART - Illumina, 454, and SOLiD read simulator
tags: [art, qc, read-simulator, illumina, 454, solid]
author: oxo-call-community
source_url: "http://www.niehs.nih.gov/research/resources/software/biostatistics/art/"
---

## Concepts

- **Tool Overview**: ART (Illumina, 454, and SOLiD read simulator) simulates sequencing reads for multiple platforms with realistic error models. Version 2016.06.05.
- **Core Function**: Generates synthetic sequencing reads from reference genomes with platform-specific error profiles and quality characteristics.
- **Platform Support**: Simulates reads for Illumina, 454, and SOLiD sequencing platforms with accurate error models.
- **Error Modeling**: Incorporates platform-specific error rates, quality score distributions, and read length variations.
- **Quality Scores**: Generates realistic quality scores matching platform characteristics (e.g., Phred scores for Illumina).
- **Coverage Control**: Allows specification of desired coverage depth and read count.
- **Input/Output**: Accepts reference genome FASTA and outputs simulated reads in FASTQ format.
- **Installation**: `conda install -c bioconda art` or download from NIEHS website.

## Pitfalls

- **Platform Specificity**: Error models are platform-specific. Use correct simulator variant for your platform.
- **Reference Quality**: Simulated read quality depends on reference genome. Errors in reference propagate to reads.
- **Memory Requirements**: Large genomes require significant memory for simulation. Monitor memory usage.
- **Read Length**: Maximum read length varies by platform simulator. Check platform-specific limits.
- **Random Seed**: Different random seeds produce different read sets. Use fixed seed for reproducibility.

## Examples

### Display help
**Args:** `art_illumina --help`
**Explanation:** Shows all available command-line options and usage information.

### Simulate Illumina reads
**Args:** `art_illumina -i genome.fasta -p -l 150 -f 30 -m 200 -s 10 -o simulated_reads`
**Explanation:** Simulates paired-end Illumina reads (150bp) with 30x coverage. Mean fragment size 200bp with 10bp standard deviation.

### Simulate 454 reads
**Args:** `art_454 -i genome.fasta -l 400 -f 20 -o simulated_454_reads`
**Explanation:** Simulates 454 pyrosequencing reads (400bp length) with 20x coverage.

### Simulate SOLiD reads
**Args:** `art_solid -i genome.fasta -l 50 -f 40 -o simulated_solid_reads`
**Explanation:** Simulates SOLiD sequencing reads (50bp) with 40x coverage.

### Specify read count instead of coverage
**Args:** `art_illumina -i genome.fasta -c 1000000 -l 100 -o reads`
**Explanation:** Generates 1 million reads (100bp) instead of specifying coverage depth.

### Set quality profile
**Args:** `art_illumina -i genome.fasta -l 150 -f 30 -qs 20 -qe 30 -o reads`
**Explanation:** Sets quality score range from 20 to 30 for simulated reads.

### Add sequencing errors
**Args:** `art_illumina -i genome.fasta -l 150 -f 30 -ir 0.001 -ir2 0.001 -dr 0.0001 -dr2 0.0001 -o reads`
**Explanation:** Sets error rates: 0.1% insertion rate, 0.1% insertion rate for read 2, 0.01% deletion rate for both reads.

### Generate paired-end with custom insert size
**Args:** `art_illumina -i genome.fasta -p -l 150 -f 30 -m 500 -s 50 -o paired_reads`
**Explanation:** Simulates paired-end reads with 500bp mean insert size and 50bp standard deviation.