---
name: das_tool
category: assembly
description: DAS Tool - recovery of genomes from metagenomes via dereplication, aggregation and scoring
tags: [das_tool, assembly, metagenomics, binning, genome-recovery]
author: oxo-call-community
source_url: "https://github.com/cmks/DAS_Tool"
---

## Concepts

- **Tool Overview**: das_tool (v1.1.7+) integrates results from multiple binning algorithms to recover high-quality genomes from metagenomic data.
- **Core Function**: Aggregates and scores bins from multiple binning tools to produce optimized, non-redundant genome bins.
- **Input/Output**: Input: Multiple binning results, contigs. Output: High-quality genome bins, completeness estimates.
- **Algorithm**: Uses dereplication, aggregation, and scoring strategy (DAS) to combine binning results.
- **Key Features**: Multi-tool integration, quality assessment, taxonomic classification.
- **Installation**: `conda install -c bioconda das_tool`

## Pitfalls

- **Binning Input**: Requires multiple binning results for effective integration.
- **Contig Quality**: Results depend on assembly quality.
- **Completeness Threshold**: Appropriate completeness thresholds must be set.
- **Contamination**: May include contaminated bins if not filtered properly.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Run DAS Tool
**Args:** `DAS_Tool -i maxbin_bins/,metabat_bins/,concoct_bins/ -c contigs.fasta -o das_bins/`
**Explanation:** Integrate multiple binning results to recover genomes.

### Specify output format
**Args:** `DAS_Tool -i bins/ -c contigs.fasta -o results/ --write_bins fasta`
**Explanation:** Output genome bins in FASTA format.

### Set quality thresholds
**Args:** `DAS_Tool -i bins/ -c contigs.fasta -o results/ --completeness 50 --contamination 10`
**Explanation:** Filter bins with minimum 50% completeness and maximum 10% contamination.
