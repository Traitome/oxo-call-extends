---
name: flash
category: utility
description: "FLASH (Fast Length Adjustment of Short reads) merges paired-end sequencing reads from fragments shorter than twice the read length."
tags: [flash, utility, sequencing, read-merging, bioinformatics, ngs, paired-end, overlap]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/FLASH/"
---

## Concepts
- **Tool Overview**: FLASH (Fast Length Adjustment of Short reads) is a tool for merging overlapping paired-end reads from Illumina sequencing data to create longer, higher-quality sequences.
- **Core Function**: Identifies overlapping regions between paired-end reads and merges them into single longer reads, improving sequence coverage and quality.
- **Input/Output**: Input: Two FASTQ files (forward and reverse reads). Output: Merged reads, unmerged reads, and statistical summary.
- **Overlap Detection**: Uses dynamic programming to find optimal overlap between read pairs based on sequence similarity.
- **Consensus Calling**: Generates consensus sequences using quality-weighted base calling for overlapping regions.
- **Quality Control**: Filters merged reads by quality scores and overlap length to ensure reliable results.
- **Installation**: `conda install -c bioconda flash` or download and compile from source.

## Pitfalls
- **Insert Size Limits**: FLASH works best for fragments shorter than twice the read length. Larger fragments won't merge properly.
- **Minimum Overlap**: Requires at least 10bp overlap for merging. Very short fragments may not have sufficient overlap.
- **Adapter Sequences**: Must remove adapters before merging. Adapter sequences cause incorrect overlap detection.
- **Read Quality**: Low-quality reads produce poor consensus sequences. Trim low-quality bases before merging.
- **Memory Usage**: Processing large FASTQ files requires significant memory. Use streaming mode for large datasets.
- **Paired-End Order**: Ensure R1 and R2 files are properly paired. Mismatched pairs produce incorrect merges.

## Examples
### Basic read merging
**Args:** `flash read1.fastq read2.fastq -o merged`
**Explanation:** Merges paired-end reads and outputs to merged.extendedFrags.fastq.

### Custom overlap parameters
**Args:** `flash read1.fastq read2.fastq -o merged -m 10 -M 200 -x 0.1`
**Explanation:** Sets minimum overlap (10bp), max fragment length (200bp), and mismatch rate (0.1).

### With quality filtering
**Args:** `flash read1.fastq read2.fastq -o merged -q -Q 33`
**Explanation:** Enables quality filtering with Phred+33 quality encoding.

### Streaming mode for large files
**Args:** `flash --stream read1.fastq read2.fastq -o merged`
**Explanation:** Processes reads in streaming mode to reduce memory usage for large datasets.

### Generate HTML report
**Args:** `flash read1.fastq read2.fastq -o merged -h`
**Explanation:** Generates HTML report with merge statistics and quality metrics.
