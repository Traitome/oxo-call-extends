---
name: sopa
category: spatial-omics
description: SOPA - Spatial-omics pipeline and analysis
tags: [sopa, spatial-omics, pipeline, analysis, spatial]
author: oxo-call-community
source_url: "https://gustaveroussy.github.io/sopa"
---

## Concepts

- **Tool Overview**: sopa (v2.2.5) - A spatial-omics analysis pipeline
- **Core Function**: Processes and analyzes spatial omics data
- **Input/Output**: Accepts spatial omics data; outputs analysis results
- **Algorithm**: Integrates multiple tools for spatial analysis
- **Installation**: `conda install -c bioconda sopa`
- **Key Features**: Spatial analysis, pipeline integration, visualization

## Pitfalls

- **Input Requirements**: Requires properly formatted spatial omics data
- **Data Format**: Different spatial technologies require different formats
- **Pipeline Steps**: Multiple pipeline steps require proper configuration
- **Memory Usage**: Large spatial datasets require significant memory
- **Visualization**: Requires proper visualization setup
- **Output Format**: Output format depends on analysis type

## Examples

### Display help
**Args:** `sopa --help`
**Explanation:** Shows available options and usage information.

### Basic pipeline run
**Args:** `sopa --input spatial_data/ --output results/`
**Explanation:** Run complete spatial-omics pipeline.

### With configuration
**Args:** `sopa --input spatial_data/ --config config.yaml --output results/`
**Explanation:** Use configuration file for pipeline.

### Spatial clustering
**Args:** `sopa --input spatial_data/ --output results/ --cluster`
**Explanation:** Perform spatial clustering analysis.

### Cell annotation
**Args:** `sopa --input spatial_data/ --output results/ --annotate`
**Explanation:** Annotate cells in spatial data.

### Visualization
**Args:** `sopa --input spatial_data/ --output results/ --visualize`
**Explanation:** Generate spatial visualization.

### Generate report
**Args:** `sopa --input spatial_data/ --output results/ --report`
**Explanation:** Generate analysis report.

### With threads
**Args:** `sopa --input spatial_data/ --output results/ --threads 8`
**Explanation:** Use multiple threads for pipeline.