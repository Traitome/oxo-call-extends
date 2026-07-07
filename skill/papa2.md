---
name: papa2
category: qc
description: PaPa2 is a Python port of DADA2 for amplicon denoising.
tags: [papa2, qc, amplicon, denoising]
author: oxo-call-community
source_url: "https://github.com/rec3141/papa2"
---

## Concepts

- **Tool Overview**: PaPa2 performs amplicon denoising, fully compatible with DADA2.
- **Core Function**: Denoises amplicon sequencing data.
- **Algorithm**: Implements DADA2 algorithms in Python/C++.
- **Input Format**: Accepts FASTQ reads from amplicon sequencing.
- **Output**: Produces denoised sequences and feature tables.
- **Use Case**: Amplicon sequencing analysis, microbiome studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Quality Dependence**: Results depend on input quality.
- **Runtime**: Analysis may take significant time.
- **Parameter Sensitivity**: Results depend on parameters.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `papa2 --help`
**Explanation:** Shows available options and usage instructions.

### Denoise single-end
**Args:** `papa2 denoise -i reads.fastq -o denoised/`
**Explanation:** Denoises single-end reads.

### Denoise paired-end
**Args:** `papa2 denoise -1 reads_1.fastq -2 reads_2.fastq -o denoised/`
**Explanation:** Denoises paired-end reads.

### With trimming
**Args:** `papa2 denoise --trim-left 10 --trunc-len 250 -i reads.fastq -o denoised/`
**Explanation:** Trims reads before denoising.

### Verbose mode
**Args:** `papa2 denoise -v -i reads.fastq -o denoised/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `papa2 denoise -t 8 -i reads.fastq -o denoised/`
**Explanation:** Uses 8 threads for parallel processing.

### Taxonomy assignment
**Args:** `papa2 assign-taxonomy -i sequences.fasta -r reference.fasta -o taxonomy.txt`
**Explanation:** Assigns taxonomy to sequences.