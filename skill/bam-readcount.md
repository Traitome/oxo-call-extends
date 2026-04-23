---
name: bam-readcount
category: variant-calling
description: bam-readcount - Generate metrics at single nucleotide positions from BAM files
tags: [bam-processing, variant-calling, coverage-metrics, nucleotide-counts]
author: oxo-call-community
source_url: "https://github.com/genome/bam-readcount"
---

## Concepts

- **Tool Overview**: bam-readcount generates detailed metrics at single nucleotide positions from BAM files, including base counts, quality scores, and read position information.

- **Per-Position Metrics**: Provides nucleotide counts, quality metrics, and mapping statistics for each specified position.

- **Variant Analysis Support**: Essential for variant calling validation and quality assessment.

- **Detailed Output**: Reports base counts, qualities, mapping qualities, and read positions for each nucleotide.

## Pitfalls

- **Reference Required**: Requires reference genome FASTA for position interpretation.

- **Memory Usage**: Large BAM files require substantial memory for processing.

- **Position Format**: Positions must be in correct format (chromosome:position). Off-by-one errors common.

- **Strand Bias**: Does not automatically correct for strand bias. Consider in downstream analysis.

## Examples

### Basic read count at position
**Args:** `bam-readcount -f reference.fasta -q 20 -b 20 alignments.bam chr1:1000`
**Explanation:** Reports nucleotide counts at chr1 position 1000 with quality filters.

### Multiple positions
**Args:** `bam-readcount -f reference.fasta alignments.bam -l positions.txt`
**Explanation:** Reads positions from file and reports metrics for each.

### Minimum quality thresholds
**Args:** `bam-readcount -f reference.fasta -q 30 -b 30 alignments.bam chr1:1000`
**Explanation:** Uses mapping quality ≥30 and base quality ≥30 thresholds.

### Output to file
**Args:** `bam-readcount -f reference.fasta alignments.bam -l positions.txt -o readcounts.txt`
**Explanation:** Writes output to file instead of stdout.

### Detailed output format
**Args:** `bam-readcount -f reference.fasta -d alignments.bam chr1:1000`
**Explanation:** Provides detailed output including per-base quality and position information.
