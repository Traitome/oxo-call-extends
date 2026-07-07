---
name: ucsc-getrnapred
category: utility
description: UCSC getRnaPred - Tool for extracting RNA predictions.
tags: [ucsc-getrnapred, ucsc, rna-seq, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC getRnaPred - A tool for extracting RNA predictions.
- **Core Function**: Extracts RNA sequences from prediction files.
- **Input**: RNA prediction file, genome FASTA.
- **Output**: RNA sequences.
- **Installation**: Part of UCSC utilities
- **Use Case**: RNA analysis, transcriptomics, gene prediction.

## Pitfalls

- **FASTA Requirement**: Requires genome FASTA file.
- **Memory**: May require significant memory for large genomes.

## Examples

### Extract RNA predictions
**Args:** `getRnaPred rna.txt genome.fa > rna.fa`
**Explanation:** Extract RNA sequences from predictions.

### With options
**Args:** `getRnaPred -strand=+ rna.txt genome.fa > rna.fa`
**Explanation:** Extract only positive strand.
