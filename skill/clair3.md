---
name: clair3
category: variant-calling
description: Deep learning-based small variant caller for long reads (ONT/PacBio) and Illumina
tags: [clair3, variant-calling, long-reads, ont, pacbio, deep-learning, snp, indel]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/Clair3"
---

## Concepts

- **Tool Overview**: Clair3 is a high-performance small variant caller for long-read sequencing data (ONT, PacBio) and Illumina short reads, using deep learning models for accurate SNP and indel calling.
- **Core Function**: Calls germline SNPs and small indels from aligned BAM/CRAM files using a combination of pileup and full-alignment approaches with neural network models.
- **Input/Output**: Input: Sorted BAM/CRAM file and reference genome. Output: VCF file with variant calls and quality scores.
- **Model Selection**: Provides pre-trained models for different sequencing platforms: ONT (Guppy5, Guppy6), PacBio (HiFi, CLR), and Illumina.
- **Pileup + Full-Alignment**: Combines pileup-based calling (fast) with full-alignment calling (accurate) for optimal performance.
- **GPU Support**: Supports GPU acceleration for faster calling. Can run on CPU-only systems but significantly slower.

## Pitfalls

- **Model Selection Critical**: Must use the correct model for your data type. ONT models differ from PacBio models. Using wrong model severely impacts accuracy.
- **Reference Genome**: Must use the same reference genome used for alignment. Mismatched references cause incorrect calls.
- **Memory Requirements**: Requires significant RAM (32GB+ recommended for human genome). Use `--chunk_size` to reduce memory.
- **BAM Index Required**: Input BAM must be indexed (.bai file present).
- **GPU vs CPU**: GPU mode is 10-50x faster than CPU. Strongly recommended for whole-genome calling.
- **Coverage Requirements**: Works best with ≥30x coverage for ONT, ≥20x for PacBio HiFi. Lower coverage reduces accuracy.

## Examples

### Call variants from ONT data
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform ont --output output_dir --model_path /path/to/ont_model`
**Explanation:** Calls variants from ONT-aligned BAM using the ONT-specific model with 8 threads.

### Call variants from PacBio HiFi data
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform hifi --output output_dir`
**Explanation:** Uses the PacBio HiFi model for high-accuracy HiFi reads, auto-downloads appropriate model.

### Call variants from Illumina short reads
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform illumina --output output_dir`
**Explanation:** Calls variants from Illumina short-read data using the Illumina-specific model.

### Enable GPU acceleration
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform ont --output output_dir --device cuda:0`
**Explanation:** Uses GPU (cuda:0) for faster variant calling, essential for large datasets.

### Call variants for specific regions
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform ont --output output_dir --bed regions.bed`
**Explanation:** Only calls variants in the regions specified in the BED file, useful for targeted sequencing.

### Use custom trained model
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform ont --output output_dir --model_path /path/to/custom_model`
**Explanation:** Uses a custom-trained Clair3 model instead of pre-trained models, useful for specialized datasets.

### Reduce memory usage
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 4 --platform ont --output output_dir --chunk_size 5000000`
**Explanation:** Processes the genome in smaller chunks (5Mb) to reduce memory consumption on memory-constrained systems.

### Output phased VCF
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform ont --output output_dir --enable_phasing`
**Explanation:** Enables read-backed phasing to output phased variants with haplotype information.

### Call variants with minimum quality filter
**Args:** `--bam_fn aligned.bam --ref_fn reference.fa --threads 8 --platform ont --output output_dir --qual_score 20`
**Explanation:** Filters output variants to include only those with quality score >= 20.
