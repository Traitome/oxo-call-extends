---
name: cnvnator
category: variant-calling
description: Tool for calling copy number variations from read depth
tags: [cnvnator, cnv, copy-number, read-depth, wgs, cancer]
author: oxo-call-community
source_url: "https://github.com/abyzovlab/CNVnator"
---

## Concepts

- **Tool Overview**: CNVnator is a tool for copy number variation discovery from read depth of mapping using a combination of read-depth and paired-end mapping approaches.
- **Core Function**: Detects CNVs by analyzing read depth distribution across the genome using histogram-based segmentation.
- **Input/Output**: Input: Sorted BAM file. Output: CNV calls in a custom format, can be converted to VCF.
- **Bin Size**: Uses a sliding window approach with configurable bin size. Recommended: 100bp for WGS, 30bp for targeted.
- **Multi-Step Pipeline**: Requires sequential steps: extract reads, generate histogram, calculate statistics, segment, call CNVs.
- **GC Correction**: Automatically corrects for GC bias in read depth.

## Pitfalls

- **Bin Size Selection**: Bin size affects sensitivity and specificity. 100bp is standard for 30x WGS. Smaller bins for higher coverage.
- **Reference Genome**: Must use the same reference genome used for alignment. Chromosome naming must match.
- **Memory Usage**: Large genomes require significant memory for histogram generation.
- **Step Order**: Must run steps in order: root, histogram, statistics, partition, call. Skipping steps causes errors.
- **Unique Reads Only**: Best results with uniquely mapped reads. Use `-unique` flag to filter multi-mapping reads.

## Examples

### Extract read depth
**Args:** `-root sample.root -unique sample.bam`
**Explanation:** Extracts read depth information from BAM file, storing in root format. Use -unique for uniquely mapped reads only.

### Generate histogram
**Args:** `-root sample.root -his 100 -d reference.genome`
**Explanation:** Generates read depth histogram with 100bp bin size using chromosome lengths from the genome file.

### Calculate statistics
**Args:** `-root sample.root -stat 100`
**Explanation:** Calculates statistics (mean, SD) for each chromosome at 100bp bin size.

### Segment the genome
**Args:** `-root sample.root -partition 100`
**Explanation:** Segments the genome into regions of constant copy number using mean-shift algorithm.

### Call CNVs
**Args:** `-root sample.root -call 100 > cnv_calls.txt`
**Explanation:** Calls CNV events from segmented data, outputs to stdout with event type, coordinates, and quality.

### Convert to VCF
**Args:** `-root sample.root -genotype 100 > cnv_genotyped.txt`
**Explanation:** Genotypes called CNVs with more detailed information about copy number states.

### View specific region
**Args:** `-root sample.root -view 100 chr1:10000000-20000000`
**Explanation:** Displays CNV calls for a specific genomic region, useful for validation.

### Compare with known CNVs
**Args:** `-root sample.root -compare 100 known_cnvs.bed`
**Explanation:** Compares called CNVs with known CNVs in BED format for validation.
