---
name: a3partitioner
category: utility
description: A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions
tags: [a3partitioner, utility, apobec, mutation, virology]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/a3partitioner/blob/main/README.md"
---

## Concepts

- **Tool Overview**: Creates APOBEC3 and non-APOBEC3 mutation partitions from viral sequence data. Version 0.1.0.
- **Core Function**: Partitions mutations in viral genomes into APOBEC3-edited (cytidine deaminase activity) and non-APOBEC3 categories for evolutionary analysis.
- **Input/Output**: Input is viral sequence data with mutation annotations; output is partitioned mutation sets.
- **Installation**: Install via bioconda: `conda install -c bioconda a3partitioner`
- **Platform Support**: Platform-independent (noarch)
- **APOBEC3 Context**: APOBEC3 enzymes cause C→T (and G→A on complementary strand) mutations in specific sequence contexts (TC→TT, CC→CT). This tool separates these from other mutation types.

## Pitfalls

- **Version Differences**: This is an early version (0.1.0). Options may change in future releases.
- **Input Requirements**: Requires properly annotated mutation data. Ensure input format matches expectations.
- **APOBEC3 Context Definition**: Different studies use slightly different APOBEC3 motif definitions. Check which context the tool uses.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic partitioning
**Args:** `input_mutations.tsv output_partitions.tsv`
**Explanation:** Reads mutation data and partitions it into APOBEC3 and non-APOBEC3 categories, writing results to the output file.

### Run with specific context definition
**Args:** `--context TC input_mutations.tsv output.tsv`
**Explanation:** Uses the TC dinucleotide context to identify APOBEC3 mutations. The context definition affects which mutations are classified as APOBEC3-edited.

### Run with verbose output
**Args:** `-v input_mutations.tsv output_partitions.tsv`
**Explanation:** Runs with verbose output to see detailed classification of each mutation, useful for debugging and validation.
