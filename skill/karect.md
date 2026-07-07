---
name: karect
category: alignment
description: Read error correction tool based on multiple alignment of overlapping reads.
tags: [karect, alignment, error correction, reads, sequencing]
author: oxo-call-community
source_url: "https://github.com/aminallam/karect/blob/master/karect_manual.pdf"
---

## Concepts

- **Tool Overview**: karect (v1.0) - Corrects sequencing errors using multiple alignment.
- **Multiple Alignment**: Uses overlapping read alignment for error detection.
- **Error Correction**: Corrects substitution, insertion, and deletion errors.
- **k-mer Based**: Uses k-mer analysis for error detection.
- **Quality Improvement**: Improves read quality for downstream analysis.
- **Parallel Processing**: Supports multi-threaded processing.

## Pitfalls

- **Read Overlap**: Requires sufficient read overlap for correction.
- **Memory Usage**: Large datasets require significant memory.
- **Time Complexity**: Complex error correction can be time-consuming.
- **Read Length**: Performance varies with read length.
- **Error Rate**: High error rates may exceed correction capacity.
- **Format Compatibility**: Requires specific input formats.

## Examples

### Correct single-end reads
**Args:** `karect -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects errors in single-end reads.

### Correct paired-end reads
**Args:** `karect -i reads_1.fastq -j reads_2.fastq -o corrected/`
**Explanation:** Corrects paired-end reads.

### Set k-mer size
**Args:** `karect -i reads.fastq -o corrected.fastq -k 31`
**Explanation:** Uses k-mer size of 31 for error detection.

### Parallel processing
**Args:** `karect -i reads.fastq -o corrected.fastq -t 8`
**Explanation:** Uses 8 threads for parallel correction.

### Quality filtering
**Args:** `karect -i reads.fastq -o corrected.fastq -q 20`
**Explanation:** Filters reads with quality < 20.

### Output statistics
**Args:** `karect -i reads.fastq -o corrected.fastq -s stats.txt`
**Explanation:** Generates correction statistics.