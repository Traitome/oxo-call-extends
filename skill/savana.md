---
name: savana
category: variant-calling
description: SAVANA - somatic structural variant caller for long-read data
tags: ["savana", "variant-calling", "long-read", "structural-variants"]
author: oxo-call-community
source_url: "https://github.com/cortes-ciriano-lab/savana"
---

## Concepts

- **Tool Overview**: SAVANA (v1.3.7) is a somatic structural variant caller specifically designed for long-read sequencing data.
- **Core Function**: Detects somatic structural variants (SVs) including deletions, duplications, inversions, and translocations from long-read alignments.
- **Algorithm**: Uses split-read mapping and read pair analysis optimized for long reads (PacBio/ONT) to identify SV breakpoints.
- **Input/Output**: Accepts BAM files with long-read alignments and reference genome, produces VCF with structural variant calls.
- **Somatic Focus**: Specifically designed to detect somatic mutations in cancer samples compared to matched normals.
- **Applications**: Cancer genomics, somatic mutation detection, and structural variant analysis in tumor samples.

## Pitfalls

- **Long-Read Specific**: Designed for long reads, may not work well with short-read data.
- **Read Quality**: Results depend on long-read accuracy and alignment quality.
- **Computational Resources**: Requires significant compute resources for large genomes.
- **False Positives**: May report false SV calls in repetitive regions.
- **Normal Sample Required**: Best results with matched normal sample for somatic calling.
- **Parameter Tuning**: Requires careful adjustment for different sequencing platforms.

## Examples

### Basic SV calling
**Args:** `savana -i tumor.bam -n normal.bam -r reference.fasta -o variants.vcf`
**Explanation:** `-i` tumor BAM; `-n` normal BAM; `-r` reference genome; `-o` output VCF.

### Tumor-only calling
**Args:** `savana -i tumor.bam -r reference.fasta -o variants.vcf --tumor-only`
**Explanation:** `--tumor-only` mode for calling without matched normal.

### With quality filtering
**Args:** `savana -i tumor.bam -n normal.bam -r reference.fasta -q 20 -o variants.vcf`
**Explanation:** `-q 20` filters variants with quality below 20.

### Breakpoint refinement
**Args:** `savana -i tumor.bam -n normal.bam -r reference.fasta --refine -o variants.vcf`
**Explanation:** `--refine` performs breakpoint refinement for precise SV boundaries.

### Output bedpe format
**Args:** `savana -i tumor.bam -n normal.bam -r reference.fasta -f bedpe -o variants.bedpe`
**Explanation:** `-f bedpe` outputs in BEDPE format instead of VCF.

### Verbose logging
**Args:** `savana -i tumor.bam -n normal.bam -r reference.fasta -v -o variants.vcf`
**Explanation:** `-v` enables verbose logging for debugging.

### Targeted analysis
**Args:** `savana -i tumor.bam -n normal.bam -r reference.fasta -t chr1:100000-200000 -o targeted.vcf`
**Explanation:** `-t` specifies target region for focused analysis.