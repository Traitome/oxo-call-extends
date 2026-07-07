---
name: snpiphy
category: phylogenetics
description: snpiphy - Automated SNP phylogeny pipeline
tags: [snpiphy, phylogenetics, snps, pipeline, phylogeny]
author: oxo-call-community
source_url: "https://github.com/bogemad/snpiphy"
---

## Concepts

- **Tool Overview**: snpiphy (v0.5) - An automated pipeline for SNP-based phylogeny
- **Core Function**: Generates phylogenetic trees from SNP data
- **Input/Output**: Accepts VCF/FASTA files; outputs phylogenetic trees
- **Algorithm**: Integrates SNP extraction, alignment, and tree building
- **Installation**: `conda install -c bioconda snpiphy`
- **Key Features**: Automated pipeline, SNP phylogeny, tree generation

## Pitfalls

- **Input Requirements**: Requires properly formatted SNP data
- **Tree Method**: Choice of tree building method affects results
- **Bootstrap Support**: Requires bootstrap for tree reliability
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for large trees
- **Interpretation**: Trees require biological interpretation

## Examples

### Display help
**Args:** `snpiphy --help`
**Explanation:** Shows available options and usage information.

### Basic phylogeny
**Args:** `snpiphy -i snps.vcf -o phylogeny/`
**Explanation:** Generate phylogenetic tree from SNPs.

### With FASTA input
**Args:** `snpiphy -i alignment.fasta -o phylogeny/`
**Explanation:** Generate tree from FASTA alignment.

### With bootstrap
**Args:** `snpiphy -i snps.vcf -o phylogeny/ --bootstrap 100`
**Explanation:** Generate tree with bootstrap support.

### Set tree method
**Args:** `snpiphy -i snps.vcf -o phylogeny/ --method maximum-likelihood`
**Explanation:** Use maximum likelihood tree method.

### Output formats
**Args:** `snpiphy -i snps.vcf -o phylogeny/ --format newick`
**Explanation:** Output tree in Newick format.

### With alignment
**Args:** `snpiphy -i snps.vcf -o phylogeny/ --output-alignment`
**Explanation:** Output SNP alignment used for tree.

### Generate report
**Args:** `snpiphy -i snps.vcf -o phylogeny/ --report`
**Explanation:** Generate phylogeny report.