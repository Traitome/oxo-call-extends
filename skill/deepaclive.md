---
name: deepaclive
category: qc
description: DeePaC-Live - real-time detection of novel pathogens from NGS reads during sequencing runs.
tags: [deepaclive, qc, pathogen-detection, real-time, deep-learning]
author: oxo-call-community
source_url: "https://gitlab.com/dacs-hpi/deepac-live"
---

## Concepts

- **Tool Overview**: deepaclive (v0.3.2+) is a deep learning-based tool for real-time detection of novel pathogens from NGS reads during sequencing runs. It enables rapid identification of potential pathogens without waiting for complete sequencing.
- **Core Function**: Detects novel pathogens in real-time by analyzing sequencing reads as they are generated, providing early warning for infectious disease surveillance.
- **Input/Output**: Input: Raw NGS reads (FASTQ), optionally reference database. Output: Real-time pathogen detection alerts, classification probabilities, summary reports.
- **Algorithm**: Uses convolutional neural networks (CNNs) optimized for real-time processing, with streaming analysis capabilities for low-latency detection.
- **Key Features**: Real-time analysis, low latency, novel pathogen detection, supports multiple sequencing platforms, continuous monitoring.
- **Installation**: `conda install -c bioconda deepaclive`

## Pitfalls

- **Real-time Constraints**: Requires sufficient computational resources for real-time processing.
- **Detection Sensitivity**: May miss low-abundance pathogens.
- **False Positives**: May produce false positive detections requiring validation.
- **Reference Database**: Detection accuracy depends on database completeness.
- **Read Quality**: Poor quality reads affect detection accuracy.

## Examples

### Start real-time monitoring
**Args:** `deepaclive -i /sequencing/reads/ -o alerts.txt`
**Explanation:** Monitor sequencing reads in real-time for pathogen detection.

### With custom database
**Args:** `deepaclive -i /sequencing/reads/ -d custom_db.fasta -o alerts.txt`
**Explanation:** Use custom reference database for pathogen detection.

### Set detection threshold
**Args:** `deepaclive -i /sequencing/reads/ -t 0.95 -o alerts.txt`
**Explanation:** Set 95% confidence threshold for pathogen detection.