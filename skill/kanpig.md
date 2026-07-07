---
name: kanpig
category: variant-calling
description: A fast tool for genotyping structural variants with long-read sequencing data.
tags: [kanpig, variant-calling, structural variants, long-reads, SV]
author: oxo-call-community
source_url: "https://github.com/ACEnglish/kanpig/wiki"
---

## Concepts

- **Tool Overview**: kanpig (v2.0.2) - Genotypes structural variants using long-read sequencing data.
- **Long-Read Support**: Optimized for long-read sequencing technologies.
- **SV Genotyping**: Genotypes deletions, insertions, inversions, and translocations.
- **Speed**: Fast processing of large structural variant datasets.
- **Accuracy**: High accuracy for complex structural variants.
- **VCF Integration**: Works with standard VCF format for variants.

## Pitfalls

- **Read Quality**: Requires high-quality long reads.
- **SV Callset**: Requires input SV callset for genotyping.
- **Reference Genome**: Needs complete reference genome.
- **Memory Usage**: Large datasets require significant memory.
- **Complex SVs**: Very complex SVs may not be genotyped correctly.
- **Alignment Quality**: Depends on quality of read alignments.

## Examples

### Genotype SVs
**Args:** `kanpig genotype -i variants.vcf -b alignments.bam -o genotyped.vcf`
**Explanation:** Genotypes structural variants from VCF using BAM.

### Specify reference
**Args:** `kanpig genotype -i variants.vcf -b alignments.bam -r ref.fasta -o genotyped.vcf`
**Explanation:** Uses specified reference genome for genotyping.

### Filter by quality
**Args:** `kanpig genotype -i variants.vcf -b alignments.bam -o genotyped.vcf -q 20`
**Explanation:** Filters variants by quality score >= 20.

### Verbose mode
**Args:** `kanpig genotype -i variants.vcf -b alignments.bam -o genotyped.vcf -v`
**Explanation:** Shows verbose output during processing.

### Batch processing
**Args:** `kanpig batch -i samples.txt -o output/`
**Explanation:** Processes multiple samples in batch mode.

### Generate report
**Args:** `kanpig report -i genotyped.vcf -o report.html`
**Explanation:** Generates HTML report of genotyping results.