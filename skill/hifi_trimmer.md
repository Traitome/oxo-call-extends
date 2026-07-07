---
name: hifi_trimmer
category: bioinformatics
description: hifi-trimmer filters and trims extraneous adapter sequences from HiFi reads using BLAST search.
tags: [hifi_trimmer, adapter-trimming, PacBio, HiFi, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/hifi-trimmer"
---

## Concepts

- **Adapter Trimming**: hifi-trimmer removes adapter sequences.

- **BLAST Search**: Uses BLAST for adapter detection.

- **PacBio HiFi**: Optimized for PacBio HiFi sequencing data.

- **Quality Control**: Improves data quality.

- **Read Filtering**: Filters reads with adapter remnants.

- **Long Reads**: Handles long read sequencing data.

## Pitfalls

- **Data Quality**: Results depend on input data quality.

- **BLAST Configuration**: Requires proper BLAST configuration.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Memory Usage**: Large datasets may require significant memory.

- **False Positives**: May incorrectly trim valid sequences.

## Examples

### Trim adapters
**Args:** `hifi-trimmer -i reads.fastq -o trimmed.fastq`
**Explanation:** Trims adapter sequences from HiFi reads.

### With custom adapters
**Args:** `hifi-trimmer -i reads.fastq -o trimmed.fastq -a adapters.fasta`
**Explanation:** Uses custom adapter sequences.

### Batch processing
**Args:** `for f in *.fastq; do hifi-trimmer -i $f -o ${f%.fastq}_trimmed.fastq; done`
**Explanation:** Processes multiple FASTQ files.

### Quality filtering
**Args:** `hifi-trimmer -i reads.fastq -o trimmed.fastq -q 20`
**Explanation:** Filters by quality score.

### Help command
**Args:** `hifi-trimmer --help`
**Explanation:** Shows available options and usage information.