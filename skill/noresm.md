---
name: noresm
category: utility
description: The Norwegian Earth System Model (NorESM) is a coupled climate model for simulating Earth’s climate system
tags: [noresm, utility]
author: oxo-call-community
source_url: "https://github.com/NorESMhub/NorESM"
---

## Concepts
- **Tool Overview**: "NorESM (Norwegian Earth System Model) is the Norwegian fully-coupled, global climate model that provides state-of-the-art computer simulations of the Earth's past, present, and future climate states. When creating a case, use `espresso` for the target machine. In addition, the following environment variables need to be defined before creating the noresm case: ``` export NETCDF_DIR=$(nc-config --prefix) export CIME_MODEL=cesm export CESM_DATA_ROOT=$HOME export CESM_WORK_ROOT=$HOME mkdir -p $CESM_DATA_ROOT/inputdata ``` "
- **Core Function**: Processes bioinformatics data for utility tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda noresm`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
