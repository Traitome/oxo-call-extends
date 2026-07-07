---
name: crypto_typer
category: variant-calling
description: Tool to subtype the parasite Cryptosporidium based on the 18S and gp60 markers.
tags: [crypto_typer, variant-calling, Cryptosporidium, subtyping, parasitology]
author: oxo-call-community
source_url: "https://github.com/christineyanta/crypto_typer"
---

## Concepts

- **Tool Overview**: crypto_typer (v1.0.0+) is a Python-based tool for subtyping Cryptosporidium parasites using 18S rRNA and gp60 gene sequences. It provides a user-friendly interface for analyzing sequence data and assigning Cryptosporidium subtypes.
- **Core Function**: Identifies Cryptosporidium species and subtypes by comparing input sequences against a curated database of reference sequences.
- **Input/Output**: Input: FASTA sequences or FASTQ reads. Output: Subtype assignments, confidence scores, and summary reports.
- **Algorithm**: Uses sequence alignment and phylogenetic matching to determine the most likely subtype for each sample.
- **Key Features**: Simple command-line interface, supports batch processing, provides confidence metrics for assignments.
- **Installation**: `conda install -c bioconda crypto_typer`

## Pitfalls

- **Sequence Quality**: Poor quality sequences may lead to incorrect subtype assignments.
- **Database Updates**: Reference database may require updates for newly discovered subtypes.
- **Ambiguous Results**: Some sequences may have ambiguous subtype assignments.
- **Input Format**: Ensure correct input format (FASTA or FASTQ).
- **Dependencies**: Requires Python and additional bioinformatics libraries.

## Examples

### Basic usage
**Args:** `--input input.fasta --output output_file.txt`
**Explanation:** Process FASTA sequences and generate subtype report.

### Analyze FASTQ reads
**Args:** `--input reads.fastq --fastq --output results.txt`
**Explanation:** Analyze raw FASTQ reads and determine subtypes.

### Display help
**Args:** `--help`
**Explanation:** Shows available options and parameters.