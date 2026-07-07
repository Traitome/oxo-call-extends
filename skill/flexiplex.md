---
name: flexiplex
category: utility
description: "Flexiplex is a fast and versatile sequence demultiplexer for omics data, supporting barcodes, UMIs, and flexible pattern matching."
tags: [flexiplex, utility, demultiplexing, barcode, umi, sequencing, bioinformatics, ngs]
author: oxo-call-community
source_url: "https://github.com/DavidsonGroup/flexiplex"
---

## Concepts
- **Tool Overview**: Flexiplex is a versatile demultiplexing tool that handles complex barcode layouts, UMIs, and supports both Illumina and custom sequencing platforms.
- **Core Function**: Demultiplexes barcoded sequencing reads by matching barcodes against a reference set with configurable mismatch tolerance.
- **Input/Output**: Input: FASTQ files (single-end or paired-end). Output: Demultiplexed FASTQ files, undetermined reads, statistics report.
- **Barcode Types**: Supports single barcodes, dual barcodes, combinatorial barcodes, and inline barcodes within reads.
- **UMI Handling**: Extracts and appends UMI sequences to read names for downstream deduplication.
- **Error Correction**: Uses fuzzy matching with configurable edit distance for barcode identification.
- **Installation**: `conda install -c bioconda flexiplex` or clone from GitHub. Requires Python 3.7+.

## Pitfalls
- **Barcode Design**: Poorly designed barcodes with low Hamming distance cause misassignment. Use barcodes with minimum 3bp difference.
- **Mismatch Tolerance**: High mismatch tolerance increases false positives. Adjust based on expected sequencing error rate.
- **UMI Length**: Variable UMI lengths require consistent configuration. Ensure all samples have same UMI structure.
- **Undetermined Reads**: High percentage of undetermined reads indicates barcode design or sequencing issues.
- **Memory Usage**: Large barcode sets or FASTQ files require significant memory. Use streaming mode for large datasets.
- **Paired-End Sync**: Ensure R1 and R2 reads remain paired after demultiplexing. Check pairing integrity post-processing.

## Examples
### Basic demultiplexing
**Args:** `flexiplex demultiplex -r reads.fastq -b barcodes.csv -o demultiplexed/`
**Explanation:** Demultiplexes reads using barcode CSV file and outputs to directory.

### Paired-end demultiplexing
**Args:** `flexiplex demultiplex -r reads_R1.fastq -R reads_R2.fastq -b barcodes.csv -o demultiplexed/`
**Explanation:** Demultiplexes paired-end reads while maintaining read pairing.

### With UMI extraction
**Args:** `flexiplex demultiplex -r reads.fastq -b barcodes.csv -u -o demultiplexed/`
**Explanation:** Extracts UMI sequences and appends to read names during demultiplexing.

### Custom mismatch tolerance
**Args:** `flexiplex demultiplex -r reads.fastq -b barcodes.csv -m 2 -o demultiplexed/`
**Explanation:** Allows up to 2 mismatches in barcode sequences during matching.

### Generate report
**Args:** `flexiplex demultiplex -r reads.fastq -b barcodes.csv -o demultiplexed/ --report report.html`
**Explanation:** Generates HTML report with demultiplexing statistics and barcode distribution.
