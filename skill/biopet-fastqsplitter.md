---
name: biopet-fastqsplitter
category: utility
description: Split FASTQ files into equal-sized chunks
tags: [fastq, splitting, parallel-processing]
author: oxo-call-community
source_url: "https://github.com/biopet/fastq-splitter"
---

## Concepts
- **Tool Overview**: FastqSplitter divides a FASTQ file into smaller, equally-sized FASTQ files for parallel processing.
- **Even Distribution**: Distributes reads evenly across output files to avoid positional bias.
- **Chunking**: Useful for parallelizing pipelines that process FASTQ files independently.
- **Applications**: Parallel processing, pipeline chunking, workload distribution.

## Pitfalls
- **File Count**: Output file count must be specified; cannot split by read count.

## Examples
### Split FASTQ into 5 chunks
**Args:** `java -jar FastqSplitter.jar -I reads.fq -n 5 -o split_`
**Explanation:** Splits FASTQ into 5 equally-sized output files.

### Split paired-end reads
**Args:** `java -jar FastqSplitter.jar -I R1.fq -I2 R2.fq -n 10 -o split_R1_ -o2 split_R2_`
**Explanation:** Splits paired-end FASTQ files maintaining read pair correspondence.
