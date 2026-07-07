---
name: glnexus
category: variant-calling
description: glnexus - Scalable gVCF merging and joint variant calling for population sequencing.
tags: [glnexus, variant-calling, gVCF, joint-calling]
author: oxo-call-community
source_url: "https://github.com/dnanexus-rND/GLnexus"
---

## Concepts
- **gVCF Merging**: Merges multiple gVCF files.
- **Joint Variant Calling**: Performs joint variant calling.
- **Population Studies**: Designed for population studies.
- **Scalable**: Scalable to large cohorts.
- **VCF Format**: Outputs standard VCF format.

## Pitfalls
- **Sample Size**: Large cohorts require memory.
- **Reference Consistency**: Requires consistent reference.
- **gVCF Quality**: Depends on gVCF quality.
- **Computational Resources**: Requires resources.
- **Result Validation**: Results should be validated.

## Examples
### Merge gVCFs
**Args:** `glnexus merge -i samples.gvcf -o merged.bcf`
**Explanation:** Merges multiple gVCFs.

### Joint call
**Args:** `glnexus joint -i samples.gvcf -o joint.vcf`
**Explanation:** Performs joint variant calling.

### With config
**Args:** `glnexus merge -i samples.gvcf -c config.txt -o merged.bcf`
**Explanation:** Uses custom configuration.

### Generate report
**Args:** `glnexus merge -i samples.gvcf -r -o merged.bcf`
**Explanation:** Generates merging report.

### Batch processing
**Args:** `glnexus merge -l samples.txt -o ./merged/`
**Explanation:** Processes multiple sample sets.