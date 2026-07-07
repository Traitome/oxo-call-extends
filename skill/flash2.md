---
name: flash2
category: utility
description: "FLASH2 is the next-generation version of FLASH, merging paired-end sequencing reads from fragments shorter than twice the read length."
tags: [flash2, utility, sequencing, read-merging, bioinformatics, ngs, paired-end]
author: oxo-call-community
source_url: "https://github.com/dstreett/FLASH2"
---

## Concepts
- **Tool Overview**: FLASH2 is an improved implementation of the FLASH read merging tool, designed to merge overlapping paired-end reads from Illumina sequencing data.
- **Core Function**: Merges paired-end reads where the insert size is shorter than twice the read length, creating longer reads with higher quality bases.
- **Input/Output**: Input: Two FASTQ files (R1 and R2) from paired-end sequencing. Output: Merged FASTQ file, unmerged reads, and statistics report.
- **Algorithm Improvements**: FLASH2 uses a more efficient overlap detection algorithm with better error handling and support for longer reads.
- **Quality Trimming**: Integrated quality trimming before and after merging to improve consensus accuracy.
- **Paired-end Support**: Handles various paired-end library layouts including standard, mate-pair, and long-read protocols.
- **Installation**: `conda install -c bioconda flash2` or compile from source code.

## Pitfalls
- **Insert Size Estimation**: Accurate insert size estimation is critical. Incorrect estimates lead to failed merges or false merges.
- **Read Quality**: Poor quality reads reduce merging efficiency. Quality filtering recommended before merging.
- **Overlap Requirements**: Requires sufficient overlap (typically >10bp). Short fragments with minimal overlap may not merge.
- **Adapter Contamination**: Adapter sequences must be removed before merging. Adapter sequences cause misalignment.
- **Memory Usage**: Large datasets require significant memory. Use --split option for memory-efficient processing.
- **Barcode Demultiplexing**: Must demultiplex barcoded libraries before merging. Mixed barcodes produce incorrect consensus sequences.

## Examples
### Basic read merging
**Args:** `flash2 -1 reads_R1.fastq -2 reads_R2.fastq -o merged`
**Explanation:** Merges paired-end reads and outputs merged reads to merged.extendedFrags.fastq.

### Custom insert size range
**Args:** `flash2 -1 reads_R1.fastq -2 reads_R2.fastq -o merged -m 20 -M 500`
**Explanation:** Sets minimum overlap to 20bp and maximum fragment length to 500bp for merging.

### With quality trimming
**Args:** `flash2 -1 reads_R1.fastq -2 reads_R2.fastq -o merged -q -t 20`
**Explanation:** Trims low-quality bases (Q<20) before merging to improve consensus quality.

### Memory-efficient processing
**Args:** `flash2 -1 reads_R1.fastq -2 reads_R2.fastq -o merged --split`
**Explanation:** Processes reads in chunks to reduce memory usage for large datasets.

### Generate detailed statistics
**Args:** `flash2 -1 reads_R1.fastq -2 reads_R2.fastq -o merged -d`
**Explanation:** Generates detailed statistics report including merge rates, quality scores, and fragment length distribution.
