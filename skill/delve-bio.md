---
name: delve-bio
category: variant-calling
description: DELVE - variant caller for mixed infections and heterogeneous samples.
tags: [delve-bio, variant-calling, mixed-infection, haplotype]
author: oxo-call-community
source_url: "https://github.com/berndbohmeier/delve"
---

## Concepts

- **Tool Overview**: delve-bio (v0.2.0+) is a variant caller designed for detecting variants in mixed infection samples. It handles samples containing multiple strains, haplotypes, or subpopulations.
- **Core Function**: Calls variants in heterogeneous samples, distinguishing between different strains or haplotypes present in the sample.
- **Input/Output**: Input: BAM/CRAM files with index, reference genome. Output: VCF with variant calls including strain-specific alleles and frequencies.
- **Algorithm**: Uses statistical models to detect variants in mixed populations, estimating allele frequencies and identifying strain-specific variants.
- **Key Features**: Mixed infection analysis, strain separation, frequency estimation, supports haplotype phasing, VCF output.
- **Installation**: `conda install -c bioconda delve-bio`

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM files with adequate coverage for strain detection.
- **Strain Diversity**: May struggle with very low-frequency strains.
- **Reference Genome**: Must use appropriate reference for the pathogen.
- **Complexity**: High strain diversity may increase computational time.
- **Quality Filtering**: Requires careful quality filtering of variants.

## Examples

### Call variants from mixed infection
**Args:** `delve call --bam sample.bam --ref ref.fa --output variants.vcf`
**Explanation:** Calls variants from mixed infection sample.

### With strain frequency estimation
**Args:** `delve call --bam sample.bam --ref ref.fa --output variants.vcf --estimate-frequency`
**Explanation:** Estimate allele frequencies for each variant.

### Phase haplotypes
**Args:** `delve phase --bam sample.bam --ref ref.fa --vcf variants.vcf --output phased.vcf`
**Explanation:** Phase variants into haplotypes for strain separation.