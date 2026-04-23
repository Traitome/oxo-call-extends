---
name: authentict
category: qc
description: AuthentiCT - Tool for estimating present-day DNA contamination in ancient DNA single-stranded libraries
tags: [ancient-dna, contamination-estimation, single-stranded-libraries, paleogenomics]
author: oxo-call-community
source_url: "https://github.com/StephanePeyregne/AuthentiCT"
---

## Concepts

- **Tool Overview**: AuthentiCT estimates present-day DNA contamination in ancient DNA datasets from single-stranded libraries by modeling ancient DNA damage patterns.

- **Damage Model**: Uses C-to-T substitution patterns at molecule ends to distinguish ancient endogenous DNA from modern contaminants lacking deamination damage.

- **Single-Stranded Focus**: Designed specifically for single-stranded library protocols. Not suitable for double-stranded libraries or UDG-treated samples.

- **Input Format**: Accepts SAM format files with MD tags. BAM files can be piped through samtools view.

- **Maximum Likelihood Estimation**: Provides contamination rate estimates with standard errors using maximum likelihood fitting.

## Pitfalls

- **Library Type Restriction**: Only works with single-stranded libraries. Double-stranded libraries have different damage patterns not captured by the model.

- **UDG Treatment**: Cannot be used with UDG-treated samples as damage patterns are removed during library preparation.

- **Reference Bias**: Results affected by reference genome choice. Use appropriate reference for your ancient samples.

- **Minimum Sequence Count**: Requires sufficient sequences for reliable estimation. Default uses up to 100,000 sequences for model fitting.

## Examples

### Basic SAM file contamination estimation
**Args:** `AuthentiCT deam2cont -o contamination.txt input.sam`
**Explanation:** Estimates contamination rate from SAM file, outputs results to contamination.txt.

### BAM file input via pipe
**Args:** `samtools view input.bam | AuthentiCT deam2cont -o contamination.txt -`
**Explanation:** Processes BAM file by piping through samtools view. Use "-" to read from stdin.

### Limit sequences for faster processing
**Args:** `AuthentiCT deam2cont -s 10000 -o contamination.txt input.sam`
**Explanation:** Uses only first 10,000 sequences for model fitting, faster but potentially less accurate.

### Terminal position estimation
**Args:** `AuthentiCT deam2cont -t -o contamination.txt input.sam`
**Explanation:** Uses C-to-T frequencies at sequence termini for contamination estimation instead of full model.

### Quality filtering
**Args:** `AuthentiCT deam2cont -m 30 -l 30 -b 20 -o contamination.txt input.sam`
**Explanation:** Filters sequences by mapping quality (≥30), length (≥30bp), and base quality (≥20) before estimation.

### Print deamination frequencies
**Args:** `AuthentiCT deamination -o deamination.txt input.sam`
**Explanation:** Calculates and prints C-to-T substitution frequencies at different positions from sequence ends.

### Simulate ancient DNA sequences
**Args:** `AuthentiCT simulation -N 10000 -GC 0.42 -L 75 -o simulated.sam`
**Explanation:** Simulates 10,000 sequences with 42% GC content and 75bp average length for testing.

### Position-specific filtering
**Args:** `AuthentiCT deam2cont -p 1-10 -o contamination.txt input.sam`
**Explanation:** Only uses sequences covering positions 1-10 of reference for contamination estimation.
