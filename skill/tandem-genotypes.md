---
name: tandem-genotypes
category: variation
description: Finds tandem repeat length changes from long DNA reads aligned to a genome.
tags: [tandem-genotypes, tandem-repeats, long-reads, variation]
author: oxo-call-community
source_url: "https://github.com/mcfrith/tandem-genotypes"
---

## Concepts

- **Tool Overview**: tandem-genotypes (v1.9.2) detects tandem repeat length changes.
- **Core Function**: Identifies length variations in tandem repeats.
- **Algorithm**: Analyzes aligned reads for repeat length differences.
- **Input/Output**: Input: BAM/SAM alignments; Output: Repeat genotypes.
- **Applications**: STR analysis, genetic variation, population genetics.
- **Installation**: `conda install -c bioconda tandem-genotypes` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large alignment files require significant memory.
- **Read Quality**: Poor quality reads affect accuracy.
- **Repeat Complexity**: Complex repeats may be missed.
- **Alignment Quality**: Requires well-aligned reads.
- **False Positives**: May report false length changes.
- **Performance**: Processing large files can be slow.

## Examples

### Display help
**Args:** `tandem-genotypes --help`
**Explanation:** Shows available options and usage information.

### Basic genotype calling
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -o genotypes.vcf`
**Explanation:** Call tandem repeat genotypes from BAM.

### With bed file
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -b repeats.bed -o genotypes.vcf`
**Explanation:** Use BED file for repeat regions.

### Verbose mode
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -o genotypes.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -o genotypes.vcf --stats`
**Explanation:** Generate statistics about genotypes.

### Batch processing
**Args:** `for f in bams/*.bam; do tandem-genotypes -i $f -r reference.fasta -o vcfs/${f%.bam}_genotypes.vcf; done`
**Explanation:** Process multiple BAM files.

### Filter by quality
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -o genotypes.vcf -q 20`
**Explanation:** Filter by minimum quality.

### Include flanking regions
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -o genotypes.vcf -f 50`
**Explanation:** Include 50bp flanking regions.

### Generate report
**Args:** `tandem-genotypes -i alignments.bam -r reference.fasta -o genotypes.vcf --report`
**Explanation:** Generate comprehensive genotype report.
