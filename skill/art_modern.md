---
name: art_modern
category: qc
description: ART_Morden - Modernized ART simulator for diverse Next-Generation Sequencing reads
tags: [art_modern, qc, read-simulator, ngs, sequencing]
author: oxo-call-community
source_url: "https://github.com/YU-Zhejian/art_modern/releases/download/1.4.0/art_modern.pdf"
---

## Concepts

- **Tool Overview**: ART_Morden is a modernized version of the ART read simulator supporting diverse Next-Generation Sequencing platforms. Version 1.4.0.
- **Core Function**: Simulates sequencing reads with realistic error models for modern NGS platforms including Illumina, PacBio, and Oxford Nanopore.
- **Platform Support**: Supports multiple sequencing platforms with updated error models reflecting current sequencing technologies.
- **Error Modeling**: Incorporates platform-specific error profiles, quality score distributions, and read characteristics.
- **Long-Read Support**: Includes simulation capabilities for long-read technologies (PacBio, Nanopore) with appropriate error profiles.
- **Quality Scores**: Generates realistic quality scores matching platform characteristics and sequencing chemistry.
- **Coverage Control**: Allows specification of coverage depth or read count for simulation.
- **Input/Output**: Accepts reference genome FASTA and outputs simulated reads in FASTQ format.
- **Installation**: `conda install -c bioconda art_modern` or download from GitHub.

## Pitfalls

- **Platform Selection**: Must select correct platform for accurate error modeling. Wrong platform produces unrealistic reads.
- **Reference Quality**: Simulated read quality depends on reference genome accuracy.
- **Memory Requirements**: Large genomes require significant memory for simulation.
- **Long-Read Complexity**: Long-read simulation may require more computational resources than short-read simulation.
- **Random Seed**: Different seeds produce different read sets. Use fixed seed for reproducibility.

## Examples

### Display help
**Args:** `art_morden --help`
**Explanation:** Shows all available command-line options and usage information.

### Simulate Illumina reads
**Args:** `art_morden -i genome.fasta -p -l 150 -f 30 -m 200 -s 10 -o illumina_reads`
**Explanation:** Simulates paired-end Illumina reads (150bp) with 30x coverage. Mean fragment size 200bp with 10bp standard deviation.

### Simulate PacBio reads
**Args:** `art_morden -i genome.fasta -l 10000 -f 30 -ss HSII -o pacbio_reads`
**Explanation:** Simulates PacBio long reads (10kb) with 30x coverage using HSII sequencing chemistry.

### Simulate Nanopore reads
**Args:** `art_morden -i genome.fasta -l 15000 -f 30 -ss R9 -o nanopore_reads`
**Explanation:** Simulates Oxford Nanopore long reads (15kb) with 30x coverage using R9 chemistry.

### Specify read count
**Args:** `art_morden -i genome.fasta -c 1000000 -l 150 -o reads`
**Explanation:** Generates 1 million reads (150bp) instead of specifying coverage depth.

### Set quality score range
**Args:** `art_morden -i genome.fasta -l 150 -f 30 -qs 20 -qe 35 -o reads`
**Explanation:** Sets quality score range from 20 to 35 for simulated reads.

### Add sequencing errors
**Args:** `art_morden -i genome.fasta -l 150 -f 30 -ir 0.001 -dr 0.0005 -sr 0.0002 -o reads`
**Explanation:** Sets error rates: 0.1% insertion rate, 0.05% deletion rate, 0.02% substitution rate.

### Use fixed random seed
**Args:** `art_morden -i genome.fasta -l 150 -f 30 -rs 12345 -o reproducible_reads`
**Explanation:** Uses fixed random seed for reproducible read generation across runs.