---
name: genrich
category: peak-calling
description: Genrich - Detecting sites of genomic enrichment from sequencing data.
tags: [genrich, peak-calling, chip-seq, genomic-enrichment]
author: oxo-call-community
source_url: "https://github.com/jsh58/Genrich"
---

## Concepts
- **Peak Calling**: Detects enriched genomic regions from sequencing data.
- **ChIP-seq Analysis**: Analyzes ChIP-seq data for transcription factor binding.
- **Enrichment Detection**: Identifies regions with significant signal enrichment.
- **Background Normalization**: Normalizes against input/control samples.
- **Statistical Significance**: Computes statistical significance of peaks.

## Pitfalls
- **Input Quality**: Requires high-quality sequencing data.
- **Control Samples**: Requires appropriate control samples.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **False Positives**: May detect false enrichment peaks.
- **Data Normalization**: Requires proper normalization.

## Examples
### Call peaks from ChIP-seq
**Args:** `genrich -i chip.bam -c input.bam -o peaks.bed`
**Explanation:** Calls peaks from ChIP-seq data using input as control.

### With multiple replicates
**Args:** `genrich -i rep1.bam rep2.bam -c control.bam -o peaks.bed`
**Explanation:** Calls peaks using multiple ChIP replicates.

### Specify genome size
**Args:** `genrich -i chip.bam -c input.bam --gsize hs -o peaks.bed`
**Explanation:** Specifies human genome size for normalization.

### Filter by q-value
**Args:** `genrich -i chip.bam -c input.bam -q 0.01 -o peaks.bed`
**Explanation:** Filters peaks by q-value threshold.

### Generate report
**Args:** `genrich -i chip.bam -c input.bam -r -o report.txt`
**Explanation:** Generates peak calling report.