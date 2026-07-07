---
name: staphopia-sccmec
category: typing
description: Predicts Staphylococcus aureus SCCmec type based on primers.
tags: [staphopia-sccmec, staphylococcus, sccmec, typing]
author: oxo-call-community
source_url: "https://github.com/staphopia/staphopia-sccmec"
---

## Concepts

- **Tool Overview**: staphopia-sccmec (v1.0.0) is a tool for predicting SCCmec (Staphylococcal Cassette Chromosome mec) type in Staphylococcus aureus.
- **Core Function**: Identifies SCCmec type by detecting specific genetic markers and primer binding sites.
- **Algorithm**: Uses BLAST-based approach to detect SCCmec-specific genes and cassette structures.
- **Input/Output**: Input: FASTA genome assembly or sequencing reads; Output: SCCmec type prediction with confidence.
- **SCCmec Database**: Contains curated primer sequences and allele definitions for SCCmec typing.
- **Installation**: `conda install -c bioconda staphopia-sccmec` or download from GitHub.

## Pitfalls

- **Assembly Quality**: Poor assembly affects detection of SCCmec genes.
- **Novel Variants**: May miss novel SCCmec types not in the database.
- **Mixed Types**: Mixed infections or contamination produce ambiguous results.
- **Database Updates**: Outdated database may miss newly discovered SCCmec types.
- **Coverage Depth**: Low sequencing coverage may miss SCCmec genes.
- **False Positives**: Primer cross-reactivity may produce false positive calls.

## Examples

### Display help
**Args:** `staphopia-sccmec --help`
**Explanation:** Shows available options and usage information.

### Basic SCCmec typing
**Args:** `staphopia-sccmec -i genome.fasta -o results.txt`
**Explanation:** Predict SCCmec type from genome assembly.

### With reads input
**Args:** `staphopia-sccmec -i reads.fastq -o results.txt --reads`
**Explanation:** Type SCCmec directly from sequencing reads.

### Verbose output
**Args:** `staphopia-sccmec -i genome.fasta -o results.txt -v`
**Explanation:** Run with detailed logging including intermediate results.

### Output GFF format
**Args:** `staphopia-sccmec -i genome.fasta -o results.gff --gff`
**Explanation:** Output results in GFF annotation format.

### Custom database
**Args:** `staphopia-sccmec -i genome.fasta -o results.txt -d custom_db/`
**Explanation:** Use custom SCCmec database.

### Quality filtering
**Args:** `staphopia-sccmec -i reads.fastq -o results.txt -q 20`
**Explanation:** Apply quality filter to reads before analysis.

### Batch processing
**Args:** `staphopia-sccmec -i sample1.fasta sample2.fasta -o results/`
**Explanation:** Process multiple genomes together.
