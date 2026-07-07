---
name: ssake
category: assembly
description: SSAKE is a genomics application for de novo assembly of millions of very short DNA sequences.
tags: [ssake, assembly, de-novo, short-read]
author: oxo-call-community
source_url: "https://github.com/warrenlr/SSAKE"
---

## Concepts

- **Tool Overview**: ssake (v4.0) is a de novo assembler designed specifically for assembling millions of very short DNA sequences (25-50bp).
- **Core Function**: Uses overlap-layout-consensus approach optimized for short reads with high coverage.
- **Algorithm**: Builds contigs by overlapping reads based on user-defined k-mer size and minimum overlap.
- **Input/Output**: Input: FASTQ/FASTA reads; Output: Assembled contigs in FASTA format.
- **Assembly Strategy**: Progressive contig building with iterative extension and error correction.
- **Installation**: `conda install -c bioconda ssake` or download from GitHub repository.

## Pitfalls

- **Read Length**: Optimal for reads ≤ 50bp; longer reads may require parameter adjustments.
- **Coverage Depth**: Requires high coverage (50x+) for reliable assembly.
- **Repeat Regions**: Struggles with repetitive sequences leading to misassemblies.
- **Memory Constraints**: Large datasets may exceed memory limits; consider splitting data.
- **Error Rate**: High error rates in input reads affect assembly quality.
- **k-mer Selection**: Incorrect k-mer size impacts assembly completeness and accuracy.

## Examples

### Display help
**Args:** `SSAKE -h`
**Explanation:** Shows available options and usage information.

### Basic de novo assembly
**Args:** `SSAKE -f reads.fastq -o output_contigs.fasta`
**Explanation:** Perform de novo assembly on short reads.

### With specific k-mer size
**Args:** `SSAKE -f reads.fastq -o output.fasta -k 25`
**Explanation:** Assemble with specified k-mer size (default: 20).

### With quality filtering
**Args:** `SSAKE -f reads.fastq -o output.fasta -q 20`
**Explanation:** Filter reads by minimum quality score.

### Paired-end assembly
**Args:** `SSAKE -f reads.fastq -p paired_reads.fastq -o output.fasta`
**Explanation:** Assemble paired-end reads.

### With error correction
**Args:** `SSAKE -f reads.fastq -o output.fasta -c`
**Explanation:** Enable error correction during assembly.

### Minimum overlap specification
**Args:** `SSAKE -f reads.fastq -o output.fasta -m 15`
**Explanation:** Set minimum overlap between reads (default: 10).
