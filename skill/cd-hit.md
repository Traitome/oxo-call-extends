---
name: cd-hit
category: formatting
description: Clusters and compares protein or nucleotide sequences by similarity
tags: [cd-hit, clustering, redundancy, protein, nucleotide, sequence]
author: oxo-call-community
source_url: "https://github.com/weizhongli/cdhit"
---

## Concepts

- **Tool Overview**: CD-HIT is a widely used program for clustering protein and nucleotide sequences by similarity. It uses a greedy incremental clustering algorithm that is extremely fast and memory-efficient.
- **Core Function**: Groups sequences into clusters based on a user-defined similarity threshold, selecting a representative sequence for each cluster.
- **Input/Output**: Input: FASTA format sequences. Output: Clustered FASTA file and .clstr file listing cluster membership.
- **Programs**: `cd-hit` (protein), `cd-hit-est` (nucleotide), `cd-hit-2d` (compare two protein sets), `cd-hit-est-2d` (compare two nucleotide sets), `psi-cd-hit.pl` (low-threshold ~25%).
- **Word Length (-n)**: Determines clustering speed. Must match similarity threshold: higher threshold = longer word length = faster clustering.
- **Memory Control**: Use `-M` to limit memory usage; `-B 1` to store sequences on disk for large datasets.

## Pitfalls

- **Word Length Must Match Threshold**: Using wrong `-n` value produces incorrect results. For proteins: `-n 5` for 0.7-1.0, `-n 4` for 0.6-0.7. For nucleotides: `-n 8-10` for 0.9-1.0, `-n 7` for 0.88-0.9.
- **Global vs Local Similarity**: Default `-G 1` uses global similarity. For domain-based clustering, use `-G 0` (local similarity) with coverage options (`-aL`, `-aS`).
- **Sequence Order Matters**: CD-HIT processes sequences in input order; the first sequence in a cluster becomes the representative. Sort by length (longest first) for best results.
- **Memory Overflow**: Large datasets may exceed `-M` limit. Increase value or use `-B 1` to use disk storage.
- **Incremental Clustering**: Use `cd-hit-2d` to add new sequences to existing clusters without re-running from scratch.

## Examples

### Cluster protein sequences at 90% identity
**Args:** `-i proteins.fa -o proteins_90.fa -c 0.9 -n 5 -M 4000`
**Explanation:** Clusters protein sequences at 90% similarity with word length 5 (appropriate for this threshold), using up to 4GB memory.

### Cluster nucleotide sequences at 95% identity
**Args:** `cd-hit-est -i transcripts.fa -o transcripts_95.fa -c 0.95 -n 8 -M 4000`
**Explanation:** Uses cd-hit-est for DNA/RNA sequences at 95% identity with word length 8, suitable for transcript deduplication.

### Cluster at 100% identity to remove exact duplicates
**Args:** `-i proteins.fa -o proteins_100.fa -c 1.0 -n 5 -M 2000`
**Explanation:** Removes exact duplicate sequences by clustering at 100% identity threshold.

### Compare two protein datasets
**Args:** `cd-hit-2d -i db1.fa -i2 db2.fa -o db2_novel.fa -c 0.9 -n 5`
**Explanation:** Finds sequences in db2 that are novel (not similar at 90% to any sequence in db1), useful for incremental database updates.

### Cluster with coverage requirements
**Args:** `-i proteins.fa -o proteins_90.fa -c 0.9 -n 5 -aL 0.8 -aS 0.8`
**Explanation:** Requires both longer and shorter sequences to have at least 80% alignment coverage, preventing short sequences from clustering with long ones based on partial matches.

### Cluster nucleotides with both strands
**Args:** `cd-hit-est -i ests.fa -o ests_95.fa -c 0.95 -n 8 -r 1`
**Explanation:** Compares both forward and reverse complement strands (-r 1), important for EST clustering where strand orientation may vary.

### Hierarchical clustering at multiple thresholds
**Args:** `-i nr.fa -o nr80.fa -c 0.8 -n 5 -M 8000`
**Explanation:** First step of hierarchical clustering at 80% identity. Output nr80.fa can then be clustered at lower thresholds (e.g., 60%).

### Low-threshold clustering with PSI-CD-HIT
**Args:** `psi-cd-hit.pl -i nr60.fa -o nr30.fa -c 0.3`
**Explanation:** Clusters at 30% identity using PSI-BLAST approach, suitable for remote homology detection.

### Parallel execution on multiple hosts
**Args:** `cd-hit-para.pl -i nr90.fa -o nr60.fa -c 0.6 -n 4 -B hosts.txt -S 64`
**Explanation:** Runs CD-HIT in parallel across multiple hosts listed in hosts.txt, splitting input into 64 chunks for distributed processing.
