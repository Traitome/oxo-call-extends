---
name: pandaseq
category: alignment
description: PANDASEQ aligns and merges overlapping paired-end Illumina reads.
tags: [pandaseq, alignment, read-merging, illumina]
author: oxo-call-community
source_url: "https://github.com/neufeld/pandaseq"
---

## Concepts

- **Tool Overview**: PANDASEQ merges overlapping paired-end sequencing reads.
- **Core Function**: Aligns and reconstructs overlapping sequences.
- **Algorithm**: Uses dynamic programming for read alignment.
- **Input Format**: Accepts FASTQ paired-end reads.
- **Output**: Produces merged sequences and quality scores.
- **Use Case**: Amplicon sequencing, metagenomics, and paired-end read processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Overlap Requirement**: Requires overlapping reads.
- **Read Quality**: Results depend on input read quality.
- **Primer Removal**: May require primer trimming first.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pandaseq --help`
**Explanation:** Shows available options and usage instructions.

### Merge reads
**Args:** `pandaseq -f reads_1.fastq -r reads_2.fastq -o merged.fastq`
**Explanation:** Merges paired-end reads.

### With quality filtering
**Args:** `pandaseq -f reads_1.fastq -r reads_2.fastq -q 20 -o merged.fastq`
**Explanation:** Filters by quality score.

### Primer trimming
**Args:** `pandaseq -f reads_1.fastq -r reads_2.fastq -p primer.fasta -o merged.fastq`
**Explanation:** Removes primers before merging.

### Verbose mode
**Args:** `pandaseq -v -f reads_1.fastq -r reads_2.fastq -o merged.fastq`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `pandaseq -f reads_1.fastq -r reads_2.fastq -o merged.fasta -F`
**Explanation:** Outputs in FASTA format.

### Number of threads
**Args:** `pandaseq -t 8 -f reads_1.fastq -r reads_2.fastq -o merged.fastq`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum overlap
**Args:** `pandaseq -m 10 -f reads_1.fastq -r reads_2.fastq -o merged.fastq`
**Explanation:** Sets minimum overlap to 10 bp.