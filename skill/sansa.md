---
name: sansa
category: variant-calling
description: Structural variant annotation, duplicate removal and comparison
tags: ["sansa", "variant-calling", "SV", "structural-variants"]
author: oxo-call-community
source_url: "https://github.com/dellytools/sansa"
---

## Concepts

- **Tool Overview**: Sansa (v0.2.5) is a structural variant annotation tool from the Delly suite, enabling SV annotation, duplicate marking, and VCF comparison.
- **Core Function**: Annotates structural variants with population frequency data, gene information, and functional consequences.
- **Algorithm**: Matches SVs based on breakpoint proximity and size ratio, supporting precise variant comparison across samples.
- **Annotation Sources**: Integrates gnomAD-SV, 1000 Genomes, and custom annotation databases for population frequency information.
- **Gene Annotation**: Uses GTF/GFF files to identify genes affected by structural variants with distance-based mapping.
- **Output**: Generates annotated BCF files and TSV reports for downstream analysis and visualization.

## Pitfalls

- **Database Compatibility**: Requires matching genome build between input VCF and annotation databases.
- **Breakpoint Sensitivity**: Default 50bp breakpoint tolerance may miss true matches for imprecise calls.
- **Memory Usage**: Processing large multi-sample VCFs requires substantial memory resources.
- **SV Type Restrictions**: By default only compares SVs within the same type (DEL-DEL, INV-INV).
- **Performance**: Complex annotation operations can be slow on large datasets.
- **File Format**: Requires indexed VCF/BCF files for efficient processing.

## Examples

### Basic SV annotation
**Args:** `sansa annotate -d gnomad_v2.1_sv.sites.vcf.gz input.vcf.gz`
**Explanation:** Annotates input SVs using gnomAD-SV database, generating `anno.bcf` and `query.tsv.gz`.

### Custom breakpoint tolerance
**Args:** `sansa annotate -b 100 -r 0.9 -d db.vcf.gz input.vcf.gz`
**Explanation:** `-b 100` sets 100bp breakpoint tolerance; `-r 0.9` requires 90% size similarity between SVs.

### Gene annotation
**Args:** `sansa annotate -g Homo_sapiens.GRCh37.87.gtf.gz input.vcf.gz`
**Explanation:** Annotates SVs with nearby genes using Ensembl GTF annotation file.

### Combined annotation
**Args:** `sansa annotate -g genes.gtf.gz -d population.sv.vcf.gz input.vcf.gz`
**Explanation:** Performs both gene and population frequency annotation in a single run.

### Mark duplicate SVs
**Args:** `sansa markdup multi_sample.vcf.gz`
**Explanation:** Identifies and marks duplicate SV sites in multi-sample VCF files.

### Compare VCF files
**Args:** `sansa compvcf -b 50 sample1.vcf.gz sample2.vcf.gz`
**Explanation:** Compares SVs between two VCF files with 50bp breakpoint tolerance.

### Include unmatched SVs
**Args:** `sansa annotate -m -d db.vcf.gz input.vcf.gz`
**Explanation:** `-m` includes query SVs without database matches in the output.