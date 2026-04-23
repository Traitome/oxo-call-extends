---
name: bfc
category: qc
description: BFC - High-performance error correction for Illumina sequencing data
tags: [error-correction, illumina, k-mer, quality-control]
author: oxo-call-community
source_url: "https://github.com/lh3/bfc"
---

## Concepts
- **Tool Overview**: BFC (Bloom Filter Corrector) is a standalone, high-performance tool for correcting sequencing errors in Illumina short-read data. It uses a non-greedy algorithm based on spectrum alignment and blocked Bloom filters for k-mer counting.
- **Algorithm**: BFC performs exhaustive search to find a path through k-mers that minimizes a heuristic objective function combining error correction penalty, quality penalty, and k-mer support penalty.
- **K-mer Counting**: Uses blocked Bloom filters to filter singleton k-mers (likely errors), storing remaining k-mers in a hash table.
- **Trimming Mode**: BFC can also operate in trimming mode, which is ~4x faster and trims reads to the longest fragment supported by k-mers.
- **Performance**: Designed for high-coverage human whole-genome data but works well on smaller genomes too.

## Pitfalls
- **Genome Size Parameter**: The `-s` parameter (genome size) must be specified accurately for proper memory allocation. Underestimating causes memory issues; overestimating wastes memory.
- **Coverage Requirement**: BFC works best with high coverage (>30x). Low-coverage data may not benefit from error correction.
- **Read Length**: Assumes Illumina short reads. Not suitable for long reads (PacBio, Nanopore).
- **Parameter Order**: Some parameters are order-sensitive. Do not swap `-s` and `-k` order.

## Examples
### Basic error correction
**Args:** `bfc -s 3g -t 16 reads.fq.gz | gzip -1 > corrected.fq.gz`
**Explanation:** Corrects errors in reads using 3GB genome size estimate and 16 threads.

### Correct one read set using another
**Args:** `bfc -s 3g -t 16 reference.fq.gz target.fq.gz | gzip -1 > corrected.fq.gz`
**Explanation:** Uses reference.fq.gz to build k-mer set, then corrects target.fq.gz.

### Trimming mode (faster)
**Args:** `bfc -1 -s 3g -k 51 -t 16 reads.fq.gz | gzip -1 > trimmed.fq.gz`
**Explanation:** Trims reads to longest fragment supported by k-mers (4x faster than correction).

### Process from compressed input
**Args:** `bfc -s 3g -t 16 <(bzip2 -dc reads.fq.bz2) | gzip -1 > corrected.fq.gz`
**Explanation:** Corrects reads from bzip2-compressed input using process substitution.

### Small genome correction
**Args:** `bfc -s 10m -k 21 -t 8 bacteria.fq.gz | gzip -1 > corrected.fq.gz`
**Explanation:** Corrects bacterial genome reads with 10MB genome size and k-mer length 21.
