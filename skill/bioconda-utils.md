---
name: bioconda-utils
category: containerization
description: Utilities for building and managing bioconda recipes
tags: [bioconda, recipe-management, build-tools, containerization]
author: oxo-call-community
source_url: "https://github.com/bioconda/bioconda-utils"
---

## Concepts

- **Tool Overview**: bioconda-utils is a suite of utilities for building, testing, and managing Bioconda recipes. It provides CLI tools for linting recipes, building packages, and running tests in Docker containers.
- **Recipe Management**: Handles meta.yaml recipe parsing, validation, and rendering with Jinja2 templates.
- **Build System**: Supports building packages locally or in Docker containers with mulled-test integration.
- **CI Integration**: Used in Bioconda's continuous integration pipeline for automated recipe testing and building.

## Pitfalls

- **Docker Requirement**: Building with `--docker` flag requires Docker to be installed and running.
- **Version Compatibility**: Recipe syntax and build requirements may change between bioconda-utils versions.
- **Resource Intensive**: Building packages, especially with Docker, can be resource-intensive.

## Examples

### Lint a recipe
**Args:** `bioconda-utils lint recipes/ --packages mytool`
**Explanation:** Validates recipe syntax and checks for common issues.

### Build package with Docker
**Args:** `bioconda-utils build --docker --mulled-test --packages mytool`
**Explanation:** Builds package in Docker container and runs mulled tests.

### Build locally
**Args:** `bioconda-utils build --packages mytool`
**Explanation:** Builds package in the local environment.