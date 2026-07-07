---
name: hormon
category: annotation
description: A tool for annotation of alpha satellite arrays in centromeres of a newly assembled human genome
tags: [hormon, centromere, annotation, alpha_satellite, HOR]
author: oxo-call-community
source_url: "https://github.com/ablab/HORmon"
---

## Concepts

- **Centromere Annotation**: Automated annotation of human centromeric regions in genome assemblies
- **Alpha Satellite Arrays**: Specialized analysis of alpha satellite DNA repeats (approximately 170 bp monomers)
- **HOR Inference**: Higher-Order Repeat detection and characterization in centromeric regions
- **Monomer Decomposition**: Transformation of centromere sequences into monomer-based representation
- **T2T Genome Support**: Optimized for telomere-to-telomere complete genome assemblies
- **Integrated Framework**: Combines monomer and HOR inference into a unified algorithm

## Pitfalls

- **Assembly Quality**: Requires high-quality, complete genome assemblies with minimal gaps
- **Computational Complexity**: Analysis of large centromeric regions can be computationally intensive
- **Repeat Complexity**: Highly repetitive nature of centromeres can challenge alignment algorithms
- **Reference Dependence**: Results may vary based on the reference genome used
- **Memory Requirements**: Large centromeric sequences require significant memory resources
- **Annotation Validation**: Manual validation often required for complex centromeric structures

## Examples

### Basic centromere annotation
**Args:** `hormon -i genome.fasta -o centromere_annotation.gff`
**Explanation:** Runs HORmon to annotate alpha satellite arrays in a genome assembly.

### HOR inference only
**Args:** `hormon -i genome.fasta -o hor_results/ --mode hor`
**Explanation:** Runs only the HOR inference module without full monomer decomposition.

### Monomer decomposition only
**Args:** `hormon -i genome.fasta -o monomer_results/ --mode monomer`
**Explanation:** Performs monomer decomposition analysis on centromeric regions.

### Custom k-mer size
**Args:** `hormon -i genome.fasta -o results/ -k 21`
**Explanation:** Uses custom k-mer size (21) for repeat detection, useful for specific research questions.

### Output in BED format
**Args:** `hormon -i genome.fasta -o centromere.bed --format bed`
**Explanation:** Generates output in BED format for easy visualization in genome browsers.