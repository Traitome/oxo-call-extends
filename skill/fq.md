---
name: fq
category: formatting
description: fq is a library to generate and validate FASTQ file pairs.
tags: [fq, FASTQ, validation, generation, Rust]
author: oxo-call-community
source_url: "https://github.com/stjude-rust-labs/fq"
---

## Concepts
- **FASTQ Validation**: Validates FASTQ file format and integrity.
- **File Generation**: Generates synthetic FASTQ data for testing.
- **Subsampling**: Extracts random subsets of reads.
- **Format Conversion**: Converts between FASTQ formats.
- **Quality Control**: Performs quality checks on FASTQ files.

## Pitfalls
- **Memory Usage**: Processing large FASTQ files requires significant memory.
- **Format Assumptions**: Assumes standard FASTQ format.
- **Compression Handling**: May have issues with some compression formats.
- **Read Pairing**: Requires careful handling of paired-end data.
- **Validation Strictness**: Strict validation may reject valid but non-standard files.

## Examples
### Validate FASTQ file
**Args:** `fq validate reads.fastq`
**Explanation:** Validates the format and integrity of a FASTQ file.

### Generate synthetic reads
**Args:** `fq generate -n 1000 -l 150 -o synthetic.fastq`
**Explanation:** Generates 1000 synthetic reads of length 150.

### Subsample reads
**Args:** `fq subsample -i reads.fastq -o subsampled.fastq -n 10000`
**Explanation:** Randomly selects 10000 reads from the input.

### Convert to interleaved format
**Args:** `fq convert -1 reads_R1.fastq -2 reads_R2.fastq -o interleaved.fastq`
**Explanation:** Converts paired-end reads to interleaved format.

### Quality statistics
**Args:** `fq stats -i reads.fastq -o quality_stats.txt`
**Explanation:** Generates quality statistics for the FASTQ file.