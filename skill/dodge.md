---
name: dodge
category: metagenomics
description: DODGE - Dynamic Outbreak Detection for Genomic Epidemiology.
tags: [dodge, metagenomics, outbreak-detection, epidemiology, genomic-surveillance]
author: oxo-call-community
source_url: "https://github.com/LanLab/dodge"
---

## Concepts

- **Tool Overview**: DODGE is an automated tool for detecting bacterial outbreaks from genomic surveillance data.
- **Core Function**: Identifies potential point-source outbreaks using cumulative long-term genomic surveillance data.
- **Input/Output**: Input: Genomic surveillance data (SNPs, metadata). Output: Outbreak detection alerts and clusters.
- **Algorithm**: Uses statistical methods to detect unusual clustering patterns in genomic data.
- **Key Features**: Automated outbreak detection, real-time monitoring, cluster identification, visualization support.
- **Installation**: `conda install -c bioconda dodge`

## Pitfalls

- **Input Requirements**: Requires properly formatted surveillance data with metadata.
- **Data Quality**: Poor quality sequencing data affects detection accuracy.
- **Baseline Data**: Requires sufficient baseline data for comparison.
- **False Positives**: May produce false alerts during periods of increased sampling.
- **Computation Time**: Large datasets may require significant processing time.
- **Interpretation**: Detected clusters require epidemiological verification.

## Examples

### Detect outbreaks
**Args:** `dodge --input surveillance.tsv --output outbreak_alerts.tsv`
**Explanation:** Detects potential outbreaks from genomic surveillance data.

### With custom threshold
**Args:** `dodge --input surveillance.tsv --output alerts.tsv --threshold 0.01`
**Explanation:** Sets a custom statistical threshold for outbreak detection.

### Include visualization
**Args:** `dodge --input surveillance.tsv --output alerts.tsv --plot plot.png`
**Explanation:** Generates a visualization of detected clusters.

### Real-time mode
**Args:** `dodge --input surveillance.tsv --output alerts.tsv --realtime`
**Explanation:** Runs in real-time monitoring mode for continuous surveillance.

### Cluster analysis
**Args:** `dodge --input surveillance.tsv --output clusters.tsv --clusters`
**Explanation:** Outputs detailed cluster information for detected outbreaks.

### Batch processing
**Args:** `dodge --input-dir surveillance_data/ --output-dir results/`
**Explanation:** Processes multiple surveillance datasets in batch mode.