---
name: clipkit
category: formatting
description: Alignment trimming software for phylogenetics
tags: [clipkit, phylogenetics, alignment, trimming, msa]
author: oxo-call-community
source_url: "https://github.com/jlsteenwyk/clipkit"
---

## Concepts

- **Tool Overview**: ClipKIT is a multiple sequence alignment trimming tool for phylogenetics that intelligently removes poorly aligned or phylogenetically uninformative sites.
- **Core Function**: Trims multiple sequence alignments to retain phylogenetically informative sites while removing noise, improving downstream tree inference.
- **Input/Output**: Input: FASTA, PHYLIP, or other alignment formats. Output: Trimmed alignment in the same format.
- **Trimming Modes**: Provides multiple modes: `smart-gap`, `kpic`, `gappy`, `kpic-gappy` for different trimming strategies.
- **Mode Selection**: `smart-gap` (default) removes gaps based on intelligent gap assessment. `kpic` keeps phylogenetically informative sites.
- **Preserves Information**: Unlike aggressive trimming, ClipKIT aims to retain sites that contribute to phylogenetic signal.

## Pitfalls

- **Mode Selection**: Different modes suit different datasets. `smart-gap` is best for most cases, `kpic` for highly divergent sequences.
- **Input Format**: Must specify correct input format with `-i` if not auto-detected. Supports FASTA, PHYLIP, CLUSTAL, etc.
- **Output Format**: Use `-o` to specify output format. Default is same as input format.
- **Complementary to Alignment**: Run after alignment (MAFFT, MUSCLE, etc.) but before tree inference (IQ-TREE, RAxML, etc.).
- **Site Removal**: Over-aggressive trimming can remove informative sites. Inspect trimmed alignment length to ensure sufficient sites remain.

## Examples

### Trim alignment with smart-gap mode
**Args:** `input.fasta output.fasta`
**Explanation:** Trims alignment using default smart-gap mode, which intelligently removes gap-rich regions while preserving informative sites.

### Trim with kpic mode
**Args:** `input.fasta output.fasta --mode kpic`
**Explanation:** Keeps only phylogenetically informative sites (constant and parsimony-informative), removes singleton and autapomorphic sites.

### Trim with gappy mode
**Args:** `input.fasta output.fasta --mode gappy`
**Explanation:** Removes columns with gaps exceeding a threshold, similar to traditional gap-trimming approaches.

### Trim PHYLIP format alignment
**Args:** `input.phy output.phy -i phylip -o phylip`
**Explanation:** Trims a PHYLIP format alignment, specifying input and output formats explicitly.

### Keep complementary sites
**Args:** `input.fasta output.fasta --mode kpic-gappy`
**Explanation:** Combines kpic and gappy modes: keeps informative sites and removes gap-rich columns.

### Output site statistics
**Args:** `input.fasta output.fasta --stats`
**Explanation:** Reports statistics about trimmed and retained sites, useful for understanding trimming impact.

### Set gap threshold for gappy mode
**Args:** `input.fasta output.fasta --mode gappy --gap_threshold 0.9`
**Explanation:** Removes columns with gaps in more than 90% of sequences, more permissive than default.

### Trim and report removed positions
**Args:** `input.fasta output.fasta --report`
**Explanation:** Outputs a file listing the positions that were removed, useful for downstream analysis.
