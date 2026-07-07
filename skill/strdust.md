---
name: strdust
category: variant-calling
description: Tandem repeat genotyper for long reads.
tags: [strdust, str-genotyping, long-reads, variant-calling]
author: oxo-call-community
source_url: "https://github.com/wdecoster/STRdust/blob/v0.16.0/README.md"
---

## Concepts

- **Tool Overview**: strdust (v0.16.0) is a tool for genotyping tandem repeats from long-read sequencing data.
- **Core Function**: Identifies and genotypes STR variations using long reads.
- **Algorithm**: Uses alignment and pattern matching to detect and genotype STRs.
- **Input/Output**: Input: Long-read BAM file, reference genome; Output: STR genotypes with repeat counts.
- **Applications**: Genetic disease diagnosis, population genetics, STR analysis.
- **Installation**: `conda install -c bioconda strdust` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect genotyping accuracy.
- **Repeat Complexity**: Complex repeat patterns are hard to genotype.
- **Alignment Quality**: Poor alignment produces incorrect calls.
- **Repeat Length**: Very long repeats may be miscalled.
- **Reference Bias**: Reference genome may not contain all known alleles.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `strdust --help`
**Explanation:** Shows available options and usage information.

### Basic STR genotyping
**Args:** `strdust -i reads.bam -r reference.fasta -o results.vcf`
**Explanation:** Genotype STRs from long-read alignment.

### With STR bed file
**Args:** `strdust -i reads.bam -r reference.fasta -s strs.bed -o results.vcf`
**Explanation:** Use custom STR coordinates for targeted genotyping.

### Verbose mode
**Args:** `strdust -i reads.bam -r reference.fasta -o results.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `strdust -i reads.bam -r reference.fasta -o results.vcf --stats`
**Explanation:** Generate statistics about STR calls.

### Custom thresholds
**Args:** `strdust -i reads.bam -r reference.fasta -o results.vcf -q 20`
**Explanation:** Minimum mapping quality threshold of 20.

### Batch processing
**Args:** `strdust -i batch/ -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by coverage
**Args:** `strdust -i reads.bam -r reference.fasta -o results.vcf -m 5`
**Explanation:** Minimum coverage threshold of 5x.

### Generate report
**Args:** `strdust -i reads.bam -r reference.fasta -o results.vcf --report`
**Explanation:** Generate comprehensive HTML report.
