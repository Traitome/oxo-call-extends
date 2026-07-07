---
name: expansionhunterdenovo
category: utility
description: "ExpansionHunter Denovo (EHdn) is a suite of tools for detecting novel expansions of short tandem repeats (STRs)."
tags: [expansionhunterdenovo, utility, STR-detection, de-novo-repeat, genome-analysis]
author: oxo-call-community
source_url: "https://github.com/Illumina/ExpansionHunterDenovo/blob/v0.9.0/documentation/00_Introduction.md"
---

## Concepts

- **Tool Overview**: ExpansionHunter Denovo is a suite of tools for detecting novel expansions of short tandem repeats (STRs) without prior knowledge of repeat locations.
- **Core Function**: Identifies previously unknown repeat expansions in genomes, enabling discovery of new repeat-associated disorders.
- **Input/Output**: Input: Aligned reads (BAM), reference genome (FASTA). Output: Novel repeat expansion calls, genomic coordinates, size estimates.
- **Algorithm**: Uses a de novo approach to detect repeat expansions by analyzing read depth and paired-end mapping patterns.
- **Key Features**: De novo repeat detection, novel expansion discovery, population-scale analysis, support for large genomes, visualization tools.
- **Installation**: `conda install -c bioconda expansionhunterdenovo`

## Pitfalls

- **False Positives**: May produce false positive calls requiring validation.
- **Read Coverage**: Requires sufficient coverage for reliable detection.
- **Computation Time**: De novo detection can be computationally intensive.
- **Memory Usage**: May require substantial RAM for large genomes.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic de novo repeat detection
**Args:** `expansionhunter_denovo analyze --reads input.bam --reference ref.fasta --output results/`
**Explanation:** Detects novel repeat expansions from aligned reads.

### Population analysis
**Args:** `expansionhunter_denovo analyze --reads samples/ --reference ref.fasta --output results/ --population`
**Explanation:** Analyzes multiple samples for population-scale repeat variation.

### Size estimation
**Args:** `expansionhunter_denovo analyze --reads input.bam --reference ref.fasta --estimate-size --output results/`
**Explanation:** Estimates sizes of detected repeat expansions.

### Visualization
**Args:** `expansionhunter_denovo visualize --input results/ --output plots/`
**Explanation:** Generates visualizations of detected repeat expansions.

### Batch processing
**Args:** `expansionhunter_denovo analyze --input samples.txt --reference ref.fasta --output results/`
**Explanation:** Processes multiple samples in batch mode.