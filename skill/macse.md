---
name: macse
category: alignment
description: "MACSE: Multiple Alignment of Coding SEquences Accounting for Frameshifts and Stop Codons."
tags: [macse, alignment, coding-sequences]
author: oxo-call-community
source_url: "https://bioweb.supagro.inra.fr/macse/"
---
## Concepts

- **Tool Overview**: macse v2.07 aligns coding nucleotide sequences while accounting for frameshifts and stop codons.
- **Core Function**: Aligns protein-coding genes while preserving codon structure.
- **Frameshift Handling**: Detects and handles frameshifts without disrupting codon structure.
- **Input/Output**: Input: FASTA files with coding sequences; Output: Aligned sequences in various formats.
- **Installation**: `conda install -c bioconda macse`
- **Key Features**: Handles pseudogenes, detects undocumented frameshifts, aligns NGS reads to reference.

## Pitfalls

- **Sequence Quality**: Low-quality sequences affect alignment accuracy.
- **Codon Frame**: Requires sequences to be in correct reading frame.
- **Memory Usage**: Aligning many sequences may require significant memory.
- **Computation Time**: Can be slow for large alignments.
- **Ambiguity Codes**: May struggle with ambiguous nucleotide codes.
- **Output Format**: Default output may require conversion for downstream tools.

## Examples

### Align coding sequences
**Args:** `macse -prog alignSequences -seq sequences.fasta -out aligned.fasta`
**Explanation:** Aligns coding sequences preserving codon structure.

### With frameshift detection
**Args:** `macse -prog alignSequences -seq sequences.fasta -out aligned.fasta -fsd`
**Explanation:** Detects and handles frameshifts during alignment.

### Align to reference
**Args:** `macse -prog alignReads -ref reference.fasta -reads reads.fasta -out aligned.fasta`
**Explanation:** Aligns reads/contigs to reference coding sequence.

### Output format
**Args:** `macse -prog alignSequences -seq sequences.fasta -out aligned.fasta -f phylip`
**Explanation:** Outputs alignment in PHYLIP format.

### Codon table
**Args:** `macse -prog alignSequences -seq sequences.fasta -out aligned.fasta -codon 1`
**Explanation:** Uses standard genetic code (code 1).

### Help documentation
**Args:** `macse -help`
**Explanation:** Displays all available commands and options.