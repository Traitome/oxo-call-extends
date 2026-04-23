---
name: seqscreen
category: metagenomics
description: SeqScreen was created to sensitively assign taxonomic classifications, functional annotations, and Functions of Sequences of Concern (FunSoCs) to single, short DNA sequences or open reading frames.
tags: [seqscreen, metagenomics]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/seqscreen/-/wikis/home"
---

## Concepts

- **Tool Overview**: seqscreen (v4.5) - SeqScreen was created to sensitively assign taxonomic classifications, functional annotations, and Functions of Sequences of Concern (FunSoCs) to single, short DNA sequences or open reading frames.
- **Core Function**: SeqScreen was created to sensitively assign taxonomic classifications, functional annotations, and Functions of Sequences of Concern (FunSoCs) to single, short DNA sequences or open reading frames.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqscreen`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqscreen -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run seqscreen with typical input and output options.
