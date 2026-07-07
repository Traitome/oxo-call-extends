---
name: smakcr
category: sequence-analysis
description: smakcr - Count short k-mers fast from sequencing data
tags: [smakcr, sequence-analysis, k-mer, counting, genomics]
author: oxo-call-community
source_url: "https://github.com/julibeg/smakcr"
---

## Concepts

- **Tool Overview**: smakcr (v0.1.0) - A fast k-mer counting tool for sequencing data
- **Core Function**: Efficiently counts short k-mers from BAM or FASTQ files
- **Input/Output**: Accepts BAM/FASTQ; outputs k-mer counts in various formats
- **Algorithm**: Uses optimized hashing for fast k-mer counting
- **Installation**: `conda install -c bioconda smakcr`
- **Key Features**: Fast performance, memory-efficient, supports multiple input formats

## Pitfalls

- **k-mer Size**: k-mer size must be specified and affects performance
- **Memory Usage**: Larger k-mer sizes require more memory
- **Input Quality**: Low-quality reads affect counting accuracy
- **Ambiguity Handling**: N-containing reads may be skipped or handled differently
- **Strand Consideration**: Strand-specific protocols need appropriate flags
- **Output Size**: Large datasets can produce very large output files

## Examples

### Display help
**Args:** `smakcr --help`
**Explanation:** Shows available options and usage information.

### Count k-mers from FASTQ
**Args:** `smakcr -i reads.fastq -k 21 -o counts.txt`
**Explanation:** Count 21-mers from FASTQ file.

### Count from BAM
**Args:** `smakcr -i aligned.bam -k 31 -o counts.txt`
**Explanation:** Count 31-mers from aligned BAM file.

### With quality filter
**Args:** `smakcr -i reads.fastq -k 25 -q 30 -o counts.txt`
**Explanation:** Count k-mers only from reads with quality >= 30.

### Output in binary format
**Args:** `smakcr -i reads.fastq -k 21 -b -o counts.bin`
**Explanation:** Output counts in binary format for efficiency.

### Count unique k-mers only
**Args:** `smakcr -i reads.fastq -k 21 -u -o unique_counts.txt`
**Explanation:** Count only unique k-mers.

### Multi-threaded counting
**Args:** `smakcr -i reads.fastq -k 21 -t 8 -o counts.txt`
**Explanation:** Use 8 threads for parallel counting.