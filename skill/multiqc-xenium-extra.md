---
name: multiqc-xenium-extra
category: expression
description: MultiQC plugin for extended Xenium spatial transcriptomics analysis and quality metrics.
tags: [multiqc-xenium-extra, multiqc, xenium, spatial-transcriptomics, qc, 10x-genomics]
author: oxo-call-community
source_url: "https://docs.seqera.io/multiqc/modules/xenium/"
---

## Concepts

- **Tool Overview**: multiqc-xenium-extra v1.0.2 is a MultiQC plugin that extends Xenium spatial transcriptomics analysis with additional QC metrics and visualizations beyond the core MultiQC xenium module.
- **Core Function**: Provides advanced quality metrics including transcript quality distributions by gene category, cell and nucleus area distributions, field-of-view quality plots, segmentation method breakdowns, and transcripts per gene distributions.
- **Input Format**: Reads Xenium experiment files (experiment.xenium JSON manifest), metrics_summary.csv, and parquet/h5 transcript data files. Requires Xenium v3.x output format.
- **Output**: Adds dedicated sections to the MultiQC HTML report with interactive plots for spatial QC metrics, cell segmentation quality, and transcript distribution analysis.
- **Installation**: Install via pip (`pip install multiqc multiqc-xenium-extra`). The plugin automatically adjusts log filesize limits to handle large parquet and h5 files.
- **Compatibility**: Tested with Xenium v3.x outputs. Older Xenium versions (v1.x, v2.x) are not supported and may cause MultiQC to crash.

## Pitfalls

- **Xenium Version Mismatch**: The module only supports Xenium v3.x output. Processing older version outputs may result in parsing errors or incomplete metrics. Always use current Xenium analysis software.
- **Large Parquet Files**: Xenium experiments generate large parquet transcript files. Ensure sufficient disk space and be aware that initial parsing may take considerable time.
- **Missing experiment.xenium**: The JSON manifest file is required for complete sample metadata. Without it, some visualizations may lack proper sample names or experimental details.
- ** Segmentation Method Changes**: Different Xenium kits use different segmentation approaches (nucleus vs. cell boundary). Metrics interpretation varies accordingly—don't compare segmentation metrics across different kit types.
- **Memory Usage**: Large Xenium experiments with many cells and high transcript counts require substantial RAM for MultiQC processing. Process large datasets on machines with adequate memory.
- **Custom Panel Genes**: Custom gene panels affect expected transcript counts and gene diversity metrics. Use appropriate thresholds for custom panels vs. standard commercial panels.

## Examples

### Generate Xenium QC report
**Args:** `multiqc xenium_output/ -o xenium_qc/`
**Explanation:** Runs MultiQC with Xenium extra module on the output directory. Automatically discovers experiment.xenium, metrics_summary.csv, and transcript parquet files.

### Include segmentation metrics
**Args:** `multiqc xenium_output/ --config xenium_config.yaml -o xenium_qc/`
**Explanation:** Uses a custom config file to include cell/nucleus area distributions and segmentation quality metrics in the report. Config file enables specific visualization options.

### Process multiple Xenium runs
**Args:** `multiqc run1_output/ run2_output/ run3_output/ -o combined_xenium_qc/`
**Explanation:** Aggregates QC data from multiple Xenium experiments into a single comparative report. Useful for comparing performance across runs or samples.

### Export data for downstream analysis
**Args:** `multiqc xenium_output/ --export -o xenium_qc/`
**Explanation:** Exports parsed Xenium metrics as JSON in multiqc_data/ directory. Enables custom analysis of cell counts, transcript densities, and segmentation metrics.

### Force re-analysis of large files
**Args:** `multiqc xenium_output/ --dirs --largefastq 1000000 -o xenium_qc/`
**Explanation:** Uses `--largefastq` to explicitly handle the large transcript files from Xenium. Combined with `--dirs` for cleaner directory structure in output.

### Custom plot styling
**Args:** `multiqc xenium_output/ --plot-theme plotly_dark -o xenium_qc/`
**Explanation:** Applies a dark theme to all Xenium visualizations using Plotly's theme system. Useful for presentations and dark-mode environments.
