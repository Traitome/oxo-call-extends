---
name: hilive2
category: bioinformatics
description: HiLive2 performs real-time read alignment of Illumina sequencing data.
tags: [hilive2, real-time-alignment, Illumina, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.com/rki_bioinformatics/HiLive2"
---

## Concepts

- **Real-time Alignment**: HiLive2 performs real-time read alignment.

- **Illumina Data**: Optimized for Illumina sequencing data.

- **Streaming Analysis**: Processes reads as they arrive.

- **Rapid Analysis**: Provides fast alignment results.

- **Sequence Alignment**: Aligns sequencing reads to reference.

- **On-demand Processing**: Processes data on demand.

## Pitfalls

- **Data Rate**: Requires sufficient processing speed.

- **Reference Genome**: Requires appropriate reference genome.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Real-time processing may require significant memory.

- **Network Latency**: Network streaming may introduce latency.

## Examples

### Real-time alignment
**Args:** `hilive2 --input reads.fastq --output alignments.sam --genome hg38`
**Explanation:** Performs real-time alignment of Illumina reads.

### With streaming input
**Args:** `hilive2 --stream --genome hg38`
**Explanation:** Processes streaming sequencing data.

### Batch processing
**Args:** `for f in *.fastq; do hilive2 --input $f --output ${f%.fastq}.sam; done`
**Explanation:** Processes multiple FASTQ files.

### Quality filtering
**Args:** `hilive2 --input reads.fastq --output alignments.sam --quality 20`
**Explanation:** Filters reads by quality score.

### Help command
**Args:** `hilive2 --help`
**Explanation:** Shows available options and usage information.