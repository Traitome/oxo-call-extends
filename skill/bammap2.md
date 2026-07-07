---
name: bammap2
category: alignment
description: bammap2 - Fast BAM file mapping tool
tags: [bammap2, alignment, BAM, mapping, fast-mapping]
author: oxo-call-community
source_url: "https://github.com/wangyibin/bammap2"
---

## Concepts

- **Tool Overview**: bammap2 is a fast BAM file mapping tool optimized for speed and efficiency in read alignment. Version 0.1.7.
- **Core Function**: Performs rapid mapping of sequencing reads to reference genome.
- **Fast Mapping**: Optimized algorithm for quick read alignment.
- **BAM Output**: Directly outputs aligned reads in BAM format.
- **Memory Efficient**: Designed to handle large datasets with minimal memory usage.
- **Input/Output**: Accepts FASTQ reads and reference genome, outputs BAM alignments.
- **Installation**: `conda install -c bioconda bammap2`.

## Pitfalls

- **Reference Index**: Requires indexed reference genome.
- **Read Quality**: Poor quality reads may affect mapping accuracy.
- **Version Compatibility**: Options may vary between versions. Check help for your version.
- **Output Size**: BAM files can be large. Ensure sufficient disk space.

## Examples

### Basic mapping
**Args:** `bammap2 -i reads.fastq -r reference.fasta -o alignments.bam`
**Explanation:** Maps reads to reference genome and outputs BAM.

### Paired-end mapping
**Args:** `bammap2 -i R1.fastq R2.fastq -r reference.fasta -o alignments.bam`
**Explanation:** Maps paired-end reads to reference genome.

### Specify threads
**Args:** `bammap2 -i reads.fastq -r reference.fasta -o alignments.bam -t 8`
**Explanation:** Uses 8 threads for parallel mapping.

### Output SAM format
**Args:** `bammap2 -i reads.fastq -r reference.fasta -o alignments.sam --sam`
**Explanation:** Outputs alignments in SAM format.

### Verbose mode
**Args:** `bammap2 -i reads.fastq -r reference.fasta -o alignments.bam -v`
**Explanation:** Shows detailed mapping progress.

### Quality filtering
**Args:** `bammap2 -i reads.fastq -r reference.fasta -o alignments.bam -q 20`
**Explanation:** Filters reads with minimum quality score of 20.

### Display help
**Args:** `bammap2 --help`
**Explanation:** Shows all available command-line options and usage information.