---
name: sscocaller
category: variant-calling
description: Haplotyping single-cell DNA sequenced gamete cells.
tags: [sscocaller, single-cell, haplotyping, gamete]
author: oxo-call-community
source_url: "https://gitlab.svi.edu.au/biocellgen-public/sscocaller"
---

## Concepts

- **Tool Overview**: sscocaller (v0.2.2) is a tool for haplotyping single-cell DNA sequenced gamete cells, enabling phasing of genetic variants.
- **Core Function**: Calls SNVs and phases haplotypes from single-cell sequencing data of gametes.
- **Phasing Algorithm**: Uses gamete-specific haplotype information to resolve phase relationships.
- **Input/Output**: Input: BAM file with single-cell reads; Output: VCF with phased variants and haplotype blocks.
- **Single-Cell Specific**: Optimized for low-coverage, high-error single-cell sequencing data.
- **Installation**: `conda install -c bioconda sscocaller` or build from source.

## Pitfalls

- **Low Coverage**: Single-cell data typically has low coverage, affecting variant calling accuracy.
- **Allelic Dropout**: Common in single-cell data; can lead to missing heterozygous calls.
- **Reference Bias**: Requires high-quality reference genome matching sample origin.
- **Contamination**: Cell-free DNA contamination affects haplotype accuracy.
- **Phase Switch Errors**: Incorrect phase assignments can occur in repetitive regions.
- **Memory Requirements**: Large genomes require significant memory for haplotype phasing.

## Examples

### Display help
**Args:** `sscocaller --help`
**Explanation:** Shows available options and usage information.

### Basic haplotyping
**Args:** `sscocaller -i input.bam -r reference.fasta -o output.vcf`
**Explanation:** Call variants and phase haplotypes from single-cell BAM.

### With quality filtering
**Args:** `sscocaller -i input.bam -r reference.fasta -o output.vcf -q 20`
**Explanation:** Apply minimum quality filter for variant calling.

### Specify region
**Args:** `sscocaller -i input.bam -r reference.fasta -o output.vcf --region chr1:1000-2000`
**Explanation:** Call variants only in specified genomic region.

### Multiple samples
**Args:** `sscocaller -i sample1.bam sample2.bam -r reference.fasta -o output.vcf`
**Explanation:** Process multiple single-cell samples together.

### Generate haplotype blocks
**Args:** `sscocaller -i input.bam -r reference.fasta -o output.vcf --blocks`
**Explanation:** Output haplotype block information.

### Verbose mode
**Args:** `sscocaller -i input.bam -r reference.fasta -o output.vcf --verbose`
**Explanation:** Run with detailed logging for debugging.
