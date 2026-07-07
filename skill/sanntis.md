---
name: sanntis
category: annotation
description: SMBGC Annotation using Neural Networks Trained on Interpro Signatures
tags: ["sanntis", "annotation", "BGC", "biosynthetic-gene-clusters"]
author: oxo-call-community
source_url: "https://github.com/Finn-Lab/SanntiS"
---

## Concepts

- **Tool Overview**: SanntiS (v0.9.4.1) is a tool for annotating Secondary Metabolite Biosynthetic Gene Clusters (SMBGCs) using neural networks trained on InterPro signatures.
- **Core Function**: Identifies and classifies biosynthetic gene clusters in genomic and metagenomic data through machine learning.
- **Algorithm**: Uses deep neural networks to predict BGC types based on protein domain composition from InterProScan annotations.
- **Input Requirements**: Requires Prodigal-predicted proteins and InterProScan results for accurate BGC identification.
- **Output Formats**: Generates GFF files with annotated BGC regions and their predicted product types.
- **Applications**: Enables discovery of novel secondary metabolites from microbial genomes and metagenomes.

## Pitfalls

- **InterProScan Dependency**: Requires prior InterProScan analysis, which is computationally intensive.
- **Training Data Bias**: Model trained on known BGCs may miss novel or divergent clusters.
- **False Positives**: May incorrectly annotate non-BGC regions containing similar protein domains.
- **Metagenome Challenges**: Fragmented metagenomic assemblies reduce prediction accuracy.
- **Parameter Sensitivity**: Detection thresholds significantly impact recall/precision trade-off.
- **Limited Taxonomic Scope**: Performance may vary across different microbial taxa.

## Examples

### Basic BGC annotation
**Args:** `sanntis annotate -i proteins.faa -p interpro.tsv -o bgc_annotations.gff`
**Explanation:** `-i` input protein FASTA; `-p` InterProScan TSV output; `-o` output GFF with BGC annotations.

### Build GenBank file
**Args:** `sanntis build-gbk -i genome.fasta -g genes.gff -o genome.gbk`
**Explanation:** Constructs a GenBank file from genome FASTA and gene predictions for BGC analysis.

### Metagenome mode
**Args:** `sanntis annotate -i metagenome.faa -p interpro.tsv -m -o metagenome_bgc.gff`
**Explanation:** `-m` enables metagenome mode for fragmented sequence analysis.

### Custom threshold
**Args:** `sanntis annotate -i proteins.faa -p interpro.tsv -t 0.7 -o bgc.gff`
**Explanation:** `-t 0.7` sets confidence threshold to 70% for BGC predictions.

### Output detailed report
**Args:** `sanntis annotate -i proteins.faa -p interpro.tsv -o bgc.gff -r report.txt`
**Explanation:** `-r` generates a detailed summary report of predicted BGCs with classification statistics.

### Batch processing
**Args:** `sanntis annotate -i ./proteins/ -p ./interpro/ -o ./bgc_results/`
**Explanation:** Processes multiple genomes in batch mode from input directories.

### Visualize BGC architecture
**Args:** `sanntis visualize -g bgc.gff -i proteins.faa -o bgc_visualization.png`
**Explanation:** Generates visual representation of predicted BGC structures.