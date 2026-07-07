---
name: neurodocker
category: containerization
description: Neurodocker generates custom Dockerfiles and Singularity recipes for neuroimaging applications.
tags: [neurodocker, containerization, docker, singularity, neuroimaging]
author: oxo-call-community
source_url: "https://github.com/kaczmarj/neurodocker"
---

## Concepts

- **Tool Overview**: Neurodocker automates container image creation for neuroimaging workflows.
- **Core Function**: Generates Dockerfiles and Singularity recipes with neuroimaging software.
- **Algorithm**: Parses configuration and generates container specification files.
- **Input Format**: Accepts JSON configuration or command-line arguments.
- **Output**: Produces Dockerfiles, Singularity recipes, or built container images.
- **Use Case**: Reproducible neuroimaging research, workflow containerization, and HPC deployment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Docker/Singularity**: Requires Docker or Singularity installation.
- **Image Size**: Generated images can be large.
- **Network Dependency**: Requires internet access for base images.
- **Configuration Complexity**: Complex workflows require detailed configuration.
- **Registry Access**: May require Docker Hub or Singularity registry access.

## Examples

### Display help
**Args:** `neurodocker --help`
**Explanation:** Shows available options and usage instructions.

### Generate Dockerfile
**Args:** `neurodocker generate docker -b ubuntu:20.04 -p apt -n fsl -o Dockerfile`
**Explanation:** Generates Dockerfile with FSL installed.

### Generate Singularity recipe
**Args:** `neurodocker generate singularity -b debian:10 -p apt -n freesurfer -o Singularity`
**Explanation:** Generates Singularity recipe with FreeSurfer.

### Build Docker image
**Args:** `neurodocker build docker -b ubuntu:20.04 -p apt -n ants -t neuroimaging:latest`
**Explanation:** Builds Docker image directly.

### JSON configuration
**Args:** `neurodocker generate docker -f config.json -o Dockerfile`
**Explanation:** Uses JSON configuration file.

### Minify container
**Args:** `neurodocker minify input.sif -o minified.sif`
**Explanation:** Minifies existing Singularity container.