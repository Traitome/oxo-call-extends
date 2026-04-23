---
name: binsanity
category: metagenomics
description: Cluster contigs based on coverage and composition for genome binning
tags: [mag, binning, coverage, composition]
author: oxo-call-community
source_url: "https://github.com/edgraham/BinSanity"
---

## Concepts
- **Tool Overview**: BinSanity clusters contigs based on a biphasic method using coverage and composition (k-mer frequencies). It recovers MAGs from metagenomic assemblies.
- **Biphasic Approach**: First uses coverage profiles to identify initial bins, then refines with composition information.
- **Coverage-Based**: Leverages differential coverage across multiple samples for binning.
- **Applications**: Metagenome binning, MAG recovery from co-assembly or multi-sample projects.

## Pitfalls
- **Multiple Samples**: Best performance requires coverage profiles from multiple samples.
- **Parameter Tuning**: May require adjustment of clustering parameters for optimal results.

## Examples
### Run BinSanity binning
**Args:** `binsanity -f contigs.fa -c coverage_matrix.tsv -o bins/`
**Explanation:** Bins contigs using coverage and composition profiles.

### Specify k-mer size
**Args:** `binsanity -f contigs.fa -c coverage.tsv -k 4 -o bins/`
**Explanation:** Uses 4-mer frequencies for composition-based binning.
