---
name: taxpasta
category: metagenomics
description: TAXonomic Profile Aggregation and STAndardisation tool for converting and merging metagenomic profiler outputs.
tags: [taxpasta, metagenomics, taxonomic-profiling, standardisation, kraken2, motus, metaphlan]
author: oxo-call-community
source_url: "https://github.com/taxprofiler/taxpasta"
---

## Concepts

- **Tool Overview**: taxpasta (v0.7.0) - TAXonomic Profile Aggregation and STAndardisation. A Python command-line tool for standardising and merging taxonomic profiles from diverse metagenomic profiling tools into consistent tabular formats.
- **Core Functions**: Two main commands: `taxpasta standardise` converts a single profiler output to standardized format; `taxpasta merge` combines multiple profiles from the same profiler into one table.
- **Supported Profilers**: Kraken2, KrakenUniq, Bracken, MetaPhlAn, mOTUs, Centrifuge, MEGAN6/MALT, Kaiju, DIAMOND, and ganon.
- **Output Formats**: TSV, CSV, or JSON. Output contains taxonomic identifiers and abundance as integer counts in a consistent format across all profilers.
- **Installation**: `conda install -c bioconda taxpasta` or `pip install taxpasta`
- **Key Benefit**: Enables direct cross-comparison of taxonomic profiling results from different tools without custom scripting.

## Pitfalls

- **Profiler-Specific Output**: Each profiler uses different output formats (hierarchical indented text, JSON, TSV). taxpasta handles conversion but requires knowing which profiler generated the input.
- **Sample Names**: taxpasta uses sample names derived from input filenames or first column - ensure consistent naming across analyses.
- **Missing Taxa**: Some profilers report unclassified reads - taxpasta keeps these but they may affect downstream analysis.
- **Percentage vs Count**: Different profilers report abundances as percentages, fractions, or raw counts. taxpasta standardizes to counts.
- **Wide vs Long Format**: Merge output defaults to wide format (samples as columns). Use `--long` flag for long format.
- **Dependencies**: Requires pandas and numpy for data manipulation. Python 3.8+ required.

## Examples

### Standardise a Kraken2 profile
**Args:** `taxpasta standardise -p kraken2 -o standardised.tsv sample.kreport.txt`
**Explanation:** Convert a single Kraken2 report file to standardised TSV format with taxonomic IDs and counts.

### Merge multiple samples
**Args:** `taxpasta merge -p kraken2 -o merged.tsv sample1.kreport.txt sample2.kreport.txt sample3.kreport.txt`
**Explanation:** Standardise and merge multiple Kraken2 reports from different samples into a single wide-format table.

### Standardise mOTUs profile
**Args:** `taxpasta standardise -p motus -o standardised.tsv sample.motus`
**Explanation:** Convert mOTUs profiler output to standard format. Works similarly for other supported profilers.

### Add taxonomy names
**Args:** `taxpasta standardise -p kraken2 -o standardised.tsv --add-name sample.kreport.txt`
**Explanation:** Add taxonomic names alongside taxonomic IDs in the output for human readability.

### Merge in long format
**Args:** `taxpasta merge -p metaphlan -o long.tsv --long sample1.tsv sample2.tsv`
**Explanation:** Use `--long` flag to output one row per taxon instead of wide format with samples as columns.

### Cross-profiler comparison preparation
**Args:** `taxpasta standardise -p kraken2 -o kraken2_std.tsv kraken2_sample.kreport.txt && taxpasta standardise -p motus -o motus_std.tsv motus_sample.motus`
**Explanation:** Standardise outputs from different profilers separately, then compare the resulting tables side-by-side.

### Use output in pandas
**Args:** `taxpasta merge -p kraken2 -o merged.tsv *.kreport.txt && python -c "import pandas as pd; df = pd.read_csv('merged.tsv', sep='\t')"`
**Explanation:** taxpasta output is directly loadable into pandas for downstream statistical analysis or visualization.
