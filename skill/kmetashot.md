---
name: kmetashot
category: metagenomics
description: Fast taxonomic classifier for metagenome bins/MAGs based on k-mer/minimizer
tags: [kmetashot, metagenomics, taxonomic-classification, MAGs, k-mer]
author: oxo-call-community
source_url: "https://github.com/gdefazio/kMetaShot"
---

## Concepts

- **Taxonomic Classification**: Classifies metagenome-assembled genomes (MAGs) taxonomically
- **K-mer Based**: Uses k-mer and minimizer signatures for classification
- **MAG Analysis**: Specialized for analyzing metagenome-assembled genomes
- **Fast Classification**: Provides rapid taxonomic assignments
- **Reference Database**: Compares against curated reference genomes
- **Bin Quality**: Handles bins of varying quality levels

## Pitfalls

- **Database Completeness**: Limited by reference database coverage
- **Bin Quality**: Low-quality bins may have incorrect taxonomic assignments
- **Novel Organisms**: May misclassify novel or poorly characterized taxa
- **Chimeric Bins**: Chimeric bins cause incorrect classifications
- **Strain-level Resolution**: Limited ability to resolve strain-level differences
- **Contamination**: Contaminated bins affect classification accuracy

## Examples

### Classify MAGs
**Args:** `kmetashot -i bins/ -o taxonomy.tsv`
**Explanation:** Classifies all MAGs in a directory.

### Single bin classification
**Args:** `kmetashot -i bin.fasta -o result.tsv`
**Explanation:** Classifies a single MAG bin.

### With custom database
**Args:** `kmetashot -i bins/ -d custom_db/ -o taxonomy.tsv`
**Explanation:** Uses custom reference database for classification.

### Specify k-mer size
**Args:** `kmetashot -i bins/ -k 31 -o taxonomy.tsv`
**Explanation:** Uses k-mer size of 31 for classification.

### Verbose output
**Args:** `kmetashot -i bins/ -o taxonomy.tsv -v`
**Explanation:** Provides detailed classification information.

### Confidence filtering
**Args:** `kmetashot -i bins/ -o taxonomy.tsv --min-confidence 0.8`
**Explanation:** Only reports classifications with >= 80% confidence.