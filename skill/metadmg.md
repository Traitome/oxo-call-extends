---
name: metadmg
category: variant-calling
description: "metaDMG-cpp: fast and efficient method for estimating mutation and damage rates in ancient DNA data."
tags: [metadmg, variant-calling, ancient-dna, damage-analysis]
author: oxo-call-community
source_url: "https://github.com/metaDMG-dev/metaDMG-cpp"
---
## Concepts

- **Tool Overview**: metaDMG-cpp v0.4.3 is a fast and efficient tool for estimating mutation and damage rates in ancient DNA (aDNA) data.
- **Core Function**: Analyzes ancient DNA sequences to estimate post-mortem damage patterns and mutation rates.
- **Damage Pattern Detection**: Identifies characteristic C->T and G->A substitutions typical of ancient DNA degradation.
- **Statistical Modeling**: Uses statistical models to quantify damage rates across sequences.
- **Input/Output**: Accepts BAM/SAM aligned reads or FASTQ sequences; outputs damage rate estimates and statistics.
- **Efficiency**: Optimized for processing large-scale ancient DNA datasets efficiently.

## Pitfalls

- **DNA Damage Levels**: Requires sufficient DNA damage signal for accurate estimation.
- **Contamination**: Modern DNA contamination can interfere with damage estimation.
- **Sequence Quality**: Low-quality sequences may affect damage rate calculations.
- **Reference Genome**: Requires high-quality reference genome for accurate alignment.
- **Sample Age**: Very old samples with severe degradation may produce unreliable results.
- **Coverage Depth**: Requires sufficient coverage depth for robust statistical analysis.

## Examples

### Estimate damage rates
**Args:** `metadmg -i reads.bam -r reference.fasta -o damage_stats.txt`
**Explanation:** Estimates damage rates from aligned ancient DNA reads.

### From FASTQ files
**Args:** `metadmg -i reads.fastq -r reference.fasta -o damage_stats.txt`
**Explanation:** Processes raw FASTQ reads and estimates damage rates.

### Paired-end data
**Args:** `metadmg -i reads_1.fastq reads_2.fastq -r reference.fasta -o damage_stats.txt`
**Explanation:** Processes paired-end ancient DNA sequencing data.

### Generate plot
**Args:** `metadmg -i reads.bam -r reference.fasta -o damage_stats.txt -p damage_plot.pdf`
**Explanation:** Generates a visual plot of damage patterns.

### With quality filtering
**Args:** `metadmg -i reads.bam -r reference.fasta -o damage_stats.txt -q 30`
**Explanation:** Applies quality filtering with minimum Phred score of 30.