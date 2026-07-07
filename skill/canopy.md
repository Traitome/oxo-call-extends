---
name: canopy
category: metagenomics
description: Metagenomics canopy clustering implementation for binning
tags: [canopy, metagenomics, binning, clustering, canopy-clustering]
author: oxo-call-community
source_url: "https://github.com/hildebra/canopy2/"
---

## Concepts

- **Tool Overview**: Canopy implements canopy clustering for metagenomic binning.
- **Core Function**: Clusters contigs into genome bins using canopy clustering algorithm.
- **Algorithm**: Uses composition and coverage information for clustering.
- **Input**: Assembled contigs and coverage information.
- **Output**: Binned contigs organized by genome.
- **Application**: Metagenome-assembled genome recovery.
- **Installation**: Install via bioconda: `conda install -c bioconda canopy`

## Pitfalls

- **Coverage Data**: Requires coverage information from multiple samples.
- **Contig Length**: Short contigs may not cluster accurately.
- **Parameter Tuning**: May need to adjust clustering parameters.
- **Memory Usage**: Large assemblies require significant memory.

## Examples

### Perform canopy binning
**Args:** `canopy -i contigs.fa -c coverage.tsv -o bins/`
**Explanation:** Clusters contigs into bins using canopy clustering.

### Set clustering parameters
**Args:** `canopy -i contigs.fa -c coverage.tsv -t 0.9 -o bins/`
**Explanation:** Uses 0.9 similarity threshold for canopy clustering.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.