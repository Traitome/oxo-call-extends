---
name: bigmap
category: metagenomics
description: BiG-MAP - Biosynthetic Gene cluster Meta'omics Abundance Profiler
tags: [bgc, biosynthetic-gene-cluster, metagenomics, abundance]
author: oxo-call-community
source_url: "https://github.com/medema-group/BiG-MAP"
---

## Concepts
- **Tool Overview**: BiG-MAP (Biosynthetic Gene cluster Meta'omics Abundance Profiler) profiles the abundance of Biosynthetic Gene Clusters (BGCs) across metagenomic samples. It quantifies BGC presence and expression in microbiome data.
- **BGC Profiling**: Maps metagenomic or metatranscriptomic reads to BGC reference databases to quantify BGC abundance across samples.
- **Applications**: Discovering BGC distribution across environments, identifying active secondary metabolite pathways, and comparing biosynthetic potential between communities.
- **Workflow**: Index BGC database → Map reads → Quantify abundance → Statistical comparison.

## Pitfalls
- **Database Dependency**: Requires a curated BGC database (e.g., MIBiG) for reference.
- **Read Mapping**: Short reads may not uniquely map to specific BGCs due to shared domains.
- **Normalization**: Abundance values need normalization for sample comparison (e.g., by sequencing depth).

## Examples
### Profile BGC abundance
**Args:** `bigmap profile -i metagenomes/ -d mibig_bgc_db -o abundance.tsv`
**Explanation:** Profiles BGC abundance across metagenomic samples against MIBiG database.

### Compare BGC distribution
**Args:** `bigmap compare -i abundance.tsv -m metadata.tsv -o comparison/`
**Explanation:** Compares BGC abundance profiles between sample groups.
