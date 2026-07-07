---
name: snakedeploy
category: programming
description: snakedeploy - Helper for deploying published Snakemake pipelines
tags: [snakedeploy, programming, snakemake, pipeline, deployment]
author: oxo-call-community
source_url: "https://github.com/snakemake/snakedeploy"
---

## Concepts

- **Tool Overview**: snakedeploy (v0.16.0) - A tool for deploying published Snakemake workflows
- **Core Function**: Downloads and sets up Snakemake pipelines from GitHub repositories
- **Input/Output**: Accepts pipeline URL and target directory; outputs deployed pipeline
- **Algorithm**: Clones repositories, creates configuration files, and sets up directory structure
- **Installation**: `conda install -c bioconda snakedeploy`
- **Key Features**: Easy pipeline deployment, version management, configuration templates

## Pitfalls

- **Network Access**: Requires internet access to download pipelines
- **Git Requirements**: Requires git to be installed
- **Directory Permissions**: Target directory must be writable
- **Version Compatibility**: Pipeline versions must be compatible with Snakemake version
- **Configuration Complexity**: May require manual config adjustments
- **Dependency Installation**: Pipeline dependencies must be installed separately

## Examples

### Display help
**Args:** `snakedeploy --help`
**Explanation:** Shows available options and usage information.

### Deploy pipeline
**Args:** `snakedeploy deploy-workflow https://github.com/snakemake-workflows/rna-seq-star-deseq2 --tag v1.0.0 output_dir/`
**Explanation:** Deploy RNA-seq pipeline from GitHub.

### Deploy with custom name
**Args:** `snakedeploy deploy-workflow https://github.com/snakemake-workflows/rna-seq-star-deseq2 --tag v1.0.0 --name my_rna_seq output_dir/`
**Explanation:** Deploy pipeline with custom name.

### List available pipelines
**Args:** `snakedeploy list-workflows`
**Explanation:** List available Snakemake workflows.

### Deploy from local directory
**Args:** `snakedeploy deploy-workflow file:///path/to/local/repo output_dir/`
**Explanation:** Deploy pipeline from local repository.

### Update deployed pipeline
**Args:** `snakedeploy update-workflow output_dir/`
**Explanation:** Update deployed pipeline to latest version.

### Create config template
**Args:** `snakedeploy init-config output_dir/config/config.yaml`
**Explanation:** Create configuration template.

### Deploy with specific branch
**Args:** `snakedeploy deploy-workflow https://github.com/snakemake-workflows/rna-seq-star-deseq2 --branch dev output_dir/`
**Explanation:** Deploy specific branch of pipeline.