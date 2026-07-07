---
name: calcs
category: alignment
description: Append minimap2's CS tag to SAM/BAM files for base-level alignment information
tags: [calcs, minimap2, cs-tag, alignment, sam, bam]
author: oxo-call-community
source_url: "https://github.com/akikuno/calcs"
---

## Concepts

- **Tool Overview**: calcs appends minimap2's CS tag to SAM/BAM alignment files.
- **Core Function**: Adds CS (color space) tag containing base-level alignment information.
- **CS Tag**: Encodes matches, mismatches, insertions, and deletions in alignment.
- **Input**: SAM or BAM file aligned with minimap2.
- **Output**: SAM/BAM file with CS tag added.
- **Application**: Variant calling and detailed alignment analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda calcs`

## Pitfalls

- **Minimap2 Required**: Input must be aligned with minimap2 for CS tag generation.
- **File Format**: Accepts SAM/BAM; output format matches input.
- **Memory Usage**: Large BAM files require significant memory.
- **Tag Compatibility**: Not all downstream tools use CS tag.

## Examples

### Add CS tag to SAM file
**Args:** `calcs -i aligned.sam -o with_cs.sam`
**Explanation:** Adds CS tag to minimap2-aligned SAM file.

### Process BAM file
**Args:** `calcs -i aligned.bam -o with_cs.bam`
**Explanation:** Adds CS tag to BAM file and outputs in BAM format.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.