---
name: bmge
category: formatting
description: Block Mapping and Gathering with Entropy for selecting suitable regions in multiple sequence alignments
tags: [bmge, alignment, phylogenetics, trimming, msa]
author: oxo-call-community
source_url: "http://ftp.pasteur.fr/pub/gensoft/projects/BMGE/"
---

## Concepts

- **Tool Overview**: BMGE selects regions in multiple sequence alignments suited for phylogenetic inference based on entropy.
- **Core Function**: Trims poorly aligned or highly variable regions from MSAs to improve phylogenetic analysis.
- **Entropy Scoring**: Identifies columns with high entropy (variable positions) for removal.
- **Input Formats**: Supports FASTA, Phylip, and Nexus alignment formats.
- **Gap Handling**: Removes columns with excessive gaps to reduce missing data.
- **Installation**: Install via bioconda: `conda install -c bioconda bmge`

## Pitfalls

- **Alignment Quality**: BMGE assumes input alignment is reasonable; very poor alignments may need other tools first.
- **Entropy Threshold**: Default threshold may be too stringent for some datasets; adjust as needed.
- **Gap Threshold**: Columns with >50% gaps are removed by default.
- **Sequence Type**: Specify nucleotide or protein mode for appropriate scoring.
- **Output Format**: Output format matches input format by default.

## Examples

### Trim nucleotide alignment
**Args:** `bmge -i alignment.fa -t DNA -o trimmed.fa`
**Explanation:** Trims nucleotide alignment using default entropy threshold.

### Trim protein alignment
**Args:** `bmge -i proteins.fa -t AA -o trimmed_proteins.fa`
**Explanation:** Trims protein alignment with amino acid-specific scoring.

### Custom entropy threshold
**Args:** `bmge -i alignment.fa -t DNA -g 0.5 -o trimmed.fa`
**Explanation:** Uses entropy threshold of 0.5 for more aggressive trimming.

### Custom gap threshold
**Args:** `bmge -i alignment.fa -t DNA -h 0.3 -o trimmed.fa`
**Explanation:** Removes columns with more than 30% gap characters.

### Phylip output format
**Args:** `bmge -i alignment.fa -t DNA -o trimmed.phy -f phylip`
**Explanation:** Outputs trimmed alignment in Phylip format for phylogenetic software.

### Verbose mode
**Args:** `bmge -i alignment.fa -t DNA -o trimmed.fa -v`
**Explanation:** Prints detailed statistics about trimmed regions.
