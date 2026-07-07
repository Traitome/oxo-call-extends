---
name: ibdmix
category: population-genomics
description: "ibdmix: estimate introgression by IBD - detects introgressed segments using identity-by-descent mapping"
tags: [ibdmix, population-genomics, IBD, introgression, genetics]
author: oxo-call-community
source_url: "https://github.com/PrincetonUniversity/IBDmix"
---
## Concepts

- **Tool Overview**: ibdmix (v1.0.1) is a tool for estimating introgression using Identity-by-Descent (IBD) segments, developed by Princeton University.
- **Core Function**: Detects segments of the genome that have been introgressed from one population into another by analyzing shared IBD regions.
- **IBD Segments**: IBD segments are identical DNA sequences inherited from a common ancestor, typically spanning 4-50 generations for SNP array data.
- **Introgression Detection**: Identifies genomic regions where genetic material has been transferred between populations, useful for studying population admixture.
- **Input/Output**: Accepts VCF format genotype data and produces IBD segment calls with introgression probabilities.
- **Installation**: `conda install -c bioconda ibdmix`

## Pitfalls

- **Sample Size Requirements**: Requires large sample sizes (typically >100 individuals per population) for reliable introgression detection.
- **Reference Panel Quality**: Accuracy depends on the quality and completeness of the reference population data.
- **Segment Length Threshold**: Shorter IBD segments may be missed, affecting detection of older introgression events.
- **Population Structure**: Complex population structures can confound introgression signals.
- **Computational Resources**: Memory-intensive for large datasets; may require parallel computing.
- **Phasing Quality**: Requires accurate haplotype phasing; switch errors can reduce detection accuracy.

## Examples

### Run basic introgression analysis
**Args:** `ibdmix --vcf input.vcf --ref ref_samples.txt --target target_samples.txt --out ibdmix_results`
**Explanation:** Detects introgressed segments using IBD mapping between reference and target populations.

### With specific IBD length cutoff
**Args:** `ibdmix --vcf input.vcf --ref ref.txt --target target.txt --min-length 1.0 --out results`
**Explanation:** Sets minimum IBD segment length to 1.0 cM to filter short, potentially spurious segments.

### Generate summary statistics
**Args:** `ibdmix --vcf input.vcf --ref ref.txt --target target.txt --stats --out results`
**Explanation:** Produces additional summary statistics including mean segment length and introgression proportion.

### Parallel processing mode
**Args:** `ibdmix --vcf input.vcf --ref ref.txt --target target.txt --threads 8 --out results`
**Explanation:** Uses 8 threads for parallel computation to speed up analysis on multi-core systems.

### Filter by allele frequency
**Args:** `ibdmix --vcf input.vcf --ref ref.txt --target target.txt --maf 0.01 --out results`
**Explanation:** Filters SNPs with minor allele frequency below 0.01 to improve marker quality.