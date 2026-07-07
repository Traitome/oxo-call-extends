---
name: squeegee
category: metagenomics
description: Squeegee - De novo computational contamination detection for metagenomic samples
tags: [squeegee, metagenomics, contamination-detection, quality-control, metagenomics]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/squeegee"
---

## Concepts

- **Tool Overview**: squeegee (v0.2.0) - A contamination detection tool
- **Core Function**: Performs de novo computational contamination detection for metagenomic samples
- **Input/Output**: Accepts metagenomic samples; outputs contamination reports
- **Algorithm**: De novo contamination detection algorithms
- **Installation**: `conda install -c bioconda squeegee`
- **Key Features**: Contamination detection, metagenomics, de novo analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted metagenomic samples
- **Sample Quality**: Sample quality affects detection accuracy
- **Contamination Types**: Different contamination types require different approaches
- **Memory Usage**: Large samples require significant memory
- **Output Format**: Output format depends on configuration
- **Detection Accuracy**: Accuracy depends on sample quality and parameters

## Examples

### Display help
**Args:** `squeegee --help`
**Explanation:** Shows available options and usage information.

### Basic contamination detection
**Args:** `squeegee -i metagenome.fastq -o contamination_report.txt`
**Explanation:** Detect contamination in metagenomic samples.

### With reference database
**Args:** `squeegee -i metagenome.fastq -d reference_db/ -o contamination_report.txt`
**Explanation:** Use reference database for detection.

### With sensitivity
**Args:** `squeegee -i metagenome.fastq -o contamination_report.txt --sensitivity high`
**Explanation:** Set detection sensitivity.

### Multiple samples
**Args:** `squeegee -i sample1.fastq sample2.fastq -o contamination_report.txt`
**Explanation:** Detect contamination in multiple samples.

### Output detailed results
**Args:** `squeegee -i metagenome.fastq -o contamination_report.txt --detailed`
**Explanation:** Output detailed contamination information.

### Output statistics
**Args:** `squeegee -i metagenome.fastq -o contamination_report.txt --stats`
**Explanation:** Output detection statistics.

### Generate report
**Args:** `squeegee -i metagenome.fastq -o contamination_report.txt --report`
**Explanation:** Generate contamination detection report.

### With threads
**Args:** `squeegee -i metagenome.fastq -o contamination_report.txt -p 8`
**Explanation:** Use multiple threads for detection.