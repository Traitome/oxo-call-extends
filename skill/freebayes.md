---
name: freebayes
category: variant-calling
description: Bayesian haplotype-based polymorphism discovery and genotyping.
tags: [freebayes, variant-calling, snp, indel, haplotype]
author: oxo-call-community
source_url: "https://github.com/freebayes/freebayes"
---

## Concepts

- **Tool Overview**: FreeBayes (v1.3.6+) is a Bayesian haplotype-based variant caller that discovers SNPs and indels by modeling read alignments against a reference genome. It uses a probabilistic approach to call variants.
- **Core Function**: Performs variant calling by analyzing read alignments and inferring haplotypes using Bayesian statistics. Can call SNPs, indels, and complex variants.
- **Input/Output**: Input: BAM file with aligned reads, reference FASTA. Output: VCF file with called variants.
- **Algorithm**: Uses a Bayesian approach to model read data and infer the most likely genotypes. Supports population-level variant calling with multiple samples.
- **Key Features**: Haplotype-based calling, population-level analysis, supports multi-sample calling, outputs phased genotypes, and handles complex variants.
- **Installation**: `conda install -c bioconda freebayes`

## Pitfalls

- **Input Requirements**: Requires sorted and indexed BAM files with proper read groups. Use `samtools sort` and `samtools index` before running.
- **Reference Index**: Reference FASTA must be indexed with `samtools faidx`.
- **Memory Usage**: For large datasets, consider using `-p` flag for per-chromosome processing to reduce memory usage.
- **Filtering**: FreeBayes outputs unfiltered variants. Use `vcffilter` or bcftools to filter variants based on quality scores, depth, and other metrics.
- **Multi-sample Calling**: When calling multiple samples, ensure all BAM files are from the same reference and have consistent read group information.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic variant calling
**Args:** `-f reference.fa aligned.bam -v variants.vcf`
**Explanation:** Calls variants from aligned BAM file against reference genome, outputting to variants.vcf.

### Multi-sample variant calling
**Args:** `-f reference.fa sample1.bam sample2.bam sample3.bam -v multi_sample.vcf`
**Explanation:** Calls variants across multiple samples simultaneously, outputting combined VCF.

### Call variants with quality filtering
**Args:** `-f reference.fa aligned.bam -v variants.vcf -m 30 -q 20`
**Explanation:** Sets minimum mapping quality (-m 30) and base quality (-q 20) thresholds for variant calling.

### Call only SNPs
**Args:** `-f reference.fa aligned.bam -v snps.vcf --no-indels`
**Explanation:** Calls only SNPs, excluding indels from the output.

### Call with population priors
**Args:** `-f reference.fa aligned.bam -v variants.vcf --population-priors populations.txt`
**Explanation:** Uses population allele frequency priors to improve variant calling accuracy.

### Output phased genotypes
**Args:** `-f reference.fa aligned.bam -v variants.vcf --phased`
**Explanation:** Outputs phased genotypes in the VCF file using the `PS` tag.

### Per-chromosome processing
**Args:** `-f reference.fa aligned.bam -v chr1.vcf -r chr1`
**Explanation:** Calls variants only on chromosome chr1, useful for large genomes with memory constraints.

### Generate haplotype-aware output
**Args:** `-f reference.fa aligned.bam -v variants.vcf --haplotype-length 20`
**Explanation:** Uses haplotype information within 20bp windows for improved variant calling.

### Filter variants with minimum depth
**Args:** `-f reference.fa aligned.bam -v variants.vcf -C 5`
**Explanation:** Sets minimum coverage threshold of 5 reads for variant calling.