---
name: micomplete
category: assembly
description: Quality control of assembled genomes
tags: [micomplete, assembly, quality-control]
author: oxo-call-community
source_url: "https://bitbucket.org/evolegiolab/micomplete"
---

## Concepts

- **Tool Overview**: miComplete v1.1.1 is a quality control tool for assembled genomes.
- **Core Function**: Evaluates completeness and quality of genome assemblies.
- **Assembly Assessment**: Assesses genome assembly quality metrics.
- **Completeness Check**: Estimates genome completeness.
- **Input/Output**: Accepts assembled genomes; outputs quality reports.
- **Genome Quality**: Provides metrics for evaluating assembly quality.

## Pitfalls

- **Computational Resources**: Processing large genomes may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assessment depends on input assembly quality.
- **Reference Database**: Requires BUSCO or similar databases.
- **Runtime**: Analysis of large assemblies can be time-consuming.

## Examples

### Assess genome completeness
**Args:** `micomplete -i genome.fasta -o report.txt`
**Explanation:** Evaluates completeness of genome assembly.

### With BUSCO database
**Args:** `micomplete -i genome.fasta -d busco_db/ -o report.txt`
**Explanation:** Uses custom BUSCO database for assessment.

### Detailed output
**Args:** `micomplete -i genome.fasta -o report.txt -v`
**Explanation:** Generates detailed quality report.

### Batch processing
**Args:** `micomplete -i fasta/ -o reports/`
**Explanation:** Processes multiple genome assemblies in batch mode.

### Generate visualization
**Args:** `micomplete -i genome.fasta -o report.txt -p plot.png`
**Explanation:** Generates quality visualization.