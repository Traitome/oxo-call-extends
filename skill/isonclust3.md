---
name: isonclust3
category: expression
description: De novo clustering of long transcript reads into genes, third generation implementation.
tags: [isonclust3, expression, long reads, transcriptomics, clustering]
author: oxo-call-community
source_url: "https://github.com/aljpetri/isONclust3"
---

## Concepts

- **De Novo Clustering**: Groups long transcriptomic reads into clusters representing distinct genes without reference genome.
- **Third-Generation Algorithm**: Improved clustering algorithm with enhanced accuracy and performance compared to previous versions.
- **Nanopore Optimization**: Specifically optimized for Oxford Nanopore sequencing data characteristics.
- **Read Overlap Detection**: Identifies overlapping reads to determine transcript boundaries.
- **Isoform Resolution**: Distinguishes between different isoforms of the same gene.
- **Scalable Processing**: Handles large datasets efficiently with optimized memory usage.

## Pitfalls

- **Read Length Variation**: Highly variable read lengths can affect clustering accuracy.
- **Error Rate Sensitivity**: High error rates in long reads may lead to incorrect clustering.
- **Computational Requirements**: Large datasets require significant computational resources.
- **Memory Constraints**: Processing millions of reads may exceed available memory.
- **Transcript Complexity**: Complex transcriptomes with many isoforms may be challenging to resolve.
- **Parameter Tuning**: Optimal parameters may vary between datasets and require experimentation.

## Examples

### Basic clustering
**Args:** `isonclust3 --reads reads.fastq --output clusters/`
**Explanation:** Performs de novo clustering of long transcriptomic reads into gene clusters.

### With quality filtering
**Args:** `isonclust3 --reads reads.fastq --min-quality 15 --output clusters/`
**Explanation:** Filters reads by quality before clustering to improve accuracy.

### Specify k-mer size
**Args:** `isonclust3 --reads reads.fastq --kmer-size 15 --output clusters/`
**Explanation:** Uses custom k-mer size for read comparison and clustering.

### Parallel processing
**Args:** `isonclust3 --reads reads.fastq --threads 8 --output clusters/`
**Explanation:** Uses multiple threads for faster clustering.

### Generate statistics
**Args:** `isonclust3 --reads reads.fastq --output clusters/ --stats`
**Explanation:** Generates clustering statistics and quality metrics.

### Batch processing
**Args:** `isonclust3 --batch samples.txt --output-dir results/`
**Explanation:** Processes multiple samples specified in a batch file.