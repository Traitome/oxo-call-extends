---
name: minimap
category: alignment
description: Experimental tool to find approximate mapping positions between long sequences
tags: [minimap, alignment, long-read]
author: oxo-call-community
source_url: "https://github.com/lh3/minimap"
---

## Concepts

- **Tool Overview**: Minimap v0.2 finds approximate mapping positions between long sequences.
- **Core Function**: Maps long sequences to reference sequences.
- **Approximate Mapping**: Uses approximate matching for speed.
- **Long-read Support**: Designed for long sequencing reads.
- **Input/Output**: Accepts long sequences; outputs mapping positions.
- **Seed-based Alignment**: Uses seed-based approach for fast mapping.

## Pitfalls

- **Experimental**: This is an experimental tool.
- **Long-read Specific**: Designed for long sequencing reads.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large reference genomes.
- **Parameter Tuning**: May require parameter adjustment for optimal mapping.
- **Accuracy Trade-off**: Speed may come at the cost of accuracy.

## Examples

### Map long reads
**Args:** `minimap reference.fasta reads.fastq > mappings.paf`
**Explanation:** Maps long reads to reference genome.

### With custom parameters
**Args:** `minimap -k 15 reference.fasta reads.fastq > mappings.paf`
**Explanation:** Uses k-mer size of 15 for mapping.

### Paired-end mapping
**Args:** `minimap reference.fasta reads_1.fastq reads_2.fastq > mappings.paf`
**Explanation:** Processes paired-end long reads.

### Batch processing
**Args:** `minimap reference.fasta fastq/*.fastq > mappings.paf`
**Explanation:** Processes multiple read files.

### Generate SAM output
**Args:** `minimap -a reference.fasta reads.fastq > mappings.sam`
**Explanation:** Generates SAM format output.