---
name: alv
category: alignment
description: A console-based sequence alignment viewer for DNA and protein multiple-sequence alignments
tags: [alv, alignment-viewer, MSA, console, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/arvestad/alv"
---

## Concepts

- **Tool Overview**: alv (alignment viewer) is a command-line tool for viewing DNA or protein multiple-sequence alignments directly in the terminal, eliminating the need for a GUI.
- **Core Function**: Displays alignments with color-coded residues, supports scrolling, zooming, and various viewing modes for analyzing sequence conservation and variation.
- **Input/Output**: Accepts FASTA, Clustal, and other standard MSA formats; outputs formatted alignment to terminal or file.
- **Installation**: Available via Bioconda (`conda install -c bioconda alv`) or PyPI (`pip install alv`).
- **Features**: Multiple color schemes, sub-alignment viewing, random sequence sampling, glimpse mode for large alignments, and support for multiple alignments per file.

## Pitfalls

- **Python Version**: Requires Python 3.6 or later; earlier versions may not work correctly.
- **Multiple Alignments**: Files with multiple alignments default to showing the first one; use `-ai` to select a specific alignment.
- **Terminal Width**: Wide alignments may wrap or require horizontal scrolling; use `-sa` to view specific columns.
- **Sequence Type Detection**: Lowercase sequences are now correctly detected as DNA/protein/codon in v1.8.1+.
- **Codon Alignments**: Ensure sequences are in triplet format for proper codon display.

## Examples

### View an alignment file
**Args:** `alv alignment.fasta`
**Explanation:** Displays the entire alignment in the terminal with default color scheme.

### View specific columns (sub-alignment)
**Args:** `alv -sa 30 60 alignment.fasta`
**Explanation:** Shows only columns 30-59 of the alignment, useful for focusing on specific regions.

### View a random sample of sequences
**Args:** `alv -r 10 large_alignment.fasta`
**Explanation:** Displays 10 randomly selected sequences from the alignment, helpful for large datasets.

### Quick glimpse of a large alignment
**Args:** `alv -g huge_alignment.fasta`
**Explanation:** Shows an informative cut-out of the alignment if it doesn't fit without scrolling.

### Select specific alignment from multi-alignment file
**Args:** `alv -ai 2 multiple_alignments.fasta`
**Explanation:** Displays the second alignment (0-indexed) from a file containing multiple alignments.

### Save alignment view to file
**Args:** `alv alignment.fasta > alignment_view.txt`
**Explanation:** Outputs the formatted alignment to a text file instead of displaying in terminal.