---
name: showali
category: utility
description: showali - Minimalistic TUI viewer for aligned biological sequences
tags: ["showali", "utility", "fasta", "alignment", "viewer"]
author: oxo-call-community
source_url: "https://github.com/kirilenkobm/showali"
---

## Concepts

- **Tool Overview**: showali (v1.0.1) is a terminal-based viewer for sequence alignments.
- **Core Function**: Displays aligned sequences in terminal with syntax highlighting.
- **Algorithm**: Parses multiple alignment formats and renders in text mode.
- **Input/Output**: Accepts FASTA, ALN, MAF, PHYLIP formats.
- **TUI Interface**: Terminal-based interactive viewer.
- **Applications**: Quick alignment inspection, sequence analysis.

## Pitfalls

- **Terminal Requirements**: Requires terminal with color support.
- **Large Alignments**: May be slow for very large alignments.
- **Format Support**: Limited to specific alignment formats.
- **Memory Usage**: High memory for large alignments.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### View alignment
**Args:** `showali alignment.fasta`
**Explanation:** Open alignment file in TUI viewer.

### View PHYLIP
**Args:** `showali -f phylip alignment.phy`
**Explanation:** `-f phylip` specifies PHYLIP format.

### View MAF
**Args:** `showali -f maf alignment.maf`
**Explanation:** `-f maf` specifies MAF format.

### Help command
**Args:** `showali --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `showali --version`
**Explanation:** Shows current version.

### With wrap
**Args:** `showali -w 80 alignment.fasta`
**Explanation:** `-w 80` wrap at 80 characters.

### No color
**Args:** `showali --no-color alignment.fasta`
**Explanation:** `--no-color` disable color output.
