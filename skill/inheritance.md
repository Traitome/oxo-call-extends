---
name: inheritance
category: genetics
description: Inheritance models for Mendelian diseases analysis
tags: [inheritance, mendelian, genetics, variant-analysis]
author: oxo-call-community
source_url: "https://github.com/brentp/inheritance"
---

## Concepts

- **Tool Overview**: inheritance (v0.1.5) is a Python library for modeling inheritance patterns in Mendelian disease analysis.
- **Core Function**: Provides tools for analyzing genetic variants and determining inheritance patterns (autosomal dominant, recessive, X-linked).
- **Input/Output**: Accepts VCF files with variant calls and pedigree information. Outputs inheritance pattern predictions and candidate variants.
- **Features**: Supports multiple inheritance models, variant filtering, and prioritization based on inheritance patterns.
- **Applications**: Identifying causative variants in familial genetic disorders.

## Pitfalls

- **Pedigree Quality**: Results depend on accurate pedigree information.
- **Variant Quality**: Low-quality variants may produce misleading inheritance patterns.
- **De Novo Mutations**: May miss de novo mutations not present in parents.
- **Compound Heterozygotes**: Complex inheritance scenarios may require manual review.
- **Incomplete Penetrance**: Reduced penetrance can complicate inheritance pattern detection.

## Examples

### Analyze VCF for autosomal recessive variants
**Args:** `inheritance analyze -v variants.vcf -p pedigree.ped -m recessive -o results.tsv`
**Explanation:** Identifies variants consistent with autosomal recessive inheritance.

### Check dominant inheritance
**Args:** `inheritance analyze -v variants.vcf -p pedigree.ped -m dominant -o dominant_results.tsv`
**Explanation:** Identifies variants consistent with autosomal dominant inheritance.

### X-linked inheritance
**Args:** `inheritance analyze -v variants.vcf -p pedigree.ped -m x-linked -o xlinked_results.tsv`
**Explanation:** Identifies variants consistent with X-linked inheritance patterns.

### De novo variant detection
**Args:** `inheritance denovo -v variants.vcf -p pedigree.ped -o denovo.tsv`
**Explanation:** Identifies potential de novo mutations not present in parents.

### Prioritize candidate genes
**Args:** `inheritance prioritize -v variants.vcf -p pedigree.ped -g candidate_genes.txt -o prioritized.tsv`
**Explanation:** Prioritizes variants in candidate gene list based on inheritance.

### Filter by variant quality
**Args:** `inheritance analyze -v variants.vcf -p pedigree.ped -m recessive -q 30 -o high_quality.tsv`
**Explanation:** Filters variants with quality score ≥ 30 before inheritance analysis.