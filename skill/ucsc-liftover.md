---
name: ucsc-liftover
category: utility
description: UCSC liftOver - Tool for coordinate conversion between assemblies.
tags: [ucsc-liftover, ucsc, coordinate-conversion, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC liftOver - A tool for converting genome coordinates between assemblies.
- **Core Function**: Maps coordinates from one genome assembly to another using chain files.
- **Input**: BED file with coordinates, chain file.
- **Output**: BED file with converted coordinates.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome assembly conversion, coordinate mapping, data integration.

## Pitfalls

- **Chain File**: Requires appropriate chain file for assembly conversion.
- **Memory**: May require significant memory for large files.

## Examples

### Lift over coordinates
**Args:** `liftOver input.bed hg19ToHg38.over.chain output.bed unMapped.bed`
**Explanation:** Convert coordinates from hg19 to hg38.

### With options
**Args:** `liftOver -minMatch=0.9 input.bed hg19ToHg38.over.chain output.bed unMapped.bed`
**Explanation:** Minimum match ratio.
