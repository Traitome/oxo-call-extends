---
name: metaamrplus
category: utility
description: Unified detection of antimicrobial and metal resistance genes with colocalisation analysis.
tags: [metaamrplus, amr, antimicrobial-resistance]
author: oxo-call-community
source_url: "https://github.com/migshaw03/MetaAMRplus"
---

## Concepts

- **Tool Overview**: MetaAMRplus detects resistance genes in bacterial genomes.
- **Core Function**: AMR and metal resistance gene detection.
- **Colocalisation Analysis**: Analyzes gene co-occurrence.
- **Database Integration**: Uses AMRFinder and BacMet databases.
- **Large-scale Analysis**: Designed for reproducible analyses.
- **Installation**: `conda install -c bioconda metaamrplus`

## Pitfalls

- **Database Updates**: Needs updated resistance databases.
- **Computation Time**: Slow for large datasets.
- **Memory Requirements**: High memory usage.
- **False Positives**: May detect non-resistance genes.
- **Database Dependencies**: Requires external databases.
- **Result Interpretation**: Complex output requires expertise.

## Examples

### Detect resistance genes
**Args:** `metaamrplus -i genome.fasta -o results/`
**Explanation:** Detects AMR and metal resistance genes.

### With plasmid
**Args:** `metaamrplus -i genome.fasta -p plasmid.fasta -o results/`
**Explanation:** Analyzes genome and plasmid together.

### Colocalisation analysis
**Args:** `metaamrplus -i genome.fasta --colocalise -o results/`
**Explanation:** Performs colocalisation analysis.

### Verbose mode
**Args:** `metaamrplus -i genome.fasta -v -o results/`
**Explanation:** Shows detailed processing progress.

### Help documentation
**Args:** `metaamrplus --help`
**Explanation:** Displays available options.
