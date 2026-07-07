---
name: rust-overlaps
category: assembly
description: A fast utility for enumerating suffix-prefix overlaps within sequence sets.
tags: ["rust-overlaps", "overlap", "assembly", "sequence", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/jbaaijens/rust-overlaps"
---

## Concepts

- **Tool Overview**: rust-overlaps (v0.1.1) is a fast command-line utility for identifying suffix-prefix overlaps between sequences. It's designed for overlap-based assembly and sequence analysis.
- **Core Function**: Enumerates all suffix-prefix overlaps within a set of sequences, satisfying user-specified minimal overlap length and maximal error rate thresholds.
- **Algorithm**: Uses efficient string comparison with error-tolerant matching to detect overlaps. Implements parallel processing for speed.
- **Input Format**: FASTA/FASTQ files containing sequences to compare.
- **Output Format**: TSV file with overlap information (sequence pairs, overlap length, error rate).
- **Use Case**: Overlap-based sequence assembly, sequence clustering, repeat detection, sequence alignment validation.

## Pitfalls

- **Memory requirements**: Large sequence sets require significant memory.
- **Performance**: Many sequences can lead to O(n²) comparisons.
- **Error rate threshold**: Too strict or too loose thresholds affect results.
- **Sequence length**: Short sequences may produce spurious overlaps.
- **Duplicate sequences**: Identical sequences produce perfect overlaps.
- **Parallelization overhead**: Small datasets may not benefit from parallel processing.

## Examples

### Find overlaps
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv`
**Explanation:** `-i` input sequences; `-o` output overlap TSV file.

### Minimum overlap length
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv -m 50`
**Explanation:** `-m` minimum overlap length in base pairs.

### Maximum error rate
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv -e 0.05`
**Explanation:** `-e` maximum allowed error rate (5%).

### Threaded processing
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv -t 8`
**Explanation:** `-t` number of threads for parallel comparison.

### Verbose output
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv -v`
**Explanation:** `-v` verbose mode with progress reporting.

### Output FASTA with overlaps
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv --fasta merged.fasta`
**Explanation:** `--fasta` outputs merged sequences based on overlaps.

### Self-comparison only
**Args:** `rust-overlaps -i sequences.fasta -o overlaps.tsv --self`
**Explanation:** `--self` only compare sequences within the same file.
