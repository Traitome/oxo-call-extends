---
name: mobidic-mpa
category: utility
description: "MPA: MoBiDiC Prioritization Algorithm"
tags: [mobidic-mpa, utility, prioritization]
author: oxo-call-community
source_url: "https://neuro-2.iurc.montp.inserm.fr/mpaweb/"
---
## Concepts

- **Tool Overview**: MoBiDiC-MPA v1.3.0 prioritizes candidate genes.
- **Core Function**: Prioritizes disease-related genes using multi-omics data.
- **Multi-omics Integration**: Combines genomic, transcriptomic, and epigenomic data.
- **Network Analysis**: Uses protein-protein interaction networks.
- **Input/Output**: Accepts variant lists; outputs prioritized genes.
- **Disease Genetics**: Supports disease gene identification.

## Pitfalls

- **Disease Specific**: Optimized for specific disease types.
- **Memory Requirements**: Memory usage depends on network size.
- **Parameter Tuning**: May require parameter adjustment for optimal prioritization.
- **Data Quality**: Results depend on input data quality.
- **Reference Databases**: Requires up-to-date reference databases.
- **Computational Resources**: Network analysis may require significant resources.

## Examples

### Prioritize genes
**Args:** `mobidic-mpa -i variants.vcf -o prioritized_genes.txt`
**Explanation:** Prioritizes candidate genes from variants.

### With custom network
**Args:** `mobidic-mpa -i variants.vcf -n network.txt -o prioritized_genes.txt`
**Explanation:** Uses custom interaction network.

### Verbose output
**Args:** `mobidic-mpa -i variants.vcf -v -o prioritized_genes.txt`
**Explanation:** Shows detailed prioritization scores.

### Filter by score
**Args:** `mobidic-mpa -i variants.vcf -t 0.8 -o prioritized_genes.txt`
**Explanation:** Filters results by priority score threshold.

### Batch processing
**Args:** `mobidic-mpa -i vcf/ -o results/`
**Explanation:** Processes multiple VCF files.