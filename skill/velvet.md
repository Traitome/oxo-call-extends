---
name: velvet
category: bioinformatics
description: Velvet - Sequence assembler.
tags: [velvet, sequence-assembly, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/dzerbino/velvet"
---

## Concepts

- **Tool Overview**: Velvet - De novo sequence assembler.
- **Core Function**: Assembles short reads into contigs.
- **Input**: FASTQ files.
- **Output**: Assembled contigs.
- **Installation**: Install via conda or source
- **Use Case**: Genome assembly, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Parameters**: Requires careful parameter tuning.

## Examples

### Assemble reads
**Args:** `velveth output_dir 31 -shortPaired reads_1.fastq reads_2.fastq`
**Explanation:** Prepare assembly.

### With options
**Args:** `velvetg output_dir -exp_cov auto -cov_cutoff 2`
**Explanation:** Generate contigs.
