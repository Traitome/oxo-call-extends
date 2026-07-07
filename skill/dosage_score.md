---
name: dosage_score
category: utility
description: "Dosage-score: pipeline to estimate dosage of each genomic region"
tags: [dosage_score, utility, dosage, genomic-region, CNV, copy-number]
author: oxo-call-community
source_url: "https://github.com/SegawaTenta/Dosage-score"
---

## Concepts

- **Tool Overview**: Dosage-score is a pipeline for estimating the dosage of each genomic region from sequencing data.
- **Core Function**: Uses read depth information to calculate copy number variation (CNV) across the genome.
- **Input/Output**: Input: BAM alignment file, reference genome (FASTA). Output: Dosage scores per genomic region (BED/TSV).
- **Algorithm**: Based on read depth normalization and statistical modeling to detect copy number changes.
- **Key Features**: Whole-genome dosage estimation, support for paired-end sequencing, quality filtering, batch processing.
- **Installation**: `conda install -c bioconda dosage_score`

## Pitfalls

- **Quality Thresholds**: Low-quality alignments can significantly affect dosage estimates. Always preprocess BAM files with quality filtering.
- **GC Bias**: GC content variation can cause read depth biases; consider GC correction.
- **Read Depth**: Requires sufficient sequencing depth (minimum 10x recommended) for reliable dosage calls.
- **Reference Genome**: Must use the same reference genome used for alignment to avoid mapping issues.
- **CNV Size**: Detection sensitivity varies with CNV size; very small CNVs may be missed.

## Examples

### Basic dosage estimation
**Args:** `--bam sample.bam --ref ref.fa --output dosage.tsv`
**Explanation:** Estimates dosage for all genomic regions from aligned sequencing data.

### Targeted region analysis
**Args:** `--bam sample.bam --ref ref.fa --output dosage.tsv --regions targets.bed`
**Explanation:** Limits analysis to specific genomic regions defined in BED file.

### GC correction enabled
**Args:** `--bam sample.bam --ref ref.fa --output dosage.tsv --gc-correct`
**Explanation:** Applies GC content correction to reduce systematic bias in read depth.

### Quality filtering
**Args:** `--bam sample.bam --ref ref.fa --output dosage.tsv --min-mapq 30`
**Explanation:** Filters reads with mapping quality below 30 to improve accuracy.

### Multiple samples
**Args:** `--bam sample1.bam sample2.bam --ref ref.fa --output dosage.tsv --batch`
**Explanation:** Processes multiple samples together for batch analysis.
