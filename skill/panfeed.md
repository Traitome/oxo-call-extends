---
name: panfeed
category: hpc
description: PanFeed computes gene-cluster specific k-mers over a pangenome.
tags: [panfeed, hpc, pangenome, k-mers]
author: oxo-call-community
source_url: "https://github.com/microbial-pangenomes-lab/panfeed"
---

## Concepts

- **Tool Overview**: PanFeed extracts k-mers specific to gene clusters in pangenomes.
- **Core Function**: Identifies gene-cluster specific k-mers for analysis.
- **Algorithm**: Uses k-mer counting and clustering algorithms.
- **Input Format**: Accepts pangenome sequences and gene cluster annotations.
- **Output**: Produces k-mer lists and cluster-specific signatures.
- **Use Case**: Pangenome analysis, metagenomics, and gene identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **k-mer Size**: Results depend on k-mer size selection.
- **Cluster Quality**: Results depend on input cluster quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `panfeed --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `panfeed -i pangenome.fasta -c clusters.txt -o kmers.txt`
**Explanation:** Computes gene-cluster specific k-mers.

### k-mer size
**Args:** `panfeed -k 31 -i pangenome.fasta -c clusters.txt -o kmers.txt`
**Explanation:** Uses k-mer size of 31.

### Verbose mode
**Args:** `panfeed -v -i pangenome.fasta -c clusters.txt -o kmers.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `panfeed -t 8 -i pangenome.fasta -c clusters.txt -o kmers.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `panfeed -i pangenome.fasta -c clusters.txt -o kmers.json --json`
**Explanation:** Outputs in JSON format.

### Filter by frequency
**Args:** `panfeed -m 10 -i pangenome.fasta -c clusters.txt -o kmers.txt`
**Explanation:** Filters by minimum frequency.