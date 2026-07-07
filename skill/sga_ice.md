---
name: sga_ice
category: assembly
description: sga_ice - Iterative error correction for Illumina reads
tags: ["sga_ice", "assembly", "error-correction", "Illumina"]
author: oxo-call-community
source_url: "https://github.com/hillerlab/IterativeErrorCorrection"
---

## Concepts

- **Tool Overview**: sga_ice (v1.01) performs iterative error correction for Illumina reads.
- **Core Function**: Corrects errors in long Illumina reads (250-300bp).
- **Algorithm**: Uses iterative k-mer based error correction.
- **Input/Output**: Accepts FASTQ files and produces corrected reads.
- **Error Correction**: Focuses on improving read quality for assembly.
- **Applications**: Sequence assembly, read preprocessing, and NGS analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Performance**: May be slow for extremely large files.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Format**: Requires correct FASTQ format.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Correct reads
**Args:** `sga_ice -i reads.fastq -o corrected.fastq`
**Explanation:** `-i` input reads; `-o` output corrected reads.

### Paired-end
**Args:** `sga_ice -1 reads_1.fastq -2 reads_2.fastq -o corrected/`
**Explanation:** `-1/-2` paired-end reads.

### With k-mer size
**Args:** `sga_ice -i reads.fastq -k 31 -o corrected.fastq`
**Explanation:** `-k 31` k-mer size.

### Verbose logging
**Args:** `sga_ice -v -i reads.fastq -o corrected.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sga_ice --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sga_ice --version`
**Explanation:** Shows current version.

### Multiple iterations
**Args:** `sga_ice -i reads.fastq -n 5 -o corrected.fastq`
**Explanation:** `-n 5` number of iterations.