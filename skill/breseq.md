---
name: breseq
category: variant-calling
description: Computational pipeline for finding mutations relative to a reference sequence in short-read DNA re-sequencing
tags: [breseq, mutation, variant-calling, resequencing, bacterial]
author: oxo-call-community
source_url: "https://github.com/barricklab/breseq"
---

## Concepts

- **Tool Overview**: Breseq is a computational pipeline for finding mutations from short-read resequencing data.
- **Core Function**: Identifies SNPs, indels, and structural variants relative to a reference genome.
- **Algorithm**: Uses both consensus and junction evidence for comprehensive mutation detection.
- **Input**: FASTQ reads and reference genome.
- **Output**: HTML report and GD (Genomic Diff) file with mutation calls.
- **Application**: Bacterial genome evolution and mutation rate studies.
- **Installation**: Install via bioconda: `conda install -c bioconda breseq`

## Pitfalls

- **Reference Required**: Must provide reference genome in FASTA format.
- **Polymorphism Mode**: Use --polymorphism for mixed population detection.
- **Memory Usage**: Large genomes require significant memory.
- **Output Format**: GD format is Breseq-specific; convert for other tools.

## Examples

### Run mutation detection
**Args:** `breseq -r reference.gbk -o output/ reads_1.fq reads_2.fq`
**Explanation:** Detects mutations from paired-end reads against annotated reference.

### Polymorphism detection
**Args:** `breseq -r reference.gbk --polymorphism -o output/ reads.fq`
**Explanation:** Detects polymorphic mutations in mixed bacterial populations.

### Compare two samples
**Args:** `gdtools COMPARE -r reference.gbk -o comparison.html sample1.gd sample2.gd`
**Explanation:** Compares mutations between two samples using GD files.

### Apply mutations to reference
**Args:** `gdtools APPLY -r reference.gbk -o mutated.gbk mutations.gd`
**Explanation:** Applies detected mutations to create mutated reference sequence.

### Use with BAM input
**Args:** `breseq -r reference.gbk -o output/ aligned.bam`
**Explanation:** Runs mutation detection from pre-aligned BAM file.

### Set minimum coverage
**Args:** `breseq -r reference.gbk --min-coverage 10 -o output/ reads.fq`
**Explanation:** Requires minimum 10x coverage for mutation calling.
