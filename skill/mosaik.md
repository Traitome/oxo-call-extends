---
name: mosaik
category: alignment
description: MOSAIK is a stable, sensitive program for mapping sequencing reads to a reference genome.
tags: [mosaik, alignment]
author: oxo-call-community
source_url: "https://github.com/wanpinglee/MOSAIK"
---

## Concepts

- **Tool Overview**: MOSAIK v2.2.26 maps second and third-generation sequencing reads to reference genomes.
- **Core Function**: Aligns sequencing reads to reference with high sensitivity.
- **Multi-platform Support**: Works with Illumina, Ion Torrent, and PacBio data.
- **Gap-aware Alignment**: Handles gaps and indels in read alignment.
- **Quality-aware**: Uses base quality scores in alignment scoring.
- **Input/Output**: Accepts FASTQ reads; outputs SAM/BAM alignments.

## Pitfalls

- **Memory Requirements**: Memory usage depends on reference size.
- **Parameter Tuning**: May require parameter adjustment for optimal mapping.
- **Data Quality**: Results depend on sequencing quality.
- **Index Building**: Requires time to build reference index.
- **Computational Resources**: Large datasets may require significant resources.
- **Version Compatibility**: Some options may vary between versions.

## Examples

### Build reference index
**Args:** `MosaikBuild -fr genome.fasta -oa genome.dat`
**Explanation:** Builds index for reference genome.

### Map reads
**Args:** `MosaikAligner -in reads.fastq -out alignments.bam -ref genome.dat`
**Explanation:** Maps reads to reference genome.

### For paired-end reads
**Args:** `MosaikAligner -in1 reads_1.fastq -in2 reads_2.fastq -out alignments.bam -ref genome.dat`
**Explanation:** Maps paired-end reads.

### With quality filtering
**Args:** `MosaikAligner -in reads.fastq -out alignments.bam -ref genome.dat -q`
**Explanation:** Applies quality filtering before mapping.

### Batch processing
**Args:** `MosaikAligner -in fastq/ -out results/ -ref genome.dat`
**Explanation:** Processes multiple read files.