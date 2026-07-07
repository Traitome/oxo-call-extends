---
name: swarm
category: clustering
description: Robust and fast clustering method for amplicon-based studies like 16S rRNA sequencing.
tags: [swarm, clustering, amplicon, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/torognes/swarm/blob/v3.1.6/man/swarm_manual.pdf"
---

## Concepts

- **Tool Overview**: swarm (v3.1.6) clusters amplicon sequences for microbial community analysis.
- **Core Function**: Groups similar sequences into operational taxonomic units (OTUs).
- **Algorithm**: Uses single-linkage clustering with abundance-based greedy approach.
- **Input/Output**: Input: FASTA/Q sequences; Output: OTU clusters.
- **Applications**: Microbiome analysis, 16S sequencing, amplicon clustering.
- **Installation**: `conda install -c bioconda swarm` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large sequence sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect clustering.
- **Sequence Quality**: Poor quality sequences affect clustering.
- **Duplicate Sequences**: May require dereplication first.
- **Output Format**: May require conversion for downstream analysis.

## Examples

### Display help
**Args:** `swarm --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `swarm -i sequences.fasta -o clusters.txt`
**Explanation:** Cluster amplicon sequences.

### With distance threshold
**Args:** `swarm -i sequences.fasta -o clusters.txt -d 1`
**Explanation:** Use distance threshold of 1.

### Verbose mode
**Args:** `swarm -i sequences.fasta -o clusters.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `swarm -i sequences.fasta -o clusters.txt --stats`
**Explanation:** Generate statistics about clustering.

### Batch processing
**Args:** `for f in fastqs/*.fasta; do swarm -i $f -o clusters/${f%.fasta}.txt; done`
**Explanation:** Process multiple sequence files together.

### Filter by abundance
**Args:** `swarm -i sequences.fasta -o clusters.txt -a 10`
**Explanation:** Minimum abundance threshold of 10.

### Include all clusters
**Args:** `swarm -i sequences.fasta -o clusters.txt --all`
**Explanation:** Output all clusters including singletons.

### Generate report
**Args:** `swarm -i sequences.fasta -o clusters.txt --report`
**Explanation:** Generate comprehensive clustering report.
