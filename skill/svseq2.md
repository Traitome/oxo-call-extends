---
name: svseq2
category: variant-calling
description: SVseq2 accurately calls structural variations from low-coverage sequencing data.
tags: [svseq2, structural-variants, low-coverage, variant-calling]
author: oxo-call-community
source_url: "https://sites.google.com/site/jinzhangwebsite/svseq2"
---

## Concepts

- **Tool Overview**: svseq2 (v2) calls structural variants from low-coverage sequencing data.
- **Core Function**: Detects SVs efficiently from low-depth sequencing data.
- **Algorithm**: Uses statistical methods optimized for low-coverage data.
- **Input/Output**: Input: BAM file, reference genome; Output: VCF with SV calls.
- **Applications**: Population genetics, low-coverage sequencing studies.
- **Installation**: `conda install -c bioconda svseq2` or download from website.

## Pitfalls

- **Coverage Requirements**: Designed for low-coverage data, may not perform well at high coverage.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large cohorts can be slow.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.
- **Reference Genome**: Requires high-quality reference genome.
- **Complex Regions**: Difficult to detect SVs in repetitive regions.

## Examples

### Display help
**Args:** `svseq2 --help`
**Explanation:** Shows available options and usage information.

### Basic SV calling
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf`
**Explanation:** Call SVs from low-coverage BAM file.

### With minimum coverage
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf -c 3`
**Explanation:** Minimum coverage threshold of 3x.

### Verbose mode
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf --stats`
**Explanation:** Generate statistics about SV calling.

### Batch processing
**Args:** `svseq2 -i bams/ -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf -q 20`
**Explanation:** Filter SVs by quality score.

### Include all SV types
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf --all-types`
**Explanation:** Detect all types of structural variants.

### Generate report
**Args:** `svseq2 -i sample.bam -r reference.fasta -o sv.vcf --report`
**Explanation:** Generate comprehensive HTML report.
