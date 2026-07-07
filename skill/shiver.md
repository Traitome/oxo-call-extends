---
name: shiver
category: utility
description: shiver - HIV sequence reconstruction
tags: ["shiver", "utility", "HIV", "sequence-reconstruction"]
author: oxo-call-community
source_url: "https://github.com/ChrisHIV/shiver"
---

## Concepts

- **Tool Overview**: shiver (v1.7.3) reconstructs HIV sequences from sequencing data.
- **Core Function**: Assembles HIV genomes from NGS reads.
- **Algorithm**: Uses reference-guided assembly for HIV sequences.
- **Input/Output**: Accepts FASTQ reads and produces consensus sequences.
- **HIV Analysis**: Focuses on HIV genome reconstruction.
- **Applications**: HIV research, virology, and clinical sequencing.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Reconstruct HIV sequence
**Args:** `shiver -i reads.fastq -r reference.fasta -o consensus.fasta`
**Explanation:** `-i` input reads; `-r` reference; `-o` output consensus.

### Paired-end
**Args:** `shiver -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o consensus.fasta`
**Explanation:** `-1/-2` paired-end reads.

### Verbose logging
**Args:** `shiver -v -i reads.fastq -r reference.fasta -o consensus.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shiver --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shiver --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shiver -t 8 -i reads.fastq -r reference.fasta -o consensus.fasta`
**Explanation:** `-t 8` uses 8 threads.

### With quality filter
**Args:** `shiver -i reads.fastq -r reference.fasta -q 20 -o consensus.fasta`
**Explanation:** `-q 20` minimum quality threshold.