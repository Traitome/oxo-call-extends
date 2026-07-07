---
name: velvet-sc
category: bioinformatics
description: Velvet-SC - Single-cell sequence assembler.
tags: [velvet-sc, sequence-assembly, single-cell, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dzerbino/velvet"
---

## Concepts

- **Tool Overview**: Velvet-SC - Single-cell sequence assembler.
- **Core Function**: Assembles single-cell sequencing reads.
- **Input**: FASTQ files from single cells.
- **Output**: Assembled contigs.
- **Installation**: Install via conda or source
- **Use Case**: Single-cell genome assembly, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Coverage**: Low coverage may affect assembly quality.

## Examples

### Assemble single-cell reads
**Args:** `velveth sc_output 27 -shortPaired cell_reads.fastq`
**Explanation:** Prepare single-cell assembly.

### With options
**Args:** `velvetg sc_output -exp_cov auto`
**Explanation:** Generate contigs with auto coverage.
