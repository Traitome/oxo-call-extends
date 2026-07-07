---
name: minipileup
category: alignment
description: Minipileup is a simple pileup-based variant caller
tags: [minipileup, alignment, variant-calling]
author: oxo-call-community
source_url: "https://github.com/lh3/minipileup"
---

## Concepts

- **Tool Overview**: MiniPileup v1.4b calls variants from pileup data.
- **Core Function**: Identifies genetic variants from alignment data.
- **Pileup Analysis**: Analyzes aligned reads at each position.
- **Variant Calling**: Detects SNPs and indels from sequencing data.
- **Input/Output**: Accepts BAM files; outputs VCF format.
- **Multi-sample**: Supports calling variants across multiple samples.

## Pitfalls

- **Pileup-based**: Uses pileup approach for variant calling.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Calling accuracy depends on input data quality.
- **Reference Genome**: Requires appropriate reference sequences.

## Examples

### Call variants
**Args:** `minipileup -f reference.fasta alignments.bam > variants.vcf`
**Explanation:** Calls variants from BAM file.

### Multi-sample calling
**Args:** `minipileup -f reference.fasta sample1.bam sample2.bam > variants.vcf`
**Explanation:** Calls variants from multiple samples.

### With quality filter
**Args:** `minipileup -f reference.fasta -q 30 alignments.bam > variants.vcf`
**Explanation:** Uses quality threshold of 30.

### Batch processing
**Args:** `minipileup -f reference.fasta bam/*.bam > variants.vcf`
**Explanation:** Processes multiple BAM files.

### Generate allele counts
**Args:** `minipileup -f reference.fasta -c alignments.bam > variants.vcf`
**Explanation:** Outputs allele counts in VCF.