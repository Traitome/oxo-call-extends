---
name: aastk
category: utility
description: Toolkit for analyses of amino acid sequences
tags: [aastk, utility, protein, amino-acid, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/dspeth/aastk/"
---

## Concepts

- **Tool Overview**: A toolkit containing several tools to generate and work with amino acid sequence datasets. Primarily designed for GlobDB genome database. Version 0.1.1.
- **Core Function**: Provides utilities for amino acid sequence analysis, dataset generation, and manipulation.
- **Input/Output**: Input/output varies by specific tool within the toolkit; generally works with FASTA format amino acid sequences.
- **Installation**: Install via bioconda: `conda install -c bioconda aastk`
- **Platform Support**: Platform-independent (noarch)
- **GlobDB Integration**: Designed primarily for working with the GlobDB genome database.

## Pitfalls

- **Version Differences**: Early version (0.1.1). Functionality may be limited or change in future releases.
- **Documentation**: Limited documentation available. Check `--help` for each subcommand.
- **Input Format**: Ensure input sequences are amino acid FASTA format, not nucleotide.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available subcommands and tools within the AASTK toolkit.

### Run basic amino acid sequence analysis
**Args:** `analyze input_proteins.fasta -o analysis_results/`
**Explanation:** Analyzes the input amino acid sequences and outputs various metrics and statistics.

### Generate amino acid dataset
**Args:** `generate --input genomes/ --output dataset.fasta`
**Explanation:** Extracts and generates an amino acid sequence dataset from input genome files.

### Filter sequences by criteria
**Args:** `filter --min-length 50 --max-length 500 input.fasta -o filtered.fasta`
**Explanation:** Filters amino acid sequences by length criteria, keeping only sequences between 50 and 500 amino acids.
