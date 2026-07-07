---
name: hmftools-sv-prep
category: variant-calling
description: SV Prep generates a maximally filtered SV BAM file by identifying candidate SV junctions and extracting all reads that may provide support to that junction.
tags: [hmftools-sv-prep, structural-variants, BAM, junction, breakend, gridss, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/sv-prep"
---

## Concepts

- **Tool Overview**: SV-PREP (v1.2.4) generates a maximally filtered structural variant BAM file by identifying candidate SV junctions from input VCF files and extracting all reads that may provide evidence for those junctions. It acts as a preprocessing step for structural variant validation and visualization workflows.

- **Candidate Junction Identification**: SV-PREP takes as input a list of candidate structural variant calls (typically from GRIDSS or similar SV callers) and identifies the precise genomic breakpoints. It determines the exact coordinates where the chromosome breaks and rejoin points occur for deletions, insertions, inversions, and translocations.

- **Read Extraction and Filtering**: The tool extracts from the primary alignment BAM all reads spanning each candidate junction, including: (1) reads with soft-clipped or split alignments at the breakpoint, (2) reads with mismatches near the junction coordinates, (3) discordant read pairs where one end maps to each side of the breakpoint.

- **SV BAM Index Generation**: SV-PREP creates a purpose-built BAM containing only SV-relevant reads, dramatically reducing file size compared to the full BAM while retaining all variant evidence. This filtered BAM is optimized for downstream visualization in tools like IGV or for manual variant review.

- **Integration with GRIDSS**: SV-PREP is designed to work with GRIDSS (Genome Rearrangement Identification Software Suite), extracting reads from GRIDSS-detected structural variants for subsequent filtering and validation. The tool depends on GRIDSS for initial breakpoint detection.

- **Maximally Filtered Output**: The filtering strategy ensures high-precision junction calls by excluding reads with ambiguous alignments or low mapping quality. This reduces false positives in downstream analysis while maintaining sensitivity for true structural variants.

## Pitfalls

- **GRIDSS Dependency**: SV-PREP requires GRIDSS output as input. Without proper GRIDSS installation and execution, SV-PREP cannot generate candidate junctions. Ensure GRIDSS is in your PATH and has successfully completed before running SV-PREP.

- **Coordinate System Mismatch**: Input VCF files must use the same genome reference build as the BAM file (GRCh37 or GRCh38). Mixing coordinate systems results in incorrect read extraction and empty junction files.

- **Large Structural Variants**: Very large deletions or inversions (>100kb) may have insufficient spanning reads for confident junction calling. Consider using assembly-based methods for large structural variants instead.

- **High Duplicate Rates**: Samples with high PCR duplication rates may have inflated junction read counts. The filtered BAM will contain duplicate reads; consider marking duplicates before interpretation.

- **Memory Requirements**: Processing whole-genome BAMs with many candidate junctions requires substantial RAM. For large cohorts, process samples in parallel with memory-optimized configurations.

- **VCF Filtering Quality**: Only high-quality SV calls should be passed to SV-PREP. Low-quality or complex SV calls (e.g., nested translocations) may cause errors in junction extraction or produce misleading evidence counts.

## Examples

### Run SV-PREP with GRIDSS VCF
**Args:** `sv-prep -vcf gridss_variants.vcf -bam tumor.bam -output_dir ./sv_prep/`
**Explanation:** Standard SV-PREP run taking GRIDSS VCF output and tumor BAM. Extracts all reads supporting candidate structural variant junctions into a filtered BAM file.

### Specify genome reference
**Args:** `sv-prep -vcf variants.vcf -bam tumor.bam -ref_genome GRCh37_hmf -output_dir ./sv_prep/`
**Explanation:** Explicitly specifies the genome reference build for coordinate conversion. Use GRCh37_hmf for legacy HMF pipelines or GRCh38 for GRCh38-aligned inputs.

### Process with multiple bam inputs
**Args:** `sv-prep -vcf variants.vcf -bam tumor.bam -ref_bam normal.bam -output_dir ./sv_prep/`
**Explanation:** Provides matched normal BAM in addition to tumor. Useful for extracting reads from both samples to distinguish somatic vs germline structural variants during manual review.

### Set minimum mapping quality
**Args:** `sv-prep -vcf variants.vcf -bam tumor.bam -min_mq 30 -output_dir ./sv_prep/`
**Explanation:** Sets minimum mapping quality threshold (30) for extracted reads. Reads with MQ below this threshold are excluded from the filtered BAM to reduce noise from ambiguous alignments.

### Process specific chromosome
**Args:** `sv-prep -vcf variants.vcf -bam tumor.bam -chromosome chr7 -output_dir ./sv_prep/`
**Explanation:** Restricts processing to a single chromosome for targeted analysis or debugging. Significantly reduces runtime and output file size when investigating specific genomic regions.

### Custom output filename
**Args:** `sv-prep -vcf variants.vcf -bam tumor.bam -output tumor.sv_prep.bam -output_dir ./sv_prep/`
**Explanation:** Specifies a custom output BAM filename instead of the default derived from the sample name. Useful when processing multiple samples or when integrating with automated pipelines.

### Enable verbose logging
**Args:** `sv-prep -vcf variants.vcf -bam tumor.bam -log_level DEBUG -output_dir ./sv_prep/`
**Explanation:** Enables debug-level logging for troubleshooting extraction issues or verifying junction detection. Logs all extracted reads and filtering decisions for audit purposes.
