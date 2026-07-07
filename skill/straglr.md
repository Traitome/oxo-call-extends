---
name: straglr
category: variant-calling
description: Short-tandem repeat genotyping using long reads.
tags: [straglr, str-genotyping, long-reads, variant-calling]
author: oxo-call-community
source_url: "https://github.com/BirolLab/straglr"
---

## Concepts

- **Tool Overview**: straglr (v1.5.6) is a tool for genotyping short tandem repeats (STRs) using long-read sequencing data.
- **Core Function**: Identifies and genotypes STR expansions and contractions from long reads.
- **Algorithm**: Uses alignment and pattern matching to detect STR variations in long reads.
- **Input/Output**: Input: Long-read BAM file, reference genome; Output: STR genotypes with repeat counts.
- **Applications**: Genetic disease diagnosis, population genetics, forensic analysis.
- **Installation**: `conda install -c bioconda straglr` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect STR calling accuracy.
- **Repeat Complexity**: Complex repeat patterns are harder to genotype.
- **Alignment Quality**: Poor alignment affects STR detection.
- **Repeat Length**: Very long repeats may be missed or miscalled.
- **Reference Bias**: Reference genome may not contain all known STR alleles.
- **Memory Requirements**: Large datasets require significant memory.

## Examples

### Display help
**Args:** `straglr --help`
**Explanation:** Shows available options and usage information.

### Basic STR genotyping
**Args:** `straglr -i reads.bam -r reference.fasta -o results.vcf`
**Explanation:** Genotype STRs from long-read alignment.

### With STR bed file
**Args:** `straglr -i reads.bam -r reference.fasta -s strs.bed -o results.vcf`
**Explanation:** Use custom STR coordinates for genotyping.

### Verbose mode
**Args:** `straglr -i reads.bam -r reference.fasta -o results.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output detailed stats
**Args:** `straglr -i reads.bam -r reference.fasta -o results.vcf --stats`
**Explanation:** Generate detailed statistics about STR calls.

### Custom threshold
**Args:** `straglr -i reads.bam -r reference.fasta -o results.vcf -q 20`
**Explanation:** Set minimum mapping quality threshold to 20.

### Batch processing
**Args:** `straglr -i batch/ -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by repeat length
**Args:** `straglr -i reads.bam -r reference.fasta -o results.vcf -m 5`
**Explanation:** Minimum repeat unit length of 5.

### Generate report
**Args:** `straglr -i reads.bam -r reference.fasta -o results.vcf --report`
**Explanation:** Generate comprehensive HTML report.
