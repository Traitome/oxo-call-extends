---
name: ensembl-vep
category: annotation
description: "Ensembl Variant Effect Predictor"
tags: [ensembl-vep, annotation, variant-annotation, VCF, Ensembl]
author: oxo-call-community
source_url: "https://useast.ensembl.org/info/docs/tools/vep/script/vep_tutorial.html"
---

## Concepts

- **Tool Overview**: The Ensembl Variant Effect Predictor (VEP) is a comprehensive tool for predicting the functional effects of genetic variants (SNPs, insertions, deletions, CNVs, structural variants) on genes, transcripts, and regulatory regions.
- **Core Function**: Annotates variants with information about their impact on gene function, protein sequence, and regulatory elements.
- **Input/Output**: Input: VCF files (variants), genome assembly. Output: Annotated VCF, HTML/JSON reports, variant effect summaries.
- **Algorithm**: Uses Ensembl's comprehensive annotation database to map variants to genes, transcripts, and regulatory features, predicting their functional consequences.
- **Key Features**: Comprehensive variant annotation, support for multiple species, regulatory region analysis, custom annotation support, batch processing, API integration.
- **Installation**: `conda install -c bioconda ensembl-vep`

## Pitfalls

- **Database Version**: Must use matching genome assembly and annotation version.
- **Memory Usage**: Large VCF files require significant memory.
- **Cache Management**: Proper cache setup is critical for performance.
- **Custom Annotations**: Custom annotation files require specific formats.
- **Regulatory Features**: Regulatory annotation may not be available for all species.

## Examples

### Basic variant annotation
**Args:** `vep -i input.vcf -o annotated.vcf --cache`
**Explanation:** Annotates variants using cached Ensembl data.

### With custom database
**Args:** `vep -i input.vcf -o annotated.vcf --custom custom_annotations.vcf,Custom,vcf,exact`
**Explanation:** Adds custom annotations to variant calls.

### Output JSON format
**Args:** `vep -i input.vcf -o annotated.json --json`
**Explanation:** Outputs annotations in JSON format.

### Include regulatory effects
**Args:** `vep -i input.vcf -o annotated.vcf --regulatory`
**Explanation:** Includes regulatory region annotations.

### Batch mode
**Args:** `vep -i input.vcf -o annotated.vcf --fork 8`
**Explanation:** Uses 8 parallel threads for faster processing.