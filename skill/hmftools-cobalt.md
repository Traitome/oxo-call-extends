---
name: hmftools-cobalt
category: utility
description: Calculate read-depth counts and GC ratios for PURPLE purity and ploidy estimation in cancer genomics.
tags: [hmftools-cobalt, read depth, GC ratio, copy number, PURPLE, tumor purity]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/cobalt/README.md"
---

## Concepts

- **Tool Overview**: hmftools-cobalt (v2.2) calculates genome-wide read depth counts and GC (guanine-cytosine) ratio normalization for use in PURPLE (Purity Ploidy Estimator), enabling accurate tumor purity and copy number profiling.
- **Read Depth Normalization**: Divides the genome into windows and calculates normalized read counts to account for GC bias, mappability issues, and other technical artifacts that affect read depth.
- **GC Ratio Calculation**: Computes the proportion of G and C nucleotides in each genomic window; GC content correlates with sequencing bias and copy number estimation accuracy.
- **PURPLE Pipeline Dependency**: COBALT output is an essential input for PURPLE, which combines BAF (B-allele frequency) from AMBER with read depth ratios from COBALT to estimate tumor purity and ploidy.
- **Copy Number Analysis**: Provides the read depth ratio component needed to distinguish copy number states (homozygous deletion, heterozygous, amplification) in tumor samples.
- **Bioconductor Dependency**: Uses Bioconductor copynumber package for segmentation-free normalization of read depth data.

## Pitfalls

- **CRITICAL: BAM Sorting Requirement**: Input BAM must be position-sorted; unsorted or query-name sorted BAM will produce incorrect results.
- **Reference Genome Matching**: Reference genome version (GRCh37 or GRCh38) must match exactly between COBALT, AMBER, and PURPLE in the workflow.
- **Minimum Window Threshold**: Small genomic windows may be filtered out due to low mappability or extreme GC content; this is expected and improves analysis accuracy.
- **Tumor-Normal Requirement**: For tumor samples, both tumor and matched normal BAMs should be analyzed; COBALT typically runs on the tumor sample, while matched normal provides reference copy number baseline.
- **Java Memory Allocation**: Large genomes with deep coverage may require increased Java heap memory; use -Xmx parameter if encountering memory errors.

## Examples

### Run COBALT on tumor BAM with reference
**Args:** `cobalt -tumor tumor.bam -reference normal.bam -ref_genome GRCh37_hmf -output_dir ./cobalt/`
**Explanation:** Calculates read depth ratios using tumor BAM with matched normal as reference. The normal sample provides baseline for diploid regions and improves copy number estimates.

### Standard tumor-only COBALT analysis
**Args:** `cobalt -tumor tumor_sample.bam -ref_genome GRCh38_hmf -output_dir ./cobalt_output`
**Explanation:** Runs COBALT when only tumor BAM is available. The tool will use built-in reference profiles for normalization instead of matched normal.

### Generate GC ratio plots for quality control
**Args:** `cobalt -tumor sample.bam -ref_genome GRCh37 -output_dir ./cobalt -gc_plot -read_depth_plot`
**Explanation:** Produces quality control plots showing GC bias correction and read depth distribution. These plots help identify problematic regions and assess sample quality.

### Process multiple tumor samples in batch
**Args:** `for bam in tumor_*.bam; do sample=$(basename $bam .bam); cobalt -tumor $bam -ref_genome GRCh37_hmf -output_dir ./cobalt/$sample; done`
**Explanation:** Iterates through all tumor BAM files and runs COBALT for each. Each sample gets its own output directory with .cobalt files for PURPLE input.

### COBALT with explicit thread count
**Args:** `cobalt -tumor sample.bam -ref_genome GRCh38_hmf -output_dir ./output -threads 8`
**Explanation:** Specifies 8 threads for parallel processing. Thread count can significantly reduce runtime for large WGS samples with high coverage.

### Run with custom chromosome naming
**Args:** `cobalt -tumor sample.bam -ref_genome GRCh37 -output_dir ./output -chr_pattern "chr[0-9XY]" -no_chr`
**Explanation:** Handles chromosome naming conventions where reference uses chr prefix but BAM uses numeric naming. The -no_chr flag strips the chr prefix from output.

### Combined COBALT and AMBER for PURPLE
**Args:** `cobalt -tumor tumor.bam -ref_genome GRCh37_hmf -output_dir ./cobalt && amber -tumor tumor.bam -reference normal.vcf -ref_genome GRCh37_hmf -output_dir ./amber`
**Explanation:** Runs both COBALT and AMBER sequentially to prepare inputs for PURPLE. COBALT provides read depth ratios while AMBER provides BAF values.
