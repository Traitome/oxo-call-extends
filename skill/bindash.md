---
name: bindash
category: metagenomics
description: Fast comparison of genomes and metagenomes on a typical personal laptop
tags: [genome-comparison, metagenomics, minhash, distance]
author: oxo-call-community
source_url: "https://github.com/zhaoxiaofei/bindash"
---

## Concepts
- **Tool Overview**: BinDash is a fast and precise tool for comparing genomes and metagenomes (terabytes of data) on a typical personal laptop. It uses MinHash-based sketching for efficient similarity estimation.
- **MinHash**: Uses MinHash signatures (dimension-reduced sketches) to estimate Jaccard similarity between sequence sets.
- **Performance**: Can process terabytes of sequencing data with minimal memory footprint.
- **Applications**: Genome clustering, metagenome comparison, duplicate detection, phylogeny estimation.

## Pitfalls
- **Sketch Size**: Smaller sketches are faster but less accurate. Choose appropriate sketch size for your accuracy needs.
- **K-mer Size**: K-mer size affects specificity. Larger k-mers are more specific to species/strains.
- **False Positives**: MinHash is an approximation; results may differ from exact methods.

## Examples
### Sketch a genome
**Args:** `bindash sketch -i genome.fa -o genome.sketch`
**Explanation:** Creates a MinHash sketch of a genome for fast comparison.

### Compare multiple genomes
**Args:** `bindash compare -i sketches/ -o distance_matrix.tsv`
**Explanation:** Computes pairwise distances between all sketches.

### Query against database
**Args:** `bindash query -q query.sketch -d database.sketches -o matches.tsv`
**Explanation:** Finds closest matches to a query genome.
