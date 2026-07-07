---
name: strvctvre
category: variant-calling
description: StrVCTVRE, a structural variant classifier for exonic deletions and duplications.
tags: [strvctvre, structural-variants, exonic-variants, variant-classification]
author: oxo-call-community
source_url: "https://github.com/andrewSharo/StrVCTVRE/tree/master"
---

## Concepts

- **Tool Overview**: strvctvre (v1.10) is a structural variant classifier for exonic deletions and duplications.
- **Core Function**: Classifies structural variants affecting exonic regions.
- **Algorithm**: Uses variant characteristics to classify deletions and duplications.
- **Input/Output**: Input: VCF file with structural variants; Output: Classified variants with impact scores.
- **Applications**: Variant classification, clinical genomics, structural variant analysis.
- **Installation**: `conda install -c bioconda strvctvre` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific VCF format with structural variants.
- **Variant Quality**: Poor quality variants affect classification.
- **Reference Dependence**: Requires high-quality reference genome.
- **Memory Requirements**: Large VCF files require significant memory.
- **Computational Time**: Classification of large datasets can be slow.
- **Interpretation**: Requires clinical expertise for variant interpretation.

## Examples

### Display help
**Args:** `strvctvre --help`
**Explanation:** Shows available options and usage information.

### Basic variant classification
**Args:** `strvctvre -i variants.vcf -o classified.txt`
**Explanation:** Classify structural variants from VCF.

### With reference genome
**Args:** `strvctvre -i variants.vcf -r reference.fasta -o classified.txt`
**Explanation:** Use reference genome for better classification.

### Verbose mode
**Args:** `strvctvre -i variants.vcf -o classified.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output VCF
**Args:** `strvctvre -i variants.vcf -o classified.vcf --vcf`
**Explanation:** Output results in VCF format.

### Batch processing
**Args:** `strvctvre -i batch/ -o results/`
**Explanation:** Process multiple VCF files together.

### Filter by quality
**Args:** `strvctvre -i variants.vcf -o classified.txt -q 20`
**Explanation:** Filter variants by quality score.

### Include impact scores
**Args:** `strvctvre -i variants.vcf -o classified.txt --impact`
**Explanation:** Include impact scores in output.

### Generate report
**Args:** `strvctvre -i variants.vcf -o classified.txt --report`
**Explanation:** Generate comprehensive HTML report.
