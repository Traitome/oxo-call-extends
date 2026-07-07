---
name: nextstrain-cli
category: utility
description: Nextstrain CLI provides a unified interface for running and visualizing pathogen builds across different computing environments.
tags: [nextstrain-cli, utility, nextstrain, bioinformatics, pathogen]
author: oxo-call-community
source_url: "https://docs.nextstrain.org/projects/cli"
---

## Concepts

- **Tool Overview**: Nextstrain CLI is the command-line interface for the Nextstrain project.
- **Core Function**: Manages and runs pathogen genomic analysis workflows.
- **Algorithm**: Orchestrates Nextstrain components (Augur, Auspice) across environments.
- **Input Format**: Accepts sequence data and configuration files.
- **Output**: Produces phylogenetic trees and visualization data.
- **Use Case**: Pathogen surveillance, outbreak analysis, and genomic epidemiology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Environment Setup**: Requires proper environment configuration.
- **Docker/Singularity**: May require container runtime.
- **Network Access**: May need internet for data downloads.
- **Memory Usage**: Large datasets require memory.
- **Configuration Complexity**: Complex workflows require detailed configuration.

## Examples

### Display help
**Args:** `nextstrain --help`
**Explanation:** Shows available options and usage instructions.

### Check setup
**Args:** `nextstrain check-setup`
**Explanation:** Verifies Nextstrain environment setup.

### Run build
**Args:** `nextstrain build --docker .`
**Explanation:** Runs Nextstrain build using Docker.

### View results
**Args:** `nextstrain view auspice/`
**Explanation:** Views results in Auspice browser.

### Upload to Nextstrain
**Args:** `nextstrain upload auspice/ my-analysis`
**Explanation:** Uploads results to Nextstrain server.

### Run with Singularity
**Args:** `nextstrain build --singularity .`
**Explanation:** Runs build using Singularity container.

### List remote analyses
**Args:** `nextstrain list`
**Explanation:** Lists analyses on Nextstrain server.