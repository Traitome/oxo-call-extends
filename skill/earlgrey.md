---
name: earlgrey
category: assembly
description: "Earl Grey: A fully automated TE curation and annotation pipeline."
tags: [earlgrey, assembly, transposable-elements, TE-annotation, genome-annotation]
author: oxo-call-community
source_url: "https://github.com/TobyBaril/EarlGrey/blob/v7.2.1/README.md"
---

## Concepts

- **Tool Overview**: Earl Grey is a fully automated transposable element (TE) curation and annotation pipeline.
- **Core Function**: Identifies, classifies, and annotates transposable elements in genome assemblies.
- **Input/Output**: Input: Genome assembly (FASTA). Output: TE annotations (GFF), consensus sequences, statistics.
- **Algorithm**: Combines multiple TE detection tools with BEAT consensus elongation process.
- **Key Features**: De novo TE annotation, consensus sequence refinement, TE classification, visualization support.
- **Installation**: `conda install -c bioconda earlgrey`

## Pitfalls

- **Genome Quality**: Requires high-quality genome assembly for accurate TE annotation.
- **Computation Time**: Comprehensive TE analysis can be computationally intensive.
- **Memory Usage**: Large genomes may require significant RAM.
- **TE Database**: Custom TE databases may improve annotation specificity.
- **False Positives**: May identify non-TE sequences as transposable elements.

## Examples

### Basic TE annotation
**Args:** `--genome genome.fa --output annotations.gff`
**Explanation:** Annotates transposable elements in genome assembly.

### With custom database
**Args:** `--genome genome.fa --output annotations.gff --te-db custom_te.fasta`
**Explanation:** Uses custom TE database for annotation.

### Generate consensus sequences
**Args:** `--genome genome.fa --output annotations.gff --consensus consensus.fasta`
**Explanation:** Generates consensus sequences for identified TE families.

### Include statistics
**Args:** `--genome genome.fa --output annotations.gff --stats stats.txt`
**Explanation:** Generates detailed statistics about TE content.

### Visualization
**Args:** `--genome genome.fa --output annotations.gff --plot te_plot.png`
**Explanation:** Generates visualization of TE distribution across the genome.