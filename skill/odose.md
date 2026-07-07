---
name: odose
category: utility
description: ODoSE is an Ortholog Direction of Selection Engine for evolutionary analysis.
tags: [odose, utility, orthologs, selection-analysis]
author: oxo-call-community
source_url: "https://github.com/ODoSE/odose.nl"
---

## Concepts

- **Tool Overview**: ODoSE analyzes orthologs to detect selection pressure.
- **Core Function**: Identifies direction of selection in orthologous genes.
- **Algorithm**: Uses evolutionary models for selection detection.
- **Input Format**: Accepts orthologous sequence alignments.
- **Output**: Produces selection pressure metrics and results.
- **Use Case**: Evolutionary biology, comparative genomics, and phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Alignment Quality**: Results depend on alignment quality.
- **Ortholog Identification**: Requires accurate ortholog prediction.
- **Model Assumptions**: Relies on evolutionary model assumptions.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `odose --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `odose analyze -i alignments.fasta -o results.txt`
**Explanation:** Analyzes selection pressure in orthologs.

### With tree
**Args:** `odose analyze -i alignments.fasta -t tree.nwk -o results.txt`
**Explanation:** Uses phylogenetic tree for analysis.

### Multiple comparisons
**Args:** `odose compare -i species1.fasta species2.fasta -o comparison.txt`
**Explanation:** Compares selection across species.

### Output format
**Args:** `odose analyze -i alignments.fasta -o results.csv --csv`
**Explanation:** Outputs results in CSV format.

### Verbose mode
**Args:** `odose analyze -i alignments.fasta -v -o results.txt`
**Explanation:** Runs with verbose output.

### Statistical test
**Args:** `odose test -i alignments.fasta -o stats.txt`
**Explanation:** Performs statistical testing for selection.