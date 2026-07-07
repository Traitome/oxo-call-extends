---
name: ucsc-fetchchromsizes
category: utility
description: UCSC fetchChromSizes - Tool for fetching chromosome sizes.
tags: [ucsc-fetchchromsizes, ucsc, genome, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC fetchChromSizes - A tool for retrieving chromosome sizes from UCSC genome browser.
- **Core Function**: Downloads chromosome size information for specified genome.
- **Input**: Genome assembly name.
- **Output**: Chromosome sizes file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome analysis, data preparation, tool configuration.

## Pitfalls

- **Network Access**: Requires internet connection.
- **Genome Name**: Requires correct genome assembly name.

## Examples

### Fetch chromosome sizes
**Args:** `fetchChromSizes hg38 > chrom.sizes`
**Explanation:** Get chromosome sizes for hg38.

### For mm10
**Args:** `fetchChromSizes mm10 > chrom.sizes`
**Explanation:** Get chromosome sizes for mouse mm10.
