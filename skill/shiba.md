---
name: shiba
category: expression
description: shiba - Differential RNA splicing identification
tags: ["shiba", "expression", "RNA-seq", "splicing"]
author: oxo-call-community
source_url: "https://sika-zheng-lab.github.io/Shiba"
---

## Concepts

- **Tool Overview**: shiba (v0.8.2) identifies differential RNA splicing across platforms.
- **Core Function**: Detects alternative splicing events from RNA-seq data.
- **Algorithm**: Uses statistical methods for splicing analysis.
- **Input/Output**: Accepts BAM files and produces splicing predictions.
- **Alternative Splicing**: Focuses on differential splicing detection.
- **Applications**: RNA-seq analysis, transcriptomics, and splicing studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Run analysis
**Args:** `shiba -i input.bam -g annotation.gtf -o results/`
**Explanation:** `-i` input BAM; `-g` annotation; `-o` output directory.

### With comparison
**Args:** `shiba -i case.bam -c control.bam -g annotation.gtf -o results/`
**Explanation:** `-c` control BAM for differential analysis.

### Verbose logging
**Args:** `shiba -v -i input.bam -g annotation.gtf -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shiba --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shiba --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shiba -t 8 -i input.bam -g annotation.gtf -o results/`
**Explanation:** `-t 8` uses 8 threads.

### Filter by expression
**Args:** `shiba -i input.bam -g annotation.gtf -f 10 -o results/`
**Explanation:** `-f 10` minimum expression filter.