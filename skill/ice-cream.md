---
name: ice-cream
category: bioinformatics
description: "ICEcream: Integrative and Conjugative Elements Classification and gRaphical gEne Arrangement Method."
tags: [ice-cream, bioinformatics, ICE, mobile-genetic-elements, genomics]
author: oxo-call-community
source_url: "https://github.com/xinehc/ice-cream"
---
## Concepts

- **Tool Overview**: ICEcream (v3.0.0) is a computational tool for the classification and visualization of Integrative and Conjugative Elements (ICEs) in bacterial genomes.
- **Integrative Conjugative Elements**: Mobile genetic elements that integrate into host chromosomes and can transfer horizontally via conjugation.
- **ICE Classification**: Categorizes ICEs based on their integrase type, conjugation machinery, and accessory gene content.
- **Gene Arrangement Visualization**: Generates graphical representations of ICE gene organization and synteny.
- **Comprehensive Analysis**: Identifies ICE boundaries, core modules, and auxiliary genes.
- **Installation**: `conda install -c bioconda ice-cream`

## Pitfalls

- **Genome Assembly Quality**: Requires complete or high-quality draft genomes for accurate ICE detection.
- **Integrase Identification**: Relies on integrase detection; divergent integrases may be missed.
- **False Positives**: May incorrectly identify genomic islands as ICEs without conjugation genes.
- **Database Dependencies**: Performance depends on the completeness of reference ICE databases.
- **Large Genomes**: Memory-intensive for very large bacterial genomes or metagenomic assemblies.
- **Annotation Quality**: Requires properly annotated genomes with gene predictions.

## Examples

### Predict ICEs in a genome
**Args:** `ice-cream --genome genome.fasta --out ice_results`
**Explanation:** Identifies and classifies ICEs in the input genome sequence.

### With gene annotation
**Args:** `ice-cream --genome genome.fasta --gff genome.gff --out ice_results`
**Explanation:** Uses provided GFF annotation to improve ICE detection accuracy.

### Visualize ICE structure
**Args:** `ice-cream --genome genome.fasta --visualize --out ice_visualization`
**Explanation:** Generates graphical representations of predicted ICE gene arrangements.

### Compare multiple genomes
**Args:** `ice-cream --genomes genome1.fasta genome2.fasta --compare --out comparison_results`
**Explanation:** Compares ICE content across multiple bacterial genomes.

### Export ICE sequences
**Args:** `ice-cream --genome genome.fasta --extract --out ice_sequences/`
**Explanation:** Extracts complete ICE sequences and saves them as separate FASTA files.