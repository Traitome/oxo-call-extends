---
name: hmftools-sage
category: variant-calling
description: SAGE is a somatic SNV, MNV and small INDEL caller optimised for 100x tumor and 40x normal coverage.
tags: [hmftools-sage, variant-calling, SNV, MNV, INDEL, somatic, tumor, germline]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/sage"
---

## Concepts

- **Tool Overview**: SAGE (v4.2) is a high-sensitivity somatic SNV, MNV, and small INDEL caller optimized for 100x tumor and 40x normal coverage. It combines multiple filtering strategies to achieve high precision while maintaining sensitivity for low-frequency variants.

- **Somatic Variant Detection**: Identifies tumor-specific mutations by comparing aligned reads from tumor and matched normal samples. Uses statistical tests to distinguish somatic variants from germline polymorphisms and sequencing artifacts.

- **MNV Support**: SAGE handles multiple nucleotide variants (MNVs) up to 32bp, correctly phasing adjacent variants and reporting them as combined events rather than separate SNVs.

- **Adaptive Filtering**: Implements adaptive filters that adjust to local sequence context, read depth, and base quality. Filters low-quality variant candidates while preserving true variants in difficult genomic regions.

- **Hotspot Database Integration**: Can incorporate known cancer mutation hotspots from COSMIC and internal databases to boost sensitivity for recurrently mutated positions.

- **Allelic Fraction Estimation**: Reports variant allelic fractions adjusted for tumor purity and copy number alterations. Enables distinction between clonal and subclonal mutations.

## Pitfalls

- **Matched Normal Required**: SAGE performs best with matched normal samples for germline filtering. Tumor-only mode increases false positives from rare germline variants. Always provide normal sample when available.

- **Coverage Requirements**: Optimized for 100x tumor / 40x normal coverage. Lower coverage reduces sensitivity for low-frequency somatic variants. Higher coverage improves detection of subclonal mutations.

- **Reference Genome Consistency**: Input BAMs must be aligned to the same reference genome (GRCh37 or GRCh38). Mixing genome versions causes coordinate misalignment and incorrect variant calls.

- **Memory for Deep Coverage**: WGS samples with 100x coverage produce millions of reads requiring 8GB+ heap memory. Use `-Xmx16G` for whole genome analysis.

- **Post-filtering Needed**: SAGE outputs require post-calling filtering for clinical use. Apply recommended AF thresholds based on tumor purity and sequencing depth.

- **Indel Alignment Challenges**: Small indels near read ends or in repetitive regions may have reduced sensitivity. Consider using local realignment tools before SAGE if indels are critical.

## Examples

### Standard tumor-normal somatic variant calling
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -reference normal1 -ref_bam normal1.bam -ref_genome GRCh37_hmf -output sage_variants.vcf -output_dir ./sage/`
**Explanation:** Standard SAGE run with matched normal for germline filtering. Detects somatic SNVs, MNVs, and small indels with allele fractions. Recommended for comprehensive tumor profiling.

### Tumor-only mode for rapid screening
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -ref_genome GRCh37_hmf -output sage_variants.vcf -output_dir ./sage/ -hotspots hotspots.tsv`
**Explanation:** Runs SAGE without matched normal using hotspot database for validation. Faster but higher false positive rate. Use for quick screening or when matched normal unavailable.

### High-sensitivity mode for low-frequency variants
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -reference normal1 -ref_bam normal1.bam -ref_genome GRCh37_hmf -output sage_variants.vcf -output_dir ./sage/ -min_allele_fraction 1.0 -high_confidence_only`
**Explanation:** Enables detection of subclonal mutations with allele fraction as low as 1%. High-confidence mode applies stricter filters to reduce false positives despite increased sensitivity.

### Include known hotspots
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -reference normal1 -ref_bam normal1.bam -ref_genome GRCh37_hmf -output sage_variants.vcf -output_dir ./sage/ -hotspots cosmic_hmf_hotspots.tsv`
**Explanation:** Uses hotspot database to boost sensitivity for known cancer mutations. Hotspots are flagged with increased priority and reduced filter stringency.

### Panel/targeted sequencing mode
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -reference normal1 -ref_bam normal1.bam -ref_genome GRCh37_hmf -output sage_variants.vcf -output_dir ./sage/ -panel -target_regions capture.bed`
**Explanation:** Optimized parameters for targeted panel sequencing with higher depth. Applies panel-specific filters and reduces noise from off-target regions.

### Run on GRCh38 reference
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -reference normal1 -ref_bam normal1.bam -ref_genome GRCh38_hmf -output sage_variants.vcf -output_dir ./sage/`
**Explanation:** Uses GRCh38 reference genome. All input BAMs must be aligned to GRCh38. GRCh38 provides improved assembly and additional gene annotations.

### High-memory mode for cohort analysis
**Args:** `sage -tumor tumor1 -tumor_bam tumor1.bam -reference normal1 -ref_bam normal1.bam -ref_genome GRCh37_hmf -output sage_variants.vcf -output_dir ./sage/ -Xmx16G`
**Explanation:** Allocates 16GB heap memory for processing multiple samples or high-depth WGS data. Recommended for batch processing large cohorts.
