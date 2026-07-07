---
name: bcftools-snvphyl-plugin
category: variant-calling
description: bcftools-snvphyl-plugin - SNVPhyl pipeline plugin for microbial phylogenomics
tags: [bcftools-snvphyl-plugin, variant-calling, microbial-genomics, phylogenomics, SNV]
author: oxo-call-community
source_url: "https://github.com/phac-nml/snvphyl-tools"
---

## Concepts

- **Tool Overview**: bcftools-snvphyl-plugin (v1.9) is a bcftools C plugin for the SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline, enabling identification of SNVs within microbial genomes and phylogenetic tree construction.
- **Core Function**: Identifies Single Nucleotide Variants (SNVs) in microbial genomes and constructs phylogenetic trees for comparative genomics.
- **Microbial Focus**: Optimized for microbial genome analysis and outbreak investigation.
- **Phylogenetic Tree Construction**: Generates phylogenetic trees from SNV profiles.
- **bcftools Integration**: Works as a C plugin for bcftools for efficient variant processing.
- **Input/Output**: Accepts VCF files; outputs SNV matrices and phylogenetic trees.
- **Installation**: `conda install -c bioconda bcftools-snvphyl-plugin`.

## Pitfalls

- **bcftools Dependency**: Requires bcftools to be installed and configured.
- **Microbial Genomes**: Designed specifically for microbial (bacterial/viral) genomes.
- **Reference Genome**: Requires high-quality reference genome for accurate SNV calling.
- **Phylogenetic Assumptions**: Tree construction assumptions may affect results.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Extract SNVs for phylogenomics
**Args:** `bcftools +snvphyl -i variants.vcf -o snv_matrix.txt`
**Explanation:** Extracts SNVs for phylogenetic analysis from VCF file.

### Filter by quality
**Args:** `bcftools +snvphyl -i variants.vcf -q 30 -o snv_matrix.txt`
**Explanation:** Filters SNVs by quality score before extraction.

### Include indels
**Args:** `bcftools +snvphyl -i variants.vcf --include-indels -o snv_matrix.txt`
**Explanation:** Includes indels in addition to SNVs for analysis.

### Multiple samples
**Args:** `bcftools +snvphyl -i sample1.vcf sample2.vcf sample3.vcf -o snv_matrix.txt`
**Explanation:** Processes multiple samples for comparative analysis.

### Output FASTA format
**Args:** `bcftools +snvphyl -i variants.vcf --fasta -o snv_alignment.fasta`
**Explanation:** Outputs SNV alignment in FASTA format for tree building.

### Generate distance matrix
**Args:** `bcftools +snvphyl -i variants.vcf --distance -o distance_matrix.txt`
**Explanation:** Generates pairwise distance matrix between samples.

### Display help
**Args:** `bcftools +snvphyl --help`
**Explanation:** Shows all available command-line options and usage information.