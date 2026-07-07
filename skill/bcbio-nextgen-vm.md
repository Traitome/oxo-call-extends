---
name: bcbio-nextgen-vm
category: containerization
description: bcbio-nextgen-vm - Run bcbio-nextgen analyses using isolated containers and virtual machines
tags: [bcbio-nextgen-vm, containerization, Docker, Singularity, reproducibility]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio-nextgen-vm"
---

## Concepts

- **Tool Overview**: bcbio-nextgen-vm (v0.1.6) enables running bcbio-nextgen genomic sequencing analyses using isolated containers (Docker/Singularity) and virtual machines for reproducibility.
- **Core Function**: Provides containerized execution of bcbio-nextgen pipelines for consistent and reproducible analyses.
- **Container Support**: Supports Docker and Singularity containers for environment isolation.
- **Reproducibility**: Ensures consistent execution environment across different systems.
- **Cloud Integration**: Works with cloud platforms for scalable analysis.
- **Input/Output**: Accepts bcbio configuration files; outputs analysis results.
- **Installation**: `conda install -c bioconda bcbio-nextgen-vm`.

## Pitfalls

- **Container Availability**: Requires Docker or Singularity to be installed and running.
- **Image Download**: Initial image download can be large (>10GB).
- **Network Access**: Requires network access to pull container images.
- **Resource Allocation**: Ensure sufficient resources for container execution.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Run pipeline with Docker
**Args:** `bcbio_vm.py docker run config.yaml workdir/`
**Explanation:** Runs bcbio-nextgen pipeline using Docker container.

### Run pipeline with Singularity
**Args:** `bcbio_vm.py singularity run config.yaml workdir/`
**Explanation:** Runs bcbio-nextgen pipeline using Singularity container.

### Pull container image
**Args:** `bcbio_vm.py docker pull`
**Explanation:** Pulls the latest bcbio-nextgen Docker image.

### List available images
**Args:** `bcbio_vm.py docker images`
**Explanation:** Lists available bcbio-nextgen container images.

### Run on AWS
**Args:** `bcbio_vm.py aws run config.yaml workdir/ --region us-east-1`
**Explanation:** Runs pipeline on AWS cloud with specified region.

### Generate cloud configuration
**Args:** `bcbio_vm.py aws config --instance-type t2.large`
**Explanation:** Generates AWS cloud configuration for pipeline execution.

### Display help
**Args:** `bcbio_vm.py --help`
**Explanation:** Shows all available command-line options and usage information.