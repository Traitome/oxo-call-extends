---
name: biopet-sampleconfig
category: utility
description: Extract and create sample configurations for Biopet pipelines
tags: [sample-config, pipeline-configuration, biopet]
author: oxo-call-community
source_url: "https://github.com/biopet/sampleconfig"
---

## Concepts
- **Tool Overview**: SampleConfig extracts samples, libraries, and readgroups from sample config files and creates configurations for Biopet pipelines.
- **Configuration Management**: Manages sample metadata including sample-library-readgroup hierarchies.
- **Format Support**: JSON and YAML configuration formats.
- **Applications**: Biopet pipeline setup, WDL pipeline support, case-control pair extraction.

## Pitfalls
- **Format Requirements**: Configuration files must follow Biopet-specific schema.

## Examples
### Extract sample information
**Args:** `java -jar SampleConfig.jar extract -I config.json -o samples.tsv`
**Explanation:** Extracts sample information from configuration file.
