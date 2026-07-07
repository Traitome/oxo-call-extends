---
name: a3partitioner
category: utility
description: A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions from sequence alignments.
tags: [a3partitioner, utility, apobec, mutation, virology, phylogenetics, mpxv, monkeypox]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/a3partitioner"
---

## Concepts

- **Tool Overview**: Creates APOBEC3 and non-APOBEC3 mutation partitions from viral sequence alignments. Version 0.1.0.
- **Core Function**: Partitions mutations in viral genomes into APOBEC3-edited (cytidine deaminase activity) and non-APOBEC3 categories for evolutionary analysis. Designed for MPXV (monkeypox virus) analysis but applicable to other viruses.
- **Input/Output**: Input is a nucleotide sequence alignment (FASTA format); output is partitioned alignment files with APOBEC3 or non-APOBEC3 sites masked.
- **Installation**: 
  - Install via bioconda: `conda install -c bioconda a3partitioner`
  - Or via mamba: `mamba install a3partitioner`
  - Or from source: `git clone https://github.com/DaanJansen94/a3partitioner && cd a3partitioner && ./install.sh`
- **Platform Support**: Platform-independent (noarch)
- **APOBEC3 Context**: APOBEC3 enzymes cause C→T (and G→A on complementary strand) mutations in specific sequence contexts (TC→TT, CC→CT). This tool separates these from other mutation types.
- **Dependencies**: Python >=3.6, Biopython >=1.80
- **License**: MIT License

## Pitfalls

- **CRITICAL: Command Name**: The command is `A3Partitioner` (camel case), not `a3partitioner` (lowercase). This is a common source of errors.
- **Input Requirements**: Requires properly aligned sequence data in FASTA format. Ensure sequences are aligned before processing.
- **APOBEC3 Context Definition**: The tool identifies APOBEC3 target sites based on dinucleotide contexts (TC, CC). Different studies may use slightly different motif definitions.
- **Version**: This is an early version (0.1.0). Options may change in future releases.
- **MPXV Context**: Tool was designed for monkeypox virus (MPXV) analysis where APOBEC3 mutations are common. May need validation for other viral systems.
- **Both Partitions**: When using `-partition both`, output files are automatically suffixed with _APOBEC3 and _non_APOBEC3.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information for A3Partitioner.

### Create APOBEC3 partition only
**Args:** `-partition apobec -i input_aln.fasta -o output_apobec.fasta`
**Explanation:** Creates a partition containing only sites with putative APOBEC3 modifications (C→T or G→A in TC/CC contexts). All other sites are masked as ambiguous nucleotides. Useful for phylogenetic analysis focusing on APOBEC3-driven evolution.

### Create non-APOBEC3 partition only
**Args:** `-partition non-apobec -i input_aln.fasta -o output_non_apobec.fasta`
**Explanation:** Creates a partition excluding APOBEC3 target sites. APOBEC3 target sites are masked, leaving only non-APOBEC3 mutations. Useful for analyzing non-APOBEC3 evolutionary signals.

### Create both partitions
**Args:** `-partition both -i input_aln.fasta -o output_prefix`
**Explanation:** Creates both APOBEC3 and non-APOBEC3 partitions in one run. Generates two output files: output_prefix_APOBEC3.fasta and output_prefix_non_APOBEC3.fasta. Most efficient for complete analysis.

### Basic partition with default settings
**Args:** `-i alignment.fasta -o results.fasta`
**Explanation:** Runs A3Partitioner with default settings. Note that `-partition` option should be specified for predictable behavior.

### Process large alignment
**Args:** `-partition both -i large_alignment.fasta -o large_partition`
**Explanation:** Processes a large viral genome alignment. The tool handles alignments of hundreds of sequences efficiently.
