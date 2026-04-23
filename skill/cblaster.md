---
name: cblaster
category: annotation
description: Find clustered gene hits from BLAST searches for biosynthetic gene cluster analysis
tags: [cblaster, blast, gene-cluster, biosynthetic, annotation]
author: oxo-call-community
source_url: "https://github.com/gamcil/cblaster"
---

## Concepts

- **Tool Overview**: cblaster finds clustered gene hits from BLAST searches for biosynthetic gene cluster analysis.
- **Core Function**: Identifies groups of homologous genes that are co-located in genomes.
- **Algorithm**: Searches NCBI databases or local BLAST results for gene clusters.
- **Input**: Protein sequences of interest or BLAST results.
- **Output**: Clustered hit summaries and visualizations.
- **Application**: Biosynthetic gene cluster discovery and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cblaster`

## Pitfalls

- **Network Required**: Remote search requires internet connection to NCBI.
- **Session Management**: Long searches can be saved and resumed.
- **Clustering Parameters**: Adjust distance and score thresholds for cluster detection.
- **Database Choice**: Choose appropriate NCBI database for search.

## Examples

### Search for gene clusters remotely
**Args:** `cblaster search -q query_proteins.fa -s session.json`
**Explanation:** Searches NCBI for clustered hits matching query protein sequences.

### Search with specific database
**Args:** `cblaster search -q query.fa -db nr -s session.json`
**Explanation:** Searches NCBI nr database for gene clusters.

### Visualize results
**Args:** `cblaster plot -s session.json -o clusters.png`
**Explanation:** Generates cluster visualization from search results.

### Extract sequences from clusters
**Args:** `cblaster extract -s session.json -o cluster_sequences.fa`
**Explanation:** Extracts protein sequences from identified gene clusters.

### Resume interrupted search
**Args:** `cblaster search -s session.json --resume`
**Explanation:** Resumes a previously interrupted search session.

### Display help
**Args:** `cblaster --help`
**Explanation:** Shows all available options and usage information.
