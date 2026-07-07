---
name: aquila_stlfr
category: variant-calling
description: Aquila_stLFR - Diploid genome assembly based structural variant calling package for stLFR linked-reads
tags: [aquila_stlfr, stLFR, linked-reads, genome-assembly, structural-variants]
author: oxo-call-community
source_url: "https://github.com/maiziex/Aquila_stLFR"
---

## Concepts

- **Tool Overview**: Aquila_stLFR (v1.2.11) - A diploid genome assembly based structural variant calling package specifically designed for stLFR (single tube Long Fragment Read) linked-reads.
- **Core Function**: Resolves structural variants through haplotype-based assembly of stLFR linked-reads, achieving complete diploid assembly and genome-wide SV detection.
- **Key Features**:
  - Haplotype-based partitioning of long fragment reads
  - Independent assembly of each haplotype
  - Complete diploid assembly reconstruction
  - Comprehensive structural variant detection
  - Hybrid mode supporting both stLFR and 10X linked-reads
- **stLFR Technology**: Single tube Long Fragment Read sequencing that enables co-barcoding of millions of 20-300 kb genomic DNA fragments
- **Analysis Workflow**:
  - Read partitioning into haplotype-specific blocks
  - Independent haplotype assembly
  - Diploid assembly reconstruction
  - Structural variant calling
- **Performance**: High sensitivity for medium to large deletions (50 bp-10 kb) and high specificity for medium-size insertions (50 bp-1 kb)
- **Input**: BAM file from stLFR sequencing
- **Output**: VCF files with structural variants, assembled contigs
- **Applications**: Structural variant detection, genome assembly, haplotype phasing
- **Installation**: `conda install -c bioconda aquila_stlfr`

## Pitfalls

- **Reference Dependencies**: Requires high-quality reference genome for read partitioning
- **Barcode Information**: BAM file must contain proper barcoding information from stLFR sequencing
- **Memory Requirements**: High memory usage for large genome assemblies
- **Input Quality**: Requires properly aligned and sorted BAM files
- **Variant Size**: Optimized for medium to large variants (50 bp-10 kb)

## Examples

### Basic structural variant calling
**Args:** `Aquila_stLFR --bam input.bam --ref hg38.fa --out_dir output`
**Explanation:** Runs complete stLFR analysis pipeline for structural variant detection.

### Hybrid mode (stLFR + 10X)
**Args:** `Aquila_stLFR --bam stlfr.bam --bam_10x tenx.bam --ref hg38.fa --out_dir output --hybrid`
**Explanation:** Uses both stLFR and 10X linked-reads for improved variant detection.

### Specify chromosomes
**Args:** `Aquila_stLFR --bam input.bam --ref hg38.fa --out_dir output --chr 1 2 3`
**Explanation:** Analyzes specific chromosomes only for faster processing.

### Help documentation
**Args:** `Aquila_stLFR --help`
**Explanation:** Shows available options and parameters.