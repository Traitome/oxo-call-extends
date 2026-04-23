---
name: cami-amber
category: metagenomics
description: Assessment of Metagenome BinnERs for benchmarking binning tools
tags: [amber, metagenomics, binning, benchmark, cami]
author: oxo-call-community
source_url: "https://github.com/CAMI-challenge/AMBER"
---

## Concepts

- **Tool Overview**: AMBER assesses and compares metagenome binning tool performance.
- **Core Function**: Evaluates binning results against gold standard using multiple metrics.
- **Input**: Binning results in CAMI format and gold standard.
- **Output**: Performance metrics including precision, recall, and F1 scores.
- **Application**: Benchmarking metagenome binning pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda cami-amber`

## Pitfalls

- **CAMI Format**: Requires binning results in CAMI-compatible format.
- **Gold Standard**: Requires ground truth binning for comparison.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Evaluate binning results
**Args:** `amber.py -g gold_standard.tsv -r binning_result.tsv -o amber_results/`
**Explanation:** Evaluates binning against gold standard and outputs metrics.

### Compare multiple binning tools
**Args:** `amber.py -g gold.tsv -r tool1.tsv tool2.tsv tool3.tsv -o comparison/`
**Explanation:** Compares multiple binning tools against gold standard.

### Display help
**Args:** `amber.py --help`
**Explanation:** Shows all available options and usage information.
