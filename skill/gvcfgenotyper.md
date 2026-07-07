---
name: gvcfgenotyper
category: bioinformatics
description: gvcfgenotyper merges and genotypes Illumina-style GVCFs, enabling variant calling across multiple samples.
tags: [gvcfgenotyper, variant-calling, GVCF, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Illumina/gvcfgenotyper"
---

## Concepts

- **GVCF Merging**: gvcfgenotyper merges multiple GVCF files into a single callset.

- **Genotyping**: Performs joint genotyping across multiple samples.

- **Illumina Format**: Optimized for Illumina-style GVCF format.

- **Variant Calling**: Identifies genetic variants from sequencing data.

- **Quality Filtering**: Filters variants based on quality metrics.

- **Efficiency**: Optimized for processing large datasets efficiently.

## Pitfalls

- **Format Compatibility**: Requires Illumina-style GVCF format.

- **Memory Usage**: Processing many samples may require significant memory.

- **Reference Genome**: Ensure all GVCFs use the same reference genome.

- **Variant Quality**: Low-quality variants may affect downstream analysis.

- **Sample Heterogeneity**: Mixed sample types may require careful handling.

## Examples

### Merge and genotype GVCFs
**Args:** `gvcfgenotyper -i sample1.g.vcf sample2.g.vcf -o merged.vcf`
**Explanation:** Merges multiple GVCFs and performs joint genotyping.

### With reference genome
**Args:** `gvcfgenotyper -i samples.g.vcf -r reference.fasta -o merged.vcf`
**Explanation:** Uses reference genome for improved genotyping.

### Filter by quality
**Args:** `gvcfgenotyper -i samples.g.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters variants by quality score threshold.

### Batch processing
**Args:** `gvcfgenotyper -i *.g.vcf -o merged.vcf`
**Explanation:** Processes all GVCF files in the current directory.

### Generate statistics
**Args:** `gvcfgenotyper -i samples.g.vcf -s -o stats.txt`
**Explanation:** Generates variant calling statistics.

### Compressed output
**Args:** `gvcfgenotyper -i samples.g.vcf -o merged.vcf.gz`
**Explanation:** Outputs compressed VCF file.

### Help command
**Args:** `gvcfgenotyper --help`
**Explanation:** Shows available options and usage information.