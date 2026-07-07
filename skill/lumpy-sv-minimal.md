---
name: lumpy-sv-minimal
category: variant-calling
description: A general probabilistic framework for structural variant discovery. Minimal package with only lumpy executable.
tags: [lumpy-sv-minimal, variant-calling, structural-variants]
author: oxo-call-community
source_url: "https://github.com/arq5x/lumpy-sv"
---

## Concepts

- **Tool Overview**: lumpy-sv-minimal v0.3.1 is a minimal package containing only the core lumpy executable for structural variant discovery.
- **Core Function**: Detects structural variants using probabilistic modeling of read pair and split read signals.
- **Minimal Dependencies**: Contains only the essential lumpy executable without additional scripts or utilities.
- **Input/Output**: Input: BAM files with aligned reads; Output: VCF or BEDPE file with SV calls.
- **Installation**: `conda install -c bioconda lumpy-sv-minimal`
- **Key Features**: Lightweight, fast installation, core SV detection functionality.

## Pitfalls

- **Limited Functionality**: Does not include helper scripts or utilities from the full lumpy-sv package.
- **Dependency Management**: Requires manual installation of dependencies like samtools.
- **Complex Usage**: May require additional processing steps not included in the minimal package.
- **Documentation**: Limited documentation compared to full package.
- **Updates**: May not include latest features from full lumpy-sv package.
- **Support**: Limited community support compared to full package.

## Examples

### Basic SV detection
**Args:** `lumpy -b sample.bam -o sv_calls.vcf`
**Explanation:** Detects structural variants from aligned reads.

### BEDPE output
**Args:** `lumpy -b sample.bam -o sv_calls.bedpe --bedpe`
**Explanation:** Outputs results in BEDPE format.

### Threads
**Args:** `lumpy -b sample.bam -t 4 -o sv_calls.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Minimum SV size
**Args:** `lumpy -b sample.bam -m 100 -o sv_calls.vcf`
**Explanation:** Sets minimum SV size to 100bp.

### Verbose output
**Args:** `lumpy -b sample.bam -v -o sv_calls.vcf`
**Explanation:** Outputs detailed progress information.

### Help documentation
**Args:** `lumpy --help`
**Explanation:** Displays all available options and parameters.