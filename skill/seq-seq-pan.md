---
name: seq-seq-pan
category: alignment
description: seq-seq-pan - Sequence-to-sequence pan-genome alignment
tags: ["seq-seq-pan", "alignment", "pan-genome"]
author: oxo-call-community
source_url: "https://gitlab.com/chrjan/seq-seq-pan"
---

## Concepts

- **Tool Overview**: seq-seq-pan (v1.1.0) performs sequence-to-sequence pan-genome alignment.
- **Core Function**: Aligns sequences against pan-genome references.
- **Algorithm**: Implements efficient alignment algorithms for pan-genome analysis.
- **Input/Output**: Accepts FASTA sequences and produces alignment results.
- **Pan-genome Analysis**: Focuses on aligning sequences to pan-genome references.
- **Applications**: Comparative genomics, pan-genome analysis, and variant discovery.

## Pitfalls

- **Memory Usage**: High memory requirements for large pan-genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Database**: Requires pan-genome reference.
- **Input Quality**: Results depend on input sequence quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Align sequences
**Args:** `seq-seq-pan -i query.fasta -r pan-genome.fasta -o alignments.sam`
**Explanation:** `-i` query sequences; `-r` pan-genome reference; `-o` output SAM.

### With threads
**Args:** `seq-seq-pan -i query.fasta -r pan-genome.fasta -t 8 -o alignments.sam`
**Explanation:** `-t 8` uses 8 threads.

### Verbose logging
**Args:** `seq-seq-pan -i query.fasta -r pan-genome.fasta -v -o alignments.sam`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seq-seq-pan --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seq-seq-pan --version`
**Explanation:** Shows current version.

### Output BAM
**Args:** `seq-seq-pan -i query.fasta -r pan-genome.fasta -b -o alignments.bam`
**Explanation:** `-b` outputs BAM format.

### Index reference
**Args:** `seq-seq-pan index -r pan-genome.fasta`
**Explanation:** Creates index for pan-genome reference.