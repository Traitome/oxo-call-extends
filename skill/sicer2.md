---
name: sicer2
category: epigenomics
description: SICER2 - Improved ChIP-seq broad peak calling tool
tags: ["sicer2", "epigenomics", "chip-seq", "peak-calling"]
author: oxo-call-community
source_url: "https://pypi.org/project/SICER2/"
---

## Concepts

- **Tool Overview**: SICER2 (v2.1.0) is a redesigned ChIP-seq broad peak calling tool.
- **Core Function**: Identifies enriched domains from histone modification ChIP-seq data.
- **Algorithm**: Uses clustering approach for broad peak detection.
- **Input/Output**: Accepts BAM/SAM files and produces peak calls in BED format.
- **Epigenomics Analysis**: Specialized for histone modification analysis.
- **Applications**: ChIP-seq data analysis, epigenomics research, and peak calling.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment of window size and gap parameters.
- **Input Quality**: Results depend on sequencing data quality.
- **Control Sample**: Requires matched control sample for accurate peak calling.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Call peaks
**Args:** `sicer2 -t treatment.bam -c control.bam -o peaks.bed`
**Explanation:** `-t` treatment BAM; `-c` control BAM; `-o` output peaks.

### With window size
**Args:** `sicer2 -t treatment.bam -c control.bam -w 200 -o peaks.bed`
**Explanation:** `-w 200` window size in base pairs.

### With gap size
**Args:** `sicer2 -t treatment.bam -c control.bam -g 600 -o peaks.bed`
**Explanation:** `-g 600` gap size between windows.

### Help command
**Args:** `sicer2 --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sicer2 --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sicer2 -v -t treatment.bam -c control.bam -o peaks.bed`
**Explanation:** `-v` verbose output.

### With FDR threshold
**Args:** `sicer2 -t treatment.bam -c control.bam -f 0.01 -o peaks.bed`
**Explanation:** `-f 0.01` FDR threshold.
