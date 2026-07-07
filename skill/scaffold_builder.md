---
name: scaffold_builder
category: assembly
description: Combining de novo and reference-guided assembly with Scaffold_builder
tags: ["scaffold_builder", "assembly", "scaffolding", "genome-assembly"]
author: oxo-call-community
source_url: "http://edwards.sdsu.edu/scaffold_builder"
---

## Concepts

- **Tool Overview**: Scaffold_builder (v2.3) is a tool for combining de novo and reference-guided assembly to construct scaffolds from sequencing reads.
- **Core Function**: Assembles sequencing reads into contigs and scaffolds using both de novo and reference-guided approaches.
- **Algorithm**: Integrates de novo assembly with reference mapping to order and orient contigs into scaffolds.
- **Input/Output**: Accepts sequencing reads (FASTQ) and optional reference genome, produces assembled scaffolds.
- **Hybrid Approach**: Combines de novo assembly with reference-guided scaffolding for improved accuracy.
- **Applications**: Genome assembly, metagenomic analysis, and sequence reconstruction.

## Pitfalls

- **Reference Dependence**: Reference-guided mode requires closely related reference genome.
- **Computational Resources**: High memory and CPU requirements for large datasets.
- **Repeat Regions**: May struggle with highly repetitive genomic regions.
- **Contig Quality**: Results depend on input contig quality from initial assembly.
- **Parameter Tuning**: Requires careful adjustment of assembly parameters.
- **Output Complexity**: May produce multiple alternative scaffolds requiring manual review.

## Examples

### De novo scaffolding
**Args:** `scaffold_builder -i reads.fastq -o scaffolds.fasta`
**Explanation:** `-i` input FASTQ reads; `-o` output scaffolds FASTA.

### Reference-guided assembly
**Args:** `scaffold_builder -i reads.fastq -r reference.fasta -o scaffolds.fasta`
**Explanation:** `-r` reference genome for guided scaffolding.

### With existing contigs
**Args:** `scaffold_builder -c contigs.fasta -r reference.fasta -o scaffolds.fasta`
**Explanation:** `-c` input contigs for scaffolding.

### Paired-end reads
**Args:** `scaffold_builder -1 reads_1.fastq -2 reads_2.fastq -o scaffolds.fasta`
**Explanation:** `-1/-2` paired-end read files.

### Quality filtering
**Args:** `scaffold_builder -i reads.fastq -q 20 -o scaffolds.fasta`
**Explanation:** `-q 20` filters reads with quality below 20.

### Minimum scaffold length
**Args:** `scaffold_builder -i reads.fastq -m 1000 -o scaffolds.fasta`
**Explanation:** `-m 1000` minimum scaffold length of 1000 bp.

### Verbose logging
**Args:** `scaffold_builder -i reads.fastq -v -o scaffolds.fasta`
**Explanation:** `-v` enables verbose output for debugging.