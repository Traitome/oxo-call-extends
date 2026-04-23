---
name: virprof
category: expression
description: Virus Identification, Quantification and Genome Recovery from RNA-Seq NGS data
tags: [virprof, expression]
author: oxo-call-community
source_url: "https://github.com/seiboldlab/virprof"
---

## Concepts

- **Tool Overview**: virprof (v0.9.2) - VirProf is a dual RNA-seq analysis pipeline integrating host expression profile generation with virus identification, quantification, and genome recovery from host tissue RNA sequencing data. VirProf combines an unguided metagenomic assembly workflow with interleaved host read depletion followed by BLAST based binning, scaffolding and classification. Application of VirProf to poly-A selected RNA-seq data from nasal swabs with respiratory virus qPCR data, revealed that VirProf was able to a) quantify a range of viral infections at detection limits and precision comparable to qPCR and b) recover complete, accurate viral genomes suitable for phylogenetic analysis.
- **Core Function**: Virus Identification, Quantification and Genome Recovery from RNA-Seq NGS data
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda virprof`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
