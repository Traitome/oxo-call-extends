---
name: hmftools-esvee
category: variant-calling
description: Efficient structural variant caller specialized for breakend and breakpoint detection using junction assembly and phased assembly.
tags: [hmftools-esvee, structural variants, SV, breakend, breakpoint, assembly, cancer genomics]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/esvee/README.md"
---

## Concepts

- **Tool Overview**: hmftools-esvee (v1.2) is an Efficient Structural Variant Engine that detects structural variants (SVs) through junction assembly and breakpoint analysis, specializing in accurate breakend and breakpoint calling.
- **Multi-step Assembly Pipeline**: The workflow includes ESvee PREP (preprocessing), ESvee ASSEMBLE (junction assembly), ESvee DEPTH_ANNOTATOR (read depth annotation), and ESvee CALL (SV filtering).
- **Phased Assembly**: Performs haplotype-specific assembly to identify which allele carries the structural variant, important for interpreting variant effects.
- **Breakend Detection**: Identifies precise breakpoint coordinates at single-nucleotide resolution by assembling reads spanning potential breakpoints.
- **Input Requirement**: Works with tumor and matched normal BAM files to distinguish somatic from germline structural variants.
- **WiGiTS Pipeline Integration**: Part of the Hartwig Medical Foundation's WiGiTS suite for comprehensive cancer genomics, feeding into LINX for SV annotation and interpretation.

## Pitfalls

- **CRITICAL: BAM Sorting**: Input BAMs must be coordinate-sorted; unsorted BAMs will cause preprocessing failures or incorrect results.
- **Sambamba Dependency**: Requires sambamba for efficient BAM processing (marked as dependency in bioconda); ensure proper installation.
- **Paired-end Data Quality**: Works best with paired-end reads with proper fragment size distributions; single-end data may have reduced sensitivity.
- **Normal Sample Requirement**: Accurate somatic SV calling requires matched normal sample; tumor-only analysis will include germline variants.
- **High Memory Usage**: Assembly-based detection is memory-intensive for large genomes; ensure adequate RAM for WGS samples.

## Examples

### Run full ESvee pipeline on tumor-normal pair
**Args:** `esvee -sample_id tumor1 -tumor tumor.bam -normal normal.bam -ref_genome GRCh37_hmf -output_dir ./esvee/`
**Explanation:** Runs the complete ESvee pipeline including PREP, ASSEMBLE, DEPTH_ANNOTATOR, and CALL steps. Produces somatic SV VCF with breakend-level resolution.

### ESvee PREP step only
**Args:** `esvee_prep -tumor tumor.bam -normal normal.bam -ref_genome GRCh38_hmf -output_dir ./esvee_prep/`
**Explanation:** Runs only the preprocessing step which extracts junction information and calculates fragment length distributions. Useful for quality control before assembly.

### ESvee ASSEMBLE for junction assembly
**Args:** `esvee_assemble -sample_id sample1 -prep_dir ./esvee_prep -ref_genome GRCh37 -output_dir ./esvee_assemble/`
**Explanation:** Performs junction assembly on preprocessed data to identify breakends and characterize structural variants at base-pair resolution.

### ESvee with custom breakend list
**Args:** `esvee -sample_id test -tumor tumor.bam -normal normal.bam -ref_genome GRCh38_hmf -output_dir ./output -breakend_bed regions.bed`
**Explanation:** Uses a custom BED file to focus analysis on specific genomic regions of interest, improving sensitivity in targeted regions.

### Batch processing multiple tumor samples
**Args:** `for bam in tumor_*.bam; do sample=$(basename $bam .bam); esvee -sample_id $sample -tumor $bam -normal normal.bam -ref_genome GRCh37_hmf -output_dir ./esvee/$sample; done`
**Explanation:** Iterates through multiple tumor BAM files paired with the same normal sample. Each sample gets its own output directory.

### ESvee with parallel processing
**Args:** `esvee -sample_id sample1 -tumor tumor.bam -normal normal.bam -ref_genome GRCh38_hmf -output_dir ./output -threads 16`
**Explanation:** Uses 16 threads for parallel processing to accelerate the assembly and calling steps. Thread count should match available CPU cores.
