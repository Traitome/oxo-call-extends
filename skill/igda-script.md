---
name: igda-script
category: variant-calling
description: Wrapper script for iGDA (integrated Genomic Data Analysis) to detect and phase minor SNVs from long-read sequencing data.
tags: [igda-script, variant-calling, SNV, long-read, phasing]
author: oxo-call-community
source_url: "https://github.com/zhixingfeng/shell"
---

## Concepts

- **Minor SNV Detection**: Specialized tool for detecting low-frequency single nucleotide variants.
- **Long-read Sequencing**: Optimized for long-read data from technologies like PacBio and Oxford Nanopore.
- **Variant Phasing**: Determines haplotype phase for detected variants.
- **iGDA Integration**: Wrapper for the iGDA pipeline components.
- **Shell Script Wrapper**: Simplifies running complex iGDA analyses through a unified interface.

## Pitfalls

- **Long-read Specific**: Designed for long-read data; may not work optimally with short reads.
- **iGDA Dependencies**: Requires iGDA tools to be installed and configured.
- **Computational Resources**: Long-read analysis can be computationally intensive.
- **Variant Frequency**: May miss very low-frequency variants depending on coverage.
- **Phasing Accuracy**: Depends on read length and coverage depth.

## Examples

### Detect minor SNVs from long-read data
**Args:** `igda-script --bam input.bam --ref reference.fasta --out results/`
**Explanation:** Runs iGDA pipeline to detect and phase minor SNVs.

### With custom parameters
**Args:** `igda-script --bam input.bam --ref ref.fa --min-af 0.01 --out results/`
**Explanation:** Sets minimum allele frequency threshold to 0.01.

### Phase detected variants
**Args:** `igda-script --bam input.bam --ref ref.fa --phase --out phased_results/`
**Explanation:** Enables variant phasing analysis.

### With parallel processing
**Args:** `igda-script --bam input.bam --ref ref.fa --threads 8 --out results/`
**Explanation:** Uses 8 threads for parallel processing.

### Generate VCF output
**Args:** `igda-script --bam input.bam --ref ref.fa --vcf --out variants.vcf`
**Explanation:** Outputs detected variants in VCF format.