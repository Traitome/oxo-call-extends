---
name: fg-stitch
category: alignment
description: "An aligner for long reads against one or more reference/expected vector/plasmid/construct(s)."
tags: [fg-stitch, alignment, long-reads, vector, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/stitch"
---

## Concepts

- **Tool Overview**: fg-stitch is an aligner designed for mapping long reads against reference vectors, plasmids, or constructs.
- **Core Function**: Aligns long reads to reference vector sequences.
- **Input/Output**: Input: Long reads, reference vectors. Output: Alignments, mappings.
- **Algorithm**: Uses efficient alignment algorithms for long reads.
- **Key Features**: Long read alignment, vector mapping, plasmid detection, construct verification, high accuracy.
- **Installation**: `conda install -c bioconda fg-stitch`

## Pitfalls

- **Read Length**: Optimized for long reads.
- **Reference Quality**: Requires accurate reference sequences.
- **Memory Usage**: Large datasets may require significant memory.
- **Alignment Parameters**: May require parameter tuning.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic alignment
**Args:** `fg-stitch -r reads.fastq -f vector.fasta -o alignments.sam`
**Explanation:** Aligns reads to vector sequence.

### Multiple references
**Args:** `fg-stitch -r reads.fastq -f vectors/ -o results/`
**Explanation:** Aligns to multiple reference vectors.

### Specify construct
**Args:** `fg-stitch -r reads.fastq -c construct.fasta -o results/`
**Explanation:** Maps to specific construct.

### Paired-end mode
**Args:** `fg-stitch -1 reads_1.fastq -2 reads_2.fastq -f vector.fasta -o results/`
**Explanation:** Processes paired-end reads.

### Detailed output
**Args:** `fg-stitch -r reads.fastq -f vector.fasta -o results/ --detailed`
**Explanation:** Generates detailed alignment report.