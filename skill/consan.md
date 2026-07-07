---
name: consan
category: alignment
description: Pairwise RNA structural alignment with constraint support
tags: [consan, rna, structural-alignment, bioinformatics, alignment]
author: oxo-call-community
source_url: "http://eddylab.org/software/consan/README"
---

## Concepts

- **Tool Overview**: Consan is a pairwise RNA structural alignment tool that performs both unconstrained and constrained alignments using alignment pins to guide the process.
- **Core Function**: Aligns RNA sequences while considering secondary structure information, supporting both global and locally constrained alignments.
- **Algorithm**: Uses dynamic programming with structural constraints and alignment pins to optimize sequence and structure similarity.
- **Input**: Two RNA sequences in FASTA format, optional structural constraints.
- **Output**: Structural alignment in standard formats with confidence scores.
- **Application**: RNA structure comparison, homology detection, and functional RNA analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda consan`

## Pitfalls

- **Sequence Length**: Long sequences may require significant computation time.
- **Structure Information**: Benefits from known secondary structure data.
- **Alignment Pins**: Incorrect pins may produce poor alignments.
- **Gap Penalties**: May require tuning for different RNA families.
- **Structural Conservation**: May miss alignments with poor structural conservation.

## Examples

### Align two RNA sequences
**Args:** `consan seq1.fasta seq2.fasta -o alignment.stk`
**Explanation:** Performs pairwise RNA structural alignment.

### With alignment constraints
**Args:** `consan seq1.fasta seq2.fasta -c constraints.txt -o alignment.stk`
**Explanation:** Uses alignment pins to constrain the alignment.

### With custom gap penalties
**Args:** `consan seq1.fasta seq2.fasta -g 10 -e 0.5 -o alignment.stk`
**Explanation:** Sets gap open penalty to 10 and extension to 0.5.

### Display help
**Args:** `consan --help`
**Explanation:** Shows all available options and usage information.