---
name: kinship-read
category: ancient-dna
description: Relationship Estimation from Ancient DNA version 2 (READv2)
tags: [kinship-read, ancient-dna, relatedness, READv2]
author: oxo-call-community
source_url: "https://github.com/GuntherLab/READv2"
---

## Concepts

- **Ancient DNA Relatedness**: Specialized tool for estimating genetic relationships from ancient DNA samples
- **READv2 Algorithm**: Implements the Relationship Estimation from Ancient DNA version 2 algorithm
- **Contamination Handling**: Accounts for modern DNA contamination in ancient samples
- **ROH Detection**: Identifies Runs of Homozygosity to infer inbreeding and relatedness
- **Low Coverage Data**: Optimized for handling low-coverage ancient DNA sequencing data
- **Population Genetics**: Integrates population structure into relatedness estimation

## Pitfalls

- **DNA Degradation**: Highly degraded samples may produce unreliable relatedness estimates
- **Contamination Levels**: High contamination rates can distort kinship inference
- **SNP Coverage**: Insufficient coverage affects genotyping accuracy
- **Reference Panel Choice**: Reference panel selection impacts relatedness estimates
- **Population Stratification**: Ignoring population structure leads to false relationships
- **Computational Resources**: Large datasets require significant memory and processing time

## Examples

### Estimate relatedness from VCF
**Args:** `READv2 -i genotypes.vcf -o relatedness_results.csv`
**Explanation:** Estimates pairwise relatedness from ancient DNA genotype data.

### Handle contaminated samples
**Args:** `READv2 -i data.vcf -o results.csv --contamination 0.03`
**Explanation:** Adjusts relatedness estimates for 3% modern DNA contamination.

### Detect ROH regions
**Args:** `READv2 -i genotypes.vcf -o roh_results.csv --roh`
**Explanation:** Identifies Runs of Homozygosity and estimates inbreeding coefficients.

### Quality control filtering
**Args:** `READv2 -i data.vcf -o filtered.csv --min-coverage 5`
**Explanation:** Filters genotypes with minimum coverage of 5 reads.

### Generate kinship matrix
**Args:** `READv2 -i genotypes.vcf -o kinship_matrix.txt --matrix`
**Explanation:** Outputs pairwise kinship coefficients as a matrix.

### Compare with known pedigree
**Args:** `READv2 -i data.vcf -p pedigree.txt -o validation.csv --validate`
**Explanation:** Validates relatedness estimates against known pedigree information.