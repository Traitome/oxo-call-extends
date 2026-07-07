---
name: fmlrc
category: formatting
description: A long-read error correction tool using the multi-string Burrows Wheeler Transform.
tags: [fmlrc, error correction, long reads, BWT, PacBio]
author: oxo-call-community
source_url: "https://github.com/holtjma/fmlrc"
---

## Concepts
- **Multi-string BWT**: Uses a specialized BWT index built from multiple sequences to enable efficient error correction.
- **Hybrid Correction**: Combines short-read data with long-read data for accurate error correction.
- **Seed-and-Extend**: Identifies seed matches between long reads and the BWT index, then extends to full-length correction.
- **Quality Value Preservation**: Maintains or improves quality scores in corrected reads.
- **Iterative Correction**: Supports multiple rounds of correction for progressively improving read accuracy.

## Pitfalls
- **Computational Intensity**: Building the BWT index requires significant computational resources for large datasets.
- **Illumina Dependency**: Requires paired-end Illumina reads as the reference for correction.
- **Read Length Limitations**: May struggle with extremely long reads (>100kb) due to memory constraints.
- **Installation Complexity**: Requires compiling from source with specific dependencies.
- **Output Size**: Corrected reads can be significantly larger than input due to quality score recalculation.

## Examples
### Basic error correction
**Args:** `fmlrc -s short_reads.fastq -l long_reads.fastq -o corrected.fastq`
**Explanation:** Corrects long reads using short reads as the reference, outputting corrected reads.

### Iterative correction with multiple passes
**Args:** `fmlrc -s short_reads.fastq -l long_reads.fastq -o corrected.fastq -i 3`
**Explanation:** Performs 3 iterations of error correction for higher accuracy.

### Correct with specific k-mer size
**Args:** `fmlrc -s short_reads.fastq -l long_reads.fastq -o corrected.fastq -k 25`
**Explanation:** Uses k-mer size 25 for matching, suitable for reads with higher error rates.

### Output in FASTA format
**Args:** `fmlrc -s short_reads.fastq -l long_reads.fastq -o corrected.fasta -f`
**Explanation:** Outputs corrected reads in FASTA format instead of FASTQ.

### Verbose mode for debugging
**Args:** `fmlrc -s short_reads.fastq -l long_reads.fastq -o corrected.fastq -v`
**Explanation:** Runs in verbose mode, providing detailed output about the correction process.