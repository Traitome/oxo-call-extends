---
name: checkm-genome
category: qc
description: Assess the quality of microbial genomes recovered from isolates, single cells, and metagenomes
tags: [checkm-genome, genome-quality, completeness, contamination, metagenomics, mag]
author: oxo-call-community
source_url: "https://ecogenomics.github.io/CheckM"
---

## Concepts

- **Tool Overview**: CheckM is a comprehensive tool for assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes.
- **Core Function**: Estimates genome completeness and contamination using lineage-specific marker sets and provides overall quality scores.
- **Algorithm**: Uses a hierarchical approach with phylogenetic marker genes to assess genome quality across different taxonomic levels.
- **Input**: Genome FASTA files (contigs/scaffolds) from isolates, single cells, or metagenome-assembled genomes (MAGs).
- **Output**: Quality reports with completeness, contamination, strain heterogeneity estimates, and taxonomic classification.
- **Application**: Genome quality assessment, MAG validation, and microbial community analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda checkm-genome`

## Pitfalls

- **Database Required**: Must download and index CheckM database before first use.
- **Lineage Selection**: Auto-lineage mode may fail for highly novel organisms.
- **Contamination Detection**: May miss subtle contamination from closely related strains.
- **Computational Time**: Full analysis can be time-consuming for large genome collections.
- **Memory Usage**: Requires significant memory for large datasets.

## Examples

### Basic quality assessment
**Args:** `checkm lineage_wf -t 8 -x fna bins/ output/`
**Explanation:** Runs complete lineage workflow on genome bins using 8 threads.

### Quick quality check
**Args:** `checkm qa -o 2 -f results.tsv tree/ markers/`
**Explanation:** Generates quality report from pre-computed analysis.

### Generate tree
**Args:** `checkm tree -t 8 bins/ tree/`
**Explanation:** Constructs phylogenetic tree from genome bins.

### Download database
**Args:** `checkm data setRoot /path/to/database/`
**Explanation:** Sets the path to the CheckM database directory.

### Display help
**Args:** `checkm --help`
**Explanation:** Shows all available commands and options.