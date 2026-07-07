---
name: drax
category: programming
description: "A pipeline for Detecting Resistome Associated taXa."
tags: [drax, programming, resistome, antimicrobial-resistance, metagenomics]
author: oxo-call-community
source_url: "https://github.com/will-rowe/drax"
---

## Concepts

- **Tool Overview**: DRAX is a pipeline for detecting resistome-associated taxa from metagenomic sequencing data.
- **Core Function**: Identifies microbial taxa carrying antimicrobial resistance genes in complex microbial communities.
- **Input/Output**: Input: Metagenomic reads (FASTQ), assembled contigs (FASTA). Output: Resistome profiles, taxonomic assignments.
- **Algorithm**: Combines read mapping, gene calling, and taxonomic classification to identify resistance determinants.
- **Key Features**: Integrated resistome analysis, supports both short and long reads, generates interactive reports.
- **Installation**: `conda install -c bioconda drax`

## Pitfalls

- **Database Updates**: Resistance gene databases require regular updates to capture new resistance mechanisms.
- **False Positives**: Highly conserved genes can produce false positive resistance calls.
- **Read Quality**: Poor quality reads may reduce mapping accuracy and affect results.
- **Community Complexity**: Highly diverse communities may require more stringent filtering.
- **Reference Bias**: Database reference bias can affect detection sensitivity for rare resistance genes.

## Examples

### Basic resistome analysis
**Args:** `--reads sample.fastq --output results/`
**Explanation:** Runs resistome detection pipeline on metagenomic reads.

### With assembled contigs
**Args:** `--contigs assembly.fasta --output results/`
**Explanation:** Analyzes assembled contigs for resistance gene content.

### Custom database
**Args:** `--reads sample.fastq --db custom_db.fasta --output results/`
**Explanation:** Uses a custom resistance gene database for analysis.

### Generate report
**Args:** `--reads sample.fastq --output results/ --report`
**Explanation:** Generates an HTML summary report of resistome findings.

### Quality filtering
**Args:** `--reads sample.fastq --output results/ --min-quality 20`
**Explanation:** Filters reads with Phred quality score below 20.