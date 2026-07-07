---
name: pear
category: utility
description: PEAR merges paired-end reads from Illumina sequencing.
tags: [pear, utility, paired-end, read-merging]
author: oxo-call-community
source_url: "https://sco.h-its.org/exelixis/web/software/pear/"
---

## Concepts

- **Tool Overview**: PEAR merges paired-end reads.
- **Core Function**: Combines overlapping paired reads.
- **Algorithm**: Uses statistical overlap detection.
- **Input Format**: Accepts paired FASTQ files.
- **Output**: Produces merged and unmerged reads.
- **Use Case**: Read preprocessing, assembly preparation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Overlap Quality**: Results depend on read quality.
- **Minimum Overlap**: Requires sufficient overlap length.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pear --help`
**Explanation:** Shows available options and usage instructions.

### Merge reads
**Args:** `pear -f forward.fastq -r reverse.fastq -o merged.fastq`
**Explanation:** Merges paired-end reads.

### With overlap
**Args:** `pear -f forward.fastq -r reverse.fastq -o merged.fastq -v 20`
**Explanation:** Sets minimum overlap to 20 bp.

### Verbose mode
**Args:** `pear -v -f forward.fastq -r reverse.fastq -o merged.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pear -j 8 -f forward.fastq -r reverse.fastq -o merged.fastq`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pear -f forward.fastq -r reverse.fastq -o output.fastq`
**Explanation:** Outputs merged and unmerged files.

### Quality threshold
**Args:** `pear -f forward.fastq -r reverse.fastq -o merged.fastq -q 30`
**Explanation:** Sets minimum quality threshold.