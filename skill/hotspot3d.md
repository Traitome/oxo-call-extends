---
name: hotspot3d
category: hpc
description: This 3D proximity tool can be used to identify mutation hotspots from linear protein sequence and correlate the hotspots with known or potentially interacting domains, mutations, or drugs. Mutation-mutation and mutation-drug clusters can also be identified and viewed.
tags: [hotspot3d, hpc]
author: oxo-call-community
source_url: "https://github.com/ding-lab/hotspot3d"
---

## Concepts

- **Tool Overview**: hotspot3d (v1.8.2) - This 3D proximity tool can be used to identify mutation hotspots from linear protein sequence and correlate the hotspots with known or potentially interacting domains, mutations, or drugs. Mutation-mutation and mutation-drug clusters can also be identified and viewed.
- **Core Function**: Provides functionality for hpc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hotspot3d`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
