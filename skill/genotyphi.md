---
name: genotyphi
category: microbial-genomics
description: GenoTyphi - Assign genotypes to Salmonella Typhi genomes based on VCF files mapped to Typhi CT18 reference genome.
tags: [genotyphi, salmonella, microbial-genomics, VCF]
author: oxo-call-community
source_url: "https://github.com/typhoidgenomics/genotyphi"
---

## Concepts
- **Salmonella Genotyping**: Genotypes Salmonella Typhi strains.
- **VCF Analysis**: Analyzes VCF files for genotyping.
- **Reference Mapping**: Uses Typhi CT18 as reference.
- **Phylogenetic Analysis**: Supports phylogenetic classification.
- **Outbreak Tracking**: Helps track disease outbreaks.

## Pitfalls
- **Reference Specificity**: Designed specifically for Salmonella Typhi.
- **Mapping Quality**: Requires accurate mapping to reference.
- **Data Quality**: Requires high-quality sequencing data.
- **Database Updates**: Requires regular database updates.
- **Validation**: Results should be validated experimentally.

## Examples
### Genotype Salmonella
**Args:** `genotyphi -i variants.vcf -o genotype.txt`
**Explanation:** Assigns genotype to Salmonella Typhi from VCF.

### Batch processing
**Args:** `genotyphi -i ./vcfs/ -o ./genotypes/`
**Explanation:** Processes multiple VCF files in batch.

### Update database
**Args:** `genotyphi --update-db`
**Explanation:** Updates reference database.

### Generate report
**Args:** `genotyphi -i variants.vcf -r -o report.html`
**Explanation:** Generates genotyping report.

### Validate genotype
**Args:** `genotyphi -i variants.vcf -v -o validation.txt`
**Explanation:** Validates genotype prediction.