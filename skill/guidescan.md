---
name: guidescan
category: bioinformatics
description: GuideScan is a tool for genome-wide CRISPR guide RNA (gRNA) design and analysis in custom genomes.
tags: [guidescan, CRISPR, gRNA-design, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pritykinlab/guidescan-cli"
---

## Concepts

- **gRNA Design**: GuideScan designs CRISPR guide RNAs across entire genomes.

- **Genome-wide Analysis**: Enables genome-wide gRNA screening and selection.

- **Custom Genomes**: Supports gRNA design in custom or non-model genomes.

- **Off-target Prediction**: Predicts potential off-target binding sites.

- **Efficiency Scoring**: Scores gRNA efficiency based on multiple criteria.

- **Library Design**: Designs optimal gRNA libraries for screening experiments.

## Pitfalls

- **Genome Quality**: Results depend on genome assembly quality.

- **Off-target Effects**: Off-target sites may cause unintended edits.

- **gRNA Efficiency**: Predicted efficiency may not match experimental results.

- **Computational Resources**: Genome-wide analysis requires significant resources.

- **Cas System Compatibility**: Ensure compatibility with target Cas system.

## Examples

### Design gRNAs for genome
**Args:** `guidescan design -g genome.fasta -o grnas.txt`
**Explanation:** Designs gRNAs across the entire genome.

### Target specific regions
**Args:** `guidescan design -g genome.fasta -t targets.bed -o grnas.txt`
**Explanation:** Designs gRNAs for specific genomic regions.

### Include off-target analysis
**Args:** `guidescan design -g genome.fasta -off -o grnas.txt`
**Explanation:** Includes off-target prediction in output.

### Batch processing
**Args:** `for f in *.fasta; do guidescan design -g $f -o ${f%.fasta}_grnas.txt; done`
**Explanation:** Processes multiple genomes.

### Filter by efficiency
**Args:** `guidescan design -g genome.fasta -e 0.7 -o grnas.txt`
**Explanation:** Filters gRNAs by minimum efficiency score.

### Generate report
**Args:** `guidescan design -g genome.fasta -r -o report.pdf`
**Explanation:** Generates detailed report of gRNA design.

### Help command
**Args:** `guidescan --help`
**Explanation:** Shows available options and usage information.