---
name: bio-ting
category: annotation
description: Cluster T cell receptor repertoires by antigen-specificity
tags: [tcr, immune-repertoire, clustering, antigen-specificity]
author: oxo-call-community
source_url: "https://github.com/FelixMoelder/ting"
---

## Concepts
- **Tool Overview**: ting is a tool for clustering large-scale T cell receptor (TCR) repertoires by antigen-specificity. It groups TCRs that recognize similar antigens.
- **TCR Clustering**: Uses sequence similarity and structural features to cluster TCRs with similar antigen specificity.
- **Applications**: Immune repertoire analysis, vaccine response studies, autoimmune disease research.

## Pitfalls
- **Ground Truth**: Antigen specificity validation requires experimental data.
- **Sequence Similarity**: Sequence-based clustering may miss structurally similar but sequence-divergent TCRs.

## Examples
### Cluster TCR sequences
**Args:** `ting cluster -i tcr_sequences.tsv -o clusters.tsv`
**Explanation:** Clusters TCR sequences by predicted antigen specificity.
