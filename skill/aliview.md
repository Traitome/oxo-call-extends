---
name: aliview
category: alignment
description: AliView is an intuitive and fast alignment viewer and editor for DNA and amino acid sequences
tags: [aliview, alignment-viewer, sequence-editor, DNA, protein, phylogeny]
author: oxo-call-community
source_url: "https://ormbunkar.se/aliview/"
---

## Concepts

- **Tool Overview**: AliView is a fast, lightweight, and intuitive alignment viewer and editor designed for viewing and editing DNA and amino acid sequence alignments, optimized for handling large datasets efficiently.
- **Core Function**: Provides interactive visualization and editing of sequence alignments with support for multiple formats and integration with external alignment tools.
- **Supported Formats**: FASTA, NEXUS, PHYLIP, CLUSTAL, MSF (unlimited file sizes)
- **Key Features**: Mouse-wheel zoom, multiple color schemes (ClustalX, SeaView), consensus highlighting, sequence editing, reverse complement, translation, and external tool integration.
- **Alignment Integration**: Built-in MUSCLE alignment with support for MAFFT and other external aligners.
- **Installation**: Install via bioconda: `conda install -c bioconda aliview`
- **Citation**: Larsson, A. (2014). AliView: a fast and lightweight alignment viewer and editor for large data sets. Bioinformatics 30(22): 3276-3278.
- **License**: GPLv3

## Pitfalls

- **Java Requirement**: Requires Java Runtime Environment for execution.
- **Memory Usage**: Very large alignments may require increased Java heap space.
- **Format Compatibility**: Ensure input files use supported formats; some exotic formats may not be supported.
- **External Aligners**: For MAFFT or other external aligners, ensure they are installed and accessible in PATH.
- **Interactive Only**: Primarily a GUI tool; limited command-line batch processing capabilities.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available command-line options.

### Open alignment file
**Args:** `aliview alignment.fasta`
**Explanation:** Opens the FASTA alignment file in the AliView GUI.

### Open multiple alignment files
**Args:** `aliview align1.fasta align2.nexus align3.phylip`
**Explanation:** Opens multiple alignment files simultaneously.

### Open with specific color scheme
**Args:** `aliview -c clustal alignment.fasta`
**Explanation:** Opens alignment with ClustalX color scheme.

### Open and auto-align with MUSCLE
**Args:** `aliview -a muscle unaligned.fasta`
**Explanation:** Opens sequences and automatically performs MUSCLE alignment.

### Export alignment as PNG image
**Args:** `aliview -e output.png alignment.fasta`
**Explanation:** Exports the alignment as a PNG image file.

### Open in read-only mode
**Args:** `aliview -r alignment.fasta`
**Explanation:** Opens alignment in read-only mode to prevent accidental edits.

### Open and translate nucleotides
**Args:** `aliview -t alignment.fasta`
**Explanation:** Opens alignment with nucleotide sequences translated to amino acids.

### Set Java heap size for large alignments
**Args:** `aliview -Xmx4g large_alignment.fasta`
**Explanation:** Allocates 4GB of Java heap space for handling large alignments.

### Print alignment
**Args:** `aliview -p alignment.fasta`
**Explanation:** Prints the current alignment view.

### Search for pattern in alignment
**Args:** `aliview -s "ATG" alignment.fasta`
**Explanation:** Searches for the pattern "ATG" across the alignment.
