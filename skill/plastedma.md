---
name: plastedma
category: annotation
description: Plastic Enzymes Degrading in Metagenomic databases Analysis
tags: [plastedma, annotation]
author: oxo-call-community
source_url: "https://github.com/ozefreitas/PlastEDMA"
---

## Concepts
- **Tool Overview**: PlastEDMA takes an input FASTA file with a variable number of aminoacidic sequences and performes a search against an considerable amount of Hidden Markov Models, previously built and trained from state of the art plastic (PE - polyethylene) degrading enzymes. This process relies on the hmmsearch function from HMMER to perform the structural annotation. Output deduces about the potential presence of plastic degradring enzymes in the inputed sequences, and is composed by 3 distinct files, in order to help the user to have an easier time to read and conclude about the results.
- **Core Function**: Plastic Enzymes Degrading in Metagenomic databases Analysis
- **Input/Output**: FASTA/GFF/GTF
- **Installation**: `conda install -c bioconda plastedma`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
