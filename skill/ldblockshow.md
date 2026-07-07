---
name: ldblockshow
category: visualization
description: Linkage disequilibrium heatmap visualization from VCF files
tags: [ldblockshow, visualization, linkage-disequilibrium, VCF, population-genomics]
author: oxo-call-community
source_url: "https://github.com/BGI-shenzhen/LDBlockShow"
---

## Concepts

- **LD Visualization**: Creates linkage disequilibrium heatmaps
- **VCF Support**: Reads variant data directly from VCF files
- **Population Analysis**: Analyzes linkage disequilibrium in populations
- **Haplotype Blocks**: Identifies haplotype blocks in genome
- **Heatmap Display**: Visualizes LD values as heatmaps
- **Genomic Regions**: Supports specific genomic region analysis

## Pitfalls

- **Sample Size**: Small sample sizes give unreliable LD estimates
- **Population Structure**: Hidden population structure affects LD
- **Variant Density**: Very high variant density hard to visualize
- **Missing Data**: Missing genotypes affect LD calculation
- **Recombination Hotspots**: May distort LD patterns
- **Memory Usage**: Large VCF files require significant memory

## Examples

### Generate LD heatmap
**Args:** `LDBlockShow -InVCF variants.vcf -OutPng output.png`
**Explanation:** Creates LD heatmap from VCF file.

### Specify chromosome
**Args:** `LDBlockShow -InVCF variants.vcf -Chr 1 -OutPng output.png`
**Explanation:** Analyzes chromosome 1 only.

### Set region
**Args:** `LDBlockShow -InVCF variants.vcf -Start 1000000 -End 2000000 -OutPng output.png`
**Explanation:** Analyzes specific genomic region.

### Calculate D prime
**Args:** `LDBlockShow -InVCF variants.vcf -Type D -OutPng output.png`
**Explanation:** Uses D' statistic for LD calculation.

### Calculate r squared
**Args:** `LDBlockShow -InVCF variants.vcf -Type R2 -OutPng output.png`
**Explanation:** Uses r² statistic for LD calculation.

### Export table
**Args:** `LDBlockShow -InVCF variants.vcf -OutText ld_values.txt`
**Explanation:** Exports LD values to text file.