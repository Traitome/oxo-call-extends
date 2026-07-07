---
name: cytoscape
category: utility
description: "Cytoscape: an open source platform for network analysis and visualization."
tags: [cytoscape, utility, network-analysis, visualization, bioinformatics, graph]
author: oxo-call-community
source_url: "https://cytoscape.org"
---
## Concepts

- **Tool Overview**: Cytoscape (v3.10.4+) is an open source platform for visualizing and analyzing biological networks, including protein-protein interactions, gene regulatory networks, and metabolic pathways.
- **Core Function**: Provides interactive visualization, analysis, and annotation of biological networks with support for numerous file formats and plugins.
- **Input/Output**: Input: Network files (SIF, GML, XGMML, SBML, BioPAX), session files (.cys). Output: Visualized networks, analysis reports, image exports (PNG, PDF, SVG).
- **Command Line Mode**: While primarily a GUI application, Cytoscape supports command-line arguments for batch operations and script execution.
- **REST API**: Can start a REST service for programmatic access to network operations.
- **Installation**: `conda install -c bioconda cytoscape` or download from cytoscape.org

## Pitfalls

- **Java Requirement**: Cytoscape requires Java 11+ to run; ensure correct Java version is available.
- **Memory Allocation**: Large networks require significant memory; adjust heap size via `_JAVA_OPTIONS`.
- **File Paths**: Network files with spaces in paths must be quoted properly.
- **Session Files**: .cys session files contain complete state including networks, styles, and layouts.
- **Script Execution**: Script files must be in Cytoscape's scripting language format (JavaScript or Python via plugins).

## Examples

### Display help
**Args:** `-h`
**Explanation:** Show all available command-line options and usage information.

### Launch with a network file
**Args:** `-N network.sif`
**Explanation:** Start Cytoscape and load a network from a SIF (Simple Interaction Format) file.

### Load multiple networks
**Args:** `-N network1.sif -N network2.gml`
**Explanation:** Load multiple network files in a single Cytoscape instance.

### Load a session file
**Args:** `-s analysis.cys`
**Explanation:** Restore a previous Cytoscape session including all networks, styles, and layouts.

### Apply visualization style
**Args:** `-V custom_style.vizmap`
**Explanation:** Load a custom visualization style file to apply consistent styling to networks.

### Execute a script
**Args:** `-S analysis_script.js`
**Explanation:** Execute a JavaScript or Python script for automated network analysis tasks.

### Start REST API service
**Args:** `-R 1234`
**Explanation:** Start Cytoscape with a REST API service on port 1234 for programmatic access.

### Set custom properties
**Args:** `-P defaultSpeciesName=Human -P noCanonicalization=true`
**Explanation:** Set individual Cytoscape properties at startup using key=value pairs.
