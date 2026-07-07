---
name: start-asap
category: utility
description: Prepare project directory and project sheet for ASA3P.
tags: [start-asap, project-management, bioinformatics-pipeline]
author: oxo-call-community
source_url: "http://github.com/quadram-institute-bioscience/start-asap/"
---

## Concepts

- **Tool Overview**: start-asap (v1.3.0) is a utility for setting up project directories and configuration sheets for the ASA3P pipeline.
- **Core Function**: Creates standardized project structure and generates configuration files for ASA3P analysis.
- **Workflow Components**: Project initialization → sample sheet generation → configuration file creation.
- **Input/Output**: Input: Sample information and sequencing metadata; Output: Project directory structure and config files.
- **ASA3P Integration**: Seamlessly integrates with the ASA3P amplicon sequencing analysis pipeline.
- **Installation**: `conda install -c bioconda start-asap` or download from GitHub.

## Pitfalls

- **Configuration Requirements**: Requires specific metadata format for sample information.
- **Directory Structure**: Incorrect directory setup affects downstream analysis.
- **Version Compatibility**: Must match ASA3P version for proper integration.
- **Metadata Completeness**: Incomplete sample information causes configuration errors.
- **Path Configuration**: Incorrect path specifications break pipeline execution.
- **Dependency Checks**: Missing dependencies affect project initialization.

## Examples

### Display help
**Args:** `start-asap --help`
**Explanation:** Shows available options and usage information.

### Initialize project
**Args:** `start-asap init -n my_project -o project_dir/`
**Explanation:** Create new project directory structure.

### Generate sample sheet
**Args:** `start-asap sheet -i samples.csv -o project_dir/samplesheet.csv`
**Explanation:** Generate sample sheet from CSV input.

### Full project setup
**Args:** `start-asap project -n my_project -i samples.csv -o project_dir/`
**Explanation:** Complete project setup with directory structure and sample sheet.

### Add samples
**Args:** `start-asap add -p project_dir/ -i new_samples.csv`
**Explanation:** Add new samples to existing project.

### Validate configuration
**Args:** `start-asap validate -p project_dir/`
**Explanation:** Validate project configuration and sample sheet.

### Generate config file
**Args:** `start-asap config -p project_dir/ -o config.yaml`
**Explanation:** Generate configuration file for ASA3P.

### Verbose mode
**Args:** `start-asap init -n my_project -o project_dir/ -v`
**Explanation:** Run with detailed logging for debugging.

### Template generation
**Args:** `start-asap template -o template/`
**Explanation:** Generate empty project template for manual editing.
