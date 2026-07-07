---
name: coinfinder
category: utility
description: Identification of coincident genes in pangenomes
tags: [coinfinder, pangenomics, gene-association, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/fwhelan/coinfinder"
---

## Concepts

- **Tool Overview**: Coinfinder is a tool for identifying coincident (associating and dissociating) genes in pangenomes, helping to understand gene co-occurrence patterns across multiple genomes.
- **Core Function**: Analyzes pangenome data to identify genes that tend to appear together (associating) or mutually exclude each other (dissociating).
- **Algorithm**: Uses statistical methods to detect significant gene-gene associations based on presence/absence patterns across genomes.
- **Input**: Pangenome matrix with gene presence/absence information.
- **Output**: Gene-gene association scores and significance values.
- **Application**: Pangenome analysis, microbial genomics, and gene function prediction.
- **Installation**: Install via bioconda: `conda install -c bioconda coinfinder`

## Pitfalls

- **Data Quality**: Requires high-quality pangenome annotations.
- **Genome Selection**: Results depend on the set of genomes included.
- **Statistical Threshold**: May require adjustment of significance thresholds.
- **Computational Resources**: May require significant resources for large pangenomes.
- **Gene Annotation**: Relies on consistent gene annotation across genomes.

## Examples

### Analyze pangenome associations
**Args:** `coinfinder -i pangenome_matrix.txt -o associations.txt`
**Explanation:** Identifies coincident genes from pangenome matrix.

### With custom significance threshold
**Args:** `coinfinder -i pangenome_matrix.txt -p 0.05 -o associations.txt`
**Explanation:** Sets significance threshold to 0.05.

### Include dissociation analysis
**Args:** `coinfinder -i pangenome_matrix.txt -d -o associations.txt`
**Explanation:** Includes dissociating gene pairs in analysis.

### Display help
**Args:** `coinfinder --help`
**Explanation:** Shows all available options and usage information.