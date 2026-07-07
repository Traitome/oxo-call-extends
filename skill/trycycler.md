---
name: trycycler
category: assembly
description: Trycycler - Tool for consensus assembly of long-read sequences.
tags: [trycycler, genome-assembly, long-reads, consensus, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rrwick/Trycycler"
---

## Concepts

- **Tool Overview**: Trycycler - A tool for generating consensus assemblies from long-read sequencing data.
- **Core Function**: Integrates multiple assemblies to produce a high-quality consensus genome.
- **Input**: Long-read assemblies (FASTA), sequencing reads.
- **Output**: Consensus assembly, assembly graphs, quality metrics.
- **Installation**: `pip install trycycler`
- **Use Case**: Genome assembly, long-read sequencing analysis, bacterial genomics.

## Pitfalls

- **Computation Time**: May be slow for large genomes.
- **Memory**: Requires significant memory for complex assemblies.

## Examples

### Run Trycycler
**Args:** `trycycler cluster -r reads.fastq -o trycycler_output/`
**Explanation:** Run Trycycler clustering and consensus assembly.

### Polish assembly
**Args:** `trycycler polish -a assembly.fasta -r reads.fastq -o polished.fasta`
**Explanation:** Polish assembly using long reads.
