---
name: cigar
category: formatting
description: Manipulate SAM CIGAR strings
tags: [cigar, formatting, SAM, BAM, alignment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/brentp/cigar"
---

## Concepts

- **Tool Overview**: cigar provides utilities for manipulating and analyzing CIGAR strings from SAM/BAM alignment files.
- **Core Function**: Parses, manipulates, and extracts information from CIGAR strings used in sequence alignment.
- **Features**: CIGAR string parsing, length calculations, soft/hard clipping handling, and alignment statistics.
- **Input**: CIGAR strings from SAM/BAM files or alignment data.
- **Output**: Parsed CIGAR information, alignment statistics, and modified CIGAR strings.
- **Application**: Alignment processing, variant calling, and sequence analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cigar`

## Pitfalls

- **CIGAR Format**: Requires properly formatted CIGAR strings.
- **Clipping**: Soft and hard clipping require different handling.
- **Indels**: Insertions and deletions affect coordinate calculations.
- **Reference Length**: CIGAR operations must match reference length.
- **Quality Scores**: May need additional quality filtering for soft-clipped regions.

## Examples

### Parse CIGAR string
**Args:** `cigar parse -c "100M2D50M"`
**Explanation:** Parses and displays CIGAR string components.

### Calculate alignment length
**Args:** `cigar length -c "100M2D50M"`
**Explanation:** Calculates total alignment length from CIGAR.

### Extract clipped regions
**Args:** `cigar clip -c "5S100M" -t soft`
**Explanation:** Extracts soft-clipped portion from CIGAR.

### Display help
**Args:** `cigar --help`
**Explanation:** Shows all available commands and options.