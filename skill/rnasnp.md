---
name: rnasnp
category: utility
description: Efficient detection of local RNA secondary structure changes induced by SNPs; compares wild-type vs mutant RNA structures and reports significant changes in MFE, ensemble defect, or base-pairing pattern.
tags: ["rnasnp", "snp", "rna-secondary-structure", "structure-disruption", "mfe", "ensemble-defect"]
author: oxo-call-community
source_url: "http://rth.dk/resources/rnasnp/software"
---

## Concepts

- **Tool Overview**: RNAsnp (v1.2, Radzikowski / DTU Bioinformatics) is a tool for detecting local RNA secondary structure changes induced by SNPs. For each SNP, it computes the structure of a window around the SNP for both wild-type and mutant sequences, then reports a p-value for the structural change based on a permutation test of shuffled sequences.
- **Core Function**: Takes a VCF file with SNP coordinates and a reference FASTA (transcriptome or genome), and reports per-SNP structural-disruption scores. The output is a TSV with columns: `SNP_id, position, ref_allele, alt_allele, d_ens, p_value, significant`. The recommended downstream step is to map these to eQTL/GWAS hits.
- **Algorithm**: For each SNP, extracts a sequence window (default 200 nt, centered on the SNP; configurable via `-w`), folds the wild-type and mutant windows with ViennaRNA's RNAfold, computes the ensemble defect (`d_ens` = 1 - sum_i (p_i^ref * p_i^mut) over all base pairs), and tests significance by comparing to a null distribution from shuffled sequences (preserving dinucleotide composition). The p-value is from a Gaussian fit to the null.
- **Input Format**: A VCF file (one or more SNPs; INDELs are skipped) and a reference FASTA. The VCF must be coordinate-sorted and indexed with `tabix`. The reference can be a transcriptome (transcript IDs as chromosomes) or a genome with a separate GTF for window extraction.
- **Output Format**: A TSV with one row per SNP: `SNP_id, chromosome, position, ref_allele, alt_allele, d_ens, p_value, significant`. The `significant` column is TRUE for p-value < 0.05 (configurable). Larger `d_ens` means stronger structural disruption.
- **Use Case**: Prioritizing eQTL SNPs that may act via RNA structure (a small but biologically important class of regulatory variants), annotating GWAS hits with a structural-disruption score, and identifying SNPs that switch miRNA-mRNA duplex stability.

## Pitfalls

- **CRITICAL — Reference FASTA must be the same build as the VCF**: A VCF with GRCh38 coordinates cannot be analyzed against a GRCh37 FASTA; the script silently reports the wild-type and mutant MFE without error, but the per-SNP coordinates will not match the variant. Verify with `bcftools view -H input.vcf | head` and `samtools faidx ref.fa | head`.
- **CRITICAL — INDELs are silently skipped**: RNAsnp only handles SNVs; an INDEL in the VCF produces a row with `d_ens = 0` and a `significant = FALSE` value, which looks like "no effect" but is actually a skip. Pre-filter with `bcftools view -v snps input.vcf > snps_only.vcf`.
- **The default window size (200 nt) is too small for long-range structures**: A 200-nt window captures local stem changes but misses helices that span > 200 nt. For lncRNAs with long-range structure, increase the window to 400–600 nt via `-w` (slows the run O(n²) in window length).
- **Multiple testing correction is NOT applied**: The output p-values are per-SNP and uncorrected; for a VCF with 10,000 SNPs, ~500 will be "significant" by chance. Apply Benjamini-Hochberg or Bonferroni before claiming enrichment.
- **ViennaRNA's RNAfold is a runtime dependency**: RNAsnp calls RNAfold internally. The Bioconda recipe pulls it; verify with `RNAfold --version`.
- **`-p` is the number of permutations, not the p-value**: The number of shuffled sequences to generate for the null distribution. Default is 1000; increase to 10,000 for more accurate p-values (especially for small p-values).

## Examples

### Standard SNP-vs-structure analysis
**Args:** `RNAsnp -i snps.vcf -r ref.fa -o structure_effects.tsv`
**Explanation:** `-i` is the VCF, `-r` is the reference FASTA, `-o` is the output TSV. The output has one row per SNP with `d_ens` (ensemble defect) and `p_value`. Use `awk '$8=="TRUE" {print}'` to get the significant hits.

### Increase the folding window
**Args:** `RNAsnp -i snps.vcf -r ref.fa -w 400 -o structure_effects_w400.tsv`
**Explanation:** `-w 400` doubles the default window size to 400 nt, capturing longer-range structural elements. Doubles the runtime per SNP; use only for lncRNAs or full mRNA analyses.

### Increase permutation count for small p-values
**Args:** `RNAsnp -i snps.vcf -r ref.fa -p 10000 -o structure_effects_10k.tsv`
**Explanation:** `-p 10000` increases the number of shuffled sequences for the null distribution from the default 1000 to 10,000, giving more accurate p-values for SNPs with very small d_ens values. ~10× slower than default.

### Restrict to SNPs in a specific gene
**Args:** `tabix snps.vcf.gz chr1:1000000-2000000 | RNAsnp -i - -r ref.fa -o chr1_region.tsv`
**Explanation:** `tabix` extracts SNPs in the region chr1:1000000-2000000; pipe to RNAsnp via stdin. The output is restricted to SNPs in that region. Useful for gene-level analyses.

### Filter to a custom significance threshold
**Args:** `RNAsnp -i snps.vcf -r ref.fa --pvalue-threshold 0.01 -o effects.tsv`
**Explanation:** `--pvalue-threshold 0.01` lowers the significance threshold from the default 0.05 to 0.01, reducing the false-positive rate. Combine with multiple-testing correction (BH) on the output for stricter analysis.

### Use a transcriptome reference
**Args:** `RNAsnp -i snps.vcf -r transcripts.fa -o effects_transcriptome.tsv`
**Explanation:** When the VCF uses transcript IDs as chromosome names (e.g., from a transcript-level quantification tool), pass a transcriptome FASTA. The window is then extracted from the transcript directly, avoiding genome-to-transcript coordinate translation.

### Output mode with structural details
**Args:** `RNAsnp -i snps.vcf -r ref.fa -m extended -o effects_extended.tsv`
**Explanation:** `-m extended` (older versions) or `--output-format extended` (v1.2+) writes the MFE structures, ensemble diversity, and base-pair probabilities for both wild-type and mutant, in addition to the per-SNP `d_ens`. Useful for visualizing the structural change in VARNA.
