---
name: pbmarkdup
category: qc
description: pbmarkdup marks duplicate reads from PacBio amplified libraries.
tags: [pbmarkdup, qc, pacbio, duplicates]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: pbmarkdup marks duplicate reads.
- **Core Function**: Identifies PCR duplicates in PacBio data.
- **Algorithm**: Uses sequence-based duplicate detection.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces marked BAM files.
- **Use Case**: Duplicate removal, quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Library Type**: Designed for amplified libraries.
- **Duplicate Definition**: May have false positives/negatives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbmarkdup --help`
**Explanation:** Shows available options and usage instructions.

### Mark duplicates
**Args:** `pbmarkdup input.bam output.bam`
**Explanation:** Marks duplicates in BAM file.

### Remove duplicates
**Args:** `pbmarkdup --remove-duplicates input.bam output.bam`
**Explanation:** Removes marked duplicates.

### Verbose mode
**Args:** `pbmarkdup -v input.bam output.bam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbmarkdup -t 4 input.bam output.bam`
**Explanation:** Uses 4 threads for parallel processing.

### Output metrics
**Args:** `pbmarkdup input.bam output.bam --metrics metrics.txt`
**Explanation:** Outputs duplicate metrics.

### Output format
**Args:** `pbmarkdup input.bam output.bam --output-format sam`
**Explanation:** Outputs in SAM format.