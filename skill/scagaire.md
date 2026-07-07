---
name: scagaire
category: annotation
description: Scagaire - filter gene predictions from metagenomic samples by bacterial/pathogenic species
tags: ["scagaire", "annotation", "metagenomics", "filtering"]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/scagaire"
---

## Concepts

- **Tool Overview**: Scagaire (v0.0.4) allows filtering gene predictions from metagenomic samples by bacterial/pathogenic species.
- **Core Function**: Filters gene annotations based on taxonomic classification to identify genes from specific bacterial or pathogenic species.
- **Algorithm**: Uses sequence similarity searches against reference databases to classify and filter genes.
- **Input/Output**: Accepts gene prediction files (GFF/FASTA) and produces filtered annotations.
- **Taxonomic Filtering**: Enables filtering by specific species, genera, or taxonomic groups.
- **Applications**: Metagenomic analysis, pathogen detection, and functional annotation filtering.

## Pitfalls

- **Database Dependencies**: Requires reference databases for taxonomic classification.
- **Sequence Similarity**: Results depend on sequence similarity thresholds.
- **False Positives**: May include false positive matches to closely related species.
- **Database Updates**: Requires regular database updates for accurate classification.
- **Computational Resources**: Sequence searches can be computationally intensive.
- **Memory Usage**: High memory requirements for large databases.

## Examples

### Basic filtering
**Args:** `scagaire -i genes.fasta -o filtered_genes.fasta -s "Escherichia coli"`
**Explanation:** `-i` input genes FASTA; `-o` filtered output; `-s` species filter.

### Multiple species
**Args:** `scagaire -i genes.fasta -o filtered_genes.fasta -s "Escherichia coli,Saccharomyces cerevisiae"`
**Explanation:** Filters genes from multiple species separated by commas.

### Taxonomic rank filtering
**Args:** `scagaire -i genes.fasta -o filtered_genes.fasta -r genus -s "Escherichia"`
**Explanation:** `-r genus` filters at genus level instead of species.

### With GFF input
**Args:** `scagaire -i genes.gff -g genome.fasta -o filtered.gff -s "Salmonella"`
**Explanation:** `-g` genome FASTA required for GFF input.

### Minimum identity
**Args:** `scagaire -i genes.fasta -o filtered_genes.fasta -s "E. coli" -id 90`
**Explanation:** `-id 90` requires minimum 90% identity match.

### Verbose output
**Args:** `scagaire -i genes.fasta -o filtered_genes.fasta -s "E. coli" -v`
**Explanation:** `-v` enables verbose logging for debugging.

### Output statistics
**Args:** `scagaire -i genes.fasta -o filtered_genes.fasta -s "E. coli" --stats stats.txt`
**Explanation:** `--stats` generates statistics report.