---
name: mcroni
category: utility
description: Analysis tool for mcr-1 gene detection and characterization.
tags: [mcroni, mcr-1, antimicrobial-resistance]
author: oxo-call-community
source_url: "https://github.com/liampshaw/mcroni"
---

## Concepts

- **Tool Overview**: mcroni analyzes mcr-1 colistin resistance gene.
- **Core Function**: Detects and characterizes mcr-1 variants.
- **Resistance Detection**: Identifies mcr-1 gene in sequences.
- **Variant Analysis**: Analyzes mcr-1 variants and mutations.
- **Input/Output**: Accepts FASTA/FASTQ, produces analysis reports.
- **Installation**: `conda install -c bioconda mcroni`

## Pitfalls

- **Sequence Quality**: Low-quality sequences affect detection.
- **Reference Database**: Requires up-to-date reference sequences.
- **False Positives**: May produce false positive results.
- **Memory Requirements**: Large datasets require memory.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **Output Interpretation**: Results require careful interpretation.

## Examples

### Detect mcr-1
**Args:** `mcroni detect -i genome.fasta -o results.txt`
**Explanation:** Detects mcr-1 gene in genome.

### Variant analysis
**Args:** `mcroni variant -i genome.fasta -o variants.txt`
**Explanation:** Analyzes mcr-1 variants.

### Multiple samples
**Args:** `mcroni batch -d genomes/ -o results/`
**Explanation:** Processes multiple genome files.

### Verbose output
**Args:** `mcroni detect -i genome.fasta -v -o results.txt`
**Explanation:** Shows detailed detection information.

### Help documentation
**Args:** `mcroni --help`
**Explanation:** Displays available commands and options.
