---
name: cami-opal
category: metagenomics
description: Assessment of taxonomic metagenome profilers performance
tags: [opal, metagenomics, taxonomy, benchmark, cami]
author: oxo-call-community
source_url: "https://github.com/CAMI-challenge/OPAL"
---

## Concepts

- **Tool Overview**: OPAL assesses and compares taxonomic metagenome profiler performance.
- **Core Function**: Evaluates taxonomic profiling results against gold standard.
- **Input**: Profiling results in CAMI format and gold standard.
- **Output**: Performance metrics including L1 distance, recall, and precision.
- **Application**: Benchmarking metagenome taxonomic profiling tools.
- **Installation**: Install via bioconda: `conda install -c bioconda cami-opal`

## Pitfalls

- **CAMI Format**: Requires profiling results in CAMI-compatible format.
- **Gold Standard**: Requires ground truth taxonomic profile for comparison.
- **Taxonomy Levels**: Evaluates at multiple taxonomic ranks.

## Examples

### Evaluate profiling results
**Args:** `opal.py -g gold_standard.tsv -r profile_result.tsv -o opal_results/`
**Explanation:** Evaluates taxonomic profiling against gold standard.

### Compare multiple profilers
**Args:** `opal.py -g gold.tsv -r kraken.tsv metaphlan.tsv bracken.tsv -o comparison/`
**Explanation:** Compares multiple taxonomic profilers against gold standard.

### Display help
**Args:** `opal.py --help`
**Explanation:** Shows all available options and usage information.
