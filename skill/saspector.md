---
name: saspector
category: assembly
description: Analysis of missing regions in bacterial draft genomes
tags: ["saspector", "assembly", "bacterial-genomics", "genome-analysis"]
author: oxo-call-community
source_url: "https://github.com/alejocrojo09/SASpector"
---

## Concepts

- **Tool Overview**: SASpector (v0.0.5) is a tool for analyzing missing regions in bacterial draft genomes, identifying gaps and incomplete assemblies.
- **Core Function**: Detects and characterizes missing genomic regions by comparing draft assemblies against reference genomes or closely related strains.
- **Algorithm**: Uses sequence alignment and coverage analysis to identify regions with low or no coverage in draft assemblies.
- **Input/Output**: Accepts FASTA assemblies and produces reports of missing regions with coordinates and annotations.
- **Applications**: Quality assessment of draft assemblies, identifying sequencing gaps, and comparative genomics.
- **Target Organisms**: Primarily designed for bacterial genomes but adaptable to other prokaryotes.

## Pitfalls

- **Reference Dependence**: Requires closely related reference genome for comparison.
- **Assembly Quality**: Results depend on input assembly quality and completeness.
- **Computational Resources**: May require significant resources for large genomes.
- **False Positives**: May report false missing regions due to sequencing artifacts.
- **Strain Specificity**: Performance varies with phylogenetic distance from reference.
- **Annotation Dependencies**: Functional analysis requires additional annotation files.

## Examples

### Basic missing region detection
**Args:** `saspector -i draft.fasta -r reference.fasta -o missing_regions.tsv`
**Explanation:** `-i` input draft assembly; `-r` reference genome; `-o` output TSV with missing regions.

### With annotation file
**Args:** `saspector -i draft.fasta -r reference.fasta -g genes.gff -o results/`
**Explanation:** `-g` GFF annotation file for functional analysis of missing regions.

### Coverage analysis
**Args:** `saspector -i draft.fasta -r reference.fasta --coverage -o coverage_report.tsv`
**Explanation:** `--coverage` generates detailed coverage analysis of missing regions.

### Visualize missing regions
**Args:** `saspector -i draft.fasta -r reference.fasta --plot -o missing_plot.png`
**Explanation:** `--plot` generates visualization of missing regions across the genome.

### Custom sensitivity
**Args:** `saspector -i draft.fasta -r reference.fasta -s 0.8 -o results.tsv`
**Explanation:** `-s 0.8` sets sensitivity threshold to 80% for detecting missing regions.

### Batch processing
**Args:** `saspector -i ./assemblies/ -r reference.fasta -o ./results/ -b`
**Explanation:** `-b` batch mode for processing multiple assemblies.

### Detailed report
**Args:** `saspector -i draft.fasta -r reference.fasta -d -o detailed_report.txt`
**Explanation:** `-d` generates comprehensive detailed report with all analysis metrics.