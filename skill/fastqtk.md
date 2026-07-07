---
name: fastqtk
category: expression
description: "fastqtk is a fast and lightweight tool for interleaving/deinterleaving/counting/trimming FASTQ files."
tags: [fastqtk, expression, FASTQ, interleaving, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ndaniel/fastqtk"
---

## Concepts

- **Tool Overview**: fastqtk is a fast and lightweight tool for manipulating FASTQ files, including interleaving, deinterleaving, counting, and trimming operations.
- **Core Function**: Provides efficient manipulation of FASTQ files with multiple operations.
- **Input/Output**: Input: FASTQ files. Output: Processed FASTQ files, statistics.
- **Algorithm**: Implements efficient parsing and manipulation algorithms.
- **Key Features**: Fast processing, interleaving/deinterleaving, counting, trimming, lightweight design.
- **Installation**: `conda install -c bioconda fastqtk`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Quality Scores**: Assumes standard Phred quality encoding.
- **Processing Time**: Very large files may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Interleave paired-end reads
**Args:** `fastqtk interleave -1 reads_1.fastq -2 reads_2.fastq -o interleaved.fastq`
**Explanation:** Interleaves paired-end FASTQ files.

### Deinterleave reads
**Args:** `fastqtk deinterleave -i interleaved.fastq -1 reads_1.fastq -2 reads_2.fastq`
**Explanation:** Deinterleaves interleaved FASTQ file.

### Count reads
**Args:** `fastqtk count -i reads.fastq`
**Explanation:** Counts number of reads in FASTQ file.

### Trim reads
**Args:** `fastqtk trim -i reads.fastq -o trimmed.fastq -l 100`
**Explanation:** Trims reads to specified length.

### Quality trimming
**Args:** `fastqtk quality-trim -i reads.fastq -o trimmed.fastq -q 20`
**Explanation:** Trims reads by quality score.