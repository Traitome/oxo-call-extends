---
name: cadd-scripts
category: annotation
description: CADD scripts for offline scoring of genetic variants
tags: [cadd, variant, annotation, scoring, pathogenicity]
author: oxo-call-community
source_url: "https://github.com/kircherlab/CADD-scripts"
---

## Concepts

- **Tool Overview**: CADD (Combined Annotation Dependent Depletion) scores variants for predicted deleteriousness.
- **Core Function**: Computes CADD scores for SNVs and small indels without web service.
- **Input**: VCF file with variants to score.
- **Output**: CADD scores (scaled and raw) for each variant.
- **Model**: Ensemble of annotations including conservation, functional impact, and regulatory features.
- **Installation**: Install via bioconda: `conda install -c bioconda cadd-scripts`

## Pitfalls

- **Model Files**: Requires downloading large pre-trained model files.
- **Memory Usage**: Scoring requires significant memory for model loading.
- **Reference Genome**: Must use GRCh37 or GRCh38 matching the variant coordinates.
- **Indel Support**: Limited support for complex indels.

## Examples

### Score variants
**Args:** `cadd.sh -g GRCh38 -o scored.vcf variants.vcf`
**Explanation:** Computes CADD scores for variants using GRCh38 reference.

### Score with scaled output
**Args:** `cadd.sh -g GRCh38 -s -o scaled_scores.tsv variants.vcf`
**Explanation:** Outputs scaled CADD scores (higher = more deleterious).

### Install model files
**Args:** `cadd-install.sh -g GRCh38 -d /path/to/models/`
**Explanation:** Downloads required model files for offline scoring.

### Score specific regions
**Args:** `cadd.sh -g GRCh38 -r chr1:1000000-2000000 variants.vcf`
**Explanation:** Scores variants in specified genomic region.

### Display help
**Args:** `cadd.sh --help`
**Explanation:** Shows all available options and usage information.
