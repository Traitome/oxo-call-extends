---
name: kcftools
category: programming
description: Rapid method to screen for introgression using k-mer counting.
tags: [kcftools, programming, k-mer, introgression, population genetics]
author: oxo-call-community
source_url: "https://github.com/sivasubramanics/kcftools"
---

## Concepts

- **Tool Overview**: kcftools (v0.4.0) - Detects introgression using k-mer based approach.
- **Introgression Detection**: Identifies gene flow between populations.
- **k-mer Analysis**: Uses k-mer counting for efficient detection.
- **Population Genetics**: Designed for population genetic analysis.
- **Rapid Screening**: Fast screening of large datasets.
- **Statistical Methods**: Implements statistical tests for introgression.

## Pitfalls

- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Population Structure**: Requires careful population sampling.
- **Reference Genome**: Needs good reference genome.
- **Memory Usage**: Large datasets require significant memory.
- **False Positives**: Can produce false positive signals.
- **Complex Demography**: Complex demographic histories affect results.

## Examples

### Detect introgression
**Args:** `kcftools detect -p population.txt -o results/`
**Explanation:** Detects introgression signals in populations.

### Set k-mer size
**Args:** `kcftools detect -p population.txt -k 31 -o results/`
**Explanation:** Uses k-mer size of 31 for analysis.

### Generate k-mer spectrum
**Args:** `kcftools spectrum -i reads.fastq -o spectrum.txt`
**Explanation:** Generates k-mer spectrum for population.

### Compare populations
**Args:** `kcftools compare -p1 pop1.txt -p2 pop2.txt -o comparison.txt`
**Explanation:** Compares k-mer profiles between populations.

### Filter by frequency
**Args:** `kcftools filter -i results.txt -f 0.05 -o filtered.txt`
**Explanation:** Filters results by frequency threshold.

### Generate report
**Args:** `kcftools report -i results.txt -o report.html`
**Explanation:** Generates HTML report of findings.