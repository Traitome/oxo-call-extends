---
name: allelecodes
category: utility
description: Allele Code Assignment Algorithm for cgMLST schemes used in public health genomics
tags: [allelecodes, cgMLST, allele-codes, public-health, genomics]
author: oxo-call-community
source_url: "https://github.com/ncezid-biome/AlleleCodes"
---

## Concepts

- **Tool Overview**: AlleleCodes is a Python-based tool that assigns nearest-neighbor hierarchical codes to allele profiles using cgMLST (core genome Multi-Locus Sequence Typing) schemes, specifically designed for public health genomics applications.
- **Core Function**: Uses a hierarchical method to assess nearest neighbor distances of input allele profiles against legacy profiles, assigning organism-specific codes based on predefined thresholds.
- **Input/Output**: Input: Config file with core loci names, allele profiles, data directory with legacy profiles. Output: Assigned allele codes and profile classifications.
- **Algorithm**: Uses tree-guided hierarchical comparison at organism-specific thresholds defined by input prefix.
- **Installation**: Install via bioconda: `conda install -c bioconda allelecodes`
- **License**: GPL-3.0

## Pitfalls

- **Config File Required**: Requires specific config file format denoting core loci names.
- **Data Directory**: Needs properly structured data directory with legacy profiles and tree file.
- **Python Version**: Requires Python 3.13 or higher.
- **Schema Compatibility**: Ensure cgMLST schema matches the organism being analyzed.
- **Threshold Settings**: Organism-specific thresholds must be correctly defined.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available command-line options and usage instructions.

### Basic allele code assignment
**Args:** `allelecodes --config config.ini --alleles profiles.tsv --datadir data/ --prefix ECOL`
**Explanation:** Assigns allele codes using config file, input profiles, data directory, and E. coli prefix.

### Run with verbose output
**Args:** `allelecodes --config config.ini --alleles profiles.tsv --datadir data/ --prefix SALM -v`
**Explanation:** Runs with verbose output showing detailed processing information.

### Specify output file
**Args:** `allelecodes --config config.ini --alleles profiles.tsv --datadir data/ --prefix KPNE --output results.tsv`
**Explanation:** Saves results to specified output file instead of default.

### Set custom threshold
**Args:** `allelecodes --config config.ini --alleles profiles.tsv --datadir data/ --prefix ECOL --threshold 0.95`
**Explanation:** Sets custom similarity threshold of 0.95 for allele matching.

### Process multiple profiles
**Args:** `allelecodes --config config.ini --alleles all_profiles.tsv --datadir data/ --prefix STPH`
**Explanation:** Processes multiple allele profiles from a single input file.

### Test mode
**Args:** `allelecodes --config config.ini --alleles test.tsv --datadir data/ --prefix ECOL --test`
**Explanation:** Runs in test mode for validation and debugging.

### Force recalculation
**Args:** `allelecodes --config config.ini --alleles profiles.tsv --datadir data/ --prefix ECOL --force`
**Explanation:** Forces recalculation even if cached results exist.

### Output JSON format
**Args:** `allelecodes --config config.ini --alleles profiles.tsv --datadir data/ --prefix ECOL --json`
**Explanation:** Outputs results in JSON format for programmatic processing.
