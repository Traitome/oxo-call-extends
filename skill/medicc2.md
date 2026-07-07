---
name: medicc2
category: population-genomics
description: Whole-genome doubling-aware copy number phylogenies for cancer evolution.
tags: [medicc2, cancer-genomics, copy-number]
author: oxo-call-community
source_url: "https://bitbucket.org/schwarzlab/medicc2"
---

## Concepts

- **Tool Overview**: MEDICC2 infers copy number phylogenies for cancer evolution.
- **Core Function**: Constructs phylogenies accounting for whole-genome doubling.
- **Copy Number Analysis**: Analyzes copy number variations.
- **WGD Detection**: Detects whole-genome doubling events.
- **Phylogenetic Reconstruction**: Builds evolutionary trees from copy number data.
- **Installation**: `conda install -c bioconda medicc2`

## Pitfalls

- **Data Requirements**: Requires high-quality copy number profiles.
- **Computation Time**: Slow for large datasets.
- **Memory Requirements**: High memory usage.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **WGD Complexity**: Whole-genome doubling events complicate analysis.
- **Output Interpretation**: Results require expertise in cancer genomics.

## Examples

### Run MEDICC2
**Args:** `medicc2 -i cnv_data.txt -o results/`
**Explanation:** Infers copy number phylogeny.

### With WGD detection
**Args:** `medicc2 -i cnv_data.txt --wgd -o results/`
**Explanation:** Enables whole-genome doubling detection.

### Plot phylogeny
**Args:** `medicc2_plot -i results/tree.nwk -o tree.png`
**Explanation:** Visualizes phylogenetic tree.

### Detailed output
**Args:** `medicc2 -i cnv_data.txt -v -o results/`
**Explanation:** Shows detailed progress.

### Help documentation
**Args:** `medicc2 --help`
**Explanation:** Displays available options.
