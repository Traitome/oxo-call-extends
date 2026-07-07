---
name: csem
category: alignment
description: ChIP-Seq multi-read allocation using Expectation-Maximization
tags: [csem, alignment, BAM, ChIP-Seq, multi-mapping, EM-algorithm]
author: oxo-call-community
source_url: "http://deweylab.biostat.wisc.edu/csem/"
---

## Concepts

- **Tool Overview**: csem (v2.4+) is a computational tool for ChIP-Seq multi-read allocation using an Expectation-Maximization (EM) algorithm.
- **Core Function**: Uses probabilistic reallocation to assign multi-mapping reads across genomic regions, improving peak calling accuracy by properly handling ambiguous reads.
- **Input/Output**: Input: BAM/SAM alignment files, genome annotation. Output: Reallocated BAM file with probability weights, quantification statistics.
- **Algorithm**: Implements an EM algorithm that iteratively estimates read assignment probabilities based on local read density and sequence context.
- **Key Features**: Handles both single-end and paired-end reads, supports strand-specific protocols, outputs posterior probabilities for each read assignment.
- **Installation**: `conda install -c bioconda csem`

## Pitfalls

- **Multi-Mapping Reads**: Requires BAM files with multi-mapping reads (MAPQ=0 or similar); pre-filtered alignments may reduce effectiveness.
- **Annotation Dependencies**: Performance depends on quality of genome annotation; fragmented annotations may affect results.
- **Memory Usage**: Large genomes or deep sequencing datasets may require significant memory for EM iterations.
- **Convergence**: EM algorithm may require many iterations to converge; use `--max-iter` to limit computation time.
- **Output Interpretation**: Posterior probabilities should be used for downstream analysis rather than hard assignments.

## Examples

### Run CSEM on aligned reads
**Args:** `csem -i input.bam -g genes.gtf -o output.bam`
**Explanation:** Process aligned ChIP-Seq reads and probabilistically reallocate multi-mapping reads based on gene annotations.

### Set maximum iterations
**Args:** `csem -i input.bam -g genes.gtf -o output.bam --max-iter 50`
**Explanation:** Limit EM algorithm to 50 iterations to reduce computation time for large datasets.

### Output probability scores
**Args:** `csem -i input.bam -g genes.gtf -o output.bam --output-probs probs.txt`
**Explanation:** Generate a text file with posterior probabilities for each read assignment.
