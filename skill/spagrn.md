---
name: spagrn
category: spatial-omics
description: SpaGRN - TF-centered spatial gene regulatory network inference
tags: [spagrn, spatial-omics, gene-regulatory-networks, spatial-transcriptomics, tf]
author: oxo-call-community
source_url: "https://github.com/BGI-Qingdao/SpaGRN"
---

## Concepts

- **Tool Overview**: spagrn (v1.1.0) - A spatial gene regulatory network tool
- **Core Function**: Infers TF-centered spatial gene regulatory networks
- **Input/Output**: Accepts spatial transcriptomics data; outputs GRNs
- **Algorithm**: Spatial analysis for regulatory network inference
- **Installation**: `conda install -c bioconda spagrn`
- **Key Features**: Spatial GRNs, TF analysis, spatial transcriptomics

## Pitfalls

- **Input Requirements**: Requires properly formatted spatial transcriptomics data
- **Spatial Information**: Requires spatial coordinates for analysis
- **TF Database**: Requires TF database for network inference
- **Memory Usage**: Large spatial datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `spagrn --help`
**Explanation:** Shows available options and usage information.

### Basic GRN inference
**Args:** `spagrn -i spatial_data.tsv -o grn.tsv`
**Explanation:** Infer spatial gene regulatory network.

### With TF list
**Args:** `spagrn -i spatial_data.tsv -t tf_list.txt -o grn.tsv`
**Explanation:** Use specific TF list for inference.

### With spatial coordinates
**Args:** `spagrn -i spatial_data.tsv -c coordinates.tsv -o grn.tsv`
**Explanation:** Use spatial coordinates for analysis.

### With cell types
**Args:** `spagrn -i spatial_data.tsv -a cell_types.tsv -o grn.tsv`
**Explanation:** Use cell type annotations.

### Output detailed network
**Args:** `spagrn -i spatial_data.tsv -o grn.tsv --detailed`
**Explanation:** Output detailed network information.

### Output statistics
**Args:** `spagrn -i spatial_data.tsv -o grn.tsv --stats`
**Explanation:** Output network statistics.

### Generate report
**Args:** `spagrn -i spatial_data.tsv -o grn.tsv --report`
**Explanation:** Generate network inference report.

### With threads
**Args:** `spagrn -i spatial_data.tsv -o grn.tsv -p 8`
**Explanation:** Use multiple threads for inference.