---
name: sumaclust
category: formatting
description: Sumaclust clusters sequences in a way that is fast and exact at the same time, using the same clustering algorithm as UCLUST and CD-HIT. For more information see url.
tags: [sumaclust, formatting, sam]
author: oxo-call-community
source_url: "https://git.metabarcoding.org/obitools/sumaclust/wikis/home"
---

## Concepts

- **Tool Overview**: sumaclust (v1.0.31) - Sumaclust clusters sequences in a way that is fast and exact at the same time, using the same clustering algorithm as UCLUST and CD-HIT. For more information see url.
- **Core Function**: Sumaclust clusters sequences in a way that is fast and exact at the same time, using the same clustering algorithm as UCLUST and CD-HIT. For more information see url.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sumaclust`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sumaclust -i <input_file> -o <output_file>`
**Explanation:** Run sumaclust with typical input and output options.
