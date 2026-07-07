---
name: matchmsextras
category: utility
description: Additional network analysis functions for matchms mass spectrometry data processing.
tags: [matchmsextras, mass-spectrometry, network-analysis]
author: oxo-call-community
source_url: "https://github.com/matchms/matchmsextras"
---

## Concepts

- **Tool Overview**: matchmsextras provides additional network analysis functions for matchms.
- **Core Function**: Extends matchms with network-based analysis of mass spectrometry data.
- **Network Construction**: Builds similarity networks from mass spec data.
- **Community Detection**: Identifies communities within mass spec networks.
- **Visualization**: Generates network visualizations for exploratory analysis.
- **Installation**: `conda install -c bioconda matchmsextras`

## Pitfalls

- **Dependency on matchms**: Requires matchms library to be installed.
- **Data Quality**: Network analysis results depend on input data quality.
- **Computation Time**: Complex network analyses can be time-consuming.
- **Memory Usage**: Large networks require significant memory.
- **Parameter Tuning**: Network parameters affect community detection results.
- **Interpretation**: Network results require careful biological interpretation.

## Examples

### Build similarity network
**Args:** `matchmsextras build-network -i spectra.mgf -o network.graphml`
**Explanation:** Constructs similarity network from mass spectra.

### Detect communities
**Args:** `matchmsextras communities -i network.graphml -o communities.csv`
**Explanation:** Identifies communities within the network.

### Visualize network
**Args:** `matchmsextras visualize -i network.graphml -o network.png`
**Explanation:** Generates visualization of the similarity network.

### Filter network
**Args:** `matchmsextras filter -i network.graphml -t 0.8 -o filtered.graphml`
**Explanation:** Filters edges below similarity threshold of 0.8.

### Export to CSV
**Args:** `matchmsextras export -i network.graphml -o edges.csv`
**Explanation:** Exports network edges to CSV format.

### Help documentation
**Args:** `matchmsextras --help`
**Explanation:** Displays available commands and options.
