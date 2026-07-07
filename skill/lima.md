---
name: lima
category: qc
description: lima - The PacBio Barcode Demultiplexer
tags: [lima, qc, barcode, demultiplexing, PacBio, sequencing]
author: oxo-call-community
source_url: "https://lima.how"
---

## Concepts

- **Barcode Demultiplexing**: Demultiplexes PacBio CCS reads by barcode
- **PacBio Sequencing**: Optimized for PacBio sequencing data
- **Barcode Recognition**: Identifies barcode sequences in reads
- **Quality Filtering**: Filters reads based on quality
- **Multiple Barcodes**: Supports multiple barcode sets
- **CCS Reads**: Works with Circular Consensus Sequence reads

## Pitfalls

- **Barcode Design**: Barcode sequences must be carefully designed
- **Read Quality**: Poor quality reads may fail demultiplexing
- **Barcode Misassignment**: May assign reads to wrong barcodes
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **File Format**: Strict format requirements for input files

## Examples

### Demultiplex reads
**Args:** `lima input.bam barcodes.fasta output.bam`
**Explanation:** Demultiplexes PacBio CCS reads by barcode sequences.

### Multiple barcode sets
**Args:** `lima input.bam --barcodes barcode_set1.fasta --barcodes barcode_set2.fasta output.bam`
**Explanation:** Uses multiple barcode sets for demultiplexing.

### Single-end mode
**Args:** `lima --single-end input.bam barcodes.fasta output.bam`
**Explanation:** Processes single-end barcodes.

### Threads
**Args:** `lima --threads 8 input.bam barcodes.fasta output.bam`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `lima --min-score 30 input.bam barcodes.fasta output.bam`
**Explanation:** Filters reads with minimum quality score of 30.

### Output statistics
**Args:** `lima --dump-clips input.bam barcodes.fasta output.bam`
**Explanation:** Outputs clipped barcode statistics.