---
name: sga
category: assembly
description: sga - String Graph Assembler for DNA sequence reads
tags: ["sga", "assembly", "de-novo", "string-graph"]
author: oxo-call-community
source_url: "https://github.com/jts/sga"
---

## Concepts

- **Tool Overview**: sga (v0.10.15) is a de novo assembler for DNA sequence reads.
- **Core Function**: Assembles sequences using string graph formulation.
- **Algorithm**: Uses FM-index/Burrows-Wheeler transform for overlap detection.
- **Input/Output**: Accepts FASTQ reads and produces contigs/scaffolds.
- **De Novo Assembly**: Focuses on string graph based assembly.
- **Applications**: Genome assembly, metagenomics, and sequence analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Preprocess reads
**Args:** `sga preprocess -o preprocessed.fastq reads.fastq`
**Explanation:** Preprocesses raw reads.

### Build index
**Args:** `sga index -a ropebwt2 -t 8 reads.fastq`
**Explanation:** Builds FM-index for reads.

### Overlap detection
**Args:** `sga overlap -t 8 -m 40 reads.fastq`
**Explanation:** Detects overlaps between reads.

### Assemble
**Args:** `sga assemble -o contigs.fasta graph.asqg`
**Explanation:** Assembles contigs from overlap graph.

### Help command
**Args:** `sga --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sga --version`
**Explanation:** Shows current version.

### Full pipeline
**Args:** `sga preprocess -o preprocessed.fastq reads.fastq && sga index preprocessed.fastq && sga overlap preprocessed.fastq && sga assemble -o contigs.fasta preprocessed.asqg`
**Explanation:** Runs complete assembly pipeline.