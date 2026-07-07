---
name: drep
category: assembly
description: "De-replication of microbial genomes assembled from multiple samples."
tags: [drep, assembly, microbial-genomes, genome-dereplication]
author: oxo-call-community
source_url: "https://drep.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: dRep is a tool for de-replicating microbial genomes assembled from multiple samples to identify unique genome representatives.
- **Core Function**: Identifies and removes redundant genomes from a collection of assembled microbial genomes.
- **Input/Output**: Input: Assembled genomes (FASTA). Output: Non-redundant genome set, clustering results.
- **Algorithm**: Uses ANI (Average Nucleotide Identity) to cluster and select representative genomes.
- **Key Features**: Fast ANI calculation, hierarchical clustering, customizable thresholds, quality-based ranking.
- **Installation**: `conda install -c bioconda drep`

## Pitfalls

- **Quality Thresholds**: Poor quality genomes can affect clustering results.
- **ANI Threshold**: Default ANI threshold (99%) may need adjustment for specific use cases.
- **Memory Usage**: Large genome collections may require significant memory.
- **Contamination**: Contaminated genomes can skew clustering results.
- **Completeness**: Incomplete genomes may not cluster correctly.

## Examples

### Basic dereplication
**Args:** `dereplicate --genomes genomes/ --output results/`
**Explanation:** De-replicates a directory of genome assemblies.

### Custom ANI threshold
**Args:** `dereplicate --genomes genomes/ --output results/ --ani 95`
**Explanation:** Uses 95% ANI threshold for genome clustering.

### Include quality filtering
**Args:** `dereplicate --genomes genomes/ --output results/ --checkm`
**Explanation:** Runs CheckM for genome quality assessment before dereplication.

### Cluster only
**Args:** `cluster --genomes genomes/ --output clusters/`
**Explanation:** Only performs clustering without dereplication.

### Compare genomes
**Args:** `compare --genome1 ref.fasta --genome2 query.fasta --output comparison.txt`
**Explanation:** Compares two genomes and outputs similarity metrics.