---
name: scepia
category: epigenomics
description: SCEPIA - Single Cell Epigenome-based Inference of Activity
tags: ["scepia", "epigenomics", "single-cell", "chromatin-activity"]
author: oxo-call-community
source_url: "https://github.com/vanheeringen-lab/scepia"
---

## Concepts

- **Tool Overview**: SCEPIA (v0.5.1) is a tool for Single Cell Epigenome-based Inference of Activity from single-cell ATAC-seq data.
- **Core Function**: Infers regulatory activity from single-cell chromatin accessibility data.
- **Algorithm**: Uses statistical models to predict transcription factor activity.
- **Input/Output**: Accepts scATAC-seq data and produces activity scores.
- **Epigenomic Analysis**: Focuses on chromatin accessibility and regulatory element activity.
- **Applications**: Single-cell epigenomics, transcription factor activity prediction, and regulatory network analysis.

## Pitfalls

- **Data Quality**: Results depend on input data quality.
- **Peak Calling**: Requires proper peak calling beforehand.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Interpretation**: Activity scores require careful biological interpretation.

## Examples

### Basic activity inference
**Args:** `scepia infer -i peaks.bed -c counts.h5ad -o activity.csv`
**Explanation:** `-i` peak regions; `-c` count matrix; `-o` activity scores.

### With motif database
**Args:** `scepia infer -i peaks.bed -c counts.h5ad -m motifs.pwm -o activity.csv`
**Explanation:** `-m` specifies motif database for TF binding prediction.

### Visualize results
**Args:** `scepia plot -i activity.csv -o plot.png`
**Explanation:** Generates visualization of activity scores.

### Multiple datasets
**Args:** `scepia infer -i peaks.bed -c dataset1.h5ad dataset2.h5ad -o comparison.csv`
**Explanation:** Compares activity across multiple datasets.

### Verbose logging
**Args:** `scepia infer -i peaks.bed -c counts.h5ad -v -o activity.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Output JSON
**Args:** `scepia infer -i peaks.bed -c counts.h5ad -f json -o activity.json`
**Explanation:** `-f json` outputs results in JSON format.

### Quality filtering
**Args:** `scepia infer -i peaks.bed -c counts.h5ad -q 0.05 -o activity.csv`
**Explanation:** `-q 0.05` filters by significance threshold.