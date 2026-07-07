---
name: hmftools-sigs
category: variant-calling
description: Fits sample SNV counts to trinucleotide signature definitions using COSMIC reference signatures.
tags: [hmftools-sigs, mutational-signatures, COSMIC, SNV, trinucleotide, cancer, NMF]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/sigs/README.md"
---

## Concepts

- **Tool Overview**: SIGS (v1.2) fits sample SNV counts to trinucleotide signature definitions to identify mutational processes active in a tumor sample. It decomposes the 96-channel mutation count vector (6 substitution types × 4 flanking 5' bases × 4 flanking 3' bases) into contributions from known COSMIC reference signatures using non-negative least squares optimization.

- **Trinucleotide Context Classification**: Mutations are classified by the base substitution type (C>A, C>G, C>T, T>A, T>C, T>G) together with the immediate 5' and 3' flanking bases, producing 96 possible mutation types. This captures the sequence context preferences of different mutational processes.

- **COSMIC Signature Reference**: SIGS uses COSMIC (Catalogue of Somatic Mutations in Cancer) signature definitions as the reference set. The COSMIC v3.2 signatures include 49 single-base substitution (SBS) signatures extracted from over 22,000 cancer genomes, each representing a distinct mutational process or exposure signature.

- **Signature Fitting Algorithm**: The tool uses non-negative least squares (NNLS) to decompose the observed 96-channel mutation count vector into a linear combination of reference signatures. The algorithm minimizes the residual while constraining all coefficients to be non-negative.

- **Input Requirements**: SIGS requires a somatic VCF file from tumor-normal sequencing. The VCF must contain PASS-filtered SNVs with accurate genotype information. The tool extracts the trinucleotide context for each variant using the reference genome.

- **Output Interpretation**: Output includes per-signature exposure weights indicating the contribution of each COSMIC signature to the sample. These weights can be used to infer etiologies (e.g., APOBEC activity, UV exposure, tobacco smoking) and predict therapeutic vulnerabilities.

## Pitfalls

- **VCF Filtering Quality**: Poorly filtered VCFs with false-positive SNVs will produce unreliable signature exposures. Ensure rigorous filtering (AD > 10, AF > 0.05, GQ > 30) before running SIGS. Including indels or structural variants corrupts the mutation count vector.

- **Signature Database Version**: Different COSMIC signature versions (v2, v3.1, v3.2) have different numbers and definitions of signatures. Using mismatched reference files can lead to incorrect exposure estimates. Always verify the signature file version matches your analysis protocol.

- **Coverage Bias**: Samples with low sequencing depth or high genome-wide copy number alterations may have biased mutation counts in certain contexts. Very-low-purity tumors may not have sufficient mutations for reliable signature decomposition.

- **Low Mutation Burden**: Tumors with fewer than ~100 SNVs may produce unstable signature fits due to counting noise. For low-mutation samples, consider using a reduced signature set or accepting higher uncertainty in exposures.

- **Mutational Signature Overlap**: Some COSMIC signatures are highly correlated (e.g., SBS2 and SBS13 both reflect APOBEC activity). The NNLS algorithm may split exposure between correlated signatures rather than assigning to the true source.

- **Genome Build Compatibility**: The somatic VCF and signature reference file must use the same genome build (GRCh37 or GRCh38). Mixing builds causes incorrect trinucleotide context assignment.

## Examples

### Run SIGS with COSMIC signatures
**Args:** `java -jar sigs.jar -sample tumor1 -signatures_file cosmic_signatures_v3.2.csv -somatic_vcf_file tumor1.somatic.vcf.gz -output_dir ./sigs_output/`
**Explanation:** Standard SIGS run decomposing tumor mutations into COSMIC signature contributions. The output directory will contain per-signature exposure weights and visualization files.

### Adjust minimum allocation threshold
**Args:** `java -jar sigs.jar -sample tumor1 -signatures_file cosmic_signatures.csv -somatic_vcf_file tumor1.vcf -output_dir ./sigs/ -min_alloc 0.02 -min_alloc_perc 0.001`
**Explanation:** Increases the minimum signature allocation threshold to filter out minor contributions. Use this when you want to focus on dominant signatures and reduce noise from very low-exposure signatures.

### Generate position frequency spectra
**Args:** `java -jar sigs.jar -sample tumor1 -signatures_file cosmic_signatures.csv -somatic_vcf_file tumor1.vcf -output_dir ./sigs/ -position_bucket_size 1000000 -max_sample_count 5000`
**Explanation:** Requests generation of genomic position frequency spectra, bucketing mutation positions into 1Mb intervals. The max_sample_count caps any single position bucket to prevent outliers from dominating visualization.

### Process COLO829 reference sample
**Args:** `java -jar sigs.jar -sample COLO829T -signatures_file /reference/snv_cosmic_signatures.csv -somatic_vcf_file /data/COLO829T.purple.somatic.vcf.gz -output_dir /output_dir/`
**Explanation:** Official HMF example using the COLO829T melanoma reference sample. COLO829 has well-characterized UV exposure signatures and serves as a validation dataset.

### Use custom signature reference file
**Args:** `java -jar sigs.jar -sample tumor1 -signatures_file custom_signatures.csv -somatic_vcf_file tumor1.vcf -output_dir ./sigs/`
**Explanation:** Uses a custom signature definition file instead of COSMIC. Custom signatures can represent novel processes specific to your cohort or filtered versions focusing on biologically relevant signatures.

### Batch processing multiple samples
**Args:** `for vcf in tumor_*.vcf.gz; do sample=$(basename $vcf .vcf.gz); java -jar sigs.jar -sample $sample -signatures_file cosmic.csv -somatic_vcf_file $vcf -output_dir ./batch_sigs/; done`
**Explanation:** Shell loop to process multiple tumor samples. Each sample gets its own output subdirectory. Parallelize with GNU parallel or submit as separate cluster jobs for large cohorts.

### Extract signatures for downstream analysis
**Args:** `java -jar sigs.jar -sample tumor1 -signatures_file cosmic_v3.2.csv -somatic_vcf_file tumor1.filtered.vcf -output_dir ./sigs/ && python extract_signatures.py sigs_output/`
**Explanation:** Runs SIGS then pipes output to a custom Python script for downstream tasks like signature exposure visualization, comparison to reference cohorts, or survival analysis.
