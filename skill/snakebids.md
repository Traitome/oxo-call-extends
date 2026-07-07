---
name: snakebids
category: programming
description: snakebids - BIDS integration into Snakemake workflows for streamlined data processing
tags: [snakebids, programming, bids, snakemake, workflow]
author: oxo-call-community
source_url: "https://github.com/khanlab/snakebids"
---

## Concepts

- **Tool Overview**: snakebids (v0.15.0) - A Snakemake extension for BIDS dataset processing
- **Core Function**: Integrates BIDS data organization with Snakemake workflow management
- **Input/Output**: Accepts BIDS-formatted data; outputs processed results
- **Algorithm**: Automates BIDS data parsing and workflow generation
- **Installation**: `conda install -c bioconda snakebids`
- **Key Features**: BIDS compliance, workflow automation, reproducibility

## Pitfalls

- **BIDS Compliance**: Input data must follow BIDS specification
- **Configuration Complexity**: Config files can be complex to set up
- **Workflow Dependencies**: Requires proper environment setup
- **Memory Usage**: Large BIDS datasets may require significant memory
- **Version Compatibility**: May require specific Snakemake version
- **Data Validation**: BIDS validation errors can break pipeline

## Examples

### Display help
**Args:** `snakebids --help`
**Explanation:** Shows available options and usage information.

### Create new project
**Args:** `snakebids init my_project`
**Explanation:** Initialize new snakebids project.

### Run workflow
**Args:** `snakebids run -c config.yaml -b bids_data/ -o results/`
**Explanation:** Run snakebids workflow on BIDS data.

### Dry run
**Args:** `snakebids run -c config.yaml -b bids_data/ --dryrun`
**Explanation:** Perform dry run to check workflow.

### Generate config
**Args:** `snakebids config -b bids_data/ -o config.yaml`
**Explanation:** Generate configuration file from BIDS dataset.

### Validate BIDS
**Args:** `snakebids validate -b bids_data/`
**Explanation:** Validate BIDS dataset compliance.

### With custom workflow
**Args:** `snakebids run -c config.yaml -b bids_data/ -w custom_workflow.smk -o results/`
**Explanation:** Use custom Snakemake workflow.

### Multi-sample analysis
**Args:** `snakebids run -c config.yaml -b bids_data/ -s sample1 sample2 -o results/`
**Explanation:** Run workflow on specific samples.