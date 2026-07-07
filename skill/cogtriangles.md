---
name: cogtriangles
category: assembly
description: Low-polynomial algorithm for assembling clusters of orthologous groups from intergenomic symmetric best matches
tags: [cogtriangles, orthologous-groups, comparative-genomics, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://ftp.ncbi.nih.gov/pub/wolf/COGs/COGsoft"
---

## Concepts

- **Tool Overview**: cogtriangles is a tool for assembling Clusters of Orthologous Groups (COGs) from intergenomic symmetric best matches using a low-polynomial algorithm.
- **Core Function**: Identifies orthologous gene clusters across multiple genomes by analyzing symmetric best match relationships.
- **Algorithm**: Uses graph-based approach with triangle detection to group orthologous sequences efficiently.
- **Input**: Sequence similarity data or BLAST results between genomes.
- **Output**: Clusters of orthologous genes with group assignments.
- **Application**: Comparative genomics, gene family analysis, and evolutionary studies.
- **Installation**: Install via bioconda: `conda install -c bioconda cogtriangles`

## Pitfalls

- **Sequence Quality**: Requires high-quality sequence data for accurate orthology detection.
- **Genome Selection**: Results depend on the set of genomes included.
- **Similarity Threshold**: May require tuning of similarity cutoffs.
- **Computational Resources**: May require significant resources for large datasets.
- **Orthology Definition**: Relies on symmetric best match definition of orthology.

## Examples

### Build COG clusters
**Args:** `cogtriangles -i blast_results.txt -o cog_clusters.txt`
**Explanation:** Assembles COG clusters from BLAST results.

### With custom threshold
**Args:** `cogtriangles -i blast_results.txt -t 1e-10 -o cog_clusters.txt`
**Explanation:** Sets E-value threshold to 1e-10 for more stringent clustering.

### Multiple genomes
**Args:** `cogtriangles -i genome1_vs_genome2.txt genome1_vs_genome3.txt -o cog_clusters.txt`
**Explanation:** Processes multiple pairwise comparison files.

### Display help
**Args:** `cogtriangles --help`
**Explanation:** Shows all available options and usage information.