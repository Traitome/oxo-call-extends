---
name: je-suite
category: qc
description: Je is a suite to handle barcoded fastq files with (or without) Unique Molecule Identifiers (UMIs) and filter read duplicates using these UMIs.
tags: [je-suite, qc, FASTQ, UMI, barcoding]
author: oxo-call-community
source_url: "https://gbcs.embl.de/Je"
---

## Concepts

- **Tool Overview**: je-suite (v2.0.RC) - A suite for handling barcoded FASTQ files with Unique Molecule Identifiers (UMIs) and filtering read duplicates.
- **UMI Processing**: Handles Unique Molecule Identifiers for accurate duplicate detection.
- **Barcode Handling**: Processes barcoded sequencing data efficiently.
- **Duplicate Filtering**: Removes PCR duplicates using UMI information.
- **FASTQ Processing**: Efficiently processes FASTQ files with support for paired-end reads.
- **Quality Control**: Provides quality control metrics for sequencing data.

## Pitfalls

- **UMI Design**: Poor UMI design can lead to incorrect duplicate detection.
- **Barcode Misassignment**: Barcode errors can cause sample mixing.
- **Read Quality**: Low-quality reads can affect UMI accuracy.
- **PCR Bias**: Uneven PCR amplification can skew results.
- **File Format**: Requires proper FASTQ format with barcodes in headers.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Process barcoded FASTQ with UMI
**Args:** `je --input reads.fastq --barcode --umi --output deduplicated.fastq`
**Explanation:** Processes barcoded FASTQ file with UMI-based deduplication.

### Paired-end processing
**Args:** `je --input1 reads_R1.fastq --input2 reads_R2.fastq --umi --output_prefix dedup`
**Explanation:** Processes paired-end reads with UMI deduplication.

### Specify UMI location
**Args:** `je --input reads.fastq --umi-position 1-10 --output deduplicated.fastq`
**Explanation:** Specifies UMI position in read (positions 1-10).

### Quality filtering
**Args:** `je --input reads.fastq --umi --min-quality 20 --output filtered.fastq`
**Explanation:** Filters low-quality reads before deduplication.

### Generate statistics
**Args:** `je --input reads.fastq --umi --stats stats.txt --output deduplicated.fastq`
**Explanation:** Generates deduplication statistics report.

### Handle multiple samples
**Args:** `je --input-dir fastq_dir/ --output-dir results/ --umi`
**Explanation:** Processes multiple FASTQ files in a directory.