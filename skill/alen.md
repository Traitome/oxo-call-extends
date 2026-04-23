---
name: alen
category: utility
description: Simple terminal-based sequence alignment viewer for DNA and amino acid alignments
tags: [alignment, viewer, terminal, visualization, fasta]
author: oxo-call-community
source_url: "https://github.com/jakobnissen/alen"
---

## Concepts

- **Tool Overview**: Alen is a lightweight terminal-based viewer for visualizing DNA and amino acid multiple sequence alignments directly in the command line.
- **Core Function**: Displays alignment files with color-coded nucleotides/amino acids, supporting interactive navigation and various output formats.
- **Input/Output**: Input: FASTA, CLUSTAL, PHYLIP alignments. Output: Terminal visualization, optionally colored output.
- **Auto-Detection**: Automatically detects whether alignment is nucleotide or amino acid and adjusts display accordingly.
- **Installation**: Install via bioconda: `conda install -c bioconda alen`

## Pitfalls

- **Memory Limitation**: Loads entire alignment into memory - not suitable for multi-gigabyte files.
- **Terminal Width**: Display quality depends on terminal width - narrow terminals may truncate.
- **Color Support**: Requires terminal with ANSI color support for colored output.
- **Interactive Mode**: Some terminal emulators may not handle interactive mode correctly.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows all available options for Alen viewer.

### View alignment file
**Args:** `alignment.fasta`
**Explanation:** Displays the alignment in terminal with color coding.

### View with line numbers
**Args:** `-n alignment.fasta`
**Explanation:** Shows alignment with position line numbers for reference.

### View specific region
**Args:** `-r 100-200 alignment.fasta`
**Explanation:** Displays only positions 100-200 of the alignment.

### View without colors
**Args:** `--no-color alignment.fasta`
**Explanation:** Displays alignment without color coding (useful for logging).

### View consensus sequence
**Args:** `-c alignment.fasta`
**Explanation:** Shows consensus sequence alongside the alignment.

### View with wrap width
**Args:** `-w 80 alignment.fasta`
**Explanation:** Wraps display at 80 characters for narrow terminals.

### View compressed file
**Args:** `alignment.fasta.gz`
**Explanation:** Automatically detects and reads gzip-compressed alignment files.
