---
name: mach2
category: utility
description: Migration Analysis of Clonal Histories 2
tags: [mach2, utility, cancer, clonal-evolution]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/mach2"
---

## Concepts

- **Tool Overview**: mach2 v1.0.2 analyzes migration patterns in clonal evolution from cancer sequencing data.
- **Core Function**: Infers the migration history of cancer clones across multiple tumor samples.
- **Phylogenetic Model**: Uses tree-based approaches to reconstruct clonal migration paths.
- **Input/Output**: Input: Variant allele frequencies from multiple samples; Output: Migration trees and patterns.
- **Installation**: `conda install -c bioconda mach2`
- **Key Features**: Handles multiple samples, infers migration direction, visualizes clonal relationships.

## Pitfalls

- **Data Requirements**: Requires data from multiple spatially separated samples.
- **Sample Quality**: Poor-quality sequencing data can affect inference accuracy.
- **Computational Complexity**: Can be computationally intensive for many samples.
- **Memory Usage**: May require significant memory for large datasets.
- **Model Assumptions**: Relies on assumptions about clonal evolution.
- **Interpretation**: Results require careful interpretation by domain experts.

## Examples

### Infer migration history
**Args:** `mach2 -i vaf_data.txt -o migration_results/`
**Explanation:** Infers clonal migration history from VAF data.

### With tree constraints
**Args:** `mach2 -i vaf_data.txt -c constraints.txt -o migration_results/`
**Explanation:** Uses constraints to guide migration inference.

### Threads
**Args:** `mach2 -i vaf_data.txt -t 8 -o migration_results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `mach2 -i vaf_data.txt -f json -o migration_results.json`
**Explanation:** Outputs results in JSON format.

### Visualization
**Args:** `mach2 -i vaf_data.txt -v -o migration_results/`
**Explanation:** Generates visualization of migration patterns.

### Help documentation
**Args:** `mach2 --help`
**Explanation:** Displays all available options and parameters.