---
name: hmftools-chord
category: utility
description: Predict homologous recombination deficiency (HRD) using somatic mutation contexts and telomeric allelic imbalance signatures.
tags: [hmftools-chord, HRD, homologous recombination deficiency, cancer, PARP inhibitor, mutational signatures]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/chord/"
---

## Concepts

- **Tool Overview**: hmftools-chord (v2.1.2) is a bioinformatics tool that predicts Homologous Recombination Deficiency (HRD) scores from somatic mutation data, providing both a composite HRD score and separate BRCA1-type and BRCA2-type probability estimates.
- **HRD Scoring Algorithm**: Analyzes three mutational signature components: SBS3 (single base substitution signature 3 associated with BRCA1/2 dysfunction), ID6 (indel signature 6), and CN17 (copy number signature 17) to calculate HRD probability.
- **Telomeric Allelic Imbalance (TAI)**: Incorporates TAI as a biomarker where unequal allelic copy numbers near telomeres indicate HRD phenotype.
- **Clinical Application**: HRD status guides PARP inhibitor (PARPi) therapy decisions in ovarian, breast, pancreatic, and prostate cancers with BRCA1/2 mutations.
- **WiGiTS Pipeline Integration**: Part of Hartwig Medical Foundation's cancer genomics analysis suite, used alongside AMBER, COBALT, and PURPLE for comprehensive tumor profiling.

## Pitfalls

- **Input VCF Quality**: CHORD requires high-quality somatic variant calls from matched tumor-normal analysis; false positives in VCF will propagate to HRD estimates.
- **Minimum Variant Count**: Requires sufficient somatic variants (typically >100) for reliable signature extraction; very low tumor cellularity samples may fail.
- **BRCA1 vs BRCA2 Distinction**: The BRCA1-type and BRCA2-type scores are probabilistic estimates, not definitive classifications; clinical interpretation should consider additional evidence.
- **Purity Dependence**: Low tumor purity (<20%) may lead to underestimation of HRD scores due to dilution of tumor-specific mutational signatures.
- **Genome Version Compatibility**: Reference genome version (GRCh37 vs GRCh38) must match between CHORD input and the variant calling pipeline.

## Examples

### Generate CHORD HRD prediction from somatic VCF
**Args:** `chord -output_dir ./chord_results -sample_id tumor_sample -somatic_vcf somatic_variants.vcf -ref_genome GRCh37_hmf`
**Explanation:** Runs CHORD analysis using somatic variants from matched tumor-normal analysis. The tool extracts mutational signatures and calculates HRD scores with BRCA1-type and BRCA2-type probabilities.

### Run CHORD with copy number and TAI data
**Args:** `chord -output_dir ./output -sample_id sample1 -somatic_vcf variants.vcf -purple_dir ./purple/ -ref_genome GRCh38_hmf`
**Explanation:** Uses PURPLE directory for copy number and TAI information to improve HRD prediction accuracy. The PURPLE output provides allele-specific copy number data.

### Generate CHORD plot and text output
**Args:** `chord -output_dir ./results -sample_id patient1 -somatic_vcf patient1_somatic.vcf -ref_genome GRCh37 -write_plot -write_text`
**Explanation:** Produces both visualization (CHORD_plot.png) and tabular (chord_scores.txt) outputs. The text output includes HRD score, BRCA1 probability, and BRCA2 probability.

### Process multiple samples in batch
**Args:** `for vcf in *.vcf; do sample=$(basename $vcf .vcf); chord -output_dir ./chord/$sample -sample_id $sample -somatic_vcf $vcf -ref_genome GRCh37_hmf; done`
**Explanation:** Iterates through all VCF files in a directory and runs CHORD for each sample. Each sample gets its own output directory.

### CHORD with explicit species and transcript parameters
**Args:** `chord -output_dir ./output -sample_id test -somatic_vcf test.vcf -ref_genome GRCh37_hmf -species human -transcripts Ensembl_v75`
**Explanation:** Specifies human species and Ensembl transcript version for gene annotation. These parameters ensure correct gene name handling for BRCA1/2.
