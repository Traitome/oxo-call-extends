---
name: duphold
category: variant-calling
description: Duphold - Adds depth information to structural variant calls from tools like LUMPY.
tags: [duphold, variant-calling, structural-variants, depth-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/brentp/duphold"
---

## Concepts

- **Tool Overview**: Duphold is a fast tool for adding depth-based evidence to structural variant calls.
- **Core Function**: Adds read depth information to VCF files containing structural variant calls.
- **Input/Output**: Input: BAM alignment files, VCF with SV calls. Output: Annotated VCF with depth statistics.
- **Algorithm**: Uses BAM files to calculate read depth at variant breakpoints and within affected regions.
- **Key Features**: Fast depth calculation, VCF annotation, breakpoint analysis, multi-sample support, parallel processing.
- **Installation**: `conda install -c bioconda duphold`

## Pitfalls

- **Input Requirements**: Requires sorted and indexed BAM files; unsorted BAMs will cause errors.
- **VCF Format**: VCF must contain valid SV records with proper breakend notation.
- **Reference Genome**: BAM and VCF must use the same reference genome.
- **Depth Variation**: Regions with naturally low coverage may produce false negatives.
- **Memory Usage**: Processing multiple large BAMs simultaneously requires significant RAM.
- **Parallel Processing**: Too many threads may cause memory issues on resource-limited systems.

## Examples

### Add depth to SV calls
**Args:** `duphold --vcf sv_calls.vcf --bam sample.bam --fasta ref.fa --output annotated.vcf`
**Explanation:** Adds depth information to structural variant calls in VCF format.

### Multiple samples
**Args:** `duphold --vcf sv_calls.vcf --bam sample1.bam sample2.bam --fasta ref.fa --output annotated.vcf`
**Explanation:** Processes multiple BAM files for multi-sample variant annotation.

### With parallel processing
**Args:** `duphold --vcf sv_calls.vcf --bam sample.bam --fasta ref.fa --output annotated.vcf --threads 8`
**Explanation:** Uses 8 threads for faster processing.

### Include depth window
**Args:** `duphold --vcf sv_calls.vcf --bam sample.bam --fasta ref.fa --output annotated.vcf --window 1000`
**Explanation:** Sets a 1000bp window for depth calculation around breakpoints.

### Output statistics
**Args:** `duphold --vcf sv_calls.vcf --bam sample.bam --fasta ref.fa --output annotated.vcf --stats stats.txt`
**Explanation:** Generates additional statistics about depth distribution.

### Filter by quality
**Args:** `duphold --vcf sv_calls.vcf --bam sample.bam --fasta ref.fa --output annotated.vcf --min-qual 20`
**Explanation:** Only processes variants with quality score >= 20.