---
name: kin
category: ancient-dna
description: A tool to estimate pairwise relatedness from ancient DNA, taking in account contamination, ROH, ascertainment bias.
tags: [kin, ancient-dna, relatedness, contamination, ROH]
author: oxo-call-community
source_url: "https://github.com/DivyaratanPopli/Kinship_Inference/blob/main/README.md"
---

## Concepts

- **Ancient DNA Analysis**: Specialized for analyzing degraded DNA from ancient samples
- **Relatedness Estimation**: Computes genetic relatedness while accounting for ancient DNA-specific challenges
- **Contamination Correction**: Models and corrects for modern DNA contamination
- **ROH Detection**: Identifies Runs of Homozygosity to infer inbreeding
- **Ascertainment Bias**: Corrects for bias introduced by SNP selection methods
- **Population Genetics**: Integrates population structure into relatedness estimation

## Pitfalls

- **DNA Degradation**: Highly degraded samples may yield unreliable estimates
- **Contamination Levels**: High contamination can distort relatedness estimates
- **SNP Coverage**: Low coverage affects genotyping accuracy and kinship estimation
- **Reference Genome Choice**: Different reference genomes can impact results
- **Population Stratification**: Ignoring population structure leads to false positives
- **Statistical Power**: Small sample sizes reduce detection power for distant relationships

## Examples

### Estimate relatedness from VCF
**Args:** `kin -i ancient_genotypes.vcf -o relatedness_results.csv`
**Explanation:** Estimates pairwise relatedness from ancient DNA genotype data.

### Correct for contamination
**Args:** `kin -i genotypes.vcf -o corrected.csv --contamination 0.05`
**Explanation:** Adjusts relatedness estimates accounting for 5% contamination.

### Detect Runs of Homozygosity
**Args:** `kin -i data.vcf -o roh_results.csv --roh`
**Explanation:** Identifies ROH regions and estimates inbreeding coefficients.

### Compare populations
**Args:** `kin -i sample1.vcf -i sample2.vcf -o comparison.csv --compare`
**Explanation:** Compares relatedness patterns between two populations.

### Validate kinship estimates
**Args:** `kin -i genotypes.vcf -o validated.csv --validate`
**Explanation:** Validates kinship estimates using known pedigree information.

### Generate comprehensive report
**Args:** `kin -i ancient.vcf -o report.pdf --report`
**Explanation:** Generates a PDF report with relatedness estimates and quality metrics.