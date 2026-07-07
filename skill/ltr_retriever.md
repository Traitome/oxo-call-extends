---
name: ltr_retriever
category: utility
description: Sensitive and accurate identification of LTR retrotransposons
tags: [ltr_retriever, utility, LTR, retrotransposons]
author: oxo-call-community
source_url: "https://github.com/oushujun/LTR_retriever"
---

## Concepts

- **Tool Overview**: ltr_retriever v3.0.5 is a tool for sensitive and accurate identification of LTR retrotransposons in genome sequences.
- **Core Function**: Integrates multiple LTR detection tools and refines predictions for high-quality LTR annotation.
- **Integration Strategy**: Combines outputs from LTR_Finder, LTR_harvest, and other tools for improved accuracy.
- **Input/Output**: Input: Raw LTR predictions from multiple tools; Output: Curated LTR annotation file.
- **Installation**: `conda install -c bioconda ltr_retriever`
- **Key Features**: High sensitivity, reduces false positives, integrates multiple prediction methods.

## Pitfalls

- **Input Requirements**: Requires outputs from multiple LTR detection tools.
- **Computation Time**: Processing multiple tool outputs can be time-consuming.
- **Memory Usage**: May require significant memory for large genomes.
- **Tool Dependencies**: Requires LTR_Finder, LTR_harvest, and other tools to be installed.
- **Parameter Tuning**: May require adjustment for different genome types.
- **Result Interpretation**: Output may require manual inspection for complex cases.

## Examples

### Run LTR retriever
**Args:** `LTR_retriever -genome genome.fasta -inharvest harvest.out -infinder finder.out -o results/`
**Explanation:** Processes LTR predictions from multiple tools.

### With RepeatMasker
**Args:** `LTR_retriever -genome genome.fasta -inharvest harvest.out -infinder finder.out -rm repeatmasker.out -o results/`
**Explanation:** Integrates RepeatMasker results for better filtering.

### Threads
**Args:** `LTR_retriever -genome genome.fasta -inharvest harvest.out -infinder finder.out -t 8 -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum length
**Args:** `LTR_retriever -genome genome.fasta -inharvest harvest.out -infinder finder.out -minlen 1000 -o results/`
**Explanation:** Sets minimum LTR length to 1000bp.

### Verbose mode
**Args:** `LTR_retriever -genome genome.fasta -inharvest harvest.out -infinder finder.out -v -o results/`
**Explanation:** Outputs detailed progress information.

### Help documentation
**Args:** `LTR_retriever --help`
**Explanation:** Displays all available options and parameters.