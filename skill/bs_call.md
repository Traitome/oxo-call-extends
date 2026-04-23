---
name: bs_call
category: epigenomics
description: DNA methylation and variant caller for bisulfite sequencing data
tags: [bs_call, methylation, variant-calling, bisulfite]
author: oxo-call-community
source_url: "https://github.com/heathsc/bs_call"
---

## Concepts

- **Tool Overview**: bs_call performs DNA methylation calling and variant calling from bisulfite sequencing data.
- **Core Function**: Simultaneously calls methylation status and genetic variants from bisulfite-treated reads.
- **Input**: Aligned BAM file from bisulfite read alignment.
- **Output**: Methylation calls and variant calls.
- **Features**: Joint modeling of methylation and variants for improved accuracy.
- **Installation**: Install via bioconda: `conda install -c bioconda bs_call`

## Pitfalls

- **BAM Required**: Requires aligned BAM from bisulfite aligner (Bismark, BSMAP, etc.).
- **Reference Genome**: Must provide same reference used for alignment.
- **Coverage**: Low coverage regions have reduced calling accuracy.
- **Strand Information**: BAM must contain proper strand tags.

## Examples

### Call methylation and variants
**Args:** `bs_call -r reference.fa -i aligned.bam -o methylation.vcf`
**Explanation:** Calls methylation status and variants from bisulfite-aligned BAM.

### Set minimum coverage
**Args:** `bs_call -r reference.fa -i aligned.bam -c 5 -o calls.vcf`
**Explanation:** Requires minimum 5x coverage for calling.

### Output methylation only
**Args:** `bs_call -r reference.fa -i aligned.bam --meth-only -o methylation.bed`
**Explanation:** Outputs only methylation calls without variant calls.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
