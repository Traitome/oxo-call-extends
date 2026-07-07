---
name: forwardgenomics
category: programming
description: Forward Genomics is a framework to associate phenotypic differences between species to differences in their genomes.
tags: [forwardgenomics, comparative genomics, phenotype-genotype association]
author: oxo-call-community
source_url: "https://github.com/hillerlab/ForwardGenomics"
---

## Concepts
- **Comparative Genomics**: Analyzes genomic differences across species.
- **Phenotype-Genotype Association**: Links phenotypic traits to genomic regions.
- **Phylogenetic Correction**: Accounts for evolutionary relationships.
- **Whole-Genome Analysis**: Scans entire genomes for candidate regions.
- **Functional Annotation**: Integrates functional genomic data.

## Pitfalls
- **Phylogenetic Dependency**: Results depend on accurate phylogenetic trees.
- **Sample Size**: Requires sufficient species sampling for statistical power.
- **Genome Quality**: Relies on high-quality genome assemblies.
- **False Positives**: May identify spurious associations without proper correction.
- **Computational Requirements**: Whole-genome analysis is computationally intensive.

## Examples
### Run forward genomics analysis
**Args:** `forwardgenomics --genomes genomes/ --phenotypes phenotypes.txt --output results/`
**Explanation:** Runs Forward Genomics analysis on genomic and phenotypic data.

### With phylogenetic tree
**Args:** `forwardgenomics --genomes genomes/ --phenotypes phenotypes.txt --tree species.tree --output results/`
**Explanation:** Runs analysis with a specified phylogenetic tree.

### Functional enrichment
**Args:** `forwardgenomics enrich --regions candidates.bed --annotations go_terms.gff --output enrichment.txt`
**Explanation:** Performs functional enrichment analysis on candidate regions.

### Permutation testing
**Args:** `forwardgenomics --genomes genomes/ --phenotypes phenotypes.txt --permutations 1000 --output results/`
**Explanation:** Runs permutation testing to assess significance.

### Visualization
**Args:** `forwardgenomics plot --results results/ --output manhattan.png`
**Explanation:** Generates a Manhattan plot of results.