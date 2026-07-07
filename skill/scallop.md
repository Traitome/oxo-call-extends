---
name: scallop
category: expression
description: Scallop - reference-based transcriptome assembler for RNA-seq
tags: ["scallop", "expression", "RNA-seq", "transcript-assembly"]
author: oxo-call-community
source_url: "https://github.com/Kingsford-Group/scallop"
---

## Concepts

- **Tool Overview**: Scallop (v0.10.5) is a reference-based transcriptome assembler for RNA-seq data, designed to accurately reconstruct transcript structures.
- **Core Function**: Assembles transcripts from short-read RNA-seq data aligned to a reference genome.
- **Algorithm**: Uses a novel graph-based approach to reconstruct transcripts with high accuracy.
- **Input/Output**: Accepts BAM alignment files and produces GTF transcript annotations.
- **Sensitivity**: Designed to detect both common and rare transcript isoforms.
- **Applications**: Transcriptome profiling, alternative splicing analysis, and gene discovery.

## Pitfalls

- **Reference Dependence**: Requires high-quality reference genome.
- **Alignment Quality**: Results depend on mapping quality of short reads.
- **Read Depth**: May miss lowly expressed transcripts.
- **Complexity**: May struggle with highly complex gene loci.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Computational Resources**: High memory usage for large datasets.

## Examples

### Basic transcript assembly
**Args:** `scallop -i alignments.bam -o transcripts.gtf`
**Explanation:** `-i` input BAM file; `-o` output GTF with assembled transcripts.

### With annotation guidance
**Args:** `scallop -i alignments.bam -a annotation.gtf -o transcripts.gtf`
**Explanation:** `-a` provides existing annotation as guidance.

### Strand-specific protocol
**Args:** `scallop -i alignments.bam -o transcripts.gtf -s`
**Explanation:** `-s` enables strand-specific assembly.

### Minimum coverage
**Args:** `scallop -i alignments.bam -o transcripts.gtf -c 2`
**Explanation:** `-c 2` requires minimum 2 read coverage.

### Maximum intron length
**Args:** `scallop -i alignments.bam -o transcripts.gtf -maxintron 500000`
**Explanation:** `-maxintron 500000` sets maximum intron length to 500kb.

### Verbose output
**Args:** `scallop -i alignments.bam -o transcripts.gtf -v`
**Explanation:** `-v` enables verbose logging for debugging.

### Output statistics
**Args:** `scallop -i alignments.bam -o transcripts.gtf --stats stats.txt`
**Explanation:** `--stats` generates assembly statistics report.