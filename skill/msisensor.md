---
name: msisensor
category: variant-calling
description: Detect replication slippage variants at microsatellite regions, somatic or germline.
tags: [msisensor, variant-calling, oncology]
author: oxo-call-community
source_url: "https://github.com/ding-lab/msisensor"
---

## Concepts

- **Tool Overview**: MSIsensor v0.5 detects microsatellite instability markers.
- **Core Function**: Identifies replication slippage variants at microsatellites.
- **Somatic/Germline**: Differentiates between somatic and germline variants.
- **Paired Analysis**: Requires tumor-normal sample pairs.
- **Cancer Research**: Specialized for cancer genomics studies.
- **Input/Output**: Accepts BAM files; outputs MSI status and scores.

## Pitfalls

- **Paired Samples**: Requires both tumor and normal samples.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for detection.
- **Data Quality**: Results depend on sequencing quality.
- **Reference Quality**: Depends on reference genome quality.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Detect MSI from paired samples
**Args:** `msisensor msi -d reference.fa -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Detects MSI from tumor-normal pairs.

### Scan for repeat regions
**Args:** `msisensor scan -d reference.fa -o repeats.txt`
**Explanation:** Identifies microsatellite repeat regions.

### System evaluation
**Args:** `msisensor system -d reference.fa -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Evaluates microsatellite sites.

### With filtering
**Args:** `msisensor msi -d reference.fa -t tumor.bam -n normal.bam -f -o results.txt`
**Explanation:** Applies site filtering.

### Batch processing
**Args:** `msisensor msi -d reference.fa -i bam/ -o results/`
**Explanation:** Processes multiple sample pairs.