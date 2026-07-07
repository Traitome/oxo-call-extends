---
name: aquila
category: variant-calling
description: Aquila - Diploid personal genome assembly and comprehensive variant detection based on linked-reads
tags: [aquila, linked-reads, genome-assembly, variant-calling, structural-variants]
author: oxo-call-community
source_url: "https://github.com/maiziex/Aquila"
---

## Concepts

- **Tool Overview**: Aquila (v1.0.0) - A reference-assisted, diploid assembly based approach for comprehensive variant detection from linked-read sequencing data.
- **Core Function**: Performs diploid personal genome assembly and comprehensive variant detection including SNPs, indels, and structural variants from 10X Genomics linked-reads.
- **Key Features**:
  - Reference-assisted haplotype partitioning
  - Local assembly of parental haplotypes
  - Comprehensive variant detection (SNPs, indels, SVs)
  - High sensitivity and accuracy for structural variants
- **Linked-read Technology**: Uses barcoded reads from 10X Genomics Chromium system
- **Analysis Pipeline**:
  - Step 0: Sort BAM file
  - Step 1: Reference-based read partitioning
  - Step 2: Haplotype-specific assembly
  - Step 3: Variant calling and phasing
- **Dependencies**: Python3, numpy, pysam, sortedcontainers, scipy, SAMtools, minimap2
- **Input**: BAM file from linked-read sequencing
- **Output**: VCF files with variants, phased haplotypes
- **Applications**: Personal genome analysis, structural variant detection, haplotype phasing
- **Installation**: `conda install -c bioconda aquila`

## Pitfalls

- **Reference Requirements**: Requires hg38 reference genome and Uniqness_map files
- **BAM File Requirements**: Requires sorted BAM file with proper barcoding information
- **Memory Usage**: May require significant memory for large genomes
- **Reference Data**: Need to download reference and Uniqness_map files from Zenodo
- **Barcode Information**: BAM file must contain 10X barcodes in the BX tag

## Examples

### Step 1: Reference-based partitioning
**Args:** `Aquila_step1 --bam input.bam --ref hg38.fa --out_dir output --chr 1-22,X,Y`
**Explanation:** Partitions reads into haplotype-specific blocks using reference genome.

### Step 2: Haplotype assembly
**Args:** `Aquila_step2 --bam input.bam --ref hg38.fa --out_dir output --chr 1`
**Explanation:** Performs haplotype-specific assembly for a specific chromosome.

### Step 3: Variant calling
**Args:** `Aquila_assembly_based_variants_call --bam input.bam --ref hg38.fa --out_dir output`
**Explanation:** Calls variants from the assembled haplotypes.

### Phase all variants
**Args:** `Aquila_phasing_all_variants --vcf variants.vcf --out_dir output`
**Explanation:** Phases all detected variants across the genome.

### Sort BAM file
**Args:** `Aquila_step0_sortbam --bam input.bam --out_bam sorted.bam`
**Explanation:** Sorts BAM file by coordinate for downstream analysis.

### Help documentation
**Args:** `Aquila_step1 --help`
**Explanation:** Shows available options for Step 1.