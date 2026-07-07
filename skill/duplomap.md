---
name: duplomap
category: alignment
description: "Tool designed to improve precision and recall of long-read alignments in segmental duplications."
tags: [duplomap, alignment, long-reads, segmental-duplications, mapping]
author: oxo-call-community
source_url: "https://gitlab.com/tprodanov/duplomap"
---

## Concepts

- **Tool Overview**: DuploMap is a tool for improving the precision and recall of long-read alignments in segmental duplications.
- **Core Function**: Resolves ambiguous alignments in repetitive genomic regions using long-read data.
- **Input/Output**: Input: Long-read alignments (BAM), reference genome (FASTA). Output: Improved alignments (BAM).
- **Algorithm**: Uses read-specific information to disambiguate alignments in segmental duplications.
- **Key Features**: Segmental duplication handling, improved precision/recall, long-read optimized, parallel processing.
- **Installation**: `conda install -c bioconda duplomap`

## Pitfalls

- **Read Quality**: Poor quality reads can produce ambiguous alignments.
- **Duplication Complexity**: Highly similar duplications may still be challenging to resolve.
- **Coverage Depth**: Low coverage reduces disambiguation accuracy.
- **Reference Quality**: Reference genome quality affects alignment improvement.
- **Computational Cost**: Processing large duplication regions can be computationally intensive.

## Examples

### Basic alignment improvement
**Args:** `--input aligned.bam --ref ref.fa --output improved.bam`
**Explanation:** Improves alignments in segmental duplication regions.

### With custom parameters
**Args:** `--input aligned.bam --ref ref.fa --output improved.bam --min-mapq 20`
**Explanation:** Sets minimum mapping quality threshold to 20.

### Parallel processing
**Args:** `--input aligned.bam --ref ref.fa --output improved.bam --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Specific regions
**Args:** `--input aligned.bam --ref ref.fa --output improved.bam --regions regions.bed`
**Explanation:** Only processes specified genomic regions.

### Generate statistics
**Args:** `--input aligned.bam --ref ref.fa --output improved.bam --stats stats.txt`
**Explanation:** Generates statistics about alignment improvements.