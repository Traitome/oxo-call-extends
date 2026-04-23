---
name: amplici
category: variant-calling
description: AmpliCI - Model-based algorithm for denoising Illumina amplicon data with or without UMI support
tags: [amplicon, denoising, clustering, umi, haplotype, illumina]
author: oxo-call-community
source_url: "https://github.com/DormanLab/AmpliCI"
---

## Concepts

- **Tool Overview**: AmpliCI (Amplicon Clustering Inference) is a reference-free, model-based method for rapidly resolving the number, abundance, and sequence of true biological haplotypes from Illumina amplicon sequencing data. Version 2.2.
- **Core Algorithm**: Uses finite mixture model to cluster amplicon sequences, distinguishing true biological variants from sequencing errors without requiring reference sequences.
- **UMI Support**: AmpliCI-UMI variant leverages Unique Molecular Identifiers for enhanced denoising accuracy by grouping reads from the same original molecule.
- **Input Requirements**: Demultiplexed FASTQ files with uniform read length, no ambiguous nucleotides (N bases). Pre-filter with seqkit if needed.
- **Two-Step Workflow**: First estimate error profile from data, then infer haplotypes and abundances using the error model.
- **Output Files**: Generates `.fa` (FASTA haplotypes with abundance/quality metrics) and `.out` (statistical information including cluster assignments).
- **Downstream Analysis**: Recommended to use usearch for chimera detection on denoised sequences.

## Pitfalls

- **Read Length Uniformity**: All reads must have identical length. Trim or filter to uniform length before running.
- **No Ambiguous Bases**: Sequences containing 'N' must be removed. Use `seqkit grep -srv -p 'N'` to filter.
- **Error Profile Dependency**: Quality of haplotype inference depends on accurate error profile estimation from representative data.
- **Abundance Threshold**: Default `--abundance 2` may miss rare variants. Adjust based on expected diversity and sequencing depth.
- **Chimeras Not Detected**: AmpliCI does not detect chimeras. Run usearch `-uchime3_denovo` on output for chimera filtering.

## Examples

### Estimate error profile from FASTQ
**Args:** `run_AmpliCI --fastq input.fastq --outfile error_profile.out --error`
**Explanation:** First step: estimates sequencing error rates and quality score calibration from the data. Creates error profile file for subsequent haplotype inference.

### Infer haplotypes and abundances
**Args:** `run_AmpliCI --fastq input.fastq --outfile result --abundance 2 --profile error_profile.out`
**Explanation:** Second step: uses error profile to cluster reads into biological haplotypes. Outputs result.fa (sequences) and result.out (statistics). Abundance threshold filters low-frequency noise.

### Assign reads to known haplotypes
**Args:** `run_AmpliCI --fastq input.fastq --outfile assignments.out --profile error_profile.out --haplotypes known_haplotypes.fa`
**Explanation:** Reassigns reads to a predefined set of haplotypes rather than de novo clustering. Useful for targeted variant detection.

### Adjust sensitivity for rare variants
**Args:** `run_AmpliCI --fastq input.fastq --outfile result --abundance 1.5 --profile error_profile.out --contaminants 0.5`
**Explanation:** Lowers abundance threshold to detect rarer variants (1.5 vs default 2.0). Reduces contaminant baseline to 0.5 for more sensitive detection. Use cautiously to avoid false positives.

### Disable JC69 model for unrelated sequences
**Args:** `run_AmpliCI --fastq input.fastq --outfile result --profile error_profile.out --nJC69`
**Explanation:** Disables Jukes-Cantor evolutionary model when sequences are not evolutionarily related (e.g., mixed-species samples). Appropriate for non-biological clustering scenarios.

### Align all reads to haplotypes
**Args:** `run_AmpliCI --fastq input.fastq --outfile result --profile error_profile.out --align`
**Explanation:** Performs full alignment of all reads to inferred haplotypes (slower but more accurate for complex datasets). Default mode uses faster approximate assignment.
