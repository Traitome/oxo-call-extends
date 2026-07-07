---
name: mm2plus
category: alignment
description: Fast long-read mapper and whole-genome aligner (accelerated version of minimap2)
tags: [mm2plus, alignment, minimap2]
author: oxo-call-community
source_url: "https://github.com/at-cg/mm2-plus"
---

## Concepts

- **Tool Overview**: mm2plus v1.2 is an accelerated version of minimap2.
- **Core Function**: Fast long-read mapping and whole-genome alignment.
- **Performance Optimization**: Accelerated implementation of minimap2.
- **Long-read Support**: Optimized for long sequencing reads.
- **Input/Output**: Accepts reads and references; outputs alignments.
- **Genome Alignment**: Supports whole-genome alignment workflows.

## Pitfalls

- **Long-read Specific**: Designed for long-read sequencing data.
- **Computational Resources**: Mapping may require significant resources.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for optimal mapping.
- **Data Quality**: Results depend on read quality.
- **Reference Dependence**: Requires appropriate reference sequences.

## Examples

### Map long reads
**Args:** `mm2plus reference.fasta reads.fastq > alignments.sam`
**Explanation:** Maps long reads to reference genome.

### Whole-genome alignment
**Args:** `mm2plus genome1.fasta genome2.fasta > alignment.paf`
**Explanation:** Aligns two genomes.

### Preset for ONT
**Args:** `mm2plus -x map-ont reference.fasta reads.fastq > alignments.sam`
**Explanation:** Uses ONT-specific preset.

### Preset for PacBio
**Args:** `mm2plus -x map-pb reference.fasta reads.fastq > alignments.sam`
**Explanation:** Uses PacBio-specific preset.

### Output BAM
**Args:** `mm2plus reference.fasta reads.fastq | samtools view -Sb > alignments.bam`
**Explanation:** Outputs sorted BAM file.