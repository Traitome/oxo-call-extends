---
name: pretextmap
category: alignment
description: Paired REad TEXTure Mapper. Converts SAM formatted read pairs into genome contact maps.
tags: ["pretextmap", "alignment", "sam"]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/PretextMap"
---

## Concepts

- **Tool Overview**: Paired REad TEXTure Mapper. Converts SAM formatted read pairs into genome contact maps. (version 0.2.4)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pretextmap`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

