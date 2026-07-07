---
name: bcbio-variation-recall
category: variant-calling
description: bcbio-variation-recall - Parallel merging, squaring off and ensemble calling for genomic variants
tags: [bcbio-variation-recall, variant-calling, ensemble-calling, variant-merging]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio.variation.recall"
---

## Concepts

- **Tool Overview**: bcbio-variation-recall (v0.2.6) provides parallel merging, squaring off, and ensemble calling for genomic variants, enabling robust variant detection across multiple callers.
- **Core Function**: Merges variants from multiple callers, performs squaring off (genotyping all samples at all sites), and creates ensemble calls for improved accuracy.
- **Parallel Processing**: Uses parallel computing for efficient processing of large datasets.
- **Ensemble Calling**: Combines results from multiple variant callers for higher confidence calls.
- **Variant Merging**: Merges VCF files from different callers while maintaining genotype consistency.
- **Input/Output**: Accepts multiple VCF files; outputs merged and ensemble-called VCF files.
- **Installation**: `conda install -c bioconda bcbio-variation-recall`.

## Pitfalls

- **Multiple Callers**: Requires output from multiple variant callers for ensemble calling.
- **Genotype Consistency**: Ensuring consistent genotyping across samples requires careful configuration.
- **Resource Requirements**: Parallel processing requires sufficient CPU cores and memory.
- **VCF Compatibility**: Input VCFs must be compatible and properly formatted.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Merge multiple VCF files
**Args:** `bcbio_variation_recall merge -i caller1.vcf caller2.vcf caller3.vcf -o merged.vcf`
**Explanation:** Merges VCF files from multiple variant callers.

### Ensemble calling
**Args:** `bcbio_variation_recall ensemble -i caller1.vcf caller2.vcf -o ensemble.vcf`
**Explanation:** Creates ensemble calls combining multiple caller results.

### Square off genotypes
**Args:** `bcbio_variation_recall square -i merged.vcf -o squared.vcf`
**Explanation:** Ensures all samples are genotyped at all variant sites.

### Parallel processing
**Args:** `bcbio_variation_recall merge -i *.vcf -o merged.vcf -n 16`
**Explanation:** Uses 16 threads for parallel merging.

### Quality filtering
**Args:** `bcbio_variation_recall filter -i variants.vcf -o filtered.vcf -q 20`
**Explanation:** Filters variants below quality threshold.

### Combine with recalibration
**Args:** `bcbio_variation_recall ensemble -i *.vcf -r reference.fasta -o ensemble.vcf`
**Explanation:** Performs ensemble calling with reference-based recalibration.

### Display help
**Args:** `bcbio_variation_recall --help`
**Explanation:** Shows all available command-line options and usage information.