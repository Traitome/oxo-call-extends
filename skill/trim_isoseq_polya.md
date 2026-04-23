---
name: trim_isoseq_polya
category: qc
description: Trims polyA tails from IsoSeq FASTA files
tags: [trim_isoseq_polya, qc]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/trim_isoseq_polyA"
---

## Concepts

- **Tool Overview**: trim_isoseq_polya (v0.0.3) - Trims polyA tails from IsoSeq FASTA files
- **Core Function**: Trims polyA tails from IsoSeq FASTA files
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trim_isoseq_polya`

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
