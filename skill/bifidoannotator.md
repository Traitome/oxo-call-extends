---
name: bifidoannotator
category: annotation
description: Fine-grained annotation of bifidobacterial enzymes involved in human-milk glycan utilization
tags: [bifidobacterium, glycoside-hydrolase, annotation, hmg]
author: oxo-call-community
source_url: "https://github.com/nicholaspucci/bifidoAnnotator"
---

## Concepts
- **Tool Overview**: bifidoAnnotator performs hierarchical annotation of bifidobacterial glycoside hydrolase (GH)-encoding genes using MMseqs2. It includes optional transporter annotation, HMG-utilization row annotation, cluster filtering, and publication-ready heatmap generation.
- **Bifidobacteria**: Important gut commensals known for their ability to utilize human milk glycans (HMGs), a key factor in infant gut colonization.
- **Annotation Hierarchy**: Uses a tiered approach with MMseqs2 for rapid homology search against curated GH databases.
- **Output**: Generates annotated heatmaps suitable for publication, showing GH gene presence/absence across strains.

## Pitfalls
- **Database Dependency**: Requires MMseqs2 and appropriate GH databases.
- **Scope**: Specifically designed for bifidobacterial GH genes; may not generalize to other taxa.
- **HMG Focus**: Annotation is focused on HMG utilization pathways.

## Examples
### Annotate bifidobacterial genomes
**Args:** `bifidoannotator annotate -i genomes/ -o results/`
**Explanation:** Annotates GH-encoding genes across bifidobacterial genomes.

### Generate heatmap
**Args:** `bifidoannotator heatmap -i annotations.tsv -o heatmap.pdf`
**Explanation:** Generates a publication-ready heatmap of GH gene annotations.
