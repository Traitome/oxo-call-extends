---
name: m-party
category: alignment
description: Mining Protein dAtasets foR Targeted EnzYmes
tags: [m-party, alignment, sequence]
author: oxo-call-community
source_url: "https://github.com/ozefreitas/M-PARTY"
---

## Concepts

- **Tool Overview**: m-party v0.2.2 - M-PARTY takes an input FASTA file with a variable number of aminoacidic sequences and performes a search against an considerable amount of Hidden Markov Models, previously built and trained from state of the art plastic (PE - polyethylene) degrading enzymes. This process relies on the hmmsearch function from HMMER to perform the structural annotation. Output deduces about the potential presence of plastic degradring enzymes in the inputed sequences, and is composed by 3 distinct files, in order to help the user to have an easier time to read and conclude about the results..
- **Core Function**: Mining Protein dAtasets foR Targeted EnzYmes
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda m-party`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
