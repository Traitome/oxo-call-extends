---
name: selscan
category: population-genomics
description: selscan - EHH-based scans for positive selection in genomes
tags: ["selscan", "population-genomics", "selection-scan", "EHH"]
author: oxo-call-community
source_url: "https://github.com/szpiech/selscan"
---

## Concepts

- **Tool Overview**: selscan (v1.2.0a) calculates EHH-based scans for positive selection in genomes.
- **Core Function**: Detects signatures of positive selection using Extended Haplotype Homozygosity.
- **Algorithm**: Implements EHH, iHS, XP-EHH, and nSL statistics.
- **Input/Output**: Accepts VCF/BED files and produces selection statistics.
- **Selection Detection**: Focuses on identifying regions under positive selection.
- **Applications**: Population genetics, evolutionary biology, and GWAS.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Format**: Requires correct VCF/BED format.
- **Population Structure**: Results may be affected by population structure.
- **False Positives**: May produce false positive signals.

## Examples

### Run iHS
**Args:** `selscan --ihs --vcf input.vcf --map map.txt --out results`
**Explanation:** Calculates iHS statistics.

### Run XP-EHH
**Args:** `selscan --xpehh --vcf input.vcf --vcf-ref ref.vcf --map map.txt --out results`
**Explanation:** Calculates XP-EHH statistics between populations.

### Run nSL
**Args:** `selscan --nsl --vcf input.vcf --map map.txt --out results`
**Explanation:** Calculates nSL statistics.

### Threads
**Args:** `selscan --ihs --vcf input.vcf --threads 8 --out results`
**Explanation:** `-threads 8` uses 8 threads.

### Verbose logging
**Args:** `selscan --ihs --vcf input.vcf --verbose --out results`
**Explanation:** Enables verbose output for debugging.

### Help command
**Args:** `selscan --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `selscan --version`
**Explanation:** Shows current version.