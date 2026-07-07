---
name: ngmerge
category: qc
description: NGmerge merges paired-end reads and removes sequencing adapters.
tags: [ngmerge, qc, read-merging, adapter-trimming]
author: oxo-call-community
source_url: "https://github.com/jsh58/NGmerge"
---

## Concepts

- **Tool Overview**: NGmerge merges overlapping paired-end sequencing reads.
- **Core Function**: Merges reads, trims adapters, and performs quality filtering.
- **Algorithm**: Uses overlap detection with quality-aware merging.
- **Input Format**: Accepts paired FASTQ files.
- **Output**: Produces merged reads and unmerged reads.
- **Use Case**: Read preprocessing, library preparation, and metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Overlap Requirements**: Requires sufficient overlap between reads.
- **Adapter Sequences**: Must specify correct adapter sequences.
- **Quality Thresholds**: Results depend on quality settings.
- **Memory Usage**: Large datasets require memory.
- **Output Size**: Merged files can be large.

## Examples

### Display help
**Args:** `NGmerge --help`
**Explanation:** Shows available options and usage instructions.

### Basic merge
**Args:** `NGmerge -1 reads_1.fastq -2 reads_2.fastq -o merged.fastq`
**Explanation:** Merges paired-end reads.

### With adapter trimming
**Args:** `NGmerge -1 reads_1.fastq -2 reads_2.fastq -a adapters.fasta -o merged.fastq`
**Explanation:** Trims adapters before merging.

### Quality filtering
**Args:** `NGmerge -1 reads_1.fastq -2 reads_2.fastq -q 30 -o merged.fastq`
**Explanation:** Filters reads by quality score.

### Minimum overlap
**Args:** `NGmerge -1 reads_1.fastq -2 reads_2.fastq -m 20 -o merged.fastq`
**Explanation:** Sets minimum overlap to 20 bases.

### Output unmerged
**Args:** `NGmerge -1 reads_1.fastq -2 reads_2.fastq -u unmerged.fastq -o merged.fastq`
**Explanation:** Outputs unmerged reads separately.

### Threads
**Args:** `NGmerge -1 reads_1.fastq -2 reads_2.fastq -t 8 -o merged.fastq`
**Explanation:** Uses 8 threads for parallel processing.