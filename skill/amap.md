---
name: amap
category: alignment
description: Multiple sequence alignment program based on sequence annealing algorithm
tags: [amap, alignment, MSA, sequence-annealing, protein, bioinformatics]
author: oxo-call-community
source_url: "http://bio.math.berkeley.edu/amap/"
---

## Concepts

- **Tool Overview**: AMAP (v2.2) is a multiple sequence alignment program based on sequence annealing, designed to align protein sequences with tunable sensitivity/specificity tradeoff.
- **Core Function**: Uses posterior decoding and sequence-annealing alignment instead of traditional progressive alignment, allowing control over the sensitivity/specificity tradeoff through adjustable parameters.
- **Input/Output**: Accepts multi-FASTA (MFA) format sequences; outputs alignments in MFA or CLUSTALW format, with optional annotation files and posterior probability matrices.
- **Installation**: Available via Bioconda (`conda install -c bioconda amap`) or as `amap-align` on some systems due to naming conflicts.
- **Algorithm**: Based on ProbCons source code but eliminates consistency transformation, maximizing the expected Alignment Metric Accuracy (AMA) score which integrates sensitivity and specificity into a balanced measure.

## Pitfalls

- **Naming Conflict**: On Debian systems, the command may be named `amap-align` instead of `amap` due to conflicts with a network diagnostic tool.
- **Input Format**: Requires multi-FASTA format; other formats like Clustal must be converted first.
- **Memory Requirements**: Large datasets may require significant memory; consider splitting large alignments.
- **Parameter Tuning**: The `--gap-factor` and `--edge-weight-threshold` parameters control sensitivity/specificity; default values may not be optimal for all datasets.
- **Java GUI**: The `-gui` option requires Java runtime environment for AMAP Display visualization.

## Examples

### Basic multiple alignment
**Args:** `amap input.fasta`
**Explanation:** Performs multiple sequence alignment on the input FASTA file using default parameters, outputting to standard output.

### Output in CLUSTALW format
**Args:** `amap -clustalw input.fasta > output.clustal`
**Explanation:** Aligns sequences and outputs in CLUSTALW format for compatibility with other tools.

### Increase sensitivity
**Args:** `amap -g 0 -w 0 input.fasta`
**Explanation:** Sets gap-factor to 0 and edge-weight-threshold to 0 for maximum sensitivity, useful for detecting distant homologs.

### Use iterative refinement
**Args:** `amap -ir 100 input.fasta`
**Explanation:** Applies 100 rounds of iterative refinement to improve alignment quality.

### Generate pairwise alignments
**Args:** `amap -pairs input.fasta`
**Explanation:** Generates all-pairs pairwise alignments before performing multiple alignment.

### Output posterior probabilities
**Args:** `amap -print input.fasta > posteriors.txt`
**Explanation:** Outputs only the posterior probability matrices instead of the full alignment.

### Enable verbose mode
**Args:** `amap -v input.fasta`
**Explanation:** Reports progress during alignment, helpful for monitoring large jobs.

### Prepare output for AMAP Display GUI
**Args:** `amap -gui 10 1 input.fasta > alignment.out`
**Explanation:** Generates output for the AMAP Display Java GUI, starting at weight 10 with step size 1.