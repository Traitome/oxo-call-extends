---
name: mapad
category: alignment
description: An aDNA aware short-read mapper
tags: [mapad, alignment, ancient-DNA, aDNA]
author: oxo-call-community
source_url: "https://github.com/mpieva/mapAD"
---

## Concepts

- **Tool Overview**: mapad v0.45.0 - An aDNA (ancient DNA) aware short-read mapper optimized for ancient DNA sequencing data.
- **Core Function**: Maps short sequencing reads to a reference genome with special consideration for ancient DNA characteristics.
- **Input/Output**: Input: FASTQ reads, reference genome; Output: BAM alignment file.
- **Installation**: `conda install -c bioconda mapad`
- **aDNA Optimization**: Specifically designed to handle ancient DNA damage patterns and fragmentation.
- **Damage-aware Mapping**: Considers characteristic aDNA damage patterns (e.g., C->T transitions).

## Pitfalls

- **Read Quality**: Poor quality ancient DNA reads affect mapping accuracy.
- **Contamination**: Modern DNA contamination affects results.
- **Reference Genome**: Must use appropriate reference genome for ancient samples.
- **Damage Patterns**: Unusual damage patterns may require parameter adjustment.
- **Computational Resources**: Large datasets require significant memory.
- **Fragment Length**: Very short fragments may map poorly.

## Examples

### Map ancient DNA reads
**Args:** `mapad -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o aligned.bam`
**Explanation:** Maps paired-end ancient DNA reads to reference.

### Single-end mapping
**Args:** `mapad -r ref.fa -s reads.fastq -o aligned.bam`
**Explanation:** Maps single-end ancient DNA reads.

### With quality filtering
**Args:** `mapad -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o aligned.bam -q 30`
**Explanation:** Filters reads with quality < 30.

### Verbose mode
**Args:** `mapad -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o aligned.bam -v`
**Explanation:** Provides detailed logging during mapping.

### Damage-aware mode
**Args:** `mapad -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o aligned.bam --damage-aware`
**Explanation:** Enables damage-aware mapping.

### Generate mapping statistics
**Args:** `mapad -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o aligned.bam --stats stats.txt`
**Explanation:** Generates mapping statistics.