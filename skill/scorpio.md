---
name: scorpio
category: variant-calling
description: scorpio - Serious constellations of reoccurring phylogenetically-independent origin
tags: ["scorpio", "variant-calling", "lineage-typing", "SARS-CoV-2"]
author: oxo-call-community
source_url: "https://github.com/cov-lineages/scorpio"
---

## Concepts

- **Tool Overview**: scorpio (v0.3.19) identifies serious constellations of reoccurring phylogenetically-independent origin.
- **Core Function**: Classifies viral sequences into lineages based on characteristic mutations.
- **Algorithm**: Uses pattern matching to identify lineage-defining mutations.
- **Input/Output**: Accepts VCF files and produces lineage assignments.
- **Lineage Typing**: Specifically designed for viral lineage classification.
- **Applications**: SARS-CoV-2 variant detection, viral genomics, and lineage tracking.

## Pitfalls

- **Data Quality**: Results depend on input sequence quality.
- **Mutation Patterns**: May miss novel variants with unknown patterns.
- **Reference Genome**: Requires compatible reference genome.
- **Version Updates**: Requires regular updates for new variants.
- **False Positives**: May report false lineage assignments.
- **Computational Resources**: May require significant compute resources.

## Examples

### Basic lineage typing
**Args:** `scorpio classify -i variants.vcf -o lineage.tsv`
**Explanation:** `-i` input VCF; `-o` lineage assignments.

### With reference
**Args:** `scorpio classify -i variants.vcf -r reference.fasta -o lineage.tsv`
**Explanation:** `-r` specifies reference genome.

### Verbose output
**Args:** `scorpio classify -i variants.vcf -v -o lineage.tsv`
**Explanation:** `-v` enables verbose output for debugging.

### Update database
**Args:** `scorpio update`
**Explanation:** Updates lineage definitions database.

### List lineages
**Args:** `scorpio list`
**Explanation:** Lists available lineage definitions.

### Check version
**Args:** `scorpio version`
**Explanation:** Shows current scorpio version.

### Batch processing
**Args:** `scorpio batch -i vcf_dir/ -o results/`
**Explanation:** Processes multiple VCF files in batch.