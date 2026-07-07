---
name: pybedtools
category: formatting
description: pybedtools wraps BEDTools for use in Python and adds many additional features for genomic interval operations.
tags: [pybedtools, formatting, bedtools, genomic-intervals]
author: oxo-call-community
source_url: "https://daler.github.io/pybedtools"
---

## Concepts

- **Tool Overview**: pybedtools wraps BEDTools.
- **Core Function**: Genomic interval manipulation.
- **Algorithm**: Uses BEDTools operations.
- **Input Format**: Accepts BED/GFF/VCF files.
- **Output**: Produces processed intervals.
- **Use Case**: Genomic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **BEDTools Dependency**: Requires BEDTools installed.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pybedtools --help`
**Explanation:** Shows available options and usage instructions.

### Intersect intervals
**Args:** `pybedtools intersect -a peaks.bed -b genes.bed -o overlap.bed`
**Explanation:** Finds overlapping intervals.

### With parameters
**Args:** `pybedtools intersect -a peaks.bed -b genes.bed -p params.yaml -o overlap.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pybedtools -v intersect -a peaks.bed -b genes.bed -o overlap.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pybedtools -t 4 intersect -a peaks.bed -b genes.bed -o overlap.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Merge intervals
**Args:** `pybedtools merge -i intervals.bed -o merged.bed`
**Explanation:** Merges overlapping intervals.

### Generate report
**Args:** `pybedtools intersect -a peaks.bed -b genes.bed -o overlap.bed --report report.html`
**Explanation:** Generates HTML report.