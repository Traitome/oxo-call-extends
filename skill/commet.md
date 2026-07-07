---
name: commet
category: metagenomics
description: Compare and combine multiple metagenomic datasets
tags: [commet, metagenomics, comparative-analysis, k-mer, bioinformatics]
author: oxo-call-community
source_url: "https://colibread.inria.fr/software/commet"
---

## Concepts

- **Tool Overview**: COMMET is a tool for comparing and combining multiple metagenomic datasets using k-mer based approaches to assess similarity and diversity between samples.
- **Core Function**: Compares metagenomic samples by analyzing k-mer distributions and provides metrics for sample similarity and diversity.
- **Algorithm**: Uses k-mer counting and statistical measures to compare sequence composition across multiple metagenomic datasets.
- **Input**: Sequencing reads or assembled contigs from multiple metagenomic samples.
- **Output**: Similarity matrices, diversity metrics, and comparative analysis reports.
- **Application**: Metagenomic sample comparison, quality control, and multi-sample analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda commet`

## Pitfalls

- **k-mer Size**: Results depend on appropriate k-mer size selection.
- **Sequencing Depth**: Uneven sequencing depth may bias comparisons.
- **Memory Usage**: Large datasets require significant memory for k-mer counting.
- **Sample Normalization**: May require normalization for fair comparisons.
- **Interpretation**: Results require careful biological interpretation.

## Examples

### Compare metagenomic samples
**Args:** `commet -i sample1.fastq,sample2.fastq,sample3.fastq -o comparison.txt`
**Explanation:** Compares multiple metagenomic samples using k-mer analysis.

### With custom k-mer size
**Args:** `commet -i samples.fastq -k 21 -o comparison.txt`
**Explanation:** Uses 21-mers for comparison analysis.

### Generate similarity matrix
**Args:** `commet -i *.fastq -m -o similarity_matrix.txt`
**Explanation:** Generates pairwise similarity matrix between samples.

### Display help
**Args:** `commet --help`
**Explanation:** Shows all available options and usage information.