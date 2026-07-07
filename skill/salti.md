---
name: salti
category: visualization
description: Terminal-based multiple sequence alignment viewer
tags: ["salti", "alignment", "visualization", "terminal", "MSA"]
author: oxo-call-community
source_url: "https://github.com/Sam-Sims/salti"
---

## Concepts

- **Tool Overview**: Salti (v0.8.0) is a modern terminal-based multiple sequence alignment (MSA) viewer designed for efficient visualization and analysis of sequence alignments.
- **Core Function**: Displays and navigates multiple sequence alignments in the terminal, supporting various alignment formats and interactive exploration.
- **Algorithm**: Implements efficient rendering of alignments with color highlighting, consensus sequence display, and interactive navigation.
- **Input Format**: Multiple sequence alignment files (FASTA, Clustal, PHYLIP, Nexus, STOCKHOLM).
- **Output Format**: Terminal-based visualization, optional export to various formats.
- **Use Case**: Sequence alignment analysis, phylogenetic studies, comparative genomics, quick alignment inspection.

## Pitfalls

- **Terminal compatibility**: Requires terminal with proper color support.
- **Large alignments**: May have performance issues with very large MSAs.
- **Font rendering**: Alignment display depends on terminal font settings.
- **Memory usage**: Large alignments require significant memory for rendering.
- **Interactive mode**: May not work well in non-interactive environments.
- **Format support**: Some rare alignment formats may not be supported.

## Examples

### View alignment
**Args:** `salti alignment.fasta`
**Explanation:** Opens alignment file in interactive viewer.

### With consensus sequence
**Args:** `salti alignment.fasta --consensus`
**Explanation:** Shows consensus sequence above alignment.

### Color by conservation
**Args:** `salti alignment.fasta --color conservation`
**Explanation:** Colors residues based on conservation level.

### Show only first 100 positions
**Args:** `salti alignment.fasta --range 1-100`
**Explanation:** Displays only specified position range.

### Export to HTML
**Args:** `salti alignment.fasta --export html > alignment.html`
**Explanation:** Exports alignment to HTML format.

### Hide gaps
**Args:** `salti alignment.fasta --hide-gaps`
**Explanation:** Hides gap characters for cleaner display.

### Highlight specific residue
**Args:** `salti alignment.fasta --highlight A`
**Explanation:** Highlights all occurrences of specified residue.