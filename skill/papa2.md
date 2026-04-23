---
name: papa2
category: qc
description: Python-first amplicon denoising — byte-identical to R's DADA2
tags: [papa2, qc]
author: oxo-call-community
source_url: "https://github.com/rec3141/papa2"
---

## Concepts
- **Tool Overview**: papa2 is a complete Python port of the DADA2 amplicon denoising pipeline. All 37 R functions have Python equivalents, producing byte-identical results with no R dependency. Includes quality filtering, dereplication, error learning, denoising, paired-end merging, chimera removal, and taxonomy assignment backed by a compiled C/C++ core.
- **Core Function**: Processes bioinformatics data for qc tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda papa2`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
