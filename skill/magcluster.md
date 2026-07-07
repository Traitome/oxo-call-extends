---
name: magcluster
category: annotation
description: Magnetosome gene cluster identification, annotation and visualization tool
tags: [magcluster, annotation, magnetosome, genomics]
author: oxo-call-community
source_url: "https://github.com/runjiaji/magcluster"
---

## Concepts

- **Tool Overview**: magcluster v0.2.5 - A tool for identifying, annotating, and visualizing magnetosome gene clusters in bacterial genomes.
- **Core Function**: Detects magnetosome gene clusters and provides comprehensive annotation and visualization.
- **Input/Output**: Input: Genomic sequence files (FASTA/GenBank); Output: Annotation files, visualization images, cluster information.
- **Installation**: `conda install -c bioconda magcluster`
- **Magnetosome Genes**: Identifies genes involved in magnetosome formation (e.g., mam, mms genes).
- **Visualization**: Generates circular and linear visualizations of magnetosome clusters.

## Pitfalls

- **Genome Quality**: Poorly assembled genomes may contain fragmented clusters.
- **Database Updates**: Outdated magnetosome gene databases may miss novel genes.
- **False Positives**: Similar genes may be incorrectly identified as magnetosome genes.
- **Annotation Quality**: Depends on reference database completeness.
- **Memory Usage**: Large genomes may require significant memory.
- **Output Formats**: Multiple output files require careful organization.

## Examples

### Identify magnetosome clusters
**Args:** `magcluster -i genome.fasta -o output_dir`
**Explanation:** Identifies and annotates magnetosome gene clusters in the input genome.

### With GenBank input
**Args:** `magcluster -i genome.gbk -o output_dir -f genbank`
**Explanation:** Processes GenBank formatted input file.

### Custom database
**Args:** `magcluster -i genome.fasta -d custom_db.fasta -o output_dir`
**Explanation:** Uses custom magnetosome gene database for identification.

### Generate visualization
**Args:** `magcluster -i genome.fasta -o output_dir --plot`
**Explanation:** Generates visualizations of detected clusters.

### Verbose mode
**Args:** `magcluster -i genome.fasta -o output_dir -v`
**Explanation:** Provides detailed logging during analysis.

### Minimum cluster size
**Args:** `magcluster -i genome.fasta -o output_dir -m 5`
**Explanation:** Sets minimum number of genes per cluster to 5.