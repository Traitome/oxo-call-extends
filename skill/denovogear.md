---
name: denovogear
category: variant-calling
description: denovogear - detecting de novo mutations from parent-offspring trios.
tags: [denovogear, variant-calling, de-novo, mutation, trio]
author: oxo-call-community
source_url: "https://github.com/denovogear/denovogear"
---

## Concepts

- **Tool Overview**: denovogear (v1.1.1+) is a tool for calling de novo mutations from parent-offspring trio sequencing data. It detects new mutations present in offspring but absent in both parents.
- **Core Function**: Uses probabilistic modeling to identify de novo mutations by comparing sequence data from all three trio members (mother, father, child).
- **Input/Output**: Input: BAM/CRAM files for trio members, PED file, reference genome. Output: VCF with de novo variant calls, confidence scores.
- **Algorithm**: Uses Bayesian probabilistic models to calculate the probability of each variant being a de novo mutation.
- **Key Features**: Probabilistic de novo calling, trio analysis, high accuracy, VCF output, supports multiple sequencing platforms.
- **Installation**: `conda install -c bioconda denovogear`

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM files for all three trio members.
- **PED File**: Requires properly formatted PED file describing family relationships.
- **Reference Genome**: Must use consistent reference genome across all samples.
- **Variant Quality**: Poor quality variants may affect calling accuracy.
- **Parental Samples**: Requires high-quality parental sequencing data.

## Examples

### Detect de novo mutations from trio
**Args:** `denovogear dnm --ped trio.ped --mom mom.bam --dad dad.bam --child child.bam --ref ref.fa --output denovo.vcf`
**Explanation:** Detects de novo mutations from trio sequencing data.

### With quality filtering
**Args:** `denovogear dnm --ped trio.ped --mom mom.bam --dad dad.bam --child child.bam --ref ref.fa --output denovo.vcf --quality 30`
**Explanation:** Apply minimum quality score filter.

### Generate statistics
**Args:** `denovogear dnm --ped trio.ped --mom mom.bam --dad dad.bam --child child.bam --ref ref.fa --output denovo.vcf --stats stats.tsv`
**Explanation:** Generate detailed statistics report.