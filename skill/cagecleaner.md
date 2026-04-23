---
name: cagecleaner
category: annotation
description: Genomic redundancy removal tool for cblaster hit sets
tags: [cagecleaner, redundancy, cblaster, annotation]
author: oxo-call-community
source_url: "https://github.com/LucoDevro/CAGEcleaner"
---

## Concepts

- **Tool Overview**: CAGEcleaner removes genomic redundancy from cblaster hit sets.
- **Core Function**: Filters cblaster results to remove redundant genome hits.
- **Input**: cblaster output files.
- **Output**: Non-redundant hit sets.
- **Application**: Gene cluster analysis and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cagecleaner`

## Pitfalls

- **cblaster Dependency**: Requires cblaster output as input.
- **Redundancy Definition**: Adjust parameters for redundancy threshold.

## Examples

### Clean cblaster results
**Args:** `cagecleaner -i cblaster_results.tsv -o cleaned.tsv`
**Explanation:** Removes redundant hits from cblaster output.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
