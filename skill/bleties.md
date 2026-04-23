---
name: bleties
category: annotation
description: Basic Long-read Enabled Toolkit for Interspersed DNA Elimination Studies
tags: [bleties, long-read, transposon, annotation, elimination]
author: oxo-call-community
source_url: "https://github.com/Swart-lab/bleties"
---

## Concepts

- **Tool Overview**: BleTIES analyzes DNA elimination events using long-read sequencing data.
- **Core Function**: Identifies and characterizes interspersed DNA elimination in ciliates and other organisms.
- **Input**: Long-read sequencing data (PacBio/ONT) and reference genome.
- **Output**: Elimination sites, sequence features, and analysis reports.
- **Application**: Study programmed DNA elimination in ciliates and similar phenomena.
- **Installation**: Install via bioconda: `conda install -c bioconda bleties`

## Pitfalls

- **Long Reads Required**: Designed for long-read data; short reads not suitable.
- **Reference Genome**: Requires well-annotated reference for accurate analysis.
- **Organism Specific**: Primarily designed for ciliate studies; may need adaptation.
- **Memory Usage**: Large genomes require significant memory for alignment.

## Examples

### Analyze elimination sites
**Args:** `bleties -r reads.fq -g genome.fa -o elimination_results`
**Explanation:** Identifies DNA elimination sites from long-read data.

### Specify minimum coverage
**Args:** `bleties -r reads.fq -g genome.fa -c 10 -o results`
**Explanation:** Requires minimum 10x coverage for elimination site calling.

### Output GFF format
**Args:** `bleties -r reads.fq -g genome.fa --gff -o elimination.gff`
**Explanation:** Outputs elimination sites in GFF format for visualization.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
