---
name: gsmap
category: bioinformatics
description: gsMap performs genetically informed spatial mapping of cells for complex traits analysis in spatial transcriptomics.
tags: [gsmap, spatial-transcriptomics, genetics, bioinformatics]
author: oxo-call-community
source_url: "https://yanglab.westlake.edu.cn/gsmap/document"
---

## Concepts

- **Spatial Mapping**: gsMap maps genetic information to spatial coordinates.

- **Cell Mapping**: Maps individual cells based on genetic information.

- **Complex Traits**: Analyzes complex traits in spatial context.

- **Integration**: Integrates genetic and spatial transcriptomics data.

- **Visualization**: Generates spatial visualizations of genetic data.

- **Statistical Analysis**: Performs statistical analysis of spatial patterns.

## Pitfalls

- **Data Quality**: Results depend on the quality of input data.

- **Spatial Resolution**: Spatial resolution affects mapping accuracy.

- **Computational Resources**: Processing large datasets may require significant resources.

- **Parameter Tuning**: Adjust parameters based on data characteristics.

- **Result Interpretation**: Interpret spatial patterns carefully.

## Examples

### Run spatial mapping
**Args:** `gsmap -i spatial_data.h5ad -g genotypes.vcf -o results/`
**Explanation:** Performs genetically informed spatial mapping.

### Include phenotype data
**Args:** `gsmap -i spatial_data.h5ad -g genotypes.vcf -p phenotypes.txt -o results/`
**Explanation:** Integrates phenotype data into analysis.

### Adjust resolution
**Args:** `gsmap -i spatial_data.h5ad -g genotypes.vcf -r 100 -o results/`
**Explanation:** Sets spatial resolution for mapping.

### Generate visualization
**Args:** `gsmap -i spatial_data.h5ad -g genotypes.vcf -p -o plot.png`
**Explanation:** Generates spatial visualization.

### Batch processing
**Args:** `gsmap batch -d samples/ -o results/`
**Explanation:** Processes multiple spatial transcriptomics samples.

### Statistical analysis
**Args:** `gsmap stats -i results/ -o stats.txt`
**Explanation:** Generates statistical summary of results.

### Help command
**Args:** `gsmap --help`
**Explanation:** Shows available options and usage information.