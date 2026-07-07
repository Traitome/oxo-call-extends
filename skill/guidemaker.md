---
name: guidemaker
category: bioinformatics
description: GuideMaker designs gRNA pools for CRISPR-Cas systems in non-model and model genomes.
tags: [guidemaker, CRISPR, gRNA-design, bioinformatics]
author: oxo-call-community
source_url: "https://guidemaker.org/"
---

## Concepts

- **gRNA Design**: GuideMaker designs guide RNAs for CRISPR-Cas systems.

- **Non-model Genomes**: Supports gRNA design in non-model organisms.

- **Multiple Cas Types**: Supports various CRISPR-Cas systems (Cas9, Cas12, etc.).

- **Off-target Prediction**: Predicts potential off-target sites.

- **Efficiency Scoring**: Scores gRNA efficiency based on multiple criteria.

- **Pool Design**: Designs optimal gRNA pools for screening experiments.

## Pitfalls

- **Genome Quality**: Results depend on genome assembly quality.

- **Off-target Effects**: Off-target sites may cause unintended edits.

- **gRNA Efficiency**: Not all designed gRNAs are equally effective.

- **Cas System Compatibility**: Ensure compatibility with target Cas system.

- **Library Size**: Large gRNA libraries may require significant resources.

## Examples

### Design gRNAs
**Args:** `guidemaker -i genome.fasta -o grnas.txt`
**Explanation:** Designs gRNAs for a genome.

### Target specific regions
**Args:** `guidemaker -i genome.fasta -t targets.bed -o grnas.txt`
**Explanation:** Designs gRNAs for specific genomic regions.

### Specify Cas type
**Args:** `guidemaker -i genome.fasta -c cas12a -o grnas.txt`
**Explanation:** Designs gRNAs for Cas12a system.

### Include off-target analysis
**Args:** `guidemaker -i genome.fasta -o grnas.txt -off`
**Explanation:** Includes off-target prediction in output.

### Batch processing
**Args:** `for f in *.fasta; do guidemaker -i $f -o ${f%.fasta}_grnas.txt; done`
**Explanation:** Processes multiple genomes.

### Filter by efficiency
**Args:** `guidemaker -i genome.fasta -e 0.7 -o grnas.txt`
**Explanation:** Filters gRNAs by minimum efficiency score.

### Help command
**Args:** `guidemaker --help`
**Explanation:** Shows available options and usage information.