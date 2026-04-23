---
name: 3seq
category: utility
description: 3SEQ tests all sequence triplets in an alignment for a mosaic recombination signal.
tags: [3seq, utility, recombination, phylogenetics, sequence-analysis]
author: oxo-call-community
source_url: "https://mol.ax/software/3seq"
---

## Concepts

- **Tool Overview**: 3SEQ is a recombination detection algorithm that tests all sequence triplets in a multiple alignment for mosaic recombination signals using an exact nonparametric method. Version 1.8.
- **Core Function**: Identifies recombinant sequences by testing every triplet in an alignment for statistical evidence of mosaic structure (one sequence being a recombinant of two others).
- **Input/Output**: Input is a PHYLIP or FASTA format multiple sequence alignment. Output includes a log file (.3s.log) and a recombination results file (.3s.rec) with recombinant parents, p-values, and breakpoint ranges.
- **Installation**: Install via bioconda: `conda install -c bioconda 3seq`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **P-value Table**: Requires a pre-computed p-value table for statistical testing. Must be generated before first analysis using `-g` flag or downloaded separately.
- **Triplet Testing**: Tests all N×(N-1)×(N-2) sequence triplets, where N is the number of sequences. Complexity is O(N³) but optimized for practical runtime.

## Pitfalls

- **P-value Table Required**: First-time users must generate or download a p-value table before running analysis. Without it, the program will fail.
- **P-value Table Size**: The p-value table can be large (438MB for 700-sequence table). Ensure sufficient disk space.
- **Alignment Quality**: Results depend heavily on alignment quality. Poorly aligned regions produce false positive recombination signals.
- **Runtime Scaling**: Analysis scales cubically with sequence count. Large alignments (>500 sequences) may take significant time.
- **Only Detects Mosaic Recombination**: 3SEQ detects mosaic patterns where a sequence appears to be a patchwork of two parent sequences. It does not detect gene conversion or other recombination forms.
- **License Restriction**: CC-BY-NC-SA-4.0 license means non-commercial use only.

## Examples

### Display help and usage information
**Args:** `-h`
**Explanation:** Shows available usage modes and command-line options for 3SEQ.

### View sequence alignment information
**Args:** `-i alignment.phy`
**Explanation:** Reads the alignment file and displays basic information (number of sequences, length, etc.) without running recombination analysis.

### Generate p-value table (first-time setup)
**Args:** `-g myPvalueTable500 500`
**Explanation:** Generates a p-value table for alignments up to 500 sequences. This step is required before running recombination analysis and takes several minutes.

### Run recombination detection analysis
**Args:** `-f alignment.phy -ptable myPvalueTable500 -id myAnalysis`
**Explanation:** Runs the full recombination detection on the alignment using the pre-computed p-value table. Output files are prefixed with "myAnalysis". Results include recombinant sequences, parent candidates, p-values, and breakpoint ranges.

### Analyze a large alignment with appropriate p-value table
**Args:** `-f large_alignment.fasta -ptable pvaluetable700 -id largeRun`
**Explanation:** Analyzes a larger alignment using the 700-sequence p-value table. Ensure the p-value table size matches or exceeds the number of sequences in the alignment.

### Quick check on a small alignment
**Args:** `-f small.phy -ptable myPvalueTable500 -id quickCheck`
**Explanation:** Runs 3SEQ on a small alignment for quick recombination screening. Small alignments (<50 sequences) complete in seconds.
