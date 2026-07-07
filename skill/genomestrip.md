---
name: genomestrip
category: structural-variation
description: Genome STRiP - Discovery and genotyping of structural variation using whole-genome sequencing data.
tags: [genomestrip, structural-variation, population-genomics, sv-discovery]
author: oxo-call-community
source_url: "http://software.broadinstitute.org/software/genomestrip/"
---

## Concepts
- **Structural Variation Discovery**: Discovers structural variants in genomes.
- **Population Genomics**: Analyzes structural variation in populations.
- **Genotyping**: Genotypes structural variants.
- **Copy Number Variation**: Detects copy number variations.
- **SV Validation**: Validates structural variation calls.

## Pitfalls
- **Read Depth**: Requires sufficient read depth.
- **Population Size**: Requires adequate population size for discovery.
- **Computational Resources**: Large datasets require significant resources.
- **False Positives**: May detect false SV signals.
- **Validation**: Results require experimental validation.

## Examples
### Discover structural variants
**Args:** `genomestrip discover -i bam_list.txt -o sv_calls.vcf`
**Explanation:** Discovers structural variants from BAM files.

### Genotype variants
**Args:** `genomestrip genotype -i sv_calls.vcf -b bam_list.txt -o genotyped.vcf`
**Explanation:** Genotypes structural variants.

### Filter variants
**Args:** `genomestrip filter -i sv_calls.vcf -q 0.95 -o filtered.vcf`
**Explanation:** Filters variants by quality.

### Batch processing
**Args:** `genomestrip discover -i ./bam_files/ -o sv_calls.vcf`
**Explanation:** Processes multiple BAM files.

### Generate report
**Args:** `genomestrip discover -i bam_list.txt -o sv_calls.vcf -r report.html`
**Explanation:** Generates SV discovery report.