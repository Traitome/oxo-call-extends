---
name: clustalw
category: alignment
description: ClustalW2 general purpose multiple sequence alignment program for DNA or proteins
tags: [clustalw, multiple-sequence-alignment, msa, protein, dna, bioinformatics]
author: oxo-call-community
source_url: "http://www.clustal.org/download/clustalw_help.txt"
---

## Concepts

- **Tool Overview**: ClustalW2 is a widely used general purpose multiple sequence alignment program for DNA or protein sequences.
- **Core Function**: Aligns multiple sequences using progressive alignment approach with pairwise alignments and guide tree construction.
- **Algorithm**: Uses progressive alignment with weighted sequence distances and guide tree.
- **Input**: FASTA format sequences (DNA or protein).
- **Output**: Aligned sequences in various formats (CLUSTAL, FASTA, PHYLIP, etc.).
- **Application**: Sequence analysis, phylogenetics, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda clustalw`

## Pitfalls

- **Sequence Type**: Must specify DNA or protein; mixed types cause errors.
- **Large Datasets**: Less scalable than Clustal Omega for very large datasets.
- **Output Format**: Default is CLUSTAL format; must specify for other formats.
- **Guide Tree**: Generated internally; limited control over tree parameters.
- **Memory Usage**: May require significant memory for large alignments.

## Examples

### Basic alignment
**Args:** `clustalw -infile=sequences.fasta -outfile=aligned.fasta -outfmt=fasta`
**Explanation:** Aligns sequences and outputs in FASTA format.

### DNA alignment
**Args:** `clustalw -infile=dna.fasta -outfile=aligned.fasta -type=dna`
**Explanation:** Explicitly specifies DNA sequence type.

### Protein alignment
**Args:** `clustalw -infile=proteins.fasta -outfile=aligned.fasta -type=protein`
**Explanation:** Aligns protein sequences with appropriate scoring matrix.

### Output PHYLIP format
**Args:** `clustalw -infile=sequences.fasta -outfile=aligned.phy -outfmt=phylip`
**Explanation:** Outputs alignment in PHYLIP format for phylogenetics.

### Generate guide tree
**Args:** `clustalw -infile=sequences.fasta -newtree=tree.dnd`
**Explanation:** Generates and saves guide tree in Newick format.

### Display help
**Args:** `clustalw -help`
**Explanation:** Shows all available options and usage information.