---
name: koverage
category: qc
description: Read-coverage statistics pipeline for multiple samples
tags: [koverage, qc, read-coverage, coverage-analysis, multi-sample]
author: oxo-call-community
source_url: "https://github.com/beardymcjohnface/Koverage"
---

## Concepts

- **Coverage Statistics**: Calculates read coverage statistics
- **Multi-sample Analysis**: Analyzes coverage across multiple samples
- **Depth Analysis**: Provides detailed depth of coverage metrics
- **Breadth Analysis**: Calculates breadth of coverage thresholds
- **Batch Processing**: Handles multiple samples efficiently
- **Quality Control**: Identifies coverage-related QC issues

## Pitfalls

- **Mapping Quality**: Low mapping quality affects coverage accuracy
- **Duplicate Reads**: Unremoved duplicates inflate coverage estimates
- **Reference Bias**: Mapping bias affects coverage uniformity
- **Target Definition**: Clear target regions needed for analysis
- **Normalization**: Proper normalization required for comparison
- **Low Complexity**: Low complexity regions give unreliable coverage

## Examples

### Calculate coverage statistics
**Args:** `koverage -i sample.bam -r reference.fasta -o stats.txt`
**Explanation:** Calculates coverage statistics for sample.

### Multi-sample analysis
**Args:** `koverage -i samples.txt -r reference.fasta -o results/`
**Explanation:** Analyzes coverage across multiple samples.

### Specify target regions
**Args:** `koverage -i sample.bam -b targets.bed -o coverage.tsv`
**Explanation:** Calculates coverage for target regions only.

### Depth threshold
**Args:** `koverage -i sample.bam --min-depth 10 -o results.txt`
**Explanation:** Reports coverage with minimum depth threshold.

### Generate report
**Args:** `koverage -i samples.txt -o report/ --report`
**Explanation:** Generates comprehensive coverage report.

### Compare samples
**Args:** `koverage compare -i sample1.bam -i sample2.bam -o comparison.txt`
**Explanation:** Compares coverage between two samples.