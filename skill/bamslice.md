---
name: bamslice
category: alignment
description: bamslice - Extract byte ranges from BAM files and convert to interleaved FASTQ format
tags: [bamslice, alignment, FASTQ, BAM, parallel-processing]
author: oxo-call-community
source_url: "https://docs.rs/bamslice"
---

## Concepts

- **Tool Overview**: bamslice extracts specific byte ranges from BAM files and converts them to interleaved FASTQ format, designed for parallel processing without requiring pre-indexing. Version 0.1.7.
- **Core Function**: Extracts byte ranges from BAM files and converts to interleaved FASTQ for parallel processing.
- **Parallel Processing**: Enables parallel processing across compute nodes without pre-indexing.
- **Byte Range Extraction**: Extracts specific byte ranges from BAM files efficiently.
- **Interleaved FASTQ**: Converts extracted reads to interleaved FASTQ format.
- **Auto-alignment**: Automatically handles alignment information during extraction.
- **Input/Output**: Accepts BAM files, outputs interleaved FASTQ files.
- **Installation**: `conda install -c bioconda bamslice`.

## Pitfalls

- **No Index Required**: Does not require BAM index, but may be slower for random access.
- **Byte Range Specification**: Requires correct byte range specification.
- **Interleaved Format**: Output is interleaved FASTQ, which may require conversion for some tools.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Extract byte range
**Args:** `bamslice -i input.bam -r 0-1000000 -o output.fastq`
**Explanation:** Extracts first 1MB byte range from BAM to interleaved FASTQ.

### Multiple ranges
**Args:** `bamslice -i input.bam -r 0-1000000 1000000-2000000 -o output_%.fastq`
**Explanation:** Extracts multiple byte ranges to separate FASTQ files.

### Output paired-end
**Args:** `bamslice -i input.bam -r 0-1000000 -o output.fastq --paired`
**Explanation:** Extracts paired-end reads in interleaved format.

### Verbose mode
**Args:** `bamslice -i input.bam -r 0-1000000 -o output.fastq -v`
**Explanation:** Shows detailed extraction progress.

### Compressed output
**Args:** `bamslice -i input.bam -r 0-1000000 -o output.fastq.gz --gzip`
**Explanation:** Outputs compressed gzipped FASTQ.

### Auto-detect ranges
**Args:** `bamslice -i input.bam --auto-split 4 -o output_%.fastq`
**Explanation:** Automatically splits BAM into 4 equal parts.

### Display help
**Args:** `bamslice --help`
**Explanation:** Shows all available command-line options and usage information.