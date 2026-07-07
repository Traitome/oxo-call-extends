---
name: isopedia
category: expression
description: Simultaneous exploration of thousands of long-read transcriptomes by read-level indexing.
tags: [isopedia, expression, long reads, transcriptomics, indexing]
author: oxo-call-community
source_url: "https://github.com/zhengxinchang/isopedia"
---

## Concepts

- **Read-Level Indexing**: Creates an index of individual reads across multiple transcriptomes.
- **Cross-Sample Comparison**: Enables comparison of transcriptomic profiles across thousands of samples.
- **Rapid Query**: Provides fast retrieval of specific transcript sequences across datasets.
- **Scalable Architecture**: Designed to handle thousands of transcriptomes efficiently.
- **Isoform Discovery**: Identifies novel isoforms present across multiple samples.
- **Expression Quantification**: Provides isoform-level expression estimates across samples.

## Pitfalls

- **Memory Requirements**: Indexing thousands of transcriptomes requires significant memory.
- **Storage Requirements**: Index files can be large for extensive datasets.
- **Computational Time**: Building the index is computationally intensive.
- **Data Quality**: Poor quality data affects index accuracy and query results.
- **Index Maintenance**: Index must be rebuilt when new samples are added.
- **Query Complexity**: Complex queries may require significant computation time.

## Examples

### Build index
**Args:** `isopedia build --input samples/ --output index/`
**Explanation:** Builds an index from multiple transcriptome samples.

### Query specific transcript
**Args:** `isopedia query --index index/ --transcript transcript_id --output results.txt`
**Explanation:** Retrieves information about a specific transcript across all samples.

### Compare samples
**Args:** `isopedia compare --index index/ --samples sample1 sample2 --output comparison.txt`
**Explanation:** Compares transcriptomic profiles between two samples.

### Expression quantification
**Args:** `isopedia quantify --index index/ --output expression_matrix.csv`
**Explanation:** Generates expression matrix across all indexed samples.

### Find novel isoforms
**Args:** `isopedia discover --index index/ --output novel_isoforms.fasta`
**Explanation:** Identifies novel isoforms present in the dataset.

### Batch query
**Args:** `isopedia batch --index index/ --queries queries.txt --output results/`
**Explanation:** Processes multiple queries listed in a batch file.