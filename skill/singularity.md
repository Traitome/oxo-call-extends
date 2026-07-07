---
name: singularity
category: containerization
description: Singularity - Container platform for HPC
tags: ["singularity", "containerization", "hpc", "docker"]
author: oxo-call-community
source_url: "http://singularity.lbl.gov"
---

## Concepts

- **Tool Overview**: Singularity (v2.4.2) is a container platform for HPC environments.
- **Core Function**: Creates and runs containers in secure environments.
- **Algorithm**: Uses containerization for reproducible software deployment.
- **Input/Output**: Accepts container images and runs commands inside.
- **HPC Containerization**: Specialized for high-performance computing environments.
- **Applications**: Reproducible research, software deployment, workflow management.

## Pitfalls

- **Root Requirements**: Some operations require root access.
- **Version Compatibility**: Different versions may have breaking changes.
- **Image Size**: Container images can be large.
- **Network Access**: Requires network for pulling images.
- **Security**: Container security must be carefully managed.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Run container
**Args:** `singularity run docker://ubuntu:latest`
**Explanation:** Runs Ubuntu container from Docker Hub.

### Build container
**Args:** `singularity build my_container.sif Singularity`
**Explanation:** Builds container from Singularity definition file.

### Shell into container
**Args:** `singularity shell my_container.sif`
**Explanation:** Starts interactive shell in container.

### Help command
**Args:** `singularity --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `singularity --version`
**Explanation:** Shows current version.

### Pull image
**Args:** `singularity pull docker://biocontainers/samtools:latest`
**Explanation:** Pulls image from Docker Hub.

### Execute command
**Args:** `singularity exec my_container.sif samtools --help`
**Explanation:** Executes command inside container.
