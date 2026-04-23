---
name: binge
category: annotation
description: Clustering transcripts based on locus orthology
tags: [transcript-clustering, orthology, gene-families]
author: oxo-call-community
source_url: "https://github.com/zkstewart/BINge"
---

## Concepts
- **Tool Overview**: BINge clusters transcripts based on locus orthology, grouping transcripts that belong to the same gene family or locus.
- **Orthology Clustering**: Groups transcripts by evolutionary relationship, identifying orthologous and paralogous relationships.
- **Applications**: Gene family identification, transcriptome annotation, comparative transcriptomics.

## Pitfalls
- **Sequence Similarity Threshold**: Clustering threshold affects grouping granularity.
- **Complex Gene Families**: Highly divergent or nested gene families may be challenging to cluster correctly.

## Examples
### Cluster transcripts
**Args:** `binge cluster -i transcripts.fa -o clusters.tsv`
**Explanation:** Clusters transcripts into orthologous groups.

### Specify similarity threshold
**Args:** `binge cluster -i transcripts.fa -t 0.8 -o clusters.tsv`
**Explanation:** Uses 80% similarity threshold for clustering.
