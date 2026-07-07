---
name: codonw
category: utility
description: Multivariate analysis of codon and amino acid usage
tags: [codonw, codon-usage, multivariate-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "http://codonw.sourceforge.net"
---

## Concepts

- **Tool Overview**: CodonW is a program designed for multivariate analysis of codon and amino acid usage patterns, using correspondence analysis to identify trends in sequence data.
- **Core Function**: Performs correspondence analysis and other multivariate statistical methods to analyze codon usage patterns across genes or genomes.
- **Algorithm**: Uses correspondence analysis (CA) to identify major trends in codon usage variation.
- **Input**: Nucleotide sequences in FASTA or custom format.
- **Output**: Correspondence analysis results, codon usage tables, and statistical summaries.
- **Application**: Comparative genomics, evolutionary studies, and gene expression analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda codonw`

## Pitfalls

- **Sequence Quality**: Requires high-quality sequence data.
- **Data Format**: Strict input format requirements.
- **Gene Number**: Requires sufficient number of genes for meaningful analysis.
- **Codon Table**: Must specify correct genetic code.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Analyze codon usage with correspondence analysis
**Args:** `codonw input.fasta output`
**Explanation:** Performs correspondence analysis on codon usage patterns.

### Generate codon usage table
**Args:** `codonw -table input.fasta output`
**Explanation:** Generates codon usage frequency table.

### With custom genetic code
**Args:** `codonw -code 11 input.fasta output`
**Explanation:** Uses genetic code 11 (bacterial) for analysis.

### Display help
**Args:** `codonw -help`
**Explanation:** Shows all available options and usage information.