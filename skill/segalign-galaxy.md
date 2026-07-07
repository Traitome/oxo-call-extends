---
name: segalign-galaxy
category: alignment
description: SegAlign-Galaxy - GPU-based whole genome aligner for Galaxy
tags: ["segalign-galaxy", "alignment", "GPU", "Galaxy"]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/SegAlign"
---

## Concepts

- **Tool Overview**: SegAlign-Galaxy (v0.1.2.7) is the Galaxy integration of SegAlign GPU-based aligner.
- **Core Function**: Aligns sequencing reads to reference genomes within Galaxy environment.
- **Algorithm**: Uses parallel computing on GPU for fast alignment.
- **Input/Output**: Accepts FASTQ reads and produces SAM/BAM alignments.
- **Galaxy Integration**: Designed for use within Galaxy workflow system.
- **Applications**: Whole-genome sequencing alignment in Galaxy workflows.

## Pitfalls

- **GPU Requirements**: Requires compatible GPU hardware on Galaxy server.
- **Galaxy Environment**: Requires proper Galaxy configuration.
- **Software Dependencies**: Requires GPU drivers and CUDA toolkit.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Index**: Requires pre-built index for reference genome.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Basic alignment
**Args:** `segalign-galaxy -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** `-i` input FASTQ; `-r` reference genome; `-o` output SAM.

### BAM output
**Args:** `segalign-galaxy -i reads.fastq -r reference.fasta -o alignments.bam --bam`
**Explanation:** Outputs BAM format instead of SAM.

### GPU selection
**Args:** `segalign-galaxy -i reads.fastq -r reference.fasta -g 0 -o alignments.sam`
**Explanation:** `-g 0` uses GPU device 0.

### Verbose logging
**Args:** `segalign-galaxy -i reads.fastq -r reference.fasta -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `segalign-galaxy -i reads.fastq -r reference.fasta -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 CPU threads.

### Quality filtering
**Args:** `segalign-galaxy -i reads.fastq -r reference.fasta -q 20 -o alignments.sam`
**Explanation:** `-q 20` filters reads with quality below 20.

### Help command
**Args:** `segalign-galaxy --help`
**Explanation:** Shows available commands and options.