---
name: seqscreen
category: metagenomics
description: seqscreen - Taxonomic classification and functional annotation of DNA sequences
tags: ["seqscreen", "metagenomics", "classification", "annotation"]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/seqscreen/-/wikis/home"
---

## Concepts

- **Tool Overview**: seqscreen (v4.5) assigns taxonomic classifications, functional annotations, and FunSoCs to short DNA sequences.
- **Core Function**: Classifies sequences and identifies Functions of Sequences of Concern.
- **Algorithm**: Uses sequence alignment and database searching for classification.
- **Input/Output**: Accepts FASTA/FASTQ files and produces annotation results.
- **Sequence Analysis**: Focuses on sensitive taxonomic and functional analysis.
- **Applications**: Metagenomics, pathogen detection, and biosecurity screening.

## Pitfalls

- **Memory Usage**: High memory requirements for large databases.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Database Requirements**: Requires large reference databases.
- **Input Quality**: Results depend on sequence quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Analyze sequences
**Args:** `seqscreen run -i sequences.fasta -o results/`
**Explanation:** `-i` input sequences; `-o` output directory.

### With database
**Args:** `seqscreen run -i sequences.fasta -d custom_db -o results/`
**Explanation:** `-d` specifies custom database.

### Verbose logging
**Args:** `seqscreen run -i sequences.fasta -v -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `seqscreen run -i sequences.fasta -t 8 -o results/`
**Explanation:** `-t 8` uses 8 threads.

### Help command
**Args:** `seqscreen --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqscreen --version`
**Explanation:** Shows current version.

### Initialize database
**Args:** `seqscreen init -d seqscreen_db`
**Explanation:** Initializes SeqScreen database.