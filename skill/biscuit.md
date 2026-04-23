---
name: biscuit
category: epigenomics
description: Utility for analyzing bisulfite conversion-based DNA methylation data
tags: [bisulfite, methylation, epigenomics, alignment]
author: oxo-call-community
source_url: "https://github.com/huishenlab/biscuit"
---

## Concepts
- **Tool Overview**: BISCUIT is a utility for analyzing sodium bisulfite conversion-based DNA methylation and modification data. It provides alignment, variant calling, and methylation analysis.
- **Features**: Bisulfite-aware alignment, SNP calling, methylation calling, NOMe-seq support, and quality control.
- **Advantages**: Handles both WGBS and NOMe-seq data, supports bisulfite-aware variant calling.
- **Workflow**: Index → align → deduplicate → call variants → extract methylation.

## Pitfalls
- **Reference Preparation**: Must run `biscuit index` before alignment.
- **NOMe-seq**: NOMe-seq analysis requires specific parameters.

## Examples
### Index reference genome
**Args:** `biscuit index reference.fa`
**Explanation:** Creates BISCUIT index for bisulfite-aware alignment.

### Align bisulfite reads
**Args:** `biscuit align -t 8 reference.fa reads.fq.gz | samtools sort -o aligned.bam`
**Explanation:** Aligns bisulfite-treated reads using 8 threads.

### Extract methylation
**Args:** `biscuit pileup -t 8 reference.fa aligned.bam > methylation.bed`
**Explanation:** Extracts methylation calls from aligned reads.
