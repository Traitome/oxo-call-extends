---
name: cladeomatic
category: variant-calling
description: Automatic recognition of population structures based on canonical SNPs
tags: [cladeomatic, population-structure, snps, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/phac-nml/cladeomatic"
---

## Concepts

- **Tool Overview**: Clade-O-Matic is a tool for automatic recognition of population structures based on canonical SNPs, enabling clade assignment and phylogenetic classification.
- **Core Function**: Identifies and assigns isolates to clades using canonical SNP markers and reference phylogenies.
- **Algorithm**: Uses SNP patterns to classify isolates into predefined or newly discovered clades.
- **Input**: SNP alignment files (FASTA), VCF files, or SNP matrices.
- **Output**: Clade assignments, phylogenetic classifications, and visualizations.
- **Application**: Population genetics, outbreak investigation, and evolutionary epidemiology.
- **Installation**: Install via bioconda: `conda install -c bioconda cladeomatic`

## Pitfalls

- **SNP Quality**: Requires high-quality SNP calls for accurate clade assignment.
- **Reference Data**: Depends on well-characterized reference clades.
- **Data Format**: Input files must be properly formatted.
- **Computational Resources**: May require significant memory for large datasets.
- **Clade Definition**: Clade boundaries must be well-defined.

## Examples

### Run clade assignment
**Args:** `cladeomatic --input snps.fasta --reference reference.fasta --output clades.txt`
**Explanation:** Assigns isolates to clades based on canonical SNPs.

### With VCF input
**Args:** `cladeomatic --vcf genotypes.vcf --output clades.txt`
**Explanation:** Performs clade assignment from VCF file.

### Generate visualization
**Args:** `cladeomatic --input snps.fasta --visualize --output clade_tree.png`
**Explanation:** Generates visual representation of clade relationships.

### Display help
**Args:** `cladeomatic --help`
**Explanation:** Shows all available options and usage information.