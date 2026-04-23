---
name: abromics_galaxy_json_extractor
category: utility
description: Tool to convert Galaxy AMR output to abromics project format.
tags: [abromics_galaxy_json_extractor, utility, amr, galaxy, format-conversion]
author: oxo-call-community
source_url: "https://gitlab.com/ifb-elixirfr/abromics/abromics-galaxy-json-extractor"
---

## Concepts

- **Tool Overview**: Converts Galaxy AMR analysis output (JSON format) to the Abromics project format for integration with the Abromics platform. Version 0.8.3.6.
- **Core Function**: Extracts and reformats antimicrobial resistance analysis results from Galaxy workflows into Abromics-compatible project files.
- **Input/Output**: Input is Galaxy AMR output in JSON format; output is Abromics project format.
- **Installation**: Install via bioconda: `conda install -c bioconda abromics_galaxy_json_extractor`
- **Platform Support**: Platform-independent (noarch)
- **Galaxy Integration**: Designed to bridge Galaxy workflow outputs with the Abromics surveillance platform.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Format**: Requires Galaxy AMR output in specific JSON format. Other formats are not supported.
- **Galaxy Version**: Galaxy tool versions may affect JSON structure. Ensure compatibility.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Convert Galaxy AMR output
**Args:** `-i galaxy_amr_output.json -o abromics_project.json`
**Explanation:** Converts Galaxy AMR analysis output from JSON to Abromics project format for platform integration.

### Convert with metadata
**Args:** `-i input.json -o output.json --sample-name sample1 --project-name project1`
**Explanation:** Converts output with additional metadata (sample and project names) for better organization in the Abromics platform.
