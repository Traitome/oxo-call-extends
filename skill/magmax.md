---
name: magmax
category: assembly
description: MAGmax is a robust tool for dereplicating MAGs through bin merging and reassembly.
tags: [magmax, assembly, MAGs, metagenomics]
author: oxo-call-community
source_url: "https://github.com/soedinglab/MAGmax"
---

## Concepts

- **Tool Overview**: magmax v1.3.0 - MAGmax is a tool for dereplicating and improving Metagenome-Assembled Genomes (MAGs) through bin merging and reassembly.
- **Core Function**: Identifies redundant MAGs, merges them, and performs reassembly to produce high-quality consensus genomes.
- **Input/Output**: Input: Multiple MAG sequences (FASTA), alignment files; Output: Dereplicated MAGs, consensus sequences.
- **Installation**: `conda install -c bioconda magmax`
- **Bin Merging**: Identifies highly similar MAGs and merges them to improve completeness.
- **Reassembly**: Uses merged bins for improved genome assembly.

## Pitfalls

- **Similarity Threshold**: Incorrect threshold settings may merge dissimilar MAGs.
- **Memory Usage**: Processing large numbers of MAGs requires significant memory.
- **Contamination**: Contaminated MAGs can affect merging quality.
- **Completeness**: Poorly assembled MAGs may not benefit from merging.
- **Reference Database**: Requires appropriate reference databases for comparison.
- **Output Organization**: Multiple output files require careful management.

## Examples

### Dereplicate MAGs
**Args:** `magmax -i mags/ -o dereplicated/ -t 0.95`
**Explanation:** Dereplicates MAGs with 95% similarity threshold.

### With reassembly
**Args:** `magmax -i mags/ -o dereplicated/ --reassemble`
**Explanation:** Performs reassembly after merging.

### Custom similarity threshold
**Args:** `magmax -i mags/ -o dereplicated/ -t 0.99`
**Explanation:** Uses 99% ANI threshold for merging.

### Verbose mode
**Args:** `magmax -i mags/ -o dereplicated/ -v`
**Explanation:** Provides detailed logging during processing.

### With minimum completeness
**Args:** `magmax -i mags/ -o dereplicated/ --min-completeness 50`
**Explanation:** Filters MAGs with minimum 50% completeness.

### Generate report
**Args:** `magmax -i mags/ -o dereplicated/ --report`
**Explanation:** Generates HTML report of dereplication results.