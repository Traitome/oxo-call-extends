---
name: cyntenator
category: alignment
description: progressive gene order alignments
tags: [cyntenator, alignment, synteny, gene-order, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/dieterich-lab/cyntenator"
---

## Concepts

- **Tool Overview**: cyntenator (v0.0.r2326+) is a tool for identifying conserved syntenic blocks between multiple genomes using progressive gene order alignments.
- **Core Function**: Computes alignments where the alphabet consists of annotated genes, identifying conserved gene order across species.
- **Input/Output**: Input: Gene annotations in BED format, genome sequences. Output: Syntenic block annotations, alignment scores.
- **Algorithm**: Uses Smith-Waterman dynamic programming with gene-level scoring to identify syntenic regions.
- **Key Features**: Multi-genome synteny analysis, progressive alignment, gene-order conservation scoring.
- **Installation**: `conda install -c bioconda cyntenator`

## Pitfalls

- **Gene Annotation**: Requires consistent gene annotations across all species.
- **Genome Quality**: Poorly assembled genomes may produce spurious synteny calls.
- **Computational Complexity**: Analyzing many genomes can be computationally intensive.
- **Parameter Selection**: Scoring parameters affect synteny detection sensitivity.
- **Output Interpretation**: Synteny blocks should be validated with visual inspection.

## Examples

### Identify syntenic blocks
**Args:** `cyntenator -i species1.bed species2.bed species3.bed -o synteny.txt`
**Explanation:** Identify conserved syntenic blocks across multiple species.

### Run progressive alignment
**Args:** `cyntenator -i *.bed -o synteny.txt --progressive`
**Explanation:** Perform progressive gene order alignment across all input species.

### Generate visualization
**Args:** `cyntenator -i species1.bed species2.bed -o synteny.txt --plot`
**Explanation:** Generate visualization of syntenic blocks.
