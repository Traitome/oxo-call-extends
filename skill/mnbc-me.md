---
name: mnbc-me
category: utility
description: MNBC-ME is a tool for mobile elements detection
tags: [mnbc-me, utility, mobile-elements]
author: oxo-call-community
source_url: "https://github.com/ComputationalPathogens/MNBC-ME"
---

## Concepts

- **Tool Overview**: MNBC-ME v1.0 identifies mobile element-originated reads.
- **Core Function**: Detects both short and long mobile element reads.
- **Mobile Elements**: Identifies transposons, plasmids, and viral sequences.
- **Read Classification**: Classifies reads by their origin (plasmid, chromosomal, viral).
- **Input/Output**: Accepts sequencing reads; outputs classified reads.
- **Pathogen Analysis**: Supports pathogen and microbial genome analysis.

## Pitfalls

- **Read Type Specific**: Optimized for specific read types.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal detection.
- **Data Quality**: Results depend on sequencing quality.
- **Host Contamination**: Requires careful handling of host reads.
- **Computational Resources**: Analysis may require significant resources.

## Examples

### Detect mobile elements
**Args:** `mnbc-me -i reads.fastq -o results/`
**Explanation:** Detects mobile element reads in sequencing data.

### With reference database
**Args:** `mnbc-me -i reads.fastq -d database.fasta -o results/`
**Explanation:** Uses custom reference database for classification.

### Verbose output
**Args:** `mnbc-me -i reads.fastq -v -o results/`
**Explanation:** Shows detailed classification results.

### Filter by length
**Args:** `mnbc-me -i reads.fastq -m 100 -M 10000 -o results/`
**Explanation:** Filters reads by length range.

### Batch processing
**Args:** `mnbc-me -i fastq/ -o results/`
**Explanation:** Processes multiple read files.