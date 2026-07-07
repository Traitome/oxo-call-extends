---
name: coverageanomalyscanner
category: qc
description: Find local anomalies in read coverage and predict putative SV events
tags: [coverageanomalyscanner, coverage-analysis, structural-variation, sv-detection, quality-control]
author: oxo-call-community
source_url: "https://github.com/rki-mf1/CoverageAnomalyScanner"
---

## Concepts

- **Tool Overview**: CoverageAnomalyScanner is a tool for detecting local anomalies in read coverage and predicting putative structural variation (SV) events from sequencing data.
- **Core Function**: Identifies coverage anomalies that may indicate deletions, duplications, or other structural variations.
- **Algorithm**: Analyzes read depth across the genome and detects regions with significant coverage deviations from expected levels.
- **Input**: Aligned reads (BAM), reference genome (FASTA), optional target regions (BED).
- **Output**: Coverage anomaly reports, predicted SV events, coverage statistics.
- **Application**: Quality control, structural variation detection, coverage analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda coverageanomalyscanner`

## Pitfalls

- **Coverage Variation**: Normal biological variation may be mistaken for anomalies.
- **Mapping Artifacts**: Mappability issues can create false positives.
- **Threshold Sensitivity**: Requires careful threshold setting for anomaly detection.
- **GC Bias**: GC content affects coverage and may cause false signals.
- **Complex Regions**: Repeat regions and segmental duplications are challenging.

## Examples

### Scan for coverage anomalies
**Args:** `coverageanomalyscanner -i aligned.bam -r reference.fasta -o anomalies.txt`
**Explanation:** Detects coverage anomalies and predicts SV events.

### With target regions
**Args:** `coverageanomalyscanner -i aligned.bam -r reference.fasta -t targets.bed -o anomalies.txt`
**Explanation:** Limits analysis to specified target regions.

### Custom threshold
**Args:** `coverageanomalyscanner -i aligned.bam -r reference.fasta -s 3.0 -o anomalies.txt`
**Explanation:** Sets significance threshold to 3.0 standard deviations.

### Generate visualization
**Args:** `coverageanomalyscanner -i aligned.bam -r reference.fasta --plot -o coverage_plot.png`
**Explanation:** Generates visualization of coverage anomalies.

### Display help
**Args:** `coverageanomalyscanner --help`
**Explanation:** Shows all available options and usage information.