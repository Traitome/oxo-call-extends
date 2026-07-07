---
name: mimick
category: variant-calling
description: Simulate linked-read data
tags: [mimick, variant-calling, simulation]
author: oxo-call-community
source_url: "https://github.com/pdimens/mimick"
---

## Concepts

- **Tool Overview**: Mimick v3.0.1 simulates linked-read sequencing data.
- **Core Function**: Simulates various linked-read chemistries.
- **Linked-read Simulation**: Supports 10x, haplotagging, stlfr, tellseq.
- **Haplotype Simulation**: Simulates multiple haplotypes.
- **Input/Output**: Accepts reference sequences; outputs simulated reads.
- **Sequencing Simulation**: Generates realistic sequencing data.

## Pitfalls

- **Computational Resources**: Simulation requires significant resources.
- **Memory Requirements**: Memory usage can be high for complex simulations.
- **Parameter Tuning**: May require parameter adjustment for realistic output.
- **Reference Genome**: Requires reference sequence as input.
- **Runtime**: Complex simulations can be time-consuming.
- **Realism**: Simulation may not perfectly match real sequencing data.

## Examples

### Simulate linked-reads
**Args:** `mimick -r reference.fasta -o reads.fastq`
**Explanation:** Simulates linked-read sequencing data.

### With custom coverage
**Args:** `mimick -r reference.fasta -o reads.fastq -c 30`
**Explanation:** Simulates 30x coverage.

### 10x chemistry
**Args:** `mimick -r reference.fasta -o reads.fastq -t 10x`
**Explanation:** Uses 10x Genomics chemistry.

### Multiple haplotypes
**Args:** `mimick -r reference.fasta -o reads.fastq -n 4`
**Explanation:** Simulates 4 haplotypes.

### Batch simulation
**Args:** `mimick -r reference.fasta -o output/ -b samples.txt`
**Explanation:** Simulates multiple samples.