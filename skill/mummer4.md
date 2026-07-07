---
name: mummer4
category: alignment
description: MUMmer is a system for rapidly aligning entire genomes
tags: [mummer4, alignment, genome-comparison, nucmer, promer, suffix-tree]
author: oxo-call-community
source_url: "https://mummer4.github.io"
---

## Concepts

- **Tool Overview**: MUMmer v4.0 is a versatile genome alignment system based on suffix tree (MUMmer) and suffix array (nucmer) algorithms. It can align entire genomes of any size, handling bacterial to mammalian genomes efficiently. The system finds maximal exact matches (MUMs) between sequences.
- **Core Function**: Provides multiple alignment modes: mummer (exact match finding), nucmer (nucleotide alignment for similar genomes), promer (protein-level alignment for divergent genomes), and dnadiff (comprehensive whole-genome comparison).
- **Algorithm**: Uses a 48-bit suffix array (vs 32-bit suffix tree in MUMmer3), enabling alignment of arbitrarily large genomes. Supports multi-threaded execution with OpenMP parallelization.
- **Input Format**: Accepts multi-FASTA files for both reference and query sequences. Can handle incomplete genomes with hundreds or thousands of contigs.
- **Output**: Delta files containing alignment coordinates, plus optional parsed outputs from show-* utilities (show-coords, show-snps, show-tiling, show-aligns).
- **Main Utilities**: nucmer (nucleotide alignment), promer (translated alignment), dnadiff (comprehensive analysis), mummer (exact MUM finding), mummerplot (dotplot visualization), run-mummer1/3 (automated workflows).

## Pitfalls

- **Version Compatibility**: MUMmer4 nucmer produces output compatible with MUMmer3 utilities, but some older scripts may need updating. Delta files are compatible across versions.
- **Genome Size Limits Removed**: Unlike MUMmer3 (~500Mb reference limit), MUMmer4 can handle genomes of any size. Human-chimp alignment is demonstrated in the paper.
- **Alignment Sensitivity**: Default nucmer settings are optimized for closely related genomes. Use `--maxgap` and `--mincluster` options to adjust for more divergent genomes.
- **Repeat Regions**: Highly repetitive genomes may produce many alignments. Use `--maxmatch` to limit or filter repeat-induced alignments.
- **Delta File Format**: The delta format is space-delimited with specific columns. Parse carefully when extracting alignment coordinates.
- **Output Interpretation**: Without additional parsing, nucmer output (delta file) requires post-processing with show-* utilities to extract meaningful alignment information.

## Examples

### Basic nucmer alignment
**Args:** `nucmer --prefix=align ref.fasta query.fasta`
**Explanation:** Aligns query sequences to reference using nucmer. Output is stored in align.delta. This is the most common use case for comparing two genome assemblies.

### Find maximal unique matches
**Args:** `mummer -mum -b -c ref.fasta query.fasta > mums.out`
**Explanation:** Finds all maximal unique matches (-mum) between reference and query on both strands (-b), reporting positions relative to forward strand (-c). Output goes to stdout.

### Generate dotplot visualization
**Args:** `mummerplot -x "[0,275287]" -y "[0,265111]" -postscript -p output mums.out`
**Explanation:** Creates a postscript dotplot from mummer output. Use sequence lengths to set axis ranges. The -p flag sets the output prefix for .gp, .fplot, .rplot, and .ps files.

### Comprehensive genome comparison with dnadiff
**Args:** `dnadiff --prefix=report ref.fasta query.fasta`
**Explanation:** Runs a complete analysis pipeline producing: .report (summary), .snps (SNP calls), .diff (breakpoints), .unref/.unqry (unaligned sequences). Most comprehensive output format.

### Extract alignment coordinates
**Args:** `show-coords -THrcl align.delta > coords.txt`
**Explanation:** Converts delta file to coordinate format. -T (tabular), -H (no header), -r (relative coordinates), -c (show coverage), -l (show length). Essential for downstream parsing.

### Call SNPs from alignment
**Args:** `show-snps -rlTHC align.delta > snps.txt`
**Explanation:** Extracts SNPs from the alignment. -r (coordinates relative to reference), -l (show alignment length), -T (tab-delimited), -H (no header), -C (show SNP context).
