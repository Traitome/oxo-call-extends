---
name: shortcut
category: qc
description: shortcut - Small RNA-seq trimmer and quality control
tags: ["shortcut", "qc", "RNA-seq", "trimming"]
author: oxo-call-community
source_url: "https://github.com/Aez35/ShortCut"
---

## Concepts

- **Tool Overview**: shortcut (v2.0) trims and quality controls small RNA-seq data.
- **Core Function**: Processes small RNA sequencing reads for downstream analysis.
- **Algorithm**: Uses quality-based trimming and adapter removal.
- **Input/Output**: Accepts FASTQ reads and produces cleaned reads.
- **Small RNA Analysis**: Focuses on miRNA and small RNA sequencing data.
- **Applications**: RNA-seq preprocessing, small RNA research, and quality control.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Format**: Requires correct FASTQ format.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Adapter Sequences**: Requires correct adapter sequence specification.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Trim reads
**Args:** `shortcut -i reads.fastq -o trimmed.fastq`
**Explanation:** `-i` input reads; `-o` output trimmed reads.

### With adapter
**Args:** `shortcut -i reads.fastq -a ADAPTER_SEQ -o trimmed.fastq`
**Explanation:** `-a` adapter sequence to remove.

### Verbose logging
**Args:** `shortcut -v -i reads.fastq -o trimmed.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shortcut --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shortcut --version`
**Explanation:** Shows current version.

### Paired-end
**Args:** `shortcut -1 reads_1.fastq -2 reads_2.fastq -o trimmed/`
**Explanation:** `-1/-2` paired-end reads.

### Quality filter
**Args:** `shortcut -i reads.fastq -q 20 -o trimmed.fastq`
**Explanation:** `-q 20` minimum quality threshold.