---
name: elprep
category: variant-calling
description: "elPrep is a high-performance tool for preparing .sam/.bam files for variant calling in sequencing pipelines. It can be used as a drop-in replacement for SAMtools/Picard/GATK4."
tags: [elprep, variant-calling, BAM-processing, preprocessing, GATK]
author: oxo-call-community
source_url: "https://github.com/ExaScience/elprep"
---

## Concepts

- **Tool Overview**: elPrep is a high-performance tool for preparing SAM/BAM files for variant calling, designed as a drop-in replacement for SAMtools/Picard/GATK4 preprocessing steps.
- **Core Function**: Performs read filtering, duplicate marking, base quality recalibration, and other preprocessing steps required for variant calling.
- **Input/Output**: Input: SAM/BAM files, reference FASTA. Output: Processed BAM files, recalibration tables, statistics.
- **Algorithm**: Uses optimized parallel processing with minimal memory overhead for high-throughput sequencing data.
- **Key Features**: Drop-in replacement for GATK4, faster execution, lower memory usage, multi-threaded processing, comprehensive QC metrics.
- **Installation**: `conda install -c bioconda elprep`

## Pitfalls

- **Reference Compatibility**: Requires matching reference genome version.
- **Memory Management**: Large BAM files require sufficient RAM for efficient processing.
- **Duplicate Marking**: Proper duplicate marking requires read group information.
- **Recalibration**: Base quality recalibration requires known variant sites.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic preprocessing
**Args:** `elprep preprocess input.bam output.bam --reference ref.fasta`
**Explanation:** Performs basic BAM preprocessing for variant calling.

### With duplicate marking
**Args:** `elprep preprocess input.bam output.bam --reference ref.fasta --mark-duplicates`
**Explanation:** Marks duplicate reads during preprocessing.

### Base quality recalibration
**Args:** `elprep preprocess input.bam output.bam --reference ref.fasta --recalibrate known_sites.vcf`
**Explanation:** Performs base quality recalibration using known variants.

### Quality filtering
**Args:** `elprep preprocess input.bam output.bam --reference ref.fasta --min-quality 20`
**Explanation:** Filters reads with mapping quality below 20.

### Multi-threaded processing
**Args:** `elprep preprocess input.bam output.bam --reference ref.fasta --threads 16`
**Explanation:** Uses 16 threads for parallel processing.