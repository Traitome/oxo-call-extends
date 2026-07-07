---
name: aquila_sv
category: variant-calling
description: Structural variant calling from linked-read sequencing data
tags: [aquila_sv, variant-calling, structural-variants, linked-reads, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/maiziezhoulab/AquilaSV"
---

## Concepts

- **Tool Overview**: AquilaSV is a structural variant calling tool designed for linked-read sequencing data (10X Genomics, stLFR). It performs haplotype-resolved variant detection by leveraging the long-range information inherent in linked reads.
- **Core Function**: Detects large-scale structural variants (deletions, duplications, inversions, translocations) by combining haplotype assembly with variant calling.
- **Linked-read Technology**: Uses barcodes to group reads originating from the same long DNA molecule, enabling detection of variants spanning hundreds of kilobases.
- **Diploid Awareness**: Explicitly handles diploid genomes, providing phased variant calls that distinguish between maternal and paternal alleles.
- **Hybrid Assembly Mode**: Can combine linked-read data with other sequencing technologies (Illumina short reads, PacBio, ONT) for improved variant detection.
- **Installation**: `conda install -c bioconda aquila_sv` or download from GitHub and compile from source.

## Pitfalls

- **Reference Genome Requirements**: Requires a FASTA-formatted reference genome with corresponding BWA index files (.amb, .ann, .bwt, .pac, .sa).
- **Input BAM Requirements**: Input BAM must be coordinate-sorted and indexed (.bai). Linked-read barcodes must be in the BX tag.
- **Memory Requirements**: Large genomes (e.g., human) require significant memory (>32GB recommended). Use chromosome-specific mode for limited resources.
- **Barcode Quality**: Poor barcode quality can reduce variant detection sensitivity. Consider preprocessing with barcode correction tools.
- **Complex Regions**: Highly repetitive regions may produce false positives. Filter results using quality scores and support metrics.
- **Version Compatibility**: Command-line options may differ between versions. Check `--help` for your installed version.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options, subcommands, and usage examples.

### Basic structural variant calling
**Args:** `--bam input.bam --ref hg38.fa --out_dir output`
**Explanation:** Performs structural variant calling on aligned linked-read BAM file using the hg38 reference genome. Outputs VCF files and intermediate results to the specified directory.

### Chromosome-specific analysis
**Args:** `--bam input.bam --ref hg38.fa --chr chr21 --out_dir output_chr21`
**Explanation:** Limits analysis to chromosome 21 only. Useful for targeted studies or when memory is constrained. Significantly reduces runtime compared to whole-genome analysis.

### Hybrid mode with multiple inputs
**Args:** `--bam input.bam --ont ont_reads.fastq --ref hg38.fa --out_dir hybrid_output`
**Explanation:** Combines linked-read BAM with Oxford Nanopore long reads for improved variant detection, especially for larger structural variants that are challenging with short reads alone.

### Enable verbose logging
**Args:** `--bam input.bam --ref hg38.fa --out_dir output --verbose --log_file aquila_sv.log`
**Explanation:** Enables detailed logging for debugging and tracking analysis progress. Log file contains timing information and intermediate processing steps.

### Adjust variant calling parameters
**Args:** `--bam input.bam --ref hg38.fa --out_dir output --min_sv_size 50 --max_sv_size 100000 --min_support 3`
**Explanation:** Sets minimum SV size to 50bp, maximum to 100kb, and requires at least 3 supporting reads for a variant call. Adjust these thresholds based on your specific requirements and data quality.