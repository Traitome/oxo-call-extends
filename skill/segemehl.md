---
name: segemehl
category: alignment
description: segemehl - Short read mapping with gaps
tags: ["segemehl", "alignment", "short-read", "gapped-alignment"]
author: oxo-call-community
source_url: "http://www.bioinf.uni-leipzig.de/Software/segemehl"
---

## Concepts

- **Tool Overview**: segemehl (v0.3.4) performs short read mapping with gap support.
- **Core Function**: Aligns short sequencing reads to reference genomes with gap handling.
- **Algorithm**: Uses seed-and-extend approach with gap-aware alignment.
- **Input/Output**: Accepts FASTQ reads and produces SAM/BAM alignments.
- **Gap Support**: Specifically designed for gapped alignment scenarios.
- **Applications**: RNA-seq alignment, spliced read mapping, and variant calling.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Index**: Requires pre-built index for reference genome.
- **Gap Sensitivity**: Gap parameters affect alignment sensitivity.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Basic alignment
**Args:** `segemehl -i reads.fastq -d reference.fasta -o alignments.sam`
**Explanation:** `-i` input FASTQ; `-d` reference genome; `-o` output SAM.

### Build index
**Args:** `segemehl -x reference.fasta -o index`
**Explanation:** Builds index for reference genome.

### Use existing index
**Args:** `segemehl -i reads.fastq -x index -o alignments.sam`
**Explanation:** Uses pre-built index for faster alignment.

### Verbose logging
**Args:** `segemehl -i reads.fastq -d reference.fasta -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `segemehl -i reads.fastq -d reference.fasta -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Quality filtering
**Args:** `segemehl -i reads.fastq -d reference.fasta -q 20 -o alignments.sam`
**Explanation:** `-q 20` filters reads with quality below 20.

### Help command
**Args:** `segemehl --help`
**Explanation:** Shows available commands and options.