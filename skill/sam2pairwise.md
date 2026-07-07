---
name: sam2pairwise
category: alignment
description: Reconstruct pairwise alignments from SAM files using CIGAR and MD tags
tags: ["sam2pairwise", "alignment", "SAM", "CIGAR", "MD tag"]
author: oxo-call-community
source_url: "https://github.com/mlafave/sam2pairwise/blob/master/README.md"
---

## Concepts

- **Tool Overview**: sam2pairwise (v1.0.0) is a tool that reconstructs pairwise alignments from SAM files by parsing CIGAR strings and MD tags to generate the actual aligned sequence pairs.
- **Core Function**: Converts compressed alignment information (CIGAR/MD) into human-readable pairwise alignments between reads and their reference sequences.
- **Algorithm**: Parses CIGAR operations and MD tags to reconstruct gaps, mismatches, and matches, generating complete pairwise alignment strings.
- **Input Format**: SAM alignment files with CIGAR and MD tags.
- **Output Format**: Pairwise alignments in various formats (FASTA-like, custom), alignment statistics.
- **Use Case**: Alignment visualization, variant validation, sequence comparison, educational purposes.

## Pitfalls

- **MD tag requirement**: Requires MD tags in SAM file for accurate mismatch detection.
- **CIGAR parsing**: Complex CIGAR strings may cause parsing issues.
- **File size**: Large SAM files require significant memory.
- **Performance**: Processing millions of reads can be time-consuming.
- **Format compatibility**: Requires properly formatted SAM files.
- **Memory usage**: Storing many pairwise alignments requires substantial memory.

## Examples

### Basic pairwise reconstruction
**Args:** `sam2pairwise -i alignments.sam -o pairwise.txt`
**Explanation:** `-i` input SAM file; `-o` output file with pairwise alignments.

### With BAM input
**Args:** `sam2pairwise -i alignments.bam -o pairwise.txt`
**Explanation:** Automatically detects and processes BAM files.

### Output FASTA format
**Args:** `sam2pairwise -i alignments.sam -o pairwise.fasta --format fasta`
**Explanation:** `--format fasta` outputs alignments in FASTA-like format.

### Limit output to first N reads
**Args:** `sam2pairwise -i alignments.sam -o pairwise.txt -n 1000`
**Explanation:** `-n` maximum number of reads to process.

### Include quality scores
**Args:** `sam2pairwise -i alignments.sam -o pairwise.txt --quality`
**Explanation:** `--quality` includes quality scores in output.

### Filter by mapping quality
**Args:** `sam2pairwise -i alignments.sam -o pairwise.txt -q 20`
**Explanation:** `-q` minimum mapping quality threshold.

### Output statistics
**Args:** `sam2pairwise -i alignments.sam -o pairwise.txt --stats stats.txt`
**Explanation:** `--stats` outputs alignment statistics to separate file.