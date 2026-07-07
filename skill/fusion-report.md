---
name: fusion-report
category: hpc
description: Tool for parsing outputs from fusion detection tools. Part of the nf-core/rnafusion pipeline.
tags: [fusion-report, gene fusion, RNA-seq, nf-core]
author: oxo-call-community
source_url: "https://github.com/Clinical-Genomics/fusion-report"
---

## Concepts
- **Fusion Output Parsing**: Parses outputs from multiple fusion detection tools.
- **Integration**: Integrates results from different fusion callers.
- **nf-core Pipeline**: Part of nf-core/rnafusion analysis pipeline.
- **Report Generation**: Generates comprehensive fusion reports.
- **Annotation**: Annotates fusion events with functional information.

## Pitfalls
- **Tool Compatibility**: Works with specific fusion detection tools.
- **Input Format**: Requires specific output formats from fusion tools.
- **Dependency**: Requires multiple fusion detection tools installed.
- **Report Interpretation**: Results require careful interpretation.
- **Complex Setup**: May require complex configuration.

## Examples
### Generate fusion report
**Args:** `fusion-report -i fusion_calls/ -o report.html`
**Explanation:** Generates HTML report from fusion detection outputs.

### Parse multiple tools
**Args:** `fusion-report -i star-fusion.txt arriba.txt -o report.html`
**Explanation:** Parses outputs from multiple fusion callers.

### Add clinical annotations
**Args:** `fusion-report -i fusions.txt --clinical -o report.html`
**Explanation:** Adds clinical annotations to fusion report.

### Batch processing
**Args:** `fusion-report --batch samples.txt -o reports/`
**Explanation:** Processes multiple samples in batch.

### Summary statistics
**Args:** `fusion-report -i fusions.txt --stats -o stats.txt`
**Explanation:** Generates summary statistics of fusion calls.