---
name: sumaclust
category: clustering
description: Sumaclust clusters sequences using the same algorithm as UCLUST and CD-HIT, fast and exact at the same time.
tags: [sumaclust, sequence-clustering, uclust, cd-hit]
author: oxo-call-community
source_url: "https://git.metabarcoding.org/obitools/sumaclust/wikis/home"
---

## Concepts

- **Tool Overview**: sumaclust (v1.0.31) is a tool for clustering sequences using UCLUST/CD-HIT algorithm.
- **Core Function**: Clusters sequences based on similarity thresholds.
- **Algorithm**: Uses greedy clustering with identity threshold for sequence clustering.
- **Input/Output**: Input: FASTA sequences; Output: Clustered sequences with centroids.
- **Applications**: Metabarcoding, sequence clustering, OTU picking, sequence analysis.
- **Installation**: `conda install -c bioconda sumaclust` or download from GitLab.

## Pitfalls

- **Sequence Quality**: Low-quality sequences affect clustering.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Clustering large datasets can be slow.
- **Parameter Tuning**: Incorrect identity threshold affects results.
- **Input Format**: Requires FASTA format input.
- **Duplicate Sequences**: Duplicates may affect clustering.

## Examples

### Display help
**Args:** `sumaclust --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta`
**Explanation:** Cluster sequences with default parameters.

### With identity threshold
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta -s 0.97`
**Explanation:** Cluster sequences with 97% identity threshold.

### Verbose mode
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta --stats`
**Explanation:** Generate statistics about clustering.

### Batch processing
**Args:** `sumaclust -i fastas/ -o results/`
**Explanation:** Process multiple FASTA files together.

### Filter by length
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta -m 100`
**Explanation:** Minimum sequence length of 100.

### Include singletons
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta --singletons`
**Explanation:** Include singleton sequences in output.

### Generate report
**Args:** `sumaclust -i sequences.fasta -o clusters.fasta --report`
**Explanation:** Generate comprehensive HTML report.
