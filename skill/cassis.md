---
name: cassis
category: structural-variation
description: Detection of genomic rearrangement breakpoints
tags: [cassis, structural-variation, breakpoint, rearrangement, genomics]
author: oxo-call-community
source_url: "http://pbil.univ-lyon1.fr/software/Cassis/"
---

## Concepts

- **Tool Overview**: Cassis detects precise genomic rearrangement breakpoints from sequencing data.
- **Core Function**: Identifies and localizes breakpoints of genomic rearrangements.
- **Algorithm**: Implements methods described in Lemaitre et al., 2008 for breakpoint detection.
- **Input**: BED files with interval data and sequence alignment information.
- **Output**: Breakpoint positions and rearrangement annotations.
- **Application**: Structural variation analysis and cancer genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cassis`

## Pitfalls

- **BED Format**: Requires properly formatted BED input files.
- **Alignment Quality**: Breakpoint detection depends on alignment quality.
- **Complex Rearrangements**: Complex rearrangements may be difficult to resolve.
- **Reference Dependence**: Results depend on reference genome quality.

## Examples

### Detect breakpoints
**Args:** `cassis -i intervals.bed -o breakpoints.txt`
**Explanation:** Detects genomic rearrangement breakpoints from interval data.

### With sequence data
**Args:** `cassis -i intervals.bed -s sequences.fa -o breakpoints.txt`
**Explanation:** Uses sequence data to refine breakpoint detection.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.