---
name: fstic
category: qc
description: High-performance Rust tool for computing multiple genetic distance metrics (FST, GST, Jost's D, etc.) from VCFs or allele-frequency tables, with parallel processing and advanced filtering.
tags: [fstic, population genetics, FST, genetic distance]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/fstic"
---

## Concepts
- **Genetic Distance Metrics**: Computes FST, GST, Jost's D and other metrics.
- **VCF Input**: Accepts VCF files as input.
- **Parallel Processing**: Uses multi-threading for performance.
- **Advanced Filtering**: Supports various filtering options.
- **Allele Frequency**: Works with allele frequency tables.

## Pitfalls
- **VCF Quality**: Requires high-quality VCF files.
- **Memory Usage**: Large VCF files require significant memory.
- **Filtering Complexity**: Many filtering options require careful configuration.
- **Output Interpretation**: Requires understanding of population genetics.
- **Reference Genome**: Needs appropriate reference genome.

## Examples
### Compute FST from VCF
**Args:** `fstic fst -i genotypes.vcf -o fst.txt`
**Explanation:** Computes FST from genotype data.

### With population groups
**Args:** `fstic fst -i genotypes.vcf -p populations.txt -o fst.txt`
**Explanation:** Computes FST between specified populations.

### Multiple metrics
**Args:** `fstic all -i genotypes.vcf -o metrics.txt`
**Explanation:** Computes all available genetic distance metrics.

### Filter by MAF
**Args:** `fstic fst -i genotypes.vcf -m 0.05 -o fst.txt`
**Explanation:** Filters variants with MAF >= 0.05.

### Parallel processing
**Args:** `fstic fst -i genotypes.vcf -t 8 -o fst.txt`
**Explanation:** Uses 8 threads for faster computation.