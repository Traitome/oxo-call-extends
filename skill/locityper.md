---
name: locityper
category: variant-calling
description: LociTyper - Targeted genotyper for complex polymorphic loci
tags: [locityper, variant-calling, genotyping, polymorphic-loci, WGS, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/tprodanov/locityper"
---

## Concepts

- **Targeted Genotyping**: Targeted genotyping of specific loci
- **Complex Polymorphisms**: Handles complex polymorphic loci
- **Short Reads**: Supports short-read sequencing data
- **Long Reads**: Supports long-read sequencing data
- **WGS Data**: Whole-genome sequencing data analysis
- **Allele Calling**: Accurate allele calling

## Pitfalls

- **Locus Complexity**: Highly complex loci may cause issues
- **Read Quality**: Poor quality reads affect genotyping
- **Mapping Quality**: Requires accurate read mapping
- **Parameter Tuning**: Requires careful parameter optimization
- **Memory Usage**: Memory-intensive for large datasets
- **False Positives**: May produce false positive calls

## Examples

### Genotype loci
**Args:** `locityper -i input.bam -r reference.fasta -o genotypes.vcf`
**Explanation:** Genotypes complex polymorphic loci.

### Targeted regions
**Args:** `locityper -i input.bam -r reference.fasta -o genotypes.vcf -t targets.bed`
**Explanation:** Genotypes specific target regions.

### Long-read mode
**Args:** `locityper -i input.bam -r reference.fasta -o genotypes.vcf -l`
**Explanation:** Optimized for long-read sequencing data.

### Threads
**Args:** `locityper -i input.bam -r reference.fasta -o genotypes.vcf -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `locityper -i input.bam -r reference.fasta -o genotypes.vcf -q 30`
**Explanation:** Filters by minimum quality score.

### Output statistics
**Args:** `locityper -i input.bam -r reference.fasta -o genotypes.vcf -s`
**Explanation:** Outputs genotyping statistics.