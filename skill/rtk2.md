---
name: rtk2
category: statistics
description: rtk2 - a CLI rarefaction toolkit for OTU tables.
tags: ["rtk2", "rarefaction", "OTU", "microbiome", "diversity"]
author: oxo-call-community
source_url: "https://github.com/hildebra/rtk2"
---

## Concepts

- **Tool Overview**: rtk2 (v2.14) is a command-line toolkit for rarefaction analysis of microbial community data stored in OTU (Operational Taxonomic Unit) tables. It generates rarefaction curves and computes diversity metrics.
- **Core Function**: Performs rarefaction (subsampling) of OTU tables to normalize sequencing depth across samples, enabling meaningful comparison of alpha diversity metrics.
- **Algorithm**: Implements repeated random subsampling without replacement to generate rarefaction curves. Supports multiple diversity indices including Shannon, Simpson, and Chao1.
- **Input Format**: BIOM format OTU tables, tab-separated count matrices, or QIIME-compatible formats.
- **Output Format**: Rarefaction curves in PDF/PNG format, diversity metrics in TSV format, resampled OTU tables.
- **Use Case**: Normalizing microbiome sequencing data, comparing alpha diversity across samples, quality control of sequencing depth, generating publication-quality rarefaction curves.

## Pitfalls

- **Sample size limitation**: Rarefaction reduces sample size; very small samples may lose statistical power.
- **Randomness**: Results vary between runs due to random subsampling; use seed for reproducibility.
- **OTU table format**: Strict format requirements; ensure input files are correctly formatted.
- **Computational time**: Many iterations can be slow for large OTU tables.
- **Diversity metric selection**: Choose appropriate metrics for your research question.
- **Depth threshold**: Rarefaction to too low depth may mask true diversity differences.

## Examples

### Generate rarefaction curve
**Args:** `rtk2 rarefy -i otu_table.biom -o rarefaction_curve.pdf`
**Explanation:** `-i` input OTU table in BIOM format; `-o` output PDF with rarefaction curve.

### Specify sampling depth
**Args:** `rtk2 rarefy -i otu_table.biom -d 10000 -o rarefaction.pdf`
**Explanation:** `-d` subsample depth (number of reads per sample). Rarefies all samples to 10,000 reads.

### Compute diversity metrics
**Args:** `rtk2 diversity -i otu_table.biom -o diversity.tsv -m shannon,simpson,chao1`
**Explanation:** `-m` diversity metrics to compute. Outputs TSV with diversity indices per sample.

### Resample OTU table
**Args:** `rtk2 resample -i otu_table.biom -d 5000 -o resampled.biom`
**Explanation:** Generates a new OTU table with all samples rarefied to 5,000 reads.

### Multiple iterations
**Args:** `rtk2 rarefy -i otu_table.biom -n 100 -o rarefaction.pdf`
**Explanation:** `-n` number of iterations for subsampling. Computes mean and standard deviation across iterations.

### Set random seed
**Args:** `rtk2 rarefy -i otu_table.biom -s 42 -o rarefaction.pdf`
**Explanation:** `-s` random seed for reproducible results across runs.

### Compare two OTU tables
**Args:** `rtk2 compare -i1 table1.biom -i2 table2.biom -o comparison.tsv`
**Explanation:** Compares diversity metrics between two OTU tables.
