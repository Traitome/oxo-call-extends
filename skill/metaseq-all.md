---
name: metaseq-all
category: utility
description: Meta-package for metaseq including bedtools and UCSC tools
tags: [metaseq-all, utility, bioinformatics-tools]
author: oxo-call-community
source_url: "https://bioconda.github.io/recipes/metaseq-all/README.html"
---

## Concepts

- **Tool Overview**: metaseq-all v0.5.6 is a meta-package that bundles metaseq along with bedtools and UCSC tools for sequence analysis.
- **Core Function**: Provides a comprehensive suite of tools for sequence analysis and manipulation.
- **Bedtools Integration**: Includes bedtools for genomic interval operations and manipulation.
- **UCSC Tools**: Bundles UCSC genome browser tools for sequence analysis and visualization.
- **Input/Output**: Accepts various sequence and genomic interval formats; outputs processed data.
- **Comprehensive Toolkit**: Provides a one-stop solution for common sequence analysis tasks.

## Pitfalls

- **Tool Versioning**: Different tools may have different version requirements.
- **Dependency Management**: Requires proper management of multiple dependencies.
- **Command Syntax**: Different tools have different command syntax and options.
- **Output Formats**: May produce different output formats depending on the tool used.
- **Documentation**: Requires consulting individual tool documentation for detailed usage.
- **Memory Requirements**: Some tools may require significant memory for large datasets.

## Examples

### Run bedtools intersect
**Args:** `bedtools intersect -a peaks.bed -b genes.bed -o result.bed`
**Explanation:** Finds overlapping intervals between two BED files.

### Extract sequences
**Args:** `bedtools getfasta -fi genome.fasta -bed regions.bed -fo sequences.fasta`
**Explanation:** Extracts sequences from genome FASTA based on BED regions.

### Sort BED file
**Args:** `bedtools sort -i unsorted.bed -o sorted.bed`
**Explanation:** Sorts a BED file by chromosome and position.

### UCSC liftOver
**Args:** `liftOver input.bed chain.chain output.bed unmapped.bed`
**Explanation:** Converts genomic coordinates between assemblies.

### UCSC faToTwoBit
**Args:** `faToTwoBit genome.fasta genome.2bit`
**Explanation:** Converts FASTA to 2bit format for efficient storage.