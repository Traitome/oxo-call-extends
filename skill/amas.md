---
name: amas
category: utility
description: Fast tool for alignment manipulation and calculating summary statistics on multiple sequence alignments
tags: [alignment, statistics, summary, fasta, phylip, nexus]
author: oxo-call-community
source_url: "https://github.com/marekborowiec/AMAS"
---

## Concepts

- **Tool Overview**: AMAS calculates summary statistics and performs manipulations on multiple sequence alignments in various formats.
- **Core Function**: Computes alignment statistics (length, variable sites, parsimony sites) and supports format conversion, concatenation, and partitioning.
- **Input/Output**: Input: FASTA, PHYLIP, NEXUS formats. Output: Same formats plus statistics reports.
- **Multi-format Support**: Handles both interleaved and sequential PHYLIP/NEXUS formats, and standard FASTA.
- **Installation**: Install via bioconda: `conda install -c bioconda amas`

## Pitfalls

- **Format Specification**: Must explicitly specify input format with `-f` flag - auto-detection is not supported.
- **Sequence Names**: Sequence names with special characters or spaces may cause issues in some output formats.
- **Missing Data**: Different gap characters (-, ?, N) may be treated differently across formats.
- **By-Taxon Mode**: Use `-s` flag for per-taxon statistics instead of overall alignment summary.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available options and format specifications.

### Calculate alignment statistics
**Args:** `summary -i alignment.fasta -f fasta`
**Explanation:** Computes overall alignment statistics including length, variable sites, and parsimony-informative sites.

### Per-taxon statistics
**Args:** `summary -i alignment.fasta -f fasta -s`
**Explanation:** Calculates statistics for each individual sequence (taxon) in the alignment.

### Convert FASTA to PHYLIP
**Args:** `convert -i alignment.fasta -f fasta -t phylip -o output.phy`
**Explanation:** Converts alignment from FASTA to sequential PHYLIP format.

### Convert to NEXUS interleaved
**Args:** `convert -i alignment.fasta -f fasta -t nexus-int -o output.nex`
**Explanation:** Converts to interleaved NEXUS format for PAUP/MrBayes.

### Concatenate multiple alignments
**Args:** `concat -i gene1.fasta gene2.fasta gene3.fasta -f fasta -t fasta -o concatenated.fasta`
**Explanation:** Concatenates multiple gene alignments into a supermatrix.

### Repartition alignment
**Args:** `split -i alignment.fasta -f fasta -p partitions.txt -o split_dir/`
**Explanation:** Splits alignment into partitions based on partition definition file.

### Remove taxa from alignment
**Args:** `remove -i alignment.fasta -f fasta -t fasta -o trimmed.fasta -n taxon1 taxon2`
**Explanation:** Removes specified taxa from the alignment.

### Calculate statistics for multiple files
**Args:** `summary -i "*.fasta" -f fasta`
**Explanation:** Computes statistics for all FASTA alignment files in the directory.
