---
name: slclust
category: population-genomics
description: A utility that performs single-linkage clustering with the option of applying a Jaccard similarity coefficient to break weakly bound clusters into distinct clusters
tags: [slclust, population-genomics, clustering, Jaccard]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/slclust"
---

## Concepts

- **Tool Overview**: slclust (v02022010) - A single-linkage clustering tool for population genetics data
- **Core Function**: Performs hierarchical clustering using single-linkage method with Jaccard similarity option
- **Input/Output**: Accepts distance matrices or VCF files; outputs cluster assignments and dendrograms
- **Algorithm**: Implements agglomerative hierarchical clustering with single-linkage criterion
- **Installation**: `conda install -c bioconda slclust`
- **Key Features**: Supports Jaccard similarity for breaking weak clusters; handles large datasets

## Pitfalls

- **Input Format**: Requires specific input format (distance matrix or VCF)
- **Distance Threshold**: Appropriate threshold selection is critical for meaningful clusters
- **Chain Effect**: Single-linkage can form chain-like clusters; use Jaccard option to mitigate
- **Memory Usage**: Large datasets may require significant memory
- **Computation Time**: O(n^3) complexity for large datasets
- **Output Interpretation**: Cluster results require careful biological interpretation

## Examples

### Display help
**Args:** `slclust --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `slclust -i distance_matrix.txt -o clusters.txt`
**Explanation:** Perform single-linkage clustering on distance matrix.

### With Jaccard coefficient
**Args:** `slclust -i distance_matrix.txt -j -o clusters.txt`
**Explanation:** Apply Jaccard similarity to break weakly bound clusters.

### From VCF file
**Args:** `slclust -v variants.vcf -o clusters.txt`
**Explanation:** Perform clustering directly from VCF file.

### Specify threshold
**Args:** `slclust -i distance_matrix.txt -t 0.1 -o clusters.txt`
**Explanation:** Set distance threshold for clustering.

### Generate dendrogram
**Args:** `slclust -i distance_matrix.txt -d dendrogram.nwk -o clusters.txt`
**Explanation:** Output dendrogram in Newick format.

### Batch processing
**Args:** `slclust -d input_dir/ -o output_dir/`
**Explanation:** Process multiple distance matrices in batch.