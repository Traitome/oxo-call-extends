---
name: hmftools-redux
category: alignment
description: Post-processing read alignments to control sequencing errors and biases in BAM files.
tags: [hmftools-redux, alignment, BAM, quality-control, sequencing-errors, bias]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/redux"
---

## Concepts

- **Tool Overview**: REDUX (v1.2.3) is a BAM post-processing tool that identifies and corrects sequencing errors and biases in read alignments. It performs per-base error detection, read filtering, and alignment refinement to improve downstream variant calling accuracy.

- **Base Error Correction**: Identifies systematic sequencing errors at specific genomic positions by analyzing patterns of base quality scores and alignment discrepancies. Tags likely erroneous base calls for downstream masking or correction.

- **Read Filtering**: Filters low-quality reads and alignments based on multiple criteria including mapping quality, base quality, alignment identity, and soft-clipping patterns. Removes reads that introduce noise in variant calling.

- **Alignment Bias Detection**: Detects and flags alignment artifacts caused by repetitive sequences, pseudogenes, and segmental duplications. Generates reports highlighting regions with elevated misalignment probability.

- **GC Bias Correction**: Quantifies and reports GC-content bias in coverage patterns. While REDUX does not perform direct normalization, it provides metrics for downstream GC-corrected analysis.

- **Duplicate Contribution Scoring**: Scores duplicate reads based on base agreement and quality, distinguishing PCR duplicates from biological duplicates. Useful for mark-duplicates workflows to retain high-quality consensus reads.

## Pitfalls

- **Input BAM Quality**: REDUX performance depends on input BAM quality. Poorly aligned or heavily contaminated BAMs may produce false positive error calls. Ensure reads are aligned with recent aligner version (BWA-MEM2 recommended).

- **Reference Genome Match**: Input BAM must be aligned to the same reference genome specified in REDUX parameters. Mismatched references cause parsing errors and incorrect coordinate-based analysis.

- **Coordinate-Sorted Requirement**: REDUX requires position-sorted BAM input with valid BAI index. Unsorted or queryname-sorted BAMs will fail. Use `samtools sort` before processing.

- **Memory for Large Genomes**: WGS BAMs with hundreds of millions of reads require 16GB+ heap memory. Consider processing chromosome-by-chromosome for very large files.

- **Sex Chromosome Handling**: Special consideration needed for male samples (XY) versus female samples (XX). BAF calculations differ for pseudoautosomal regions (PAR) on sex chromosomes.

- **Bioconductor Dependencies**: REDUX depends on R packages Bioconductor-GenomicRanges and Bioconductor-VariantAnnotation for interval-based operations. Ensure R environment is properly configured with required Bioconductor packages.

## Examples

### Run REDUX on aligned BAM
**Args:** `redux -input tumor.sorted.bam -ref_genome GRCh37_hmf -output tumor.redux.bam -metrics tumor.redux.metrics`
**Explanation:** Standard REDUX processing on sorted BAM. Identifies base errors, filters low-quality reads, and outputs corrected BAM with metrics report.

### Process with strict quality thresholds
**Args:** `redux -input tumor.sorted.bam -ref_genome GRCh37_hmf -output tumor.redux.bam -min_base_qual 30 -min_map_qual 60 -min_alignment_identity 0.95`
**Explanation:** Applies strict filtering thresholds for high-confidence downstream analysis. Removes reads with base quality <30, mapping quality <60, or alignment identity <95%.

### Generate error reports only
**Args:** `redux -input tumor.sorted.bam -ref_genome GRCh37_hmf -output_dir ./redux_reports/ -report_only`
**Explanation:** Generates error detection reports without modifying the input BAM. Useful for quality assessment before committing to corrected output.

### Process with duplicate scoring
**Args:** `redux -input tumor.sorted.bam -ref_genome GRCh37_hmf -output tumor.redux.bam -score_duplicates -duplicate_metrics dup_scores.tsv`
**Explanation:** Enables duplicate scoring to distinguish PCR duplicates from biological duplicates. Outputs duplicate scores useful for mark-duplicates tools to retain high-quality consensus reads.

### Chromosome-specific processing
**Args:** `redux -input tumor.sorted.bam -ref_genome GRCh37_hmf -output tumor.redux.bam -region chr1:1-249250621 -region chr2:1-243199373`
**Explanation:** Processes only specified genomic regions. Useful for testing parameters or processing large BAMs in parallel chunks.

### Run on GRCh38 reference
**Args:** `redux -input tumor.sorted.bam -ref_genome GRCh38_hmf -output tumor.redux.bam -metrics tumor.redux.metrics`
**Explanation:** Uses GRCh38 reference genome. All input reads must be aligned to GRCh38. GRCh38 includes additional alt contigs for difficult regions.

### High-memory mode for WGS
**Args:** `redux -input wgs_tumor.sorted.bam -ref_genome GRCh37_hmf -output tumor.redux.bam -Xmx32G`
**Explanation:** Allocates 32GB heap memory for whole-genome samples with hundreds of millions of reads. Recommended for cohort-scale processing.
