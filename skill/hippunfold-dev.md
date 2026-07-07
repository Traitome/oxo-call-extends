---
name: hippunfold-dev
category: utility
description: Meta-package that installs hippunfold with development dependencies for testing and development purposes.
tags: [hippunfold-dev, development, neuroimaging, utility]
author: oxo-call-community
source_url: "https://github.com/khanlab/hippunfold"
---

## Concepts

- **Development Environment**: Provides all dependencies needed for HippUnfold development.

- **Meta-package**: Installs the main hippunfold package along with development tools.

- **Testing Support**: Includes testing frameworks and dependencies.

- **Debugging Tools**: Provides tools for debugging and profiling.

- **Continuous Integration**: Supports CI/CD workflows for development.

- **Pre-release Features**: May include unreleased features for testing.

## Pitfalls

- **Unstable Features**: Development version may contain experimental or unstable features.

- **Compatibility**: May not be compatible with production pipelines.

- **Documentation**: Documentation may be incomplete for new features.

- **Dependency Conflicts**: Development dependencies may conflict with other packages.

- **Version Compatibility**: Ensure compatibility with other neuroimaging tools.

## Examples

### Install hippunfold-dev
**Args:** `conda install -c bioconda hippunfold-dev`
**Explanation:** Installs hippunfold with development dependencies.

### Install in development mode
**Args:** `pip install -e .[dev]`
**Explanation:** Installs in editable mode with development extras.

### Run tests
**Args:** `pytest tests/`
**Explanation:** Runs the test suite for hippunfold.

### Build documentation
**Args:** `sphinx-build docs/ docs/_build/html`
**Explanation:** Builds the documentation locally.

### Run with debug mode
**Args:** `hippunfold /input/dir /output/dir participant --debug`
**Explanation:** Runs HippUnfold with debug logging enabled.

### Check version
**Args:** `hippunfold --version`
**Explanation:** Shows the installed version.

### Help command
**Args:** `hippunfold --help`
**Explanation:** Shows available options and usage information.