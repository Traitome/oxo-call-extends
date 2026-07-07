---
name: guide-counter
category: bioinformatics
description: guide-counter provides fast and accurate guide counting for CRISPR screening experiments.
tags: [guide-counter, CRISPR, screening, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/guide-counter"
---

## Concepts

- **Guide Counting**: guide-counter counts CRISPR guide RNA reads.

- **CRISPR Screening**: Designed for CRISPR knockout/activation screening data.

- **Fast Processing**: Optimized for speed with large sequencing datasets.

- **Accurate Matching**: Uses exact or fuzzy matching for guide identification.

- **Barcode Support**: Handles barcoded screening libraries.

- **Quality Filtering**: Filters low-quality reads before counting.

## Pitfalls

- **Guide Library Design**: Results depend on guide library quality.

- **Sequencing Depth**: Low depth reduces counting accuracy.

- **Off-target Effects**: Off-target matches may affect results.

- **Barcode Misidentification**: Barcode errors can cause miscounts.

- **Read Quality**: Poor quality reads affect matching accuracy.

## Examples

### Count guides
**Args:** `guide-counter -i reads.fastq -g guides.txt -o counts.txt`
**Explanation:** Counts CRISPR guides from sequencing reads.

### Paired-end reads
**Args:** `guide-counter -i reads_1.fastq -i2 reads_2.fastq -g guides.txt -o counts.txt`
**Explanation:** Processes paired-end sequencing data.

### Allow mismatches
**Args:** `guide-counter -i reads.fastq -g guides.txt -m 2 -o counts.txt`
**Explanation:** Allows up to 2 mismatches in guide matching.

### Batch processing
**Args:** `for f in *.fastq; do guide-counter -i $f -g guides.txt -o ${f%.fastq}_counts.txt; done`
**Explanation:** Processes multiple sequencing files.

### Barcode-aware counting
**Args:** `guide-counter -i reads.fastq -g guides.txt -b barcodes.txt -o counts.txt`
**Explanation:** Handles barcoded screening libraries.

### Quality filtering
**Args:** `guide-counter -i reads.fastq -g guides.txt -q 30 -o counts.txt`
**Explanation:** Filters reads by quality score.

### Help command
**Args:** `guide-counter --help`
**Explanation:** Shows available options and usage information.