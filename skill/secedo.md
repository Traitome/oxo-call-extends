---
name: secedo
category: single-cell
description: secedo - SNV-based clustering for single-cell sequencing data
tags: ["secedo", "single-cell", "SNV-clustering", "variant-analysis"]
author: oxo-call-community
source_url: "https://github.com/ratschlab/secedo"
---

## Concepts

- **Tool Overview**: secedo (v1.0.7) performs SNV-based clustering for single-cell sequencing data.
- **Core Function**: Clusters single cells based on single nucleotide variants.
- **Algorithm**: Uses SNV patterns to identify cell populations and subclones.
- **Input/Output**: Accepts VCF files and produces cluster assignments.
- **Single-Cell Focus**: Specifically designed for single-cell sequencing data.
- **Applications**: Cancer genomics, clonal evolution, and cell population analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on variant calling quality.
- **False Positives**: May incorrectly cluster cells.
- **Sample Size**: Requires sufficient number of cells for meaningful clustering.

## Examples

### Basic clustering
**Args:** `secedo cluster -i variants.vcf -o clusters.txt`
**Explanation:** `-i` input VCF; `-o` output cluster assignments.

### With quality filtering
**Args:** `secedo cluster -i variants.vcf -q 30 -o clusters.txt`
**Explanation:** `-q 30` filters variants by quality score.

### Verbose logging
**Args:** `secedo cluster -i variants.vcf -v -o clusters.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `secedo cluster -i variants.vcf -t 8 -o clusters.txt`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Generate visualization
**Args:** `secedo plot -i clusters.txt -o umap.png`
**Explanation:** Generates visualization of clusters.

### Help command
**Args:** `secedo --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `secedo --version`
**Explanation:** Shows current version.