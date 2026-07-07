---
name: sem
category: epigenomics
description: sem - Nucleosome calling package for nucleosome subtype detection
tags: ["sem", "epigenomics", "nucleosome", "ChIP-seq"]
author: oxo-call-community
source_url: "https://github.com/YenLab/SEM"
---

## Concepts

- **Tool Overview**: sem (v1.2.3) is a nucleosome calling package for nucleosome subtype detection.
- **Core Function**: Identifies and classifies nucleosome subtypes from sequencing data.
- **Algorithm**: Uses hidden Markov models for nucleosome detection.
- **Input/Output**: Accepts ChIP-seq data and produces nucleosome positions.
- **Nucleosome Analysis**: Focuses on nucleosome positioning and subtype classification.
- **Applications**: Epigenomics, chromatin biology, and gene regulation research.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Reference Genome**: Requires proper reference genome setup.
- **Documentation**: Some features have limited documentation.

## Examples

### Call nucleosomes
**Args:** `sem call -i reads.bam -o nucleosomes.bed`
**Explanation:** `-i` input BAM; `-o` output BED with nucleosome positions.

### With reference
**Args:** `sem call -i reads.bam -r reference.fasta -o nucleosomes.bed`
**Explanation:** `-r` reference genome for better accuracy.

### Classify subtypes
**Args:** `sem classify -i nucleosomes.bed -o subtypes.txt`
**Explanation:** Classifies nucleosome subtypes.

### Verbose logging
**Args:** `sem call -i reads.bam -v -o nucleosomes.bed`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `sem call -i reads.bam -t 8 -o nucleosomes.bed`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `sem --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sem --version`
**Explanation:** Shows current version.