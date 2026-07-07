---
name: filtlong
category: qc
description: "A quality filtering tool for Nanopore and PacBio long reads that uses read length and quality scores to produce better subsets."
tags: [filtlong, qc, long-reads, Nanopore, PacBio, quality-filtering, bioinformatics, sequencing]
author: oxo-call-community
source_url: "https://github.com/rrwick/Filtlong"
---

## Concepts

- **Tool Overview**: Filtlong is a tool for filtering long reads by quality. It takes a set of Nanopore or PacBio reads and produces a smaller, better subset based on both read length (longer is better) and read identity (higher is better).
- **Core Function**: Scores each read using length, mean quality, and window quality metrics, then filters to retain only the best reads according to configurable thresholds and weights.
- **Input/Output**: Input: FASTQ/FASTA long reads (optionally with reference). Output: Filtered FASTQ/FASTA reads to stdout.
- **Algorithm**: Uses k-mer matching when reference is provided to determine read quality instead of Phred scores. Without reference, uses embedded quality scores. Supports read trimming and splitting at regions of poor k-mer coverage.
- **Key Features**: Dual quality assessment (Phred or k-mer based), read trimming/splitting, flexible thresholds, score weighting, unit suffixes for lengths.
- **Installation**: `conda install -c bioconda filtlong` or `git clone https://github.com/rrwick/Filtlong.git && cd Filtlong && make`

## Pitfalls

- **External Reference Quality**: Using short reads as reference is only recommended if they are high quality with complete coverage. Poor short reads can lead to incorrect filtering decisions.
- **Output to stdout**: Filtlong outputs to stdout, so must be piped or redirected. forgetting to redirect output results in filtered reads being lost.
- **Quality Score Interpretation**: `--min_mean_q` and `--min_window_q` use percent identity (0-100), not Phred scores. A quality of 90 means 90% identity, not Q90.
- **Target Bases vs Keep Percent**: When both `--target_bases` and `--keep_percent` are used, the more stringent threshold is applied.
- **Window Size Default**: Default sliding window size of 250bp may miss local quality issues in very long reads; consider reducing window size for long nanopore reads.

## Examples

### Basic filtering
**Args:** `filtlong --min_length 1kb --keep_percent 90 input.fastq.gz | gzip > output.fastq.gz`
**Explanation:** Filters to retain only reads >= 1kb and keeps the best 90% by bases. Output is piped through gzip to compress.

### With target bases limit
**Args:** `filtlong --min_length 1000 --target_bases 500m --keep_percent 90 input.fastq.gz | gzip > output.fastq.gz`
**Explanation:** Limits output to 500 megabases of the best reads while maintaining length and quality thresholds.

### With short read reference
**Args:** `filtlong -1 short_1.fastq.gz -2 short_2.fastq.gz --min_length 1kb --keep_percent 90 input.fastq.gz | gzip > output.fastq.gz`
**Explanation:** Uses k-mer matching against Illumina reads to assess quality instead of Phred scores, providing more accurate quality assessment.

### With trimming and splitting
**Args:** `filtlong -1 short_1.fastq.gz -2 short_2.fastq.gz --min_length 1kb --trim --split 500 input.fastq.gz | gzip > output.fastq.gz`
**Explanation:** Trims unmatching bases from read ends and splits reads at 500+ consecutive non-matching bases, keeping only high-quality segments.

### Quality-focused filtering
**Args:** `filtlong --min_mean_q 85 --min_window_q 75 --min_length 2kb input.fastq.gz | gzip > output.fastq.gz`
**Explanation:** Applies strict quality thresholds (85% mean identity, 75% window identity) for high-accuracy applications like assembly.

### Using unit suffixes
**Args:** `filtlong --min_length 1kb --max_length 100kb --target_bases 2gb input.fastq.gz | gzip > output.fastq.gz`
**Explanation:** Uses convenient unit suffixes (kb, mb, gb) for specifying thresholds. Supports k, kb, m, mb, g, gb (case insensitive).

### Verbose output
**Args:** `filtlong --verbose input.fastq.gz 2>&1 | head -100`
**Explanation:** Shows detailed information for each read including length, quality scores, and any trimming/splitting actions.
