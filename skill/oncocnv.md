---
name: oncocnv
category: utility
description: ONCOCNV detects copy number changes in deep sequencing data for cancer genomics.
tags: [oncocnv, utility, copy-number-variation, cancer-genomics]
author: oxo-call-community
source_url: "https://github.com/BoevaLab/ONCOCNV/blob/master/README.md"
---

## Concepts

- **Tool Overview**: ONCOCNV detects copy number variations in cancer sequencing data.
- **Core Function**: Identifies copy number changes from deep sequencing data.
- **Algorithm**: Uses statistical methods for CNV detection.
- **Input Format**: Accepts BAM alignment files and segmentation data.
- **Output**: Produces copy number profiles and segmentations.
- **Use Case**: Cancer genomics, copy number analysis, and tumor profiling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Quality**: Results depend on sequencing depth and quality.
- **Tumor Purity**: Affects CNV detection accuracy.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `oncocnv --help`
**Explanation:** Shows available options and usage instructions.

### Detect CNVs
**Args:** `oncocnv -i tumor.bam -n normal.bam -o cnv_results.txt`
**Explanation:** Detects copy number changes in tumor sample.

### With segmentation
**Args:** `oncocnv -i tumor.bam -s segments.txt -o cnv_results.txt`
**Explanation:** Uses pre-computed segments for analysis.

### Output format
**Args:** `oncocnv -i tumor.bam -n normal.bam -o results.csv --csv`
**Explanation:** Outputs results in CSV format.

### Verbose mode
**Args:** `oncocnv -i tumor.bam -n normal.bam -v -o cnv_results.txt`
**Explanation:** Runs with verbose output.

### Minimum coverage
**Args:** `oncocnv -i tumor.bam -n normal.bam -c 10 -o cnv_results.txt`
**Explanation:** Sets minimum coverage threshold to 10.

### Threads
**Args:** `oncocnv -i tumor.bam -n normal.bam -t 4 -o cnv_results.txt`
**Explanation:** Uses 4 threads for parallel processing.