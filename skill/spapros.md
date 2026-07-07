---
name: spapros
category: spatial-omics
description: Spapros - Probe set selection for targeted spatial transcriptomics
tags: [spapros, spatial-omics, probe-selection, spatial-transcriptomics, targeted]
author: oxo-call-community
source_url: "https://spapros.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: spapros (v0.1.6) - A probe set selection tool
- **Core Function**: Selects optimal probe sets for targeted spatial transcriptomics
- **Input/Output**: Accepts expression data; outputs probe sets
- **Algorithm**: Optimizes probe selection for spatial coverage
- **Installation**: `conda install -c bioconda spapros`
- **Key Features**: Probe selection, spatial optimization, targeted analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted expression data
- **Spatial Information**: Requires spatial coordinates for optimization
- **Probe Constraints**: Probe design constraints affect selection
- **Memory Usage**: Large expression datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Optimization**: Optimization parameters affect probe set quality

## Examples

### Display help
**Args:** `spapros --help`
**Explanation:** Shows available options and usage information.

### Basic probe selection
**Args:** `spapros -i expression.tsv -o probes.tsv`
**Explanation:** Select probe set from expression data.

### With spatial coordinates
**Args:** `spapros -i expression.tsv -c coordinates.tsv -o probes.tsv`
**Explanation:** Use spatial coordinates for selection.

### With gene list
**Args:** `spapros -i expression.tsv -g genes.txt -o probes.tsv`
**Explanation:** Select probes for specific genes.

### With probe constraints
**Args:** `spapros -i expression.tsv -o probes.tsv --max-probes 100`
**Explanation:** Set maximum number of probes.

### With optimization
**Args:** `spapros -i expression.tsv -o probes.tsv --optimize`
**Explanation:** Optimize probe set for spatial coverage.

### Output detailed results
**Args:** `spapros -i expression.tsv -o probes.tsv --detailed`
**Explanation:** Output detailed probe information.

### Output statistics
**Args:** `spapros -i expression.tsv -o probes.tsv --stats`
**Explanation:** Output selection statistics.

### Generate report
**Args:** `spapros -i expression.tsv -o probes.tsv --report`
**Explanation:** Generate probe selection report.