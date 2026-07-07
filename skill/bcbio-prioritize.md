---
name: bcbio-prioritize
category: variant-calling
description: bcbio-prioritize - Prioritize variants based on biological relevance and functional impact
tags: [bcbio-prioritize, variant-calling, variant-prioritization, functional-annotation]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio.prioritize"
---

## Concepts

- **Tool Overview**: bcbio-prioritize (v0.0.8) prioritizes small variants, structural variants, and coverage data based on biological inputs and functional impact.
- **Core Function**: Ranks variants by their biological relevance, functional impact, and clinical significance.
- **Multi-omics Integration**: Combines variant data with gene expression, conservation, and functional annotation.
- **Prioritization Criteria**: Uses multiple criteria including population frequency, pathogenicity scores, and gene-phenotype associations.
- **Clinical Relevance**: Identifies variants with potential clinical significance.
- **Input/Output**: Accepts VCF files and annotation data; outputs prioritized variant lists.
- **Installation**: `conda install -c bioconda bcbio-prioritize`.

## Pitfalls

- **Annotation Data**: Requires comprehensive annotation databases for effective prioritization.
- **Score Thresholds**: Default thresholds may need adjustment for specific use cases.
- **Variant Quality**: Low-quality variants should be filtered before prioritization.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic prioritization
**Args:** `bcbio_prioritize.py variants.vcf -o prioritized.txt`
**Explanation:** Prioritizes variants based on default criteria.

### With gene list
**Args:** `bcbio_prioritize.py variants.vcf -g candidate_genes.txt -o prioritized.txt`
**Explanation:** Prioritizes variants within specified candidate genes.

### Include functional scores
**Args:** `bcbio_prioritize.py variants.vcf -s dbnsfp -o prioritized.txt`
**Explanation:** Uses dbNSFP functional scores for prioritization.

### Clinical filtering
**Args:** `bcbio_prioritize.py variants.vcf --clinical -o prioritized.txt`
**Explanation:** Applies clinical relevance filters.

### Population frequency filter
**Args:** `bcbio_prioritize.py variants.vcf --max-af 0.01 -o prioritized.txt`
**Explanation:** Filters out common variants (AF > 1%).

### Output VCF with scores
**Args:** `bcbio_prioritize.py variants.vcf -o prioritized.vcf --vcf-output`
**Explanation:** Outputs VCF with prioritization scores added.

### Display help
**Args:** `bcbio_prioritize.py --help`
**Explanation:** Shows all available command-line options and usage information.