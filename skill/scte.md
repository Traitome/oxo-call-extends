---
name: scte
category: alignment
description: scTE - Genome index building for alignment of reads to genes and transposable elements
tags: ["scte", "alignment", "TE-analysis", "RNA-seq"]
author: oxo-call-community
source_url: "https://github.com/JiekaiLab/scTE"
---

## Concepts

- **Tool Overview**: scTE (v1.0.0) builds genome indices for fast alignment of reads to genes and transposable elements.
- **Core Function**: Creates indices for mapping reads to both genes and transposable elements.
- **Algorithm**: Uses custom indexing for efficient read mapping.
- **Input/Output**: Accepts genome sequences and produces indexed databases.
- **TE Analysis**: Specifically designed for transposable element analysis in RNA-seq data.
- **Applications**: RNA-seq analysis, transposable element expression, and gene expression profiling.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Index Building Time**: May require long index building times.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Genome Compatibility**: Requires compatible genome sequences.
- **Documentation**: Some features have limited documentation.

## Examples

### Build index
**Args:** `scte build -i genome.fasta -t te_annotations.gtf -o index/`
**Explanation:** `-i` genome FASTA; `-t` TE annotations; `-o` index directory.

### Align reads
**Args:** `scte align -i reads.fastq -x index/ -o alignments.sam`
**Explanation:** `-i` input reads; `-x` index directory; `-o` output SAM.

### BAM output
**Args:** `scte align -i reads.fastq -x index/ -o alignments.bam --bam`
**Explanation:** Outputs BAM format instead of SAM.

### Verbose logging
**Args:** `scte align -i reads.fastq -x index/ -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `scte align -i reads.fastq -x index/ -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Count reads
**Args:** `scte count -i alignments.bam -o counts.tsv`
**Explanation:** Counts reads per feature.

### Quality filtering
**Args:** `scte align -i reads.fastq -x index/ -q 20 -o alignments.sam`
**Explanation:** `-q 20` filters reads with quality below 20.