---
name: mgatk
category: variant-calling
description: Mitochondrial genome analysis toolkit.
tags: [mgatk, variant-calling, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/caleblareau/mgatk"
---

## Concepts

- **Tool Overview**: mgatk v0.7.0 is a toolkit for analyzing mitochondrial genome data from single-cell sequencing.
- **Core Function**: Processes and analyzes mitochondrial genome sequences.
- **Mitochondrial Focus**: Specialized for mitochondrial DNA analysis.
- **Variant Calling**: Calls variants in mitochondrial genomes.
- **Input/Output**: Accepts sequencing reads; outputs mitochondrial variants and statistics.
- **Single-cell Support**: Optimized for single-cell sequencing data.

## Pitfalls

- **Mitochondrial Specific**: Designed specifically for mitochondrial analysis.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis quality depends on input data quality.
- **Reference Genome**: Requires mitochondrial reference genome.

## Examples

### Process mitochondrial reads
**Args:** `mgatk process -i reads.fastq -o mt_results.txt`
**Explanation:** Processes mitochondrial sequencing reads.

### Call mitochondrial variants
**Args:** `mgatk call -i reads.fastq -o variants.vcf`
**Explanation:** Calls variants in mitochondrial genome.

### With reference genome
**Args:** `mgatk process -i reads.fastq -r mt_reference.fasta -o results.txt`
**Explanation:** Uses mitochondrial reference genome.

### Quality control
**Args:** `mgatk qc -i reads.fastq -o qc_report.txt`
**Explanation:** Performs quality control on mitochondrial data.

### Batch processing
**Args:** `mgatk batch -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.