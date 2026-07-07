---
name: nudup
category: utility
description: nudup marks or removes duplicate molecules using NuGEN molecular tagging technology.
tags: [nudup, utility, deduplication, molecular-tagging]
author: oxo-call-community
source_url: "http://nugentechnologies.github.io/nudup/"
---

## Concepts

- **Tool Overview**: nudup removes PCR duplicates using molecular barcodes.
- **Core Function**: Identifies and removes duplicate reads based on molecular tags.
- **Algorithm**: Uses molecular barcode information for duplicate detection.
- **Input Format**: Accepts FASTQ reads with molecular tags.
- **Output**: Produces deduplicated reads or marked BAM files.
- **Use Case**: Sequencing data deduplication, reducing PCR bias, and improving variant calling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Barcode Quality**: Results depend on barcode quality.
- **Tag Format**: Requires specific molecular tag format.
- **Read Quality**: Results depend on input read quality.
- **False Positives**: May incorrectly mark unique reads as duplicates.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `nudup --help`
**Explanation:** Shows available options and usage instructions.

### Remove duplicates
**Args:** `nudup -i reads.fastq -o deduplicated.fastq`
**Explanation:** Removes duplicates from FASTQ file.

### With BAM input
**Args:** `nudup -i alignments.bam -o deduplicated.bam --bam`
**Explanation:** Processes BAM file and outputs deduplicated BAM.

### Mark duplicates
**Args:** `nudup -i reads.fastq -o marked.fastq --mark-only`
**Explanation:** Marks duplicates without removing them.

### Barcode length
**Args:** `nudup -i reads.fastq -b 8 -o deduplicated.fastq`
**Explanation:** Sets barcode length to 8 bases.

### Mismatch tolerance
**Args:** `nudup -i reads.fastq -m 1 -o deduplicated.fastq`
**Explanation:** Allows 1 mismatch in barcode comparison.

### Threads
**Args:** `nudup -i reads.fastq -t 8 -o deduplicated.fastq`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nudup -i reads.fastq -v -o deduplicated.fastq`
**Explanation:** Runs with verbose output.