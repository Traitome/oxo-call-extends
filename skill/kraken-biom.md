---
name: kraken-biom
category: metagenomics
description: Convert Kraken output to BIOM-format tables for ecosystem analysis
tags: [kraken-biom, metagenomics, BIOM, Kraken, format-conversion]
author: oxo-call-community
source_url: "https://github.com/smdabdoub/kraken-biom"
---

## Concepts

- **Format Conversion**: Converts Kraken output to BIOM format
- **BIOM Support**: Creates BIOM tables for ecosystem analysis
- **Taxonomic Profiles**: Generates taxonomic abundance profiles
- **Sample Integration**: Combines multiple samples into single table
- **Diversity Analysis**: Supports downstream diversity analyses
- **Cross-platform**: Works with various bioinformatics platforms

## Pitfalls

- **Kraken Output**: Requires correct Kraken output format
- **Sample Consistency**: Samples must have consistent taxonomy
- **Missing Taxa**: Samples with no reads for certain taxa
- **Normalization**: May require additional normalization steps
- **BIOM Version**: Different BIOM versions have different compatibility
- **Rank Selection**: Choosing taxonomic rank affects table structure

## Examples

### Convert to BIOM
**Args:** `kraken-biom results.kraken -o table.biom`
**Explanation:** Converts Kraken output to BIOM format.

### Include all ranks
**Args:** `kraken-biom results.kraken --all-ranks -o table.biom`
**Explanation:** Includes all taxonomic ranks in BIOM table.

### Batch conversion
**Args:** `kraken-biom --batch results_dir/ -o combined.biom`
**Explanation:** Converts multiple Kraken files to single BIOM.

### Add sample metadata
**Args:** `kraken-biom results.kraken --meta metadata.txt -o table.biom`
**Explanation:** Includes sample metadata in BIOM table.

### Filter by confidence
**Args:** `kraken-biom results.kraken --min-confidence 0.1 -o filtered.biom`
**Explanation:** Filters by minimum confidence score.

### Export as TSV
**Args:** `kraken-biom results.kraken -o table.tsv --tsv`
**Explanation:** Exports BIOM table as TSV format.