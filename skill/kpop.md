---
name: kpop
category: comparative-genomics
description: Assembly-free and scalable microbial genome comparison using k-mer spectra
tags: [kpop, comparative-genomics, k-mer, microbial, assembly-free]
author: oxo-call-community
source_url: "https://github.com/PaoloRibeca/KPop"
---

## Concepts

- **Assembly-free Analysis**: Compares genomes without assembly
- **K-mer Spectra**: Uses full k-mer spectra for comparison
- **Scalable Method**: Handles large-scale genome comparisons
- **Microbial Genomics**: Specialized for microbial genome analysis
- **Dataset Transformations**: Applies dataset-specific transformations
- **Whole Genome Comparison**: Compares complete genome content

## Pitfalls

- **K-mer Size Selection**: K-mer size affects comparison resolution
- **Database Size**: Large genome collections require more resources
- **Strain-level Resolution**: May miss subtle strain-level differences
- **Horizontal Transfer**: HGT can confound species identification
- **Repetitive Elements**: Repetitive sequences affect k-mer counts
- **Computational Resources**: Large comparisons need significant memory

## Examples

### Compare genomes
**Args:** `kpop compare -i genome1.fna -i genome2.fna -k 31 -o comparison.txt`
**Explanation:** Compares two microbial genomes using k-mers.

### Batch comparison
**Args:** `kpop batch -d genomes/ -o results/`
**Explanation:** Compares multiple genomes in batch mode.

### Specify k-mer size
**Args:** `kpop compare -i genome1.fna -i genome2.fna -k 51 -o results.txt`
**Explanation:** Uses k-mer size of 51 for comparison.

### Generate distance matrix
**Args:** `kpop distance -i genomes.txt -o distance_matrix.tsv`
**Explanation:** Generates pairwise distance matrix.

### Transform spectra
**Args:** `kpop transform -i spectrum.txt -m normalization -o transformed.txt`
**Explanation:** Applies transformation to k-mer spectra.

### Cluster genomes
**Args:** `kpop cluster -i distance_matrix.tsv -o clusters.txt`
**Explanation:** Clusters genomes based on k-mer distances.