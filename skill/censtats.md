---
name: censtats
category: genome-analysis
description: Centromere statistics toolkit for analyzing centromere characteristics
tags: [censtats, centromere, statistics, genomics, analysis]
author: oxo-call-community
source_url: "https://github.com/logsdon-lab/CenStats"
---

## Concepts

- **Tool Overview**: CenStats is a toolkit for calculating and analyzing centromere statistics from genome assemblies.
- **Core Function**: Computes various metrics for centromeric regions including length, repeat content, and sequence composition.
- **Features**: Centromere length calculation, satellite repeat analysis, GC content, and comparative statistics.
- **Input**: Genome assembly FASTA and centromere annotations.
- **Output**: Statistical reports and summary tables.
- **Application**: Analyzing centromere characteristics in genome assemblies.
- **Installation**: Install via bioconda: `conda install -c bioconda censtats`

## Pitfalls

- **Annotation Quality**: Requires accurate centromere annotations.
- **Assembly Completeness**: Incomplete assemblies may affect statistics.
- **Repeat Masking**: May need repeat-masked sequences for accurate analysis.
- **Sequence Format**: Requires properly formatted FASTA files.

## Examples

### Calculate centromere statistics
**Args:** `censtats --genome genome.fasta --annotations centromeres.gff --output stats.tsv`
**Explanation:** Computes statistics for annotated centromeric regions.

### Compare centromeres across species
**Args:** `censtats compare --species1 species1.fasta --species2 species2.fasta --output comparison.tsv`
**Explanation:** Compares centromere statistics between two species.

### Generate report
**Args:** `censtats report --stats stats.tsv --output report.html`
**Explanation:** Generates HTML report with visualizations.

### Display help
**Args:** `censtats --help`
**Explanation:** Shows all available commands and options.