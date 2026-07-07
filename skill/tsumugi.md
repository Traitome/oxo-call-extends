---
name: tsumugi
category: assembly
description: Tsumugi - Tool for de novo assembly of long-read sequencing data.
tags: [tsumugi, genome-assembly, long-reads, de-novo, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fenderglass/tsumugi"
---

## Concepts

- **Tool Overview**: Tsumugi - A tool for de novo assembly of long-read sequencing data using overlap-based methods.
- **Core Function**: Assembles long reads into contiguous sequences using overlap-layout-consensus approach.
- **Input**: Long-read sequencing data (FASTQ).
- **Output**: Genome assembly (FASTA), assembly statistics.
- **Installation**: `conda install -c bioconda tsumugi`
- **Use Case**: Genome assembly, long-read sequencing analysis, bacterial genomics.

## Pitfalls

- **Computation Time**: May be slow for large datasets.
- **Memory**: Requires significant memory for complex assemblies.

## Examples

### Assemble genome
**Args:** `tsumugi -i reads.fastq -o assembly.fasta`
**Explanation:** Perform de novo assembly of long reads.

### With error correction
**Args:** `tsumugi -i reads.fastq -c -o corrected_assembly.fasta`
**Explanation:** Assemble with error correction.
