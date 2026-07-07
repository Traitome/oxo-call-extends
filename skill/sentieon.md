---
name: sentieon
category: variant-analysis
description: sentieon - Accelerated bioinformatics tools for mapping and variant calling
tags: ["sentieon", "variant-analysis", "alignment", "variant-calling"]
author: oxo-call-community
source_url: "https://www.sentieon.com"
---

## Concepts

- **Tool Overview**: sentieon (v202503.03) provides accelerated bioinformatics tools for mapping and variant calling.
- **Core Function**: Performs high-performance sequence alignment and variant calling.
- **Algorithm**: Implements optimized versions of GATK tools with GPU acceleration.
- **Input/Output**: Accepts FASTQ/BAM files and produces variant calls.
- **Acceleration**: Leverages GPU and multi-threading for high performance.
- **Applications**: Whole-genome sequencing, exome sequencing, and variant analysis.

## Pitfalls

- **License Required**: Commercial software requiring license.
- **GPU Requirements**: Requires compatible GPU hardware for acceleration.
- **Software Dependencies**: Requires GPU drivers and CUDA toolkit.
- **Cost**: Commercial license may be expensive.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features may have limited public documentation.

## Examples

### Map reads
**Args:** `sentieon bwa mem -R "@RG\tID:sample\tSM:sample" reference.fasta reads.fastq -o aligned.bam`
**Explanation:** Maps reads to reference genome.

### Sort BAM
**Args:** `sentieon util sort -i aligned.bam -o sorted.bam`
**Explanation:** Sorts BAM file by coordinate.

### Mark duplicates
**Args:** `sentieon driver -i sorted.bam --algo LocusCollector --fun score_info score.txt`
**Explanation:** Collects duplicate scoring information.

### Variant calling
**Args:** `sentieon driver -i sorted.bam -r reference.fasta --algo Haplotyper -v variants.vcf`
**Explanation:** Calls variants using HaplotypeCaller.

### Threads
**Args:** `sentieon bwa mem -t 8 reference.fasta reads.fastq -o aligned.bam`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `sentieon --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sentieon version`
**Explanation:** Shows current version.