---
name: count_constant_sites
category: alignment
description: Compute count of constant sites in multiple sequence alignment
tags: [count_constant_sites, alignment, fasta, phylogenetics, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/pvanheus/count_constant_sites"
---

## Concepts

- **Tool Overview**: count_constant_sites is a tool for computing the count of constant (invariant) sites in a FASTA-formatted multiple sequence alignment, primarily used for phylogenetic analysis.
- **Core Function**: Counts invariant nucleotide sites in alignments and outputs results in a format compatible with IQ-TREE's `-fconst` option.
- **Algorithm**: Scans each column in the alignment and counts sites where all sequences have the same nucleotide.
- **Input**: FASTA file containing multiple sequence alignment.
- **Output**: Counts of constant sites for each nucleotide (A, C, G, T), formatted for IQ-TREE.
- **Application**: Phylogenetic tree inference, sequence conservation analysis, evolutionary studies.
- **Installation**: Install via bioconda: `conda install -c bioconda count_constant_sites`

## Pitfalls

- **Alignment Quality**: Requires well-aligned sequences for accurate counting.
- **Ambiguous Bases**: Ns and ambiguous characters may affect counting.
- **Gap Handling**: Gaps may be treated differently depending on options.
- **Sequence Length**: Short sequences may produce unreliable results.
- **Format Compatibility**: Only works with FASTA format alignments.

## Examples

### Count constant sites
**Args:** `count_constant_sites alignment.fasta`
**Explanation:** Counts constant sites and outputs in IQ-TREE format.

### With gap filtering
**Args:** `count_constant_sites --ignore-gaps alignment.fasta`
**Explanation:** Ignores sites containing gaps when counting.

### Output detailed counts
**Args:** `count_constant_sites --verbose alignment.fasta`
**Explanation:** Outputs detailed breakdown of each constant site type.

### Save to file
**Args:** `count_constant_sites alignment.fasta > constant_sites.txt`
**Explanation:** Saves results to file for use with IQ-TREE.

### Display help
**Args:** `count_constant_sites --help`
**Explanation:** Shows all available options and usage information.