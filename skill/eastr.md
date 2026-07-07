---
name: eastr
category: alignment
description: "Tool for emending alignments of spuriously spliced transcript reads."
tags: [eastr, alignment, RNA-seq, splicing, transcriptomics]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/eastr/#usage"
---

## Concepts

- **Tool Overview**: EaStR is a tool for correcting misaligned RNA-seq reads that have spuriously spliced alignments.
- **Core Function**: Identifies and corrects incorrectly spliced read alignments by re-aligning across splice junctions.
- **Input/Output**: Input: BAM file with aligned reads. Output: Corrected BAM file with improved alignments.
- **Algorithm**: Uses dynamic programming to detect and correct spurious splice sites in read alignments.
- **Key Features**: Splice site correction, misalignment detection, preserves read pairs, improves variant calling accuracy.
- **Installation**: `conda install -c bioconda eastr`

## Pitfalls

- **Alignment Quality**: Requires high-quality initial alignments.
- **Memory Usage**: Large BAM files require significant RAM.
- **Processing Time**: Can be slow for large datasets.
- **Reference Genome**: Requires indexed reference genome.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic usage
**Args:** `eastr -i input.bam -o output.bam -r ref.fasta`
**Explanation:** Corrects spurious splice alignments in input BAM file.

### With verbose output
**Args:** `eastr -i input.bam -o output.bam -r ref.fasta -v`
**Explanation:** Runs with verbose output to see correction details.

### With maximum intron size
**Args:** `eastr -i input.bam -o output.bam -r ref.fasta -m 100000`
**Explanation:** Sets maximum intron size to 100kb.

### Paired-end mode
**Args:** `eastr -i input.bam -o output.bam -r ref.fasta --paired`
**Explanation:** Processes paired-end reads preserving read pair information.

### Output statistics
**Args:** `eastr -i input.bam -o output.bam -r ref.fasta -s stats.txt`
**Explanation:** Generates statistics about corrections made.