---
name: mummer
category: alignment
description: MUMmer is a system for rapidly aligning entire genomes
tags: [mummer, alignment, genome-comparison, suffix-tree]
author: oxo-call-community
source_url: "http://mummer.sourceforge.net/"
---

## Concepts

- **Tool Overview**: MUMmer v3.23 is a genome alignment system based on suffix tree algorithms. It finds maximal exact matches (MUMs) between two DNA sequences. While older than MUMmer4, it remains widely used for bacterial genome comparisons and is the predecessor to the modern MUMmer4 system.
- **Core Function**: Identifies maximal unique matches between reference and query genomes. These matches can be used directly for dotplot visualization or fed into clustering algorithms for identifying conserved regions.
- **Algorithm**: Uses suffix tree data structure to find exact matches of minimum length (default 20bp) between sequences. The algorithm is fast but has memory requirements proportional to genome size.
- **Input Format**: Accepts multi-FASTA files for reference and query sequences. Can handle one reference vs multiple queries.
- **Output**: Lists all MUMs with their positions in reference and query, orientation, and length. Output is typically redirected to a file.
- **Comparison with MUMmer4**: MUMmer3 is the legacy version. MUMmer4 offers better scalability (48-bit vs 32-bit addressing), multi-threading, and handles larger genomes efficiently.

## Pitfalls

- **Memory Limitations**: MUMmer3 uses 32-bit addressing, limiting it to genomes of approximately 500Mb. For larger genomes, use MUMmer4.
- **Reference vs Query Order**: Unlike BLAST, MUMmer output depends on which sequence is reference and which is query. Swapping inputs produces different output.
- **Minimum Match Length**: Default minimum match length is 20bp. Adjust with `-l` flag for shorter matches (faster) or longer matches (more unique).
- **Non-unique Matches**: By default, matches must be unique in both reference and query (-mum option). Using `-b` (both strands) changes match uniqueness criteria.
- **Gap Handling**: MUMmer itself doesn't handle gaps. Use nucmer (part of MUMmer package) for gapped alignments.
- **Deprecated Status**: MUMmer3 is no longer actively maintained. New projects should use MUMmer4 for better performance and features.

## Examples

### Find maximal unique matches
**Args:** `mummer -mum ref.fasta query.fasta > matches.mums`
**Explanation:** Finds maximal unique matches present in both reference and query. Output contains match positions and lengths. This is the most common operating mode.

### Search both strands
**Args:** `mummer -mum -b ref.fasta query.fasta > matches.both`
**Explanation:** The `-b` flag reports matches on both forward and reverse complement strands. Essential when strand orientation is unknown or when comparing sequences that may be inverted.

### Report reverse complement positions
**Args:** `mummer -mum -b -c ref.fasta query.fasta > matches.rc`
**Explanation:** The `-c` flag reports query match positions relative to the forward strand, even if the match is on the reverse complement. Converts reverse coordinates to forward orientation.

### Use with run-mummer1 for automated alignment
**Args:** `run-mummer1 ref.fasta query.fasta prefix`
**Explanation:** Automated workflow for 1-to-1 genome alignment. Combines mummer, mgaps, and combineMUMs for finding ungapped alignments between two closely related genomes.

### Generate dotplot with mummerplot
**Args:** `mummerplot -postscript -p output matches.mums`
**Explanation:** Creates a postscript dotplot from mummer output. Requires gnuplot. The -p flag sets the output prefix. Edit the generated .gp file to customize colors and styling.
