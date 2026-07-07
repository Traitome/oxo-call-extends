---
name: hmftools-cider
category: utility
description: Determine comprehensive CDR3 sequences for IG and TCR loci from RNA and DNA sequencing data for immune repertoire analysis.
tags: [hmftools-cider, CDR3, immunoglobulin, TCR, immune repertoire, VDJ recombination]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/cider/README.md"
---

## Concepts

- **Tool Overview**: hmftools-cider (v1.1) identifies and characterizes CDR3 (Complementarity-Determining Region 3) sequences from Immunoglobulin (IG) and T-cell Receptor (TCR) loci, providing comprehensive immune repertoire profiling from sequencing data.
- **CDR3 Significance**: CDR3 is the most variable region of IG/TCR and is critical for antigen recognition; its sequence diversity reflects the adaptive immune response repertoire.
- **Input Flexibility**: Accepts both RNA-seq and DNA-seq aligned data (BAM format), enabling flexibility in immune repertoire studies from different sequencing approaches.
- **Loci Coverage**: Analyzes all IG loci (IGH, IGK, IGL) and TCR loci (TRA, TRB, TRG, TRD) for complete immune repertoire characterization.
- **BLAST-based Validation**: Uses BLAST for sequence alignment validation to ensure accurate CDR3 identification against reference V(D)J gene segments.
- **WiGiTS Integration**: Part of the Hartwig Medical Foundation's WiGiTS pipeline for comprehensive cancer genomics, particularly relevant for tumor microenvironment immune infiltration analysis.

## Pitfalls

- **BLAST Dependency**: Requires BLAST to be installed and in PATH; without it, CDR3 identification will fail despite other dependencies being satisfied.
- **RNA vs DNA Sensitivity**: RNA-seq data typically provides better CDR3 detection due to higher expression of immune transcripts, while DNA may miss low-abundance clones.
- **V(D)J Recombination Complexity**: Incomplete or partial V(D)J recombination events may produce ambiguous results; review reads with multiple alignments.
- **Paired-end Read Requirements**: Optimal performance requires paired-end reads with sufficient overlap to span the CDR3 region; single-end reads may have lower accuracy.
- **Species Specificity**: Designed primarily for human data; mouse or other species may require different reference gene sets.

## Examples

### Run CIDER on RNA-seq BAM file
**Args:** `cider -sample_id patient1 -bam rna_aligned.bam -output_dir ./cider_results -ref_genome GRCh38_hmf`
**Explanation:** Performs CDR3 identification from RNA-seq alignments. The tool scans reads mapping to IG/TCR loci and reconstructs CDR3 sequences using V, D, and J gene segment information.

### Analyze tumor and normal paired samples
**Args:** `cider -sample_id tumor1 -bam tumor.bam -ref_genome GRCh37 -output_dir ./cider/tumor -species human`
**Explanation:** Compares CDR3 repertoires between tumor and matched normal samples to identify tumor-infiltrating lymphocyte clones. Output includes clone frequencies and diversity metrics.

### Process DNA sequencing data
**Args:** `cider -sample_id sample1 -bam dna_aligned.bam -output_dir ./cider_dna -ref_genome GRCh38 -seq_type DNA`
**Explanation:** Runs CDR3 detection on DNA sequencing data. DNA-based immune repertoire sequencing (Rep-Seq) provides germline-encoded information without expression bias.

### Generate full locus-specific report
**Args:** `cider -sample_id immune_sample -bam rnaseq.bam -output_dir ./cider_full -loci IGH,IGK,IGL,TRA,TRB -ref_genome GRCh38_hmf`
**Explanation:** Produces comprehensive CDR3 analysis across multiple IG and TCR loci. The -loci parameter specifies which loci to analyze (default: all loci).

### Run with custom reference database
**Args:** `cider -sample_id custom -bam input.bam -output_dir ./output -ref_genome GRCh38 -custom_ref custom_cdr3_ref.fasta`
**Explanation:** Uses a custom CDR3 reference database instead of the default. This is useful for analyzing non-standard sequences or modified immune receptors.

### Batch processing multiple samples
**Args:** `for bam in tumor_*.bam; do sample=$(basename $bam .bam); cider -sample_id $sample -bam $bam -output_dir ./cider/$sample -ref_genome GRCh37_hmf; done`
**Explanation:** Iterates through all tumor BAM files and runs CIDER for each. Each sample gets its own output directory with CDR3 results.
