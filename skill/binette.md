---
name: binette
category: metagenomics
description: Fast and accurate binning refinement to construct high-quality MAGs
tags: [mag, binning-refinement, metagenomics, binning]
author: oxo-call-community
source_url: "https://github.com/genotoul-bioinfo/binette"
---

## Concepts
- **Tool Overview**: Binette is a fast and accurate binning refinement tool that constructs high-quality MAGs from the output of multiple binning tools. It combines and refines bins from different algorithms.
- **Binning Refinement**: Takes bins from multiple binning tools (MetaBAT2, MaxBin2, CONCOCT, etc.) and produces refined, higher-quality MAGs.
- **Quality Metrics**: Uses completeness, contamination, and strain heterogeneity to evaluate and select best bins.
- **Workflow**: Input bins → quality assessment → bin merging/splitting → refined MAG output.

## Pitfalls
- **Input Quality**: Output quality depends on input bin quality. Poor input bins cannot be fully recovered.
- **CheckM Dependency**: Requires CheckM for quality assessment.
- **Computational Cost**: Quality assessment can be time-consuming for large bin collections.

## Examples
### Refine bins from multiple tools
**Args:** `binette -i metabat_bins/ maxbin_bins/ concoct_bins/ -o refined_bins/`
**Explanation:** Combines and refines bins from three binning tools.

### Specify quality thresholds
**Args:** `binette -i bins/ -o refined/ --min-completeness 90 --max-contamination 5`
**Explanation:** Only outputs MAGs with ≥90% completeness and ≤5% contamination.
