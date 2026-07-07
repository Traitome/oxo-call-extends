---
name: falcon2
category: utility
description: "FALCON2 genomic compression tool"
tags: [falcon2, utility, compression, genomic-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cobilab/FALCON2"
---

## Concepts

- **Tool Overview**: FALCON2 is a genomic compression tool designed for efficient storage and retrieval of sequencing data.
- **Core Function**: Compresses genomic sequences and variant data for reduced storage requirements while maintaining fast access.
- **Input/Output**: Input: Genomic data (FASTA, VCF, BAM). Output: Compressed files, decompressed data.
- **Algorithm**: Uses specialized compression algorithms optimized for genomic data patterns.
- **Key Features**: High compression ratio, fast decompression, support for multiple formats, parallel processing, random access.
- **Installation**: `conda install -c bioconda falcon2`

## Pitfalls

- **Compression Ratio**: Results may vary depending on data type.
- **Memory Usage**: Large datasets may require significant memory.
- **Format Compatibility**: Requires specific input formats.
- **Version Compatibility**: Options may vary between versions.
- **Decompression Time**: Decompression may require time for large files.

## Examples

### Basic compression
**Args:** `falcon2 compress -i genome.fasta -o genome.falcon`
**Explanation:** Compresses genomic sequence file.

### Decompression
**Args:** `falcon2 decompress -i genome.falcon -o genome.fasta`
**Explanation:** Decompresses FALCON2 compressed file.

### VCF compression
**Args:** `falcon2 compress -i variants.vcf -o variants.falcon`
**Explanation:** Compresses VCF variant file.

### Parallel processing
**Args:** `falcon2 compress -i genome.fasta -o genome.falcon -t 8`
**Explanation:** Uses 8 threads for parallel compression.

### Batch processing
**Args:** `falcon2 compress -i files/ -o compressed/ --batch`
**Explanation:** Compresses multiple files in batch mode.