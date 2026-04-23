---
name: atlas
category: variant-calling
description: ATLAS - Analysis Tools for Low-depth and Ancient Samples for accurate genotyping
tags: [ancient-dna, low-depth, genotyping, pmd-aware, population-genetics]
author: oxo-call-community
source_url: "https://bitbucket.org/wegmannlab/atlas"
---

## Concepts

- **Tool Overview**: ATLAS is a suite of methods for accurate genotyping and genetic diversity estimation from ancient and low-depth samples, accounting for post-mortem damage (PMD).

- **PMD-Aware Analysis**: Explicitly models post-mortem damage patterns to improve genotyping accuracy in ancient DNA samples where damage causes sequence errors.

- **Low-Depth Optimization**: Designed for samples with low coverage, using probabilistic methods to extract maximum information from limited data.

- **BAM Input**: Works directly from BAM files, eliminating need for extensive preprocessing beyond standard alignment.

- **Complete Pipeline**: Provides tools for the entire analysis workflow from quality control to population genetic inference.

## Pitfalls

- **PMD Pattern**: Requires correct specification of PMD pattern (single-stranded vs double-stranded library) for accurate modeling.

- **Reference Bias**: Ancient DNA analyses are susceptible to reference bias. ATLAS attempts to minimize this but cannot eliminate it completely.

- **Minimum Coverage**: Very low coverage samples (<0.5x) may have unreliable genotype estimates regardless of method.

- **Reference Genome**: Requires appropriate reference genome. Poor reference choice increases bias and reduces accuracy.

## Examples

### Estimate allele frequencies
**Args:** `atlas PMD=input.bam method=alleleFreq out=alleleFreq.txt`
**Explanation:** Estimates allele frequencies from BAM file while accounting for post-mortem damage patterns.

### Genotype calling
**Args:** `atlas task=GL method=MLE bam=input.bam out=genotypes.vcf`
**Explanation:** Calls genotypes using maximum likelihood estimation, output in VCF format.

### PMD estimation
**Args:** `atlas PMD=input.bam method=estimate out=pmd_estimates.txt`
**Explanation:** Estimates post-mortem damage parameters from aligned reads for use in downstream analysis.

### Quality filtering
**Args:** `atlas task=GL method=MLE bam=input.bam minMQ=30 minBQ=20 out=genotypes.vcf`
**Explanation:** Applies quality filters (mapping quality ≥30, base quality ≥20) before genotype calling.

### Recalibrate base qualities
**Args:** `atlas recalibrate bam=input.bam out=recalibrated.bam`
**Explanation:** Recalibrates base quality scores based on observed error patterns in data.
