---
name: satsuma2
category: alignment
description: FFT cross-correlation based synteny aligner designed for parallel computing
tags: ["satsuma2", "alignment", "synteny", "FFT"]
author: oxo-call-community
source_url: "https://github.com/bioinfologics/satsuma2"
---

## Concepts

- **Tool Overview**: Satsuma2 (v20161123) is an FFT cross-correlation based synteny aligner designed to make full use of parallel computing for large-scale genome alignments.
- **Core Function**: Performs fast and accurate whole-genome alignments by leveraging FFT-based cross-correlation to identify syntenic regions.
- **Algorithm**: Uses Fast Fourier Transform (FFT) to efficiently compute cross-correlations between sequences, enabling rapid detection of homologous regions.
- **Parallel Computing**: Designed to run on multi-core processors and clusters for high-performance alignment.
- **Input/Output**: Accepts FASTA genome sequences and produces alignment files in various formats.
- **Applications**: Comparative genomics, evolutionary analysis, and genome rearrangement studies.

## Pitfalls

- **Memory Requirements**: High memory usage for large genome alignments.
- **Computational Resources**: Requires significant compute resources for optimal performance.
- **Sensitivity Tuning**: May miss distant homologies without proper parameter adjustment.
- **Output Complexity**: Large output files require careful parsing and analysis.
- **Reference Bias**: Alignment quality depends on reference genome choice.
- **Runtime**: May be slow for very large or highly divergent genomes.

## Examples

### Basic genome alignment
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -o output_dir`
**Explanation:** `-q` query genome; `-t` target genome; `-o` output directory.

### With multiple threads
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -o output_dir -threads 16`
**Explanation:** `-threads 16` uses 16 threads for parallel processing.

### Adjust sensitivity
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -o output_dir -sensitivity high`
**Explanation:** `-sensitivity high` increases sensitivity for distant homologies.

### Output in MAF format
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -o output_dir -format maf`
**Explanation:** `-format maf` outputs alignments in MAF format.

### Chained alignments
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -o output_dir -chain`
**Explanation:** `-chain` generates chained alignments for synteny blocks.

### Progressive alignment
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -r reference.fasta -o output_dir`
**Explanation:** `-r` uses reference genome for progressive alignment.

### Quality filtering
**Args:** `SatsumaSynteny2 -q query.fasta -t target.fasta -o output_dir -minScore 500`
**Explanation:** `-minScore 500` filters alignments with score below 500.