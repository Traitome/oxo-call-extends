---
name: collect_mgf
category: utility
description: Collects MGF files from XMass experiments into a single file
tags: [collect_mgf, mass-spectrometry, proteomics, mgf, bioinformatics]
author: oxo-call-community
source_url: "http://www.ms-utils.org/collect_mgf.c"
---

## Concepts

- **Tool Overview**: collect_mgf is a utility for collecting Mascot Generic Format (MGF) files and data-dependent results from XMass experiments into a single consolidated MGF file for downstream analysis.
- **Core Function**: Aggregates multiple MGF files from mass spectrometry experiments into one file for easier processing.
- **Algorithm**: Parses and merges MGF files while maintaining spectrum metadata and peak lists.
- **Input**: Multiple MGF files from XMass or similar mass spectrometry experiments.
- **Output**: Single consolidated MGF file with all spectra.
- **Application**: Proteomics data processing, mass spectrometry analysis, and database searching.
- **Installation**: Install via bioconda: `conda install -c bioconda collect_mgf`

## Pitfalls

- **File Format**: Requires properly formatted MGF files.
- **Metadata Preservation**: May lose some experiment-specific metadata during merging.
- **Duplicate Spectra**: Does not automatically remove duplicate spectra.
- **File Size**: Combined file may be very large for high-throughput experiments.
- **Encoding**: May have issues with non-standard character encodings.

## Examples

### Collect MGF files from directory
**Args:** `collect_mgf -i experiment_dir/ -o combined.mgf`
**Explanation:** Collects all MGF files from directory into single output file.

### With pattern matching
**Args:** `collect_mgf -i *.mgf -o combined.mgf`
**Explanation:** Collects all MGF files matching pattern.

### Include dd_results
**Args:** `collect_mgf -i experiment_dir/ -d dd_results/ -o combined.mgf`
**Explanation:** Includes data-dependent results in collection.

### Display help
**Args:** `collect_mgf --help`
**Explanation:** Shows all available options and usage information.