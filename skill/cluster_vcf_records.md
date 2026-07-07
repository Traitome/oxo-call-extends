---
name: cluster_vcf_records
category: formatting
description: Package to cluster VCF records, used by gramtools and minos
tags: [cluster_vcf_records, vcf, variant-clustering, bioinformatics, genetics]
author: oxo-call-community
source_url: "https://github.com/iqbal-lab-org/cluster_vcf_records"
---

## Concepts

- **Tool Overview**: cluster_vcf_records is a Python package for clustering VCF (Variant Call Format) records based on their genomic positions and relationships.
- **Core Function**: Groups overlapping or related VCF records into clusters for downstream analysis.
- **Algorithm**: Uses positional and variant relationship criteria to cluster VCF records.
- **Input**: VCF file containing variant calls.
- **Output**: Clustered VCF records with group identifiers.
- **Application**: Variant analysis, population genetics, and as a dependency for gramtools and minos.
- **Installation**: Install via bioconda: `conda install -c bioconda cluster_vcf_records`

## Pitfalls

- **VCF Format**: Requires properly formatted VCF files.
- **Memory Usage**: May require significant memory for large VCF files.
- **Overlap Criteria**: Clustering depends on overlap definition parameters.
- **Dependency**: Primarily designed as a dependency for other tools.
- **Parameter Tuning**: May require adjustment of clustering thresholds.

## Examples

### Cluster VCF records
**Args:** `cluster_vcf_records -i variants.vcf -o clustered.vcf`
**Explanation:** Clusters overlapping VCF records.

### With custom distance
**Args:** `cluster_vcf_records -i variants.vcf -o clustered.vcf -d 100`
**Explanation:** Sets maximum distance between variants in same cluster to 100bp.

### Output cluster information
**Args:** `cluster_vcf_records -i variants.vcf -o clustered.vcf --print-clusters`
**Explanation:** Outputs cluster membership information.

### Display help
**Args:** `cluster_vcf_records --help`
**Explanation:** Shows all available options and usage information.