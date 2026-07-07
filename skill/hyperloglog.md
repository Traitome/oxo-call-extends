---
name: hyperloglog
category: utility
description: HyperLogLog cardinality counter for efficient unique element counting
tags: [hyperloglog, cardinality, statistics]
author: oxo-call-community
source_url: "https://github.com/svpcom/hyperloglog"
---

## Concepts

- **Tool Overview**: HyperLogLog is a probabilistic algorithm for estimating the cardinality (number of unique elements) of large datasets with minimal memory usage.
- **Cardinality Estimation**: Uses a probabilistic sketching algorithm to estimate unique count without storing all elements.
- **Memory Efficiency**: Can estimate cardinality of billions of elements using only kilobytes of memory.
- **Relative Error**: Provides configurable accuracy with typical error rates around 1-2%.
- **Leading Zero Principle**: Based on counting leading zeros in hash values to estimate cardinality.
- **Installation**: `conda install -c bioconda hyperloglog`

## Pitfalls

- **Approximate Results**: HyperLogLog provides estimates, not exact counts.
- **Hash Quality**: Accuracy depends on the quality of the hash function used.
- **Memory vs Accuracy**: Higher accuracy requires more memory for registers.
- **Merge Operation**: Merging sketches may introduce additional error.
- **Small Cardinalities**: Less accurate for very small datasets.
- **Implementation Differences**: Different implementations may produce slightly different results.

## Examples

### Estimate cardinality from file
**Args:** `hyperloglog --input data.txt --output estimate.txt`
**Explanation:** Estimates the number of unique elements in data.txt.

### Custom precision
**Args:** `hyperloglog --input reads.fastq --precision 14 --output result.txt`
**Explanation:** Uses 14-bit precision (16384 registers) for higher accuracy.

### Stream from stdin
**Args:** `cat large_file.txt | hyperloglog -`
**Explanation:** Reads input from standard input and prints cardinality estimate.

### Merge multiple sketches
**Args:** `hyperloglog --merge sketch1.hll sketch2.hll --output merged.hll`
**Explanation:** Merges two HyperLogLog sketches into one.

### Export to JSON
**Args:** `hyperloglog --input data.csv --json --output result.json`
**Explanation:** Outputs the cardinality estimate in JSON format.