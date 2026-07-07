---
name: mameshiba
category: utility
description: mameshiba installs only the dependencies needed to run MameShiba.
tags: [mameshiba, utility, meta-package, dependencies]
author: oxo-call-community
source_url: "https://github.com/Sika-Zheng-Lab/Shiba"
---

## Concepts

- **Tool Overview**: mameshiba v0.8.2 - A minimal conda meta-package that installs all dependencies required for running MameShiba, a tool for analyzing single-cell RNA-seq data.
- **Core Function**: Provides dependency management for MameShiba, ensuring all required packages are installed with compatible versions.
- **Input/Output**: Input: None (meta-package); Output: Installed dependencies.
- **Installation**: `conda install -c bioconda mameshiba`
- **Meta-package**: Acts as a virtual package that depends on other packages but contains no actual code.
- **Dependency Coordination**: Ensures consistent versions of dependent packages for MameShiba compatibility.

## Pitfalls

- **Version Conflicts**: May conflict with other installed packages.
- **Environment Management**: Requires careful environment management to avoid dependency issues.
- **Conda Channels**: Requires proper channel configuration for bioconda packages.
- **Update Issues**: May require manual updates when dependencies change.
- **Virtual Environment**: Best used in dedicated conda environments.
- **Package Availability**: Dependencies must be available in bioconda channels.

## Examples

### Install mameshiba
**Args:** `conda install -c bioconda mameshiba`
**Explanation:** Installs mameshiba and all its dependencies.

### Create dedicated environment
**Args:** `conda create -n mameshiba_env -c bioconda mameshiba`
**Explanation:** Creates new conda environment with mameshiba.

### Update mameshiba
**Args:** `conda update -c bioconda mameshiba`
**Explanation:** Updates mameshiba to latest version.

### List dependencies
**Args:** `conda list | grep -E "(mameshiba|shiba)"`
**Explanation:** Lists mameshiba and related packages.

### Check package info
**Args:** `conda info mameshiba`
**Explanation:** Shows information about mameshiba package.

### Export environment
**Args:** `conda env export > mameshiba_env.yml`
**Explanation:** Exports environment configuration.