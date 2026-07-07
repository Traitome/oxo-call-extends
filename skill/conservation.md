---
name: conservation
category: utility
description: Calculate evolutionary conservation of amino acids and codons
tags: [conservation, evolutionary-biology, conservation-analysis, amino-acid, codon]
author: oxo-call-community
source_url: "https://github.com/hanjunlee21/conservation"
---

## Concepts

- **Tool Overview**: Conservation is a tool for calculating evolutionary conservation scores of amino acids and codons in protein-coding sequences across multiple species.
- **Core Function**: Quantifies evolutionary conservation at both amino acid and codon levels using multiple sequence alignments.
- **Algorithm**: Computes conservation metrics based on sequence alignment entropy and phylogenetic relationships.
- **Input**: Multiple sequence alignments in FASTA or other standard formats.
- **Output**: Conservation scores per position, often in tabular or visualization-ready formats.
- **Application**: Protein function prediction, domain identification, and evolutionary analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda conservation`

## Pitfalls

- **Alignment Quality**: Results depend on accurate multiple sequence alignment.
- **Species Selection**: Biased species sampling affects conservation scores.
- **Gap Handling**: Gaps in alignment may skew conservation calculations.
- **Codon vs Amino Acid**: Different conservation patterns at codon vs amino acid level.
- **Phylogenetic Correction**: May require phylogenetic correction for deep evolutionary relationships.

## Examples

### Calculate amino acid conservation
**Args:** `conservation -i alignment.fasta -o conservation_scores.txt`
**Explanation:** Calculates conservation scores from multiple sequence alignment.

### Codon-level analysis
**Args:** `conservation -i alignment.fasta --codon -o codon_conservation.txt`
**Explanation:** Calculates conservation at codon level instead of amino acid level.

### With phylogenetic weighting
**Args:** `conservation -i alignment.fasta -t tree.nwk --weighted -o weighted_scores.txt`
**Explanation:** Applies phylogenetic weighting to conservation calculations.

### Display help
**Args:** `conservation --help`
**Explanation:** Shows all available options and usage information.