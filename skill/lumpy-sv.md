---
name: lumpy-sv
category: variant-calling
description: A general probabilistic framework for structural variant discovery
tags: [lumpy-sv, variant-calling, structural-variants]
author: oxo-call-community
source_url: "https://github.com/arq5x/lumpy-sv"
---

## Concepts

- **Tool Overview**: lumpy-sv v0.3.1 is a probabilistic framework for discovering structural variants (SVs) from next-generation sequencing data.
- **Core Function**: Detects various types of structural variants including deletions, duplications, inversions, and translocations.
- **Probabilistic Model**: Uses a Bayesian approach to integrate multiple signals (split reads, read pairs, depth).
- **Input/Output**: Input: BAM files with aligned reads; Output: VCF file with structural variant calls.
- **Installation**: `conda install -c bioconda lumpy-sv`
- **Key Features**: High sensitivity, supports multiple sequencing platforms, integrates multiple evidence types.

## Pitfalls

- **Complexity**: High false positive rate requires careful filtering and validation.
- **Memory Usage**: Processing large BAM files may require significant memory.
- **Computation Time**: SV detection can be computationally intensive.
- **Read Length**: Performance varies with read length; longer reads improve detection.
- **Parameter Tuning**: Requires careful parameter adjustment for different datasets.
- **Variant Size**: May miss very small or very large structural variants.

## Examples

### Detect SVs from BAM
**Args:** `lumpy -b sample.bam -o sv_calls.vcf`
**Explanation:** Detects structural variants from aligned reads.

### With multiple BAMs
**Args:** `lumpy -b sample1.bam,sample2.bam -o sv_calls.vcf`
**Explanation:** Analyzes multiple samples simultaneously.

### Bedpe output
**Args:** `lumpy -b sample.bam -o sv_calls.bedpe --bedpe`
**Explanation:** Outputs results in BEDPE format.

### Threads
**Args:** `lumpy -b sample.bam -t 8 -o sv_calls.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum size
**Args:** `lumpy -b sample.bam -m 50 -o sv_calls.vcf`
**Explanation:** Sets minimum SV size to 50bp.

### Help documentation
**Args:** `lumpy --help`
**Explanation:** Displays all available options and parameters.