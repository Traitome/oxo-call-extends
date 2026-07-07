---
name: mwga-utils
category: alignment
description: MWGA-utils - Utilities for processing Multispecies Whole Genome Alignments
tags: [mwga-utils, alignment, whole-genome, multispecies, maf, utilities]
author: oxo-call-community
source_url: "https://github.com/RomainFeron/mgwa_utils"
---

## Concepts

- **Tool Overview**: MWGA-utils v0.1.6 is a collection of utilities for manipulating and analyzing multispecies whole genome alignments (MWGA). It provides tools for processing alignment files in MAF (Multiple Alignment Format) and other common alignment formats.
- **Core Function**: Offers various commands to filter, extract, convert, and summarize whole genome alignment data. Enables comparative genomics analysis workflows involving multiple species alignments.
- **Subcommands**: Includes commands for extracting regions of interest, filtering alignment blocks, converting between formats, and generating summary statistics from MWGA data.
- **Input Format**: Works with MAF (Multiple Alignment Format) files as primary input, along with related alignment formats. May require sorted and indexed alignment files for efficient random access.
- **Output**: Produces processed alignment files, extracted regions, filtered blocks, or summary statistics depending on the specific utility command used.
- **Use Case**: Comparative genomics, evolutionary biology, phylogenetic analysis, synteny detection, and genome evolution studies involving multiple species.

## Pitfalls

- **MAF Format Complexity**: MAF files can be complex with multiple blocks and species. Understanding the block structure is essential for correct processing.
- **Coordinate Systems**: Whole genome alignments use coordinates that may differ between species due to insertions/deletions. Be aware of coordinate transformations when comparing across species.
- **Memory Usage**: Processing large MAF files (multiple species, whole genomes) can be memory-intensive. Consider working with chromosome-level or region-specific files for large-scale analyses.
- **Tool Dependencies**: Some subcommands may require additional alignment tools (likePHA模块) to be installed for format conversions.
- **Sorting Requirements**: Many operations require alignments to be sorted by genomic position. Unsorted alignments may produce errors or incorrect results.
- **Version Compatibility**: Format converters may produce output that is not fully compatible with all downstream tools. Validate output format when changing tools in a pipeline.

## Examples

### Display available commands
**Args:** `--help`
**Explanation:** Lists all available subcommands and utilities in the MWGA-utils package.

### Extract alignment region
**Args:** `extract -i alignment.maf -o output.maf -c chr1:1000000-2000000`
**Explanation:** Extracts alignment data for a specific genomic region from the whole genome alignment.

### Filter alignment blocks by species
**Args:** `filter -i full_alignment.maf -o species_filtered.maf -s "species1,species2"`
**Explanation:** Keeps only specified species in the alignment, removing others from all blocks.

### Convert MAF to FASTA
**Args:** `convert -i alignment.maf -o alignment.fasta -f fasta`
**Explanation:** Converts a multiple alignment in MAF format to concatenated FASTA format for each species.

### Generate alignment summary statistics
**Args:** `stats -i alignment.maf -o summary.tsv`
**Explanation:** Computes and outputs summary statistics including alignment coverage, conservation scores, and species representation per block.
