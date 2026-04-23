---
name: auspice
category: utility
description: Auspice - Open-source interactive web application for visualizing phylogenomic data from Nextstrain
tags: [visualization, phylogenetics, nextstrain, interactive, web-application]
author: oxo-call-community
source_url: "https://github.com/nextstrain/auspice"
---

## Concepts

- **Tool Overview**: Auspice is an open-source interactive web application for visualizing phylogenomic data, particularly pathogen evolution. It is the visualization component of the Nextstrain platform and works with Augur analysis outputs.

- **Interactive Exploration**: Provides rich interactive features including zooming, panning, filtering by metadata, coloring by various traits (clades, mutations, geographic location), and temporal animation.

- **Augur Integration**: Designed to visualize JSON output files from Augur pipeline, creating seamless workflow from sequence analysis to interactive visualization.

- **Multiple Display Modes**: Supports multiple visualization types including phylogenetic trees, geographic maps, temporal frequency plots, and diversity displays.

- **Customizable Appearance**: Allows customization of colors, layouts, and displayed metadata through configuration files, enabling tailored visualizations for different pathogens and research questions.

- **Deployment Options**: Can run locally for private data exploration or be deployed as a web server for sharing results publicly, as demonstrated by nextstrain.org.

- **Metadata Integration**: Displays rich metadata including sample dates, geographic locations, host information, and custom annotations directly on the tree and map visualizations.

## Pitfalls

- **JSON Format Requirements**: Requires properly formatted JSON files from Augur export. Manually created JSON files must follow strict schema specifications.

- **Browser Compatibility**: Works best in modern browsers (Chrome, Firefox, Safari). Older browsers may have rendering issues or missing features.

- **Dataset Size Limits**: Very large trees (>10,000 tips) can cause performance issues. Consider subsampling or aggregating for large datasets.

- **Geographic Data**: Map visualizations require proper geographic metadata (latitude/longitude or country/region names) in standardized formats.

- **URL Parameters**: Sharing visualizations via URL requires understanding parameter encoding. Complex states may generate very long URLs.

- **Custom Build Requirements**: Customizing Auspice for specific projects requires JavaScript/React knowledge and understanding of the codebase structure.

- **Data Privacy**: When deploying publicly, ensure no sensitive or confidential data is included in the visualization dataset.

## Examples

### View local dataset
**Args:** `auspice view --datasetDir ./data`
**Explanation:** Starts local Auspice server to visualize datasets in the ./data directory. Opens browser to interactive visualization.

### View specific dataset
**Args:** `auspice view --datasetDir ./data --datasetName zika`
**Explanation:** Starts server and directly loads the "zika" dataset from the data directory, skipping dataset selection screen.

### Custom port for local server
**Args:** `auspice view --datasetDir ./data --port 4000`
**Explanation:** Runs Auspice on custom port 4000 instead of default port, useful when default port is occupied.

### Build custom Auspice
**Args:** `auspice build --datasetDir ./data --extend custom_config.json`
**Explanation:** Builds custom Auspice deployment with extended configuration for specific visualization needs and branding.

### Develop with hot reload
**Args:** `auspice develop --datasetDir ./data`
**Explanation:** Starts development server with hot reload for testing custom modifications to Auspice codebase.

### Export static visualization
**Args:** `auspice export --datasetDir ./data --output ./export`
**Explanation:** Exports static HTML files for deployment on any web server without requiring Node.js runtime.

### Run with verbose logging
**Args:** `auspice view --datasetDir ./data --verbose`
**Explanation:** Starts server with detailed logging for debugging issues with dataset loading or rendering.

### Serve with HTTPS
**Args:** `auspice view --datasetDir ./data --https --cert ./cert.pem --key ./key.pem`
**Explanation:** Runs Auspice with HTTPS encryption using provided SSL certificate and key for secure access.

### Specify custom auspice.json path
**Args:** `auspice view --datasetDir ./data --config ./custom_auspice.json`
**Explanation:** Uses custom configuration file instead of default auspice.json for server settings and customization.

### Access remote dataset
**Args:** `auspice view --datasetUrl https://data.nextstrain.org/zika.json`
**Explanation:** Visualizes dataset from remote URL instead of local files, useful for viewing publicly shared datasets.

### Run with authentication
**Args:** `auspice view --datasetDir ./data --auth0-clientId CLIENT_ID --auth0-domain DOMAIN`
**Explanation:** Enables Auth0 authentication for access control, restricting visualization access to authorized users.
