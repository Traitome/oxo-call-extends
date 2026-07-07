---
name: spclust
category: sequence-analysis
description: SpCLUST - Spectral clustering for biological sequences
tags: [spclust, sequence-analysis, clustering, spectral, biological-sequences]
author: oxo-call-community
source_url: "https://github.com/johnymatar/SpCLUST/"
---

## Concepts

- **Tool Overview**: spclust (v28.5.19) - A spectral clustering tool
- **Core Function**: Performs spectral clustering on biological sequences
- **Input/Output**: Accepts sequence data; outputs cluster assignments
- **Algorithm**: Spectral clustering algorithm for sequences
- **Installation**: `conda install -c bioconda spclust`
- **Key Features**: Spectral clustering, sequence analysis, biological data

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence data
- **Similarity Matrix**: Requires similarity matrix computation
- **Cluster Number**: Number of clusters must be specified
- **Memory Usage**: Large sequence sets require significant memory
- **Output Format**: Output format depends on configuration
- **Cluster Quality**: Cluster quality depends on similarity measure

## Examples

### Display help
**Args:** `spclust --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5`
**Explanation:** Perform spectral clustering on sequences.

### With similarity measure
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5 --similarity jaccard`
**Explanation:** Use specific similarity measure.

### With multiple clusters
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 10`
**Explanation:** Set number of clusters.

### Output detailed results
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5 --detailed`
**Explanation:** Output detailed cluster information.

### Output similarity matrix
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5 --matrix`
**Explanation:** Output similarity matrix.

### Output statistics
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5 --stats`
**Explanation:** Output clustering statistics.

### Generate report
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5 --report`
**Explanation:** Generate clustering report.

### With threads
**Args:** `spclust -i sequences.fasta -o clusters.txt -k 5 -p 8`
**Explanation:** Use multiple threads for clustering.