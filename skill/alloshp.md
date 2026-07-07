---
name: alloshp
category: alignment
description: Pipeline for detecting Single Homeologous Polymorphisms (SHPs) from mapped reads for phylogenetic studies of allopolyploids
tags: [alloshp, allopolyploid, SHP, homeologous-polymorphisms, phylogenetics, synteny]
author: oxo-call-community
source_url: "https://github.com/eead-csic-compbio/AlloSHP"
---

## Concepts

- **Tool Overview**: AlloSHP is a command-line tool for detecting and extracting Single Homeologous Polymorphisms (SHPs) from the subgenomes of allopolyploid species, enabling phylogenetic analysis without requiring genome assembly.
- **Core Function**: Integrates three main algorithms (WGA, VCF2ALIGNMENT, VCF2SYNTENY) to compute Whole Genome Alignments and discover SHPs from reads mapped to concatenated genome sequences.
- **Key Innovation**: Enables evolutionary analysis of allopolyploids without assembling and annotating their genomes, using only a VCF file and reference genomes of diploid progenitor species.
- **Pipeline Steps**: WGA (Whole Genome Alignment) → VCF2ALIGNMENT → VCF2SYNTENY
- **Supported Organisms**: Validated on Brachypodium, Brassica, Triticum-Aegilops complexes and synthetic hybrid yeasts
- **Input/Output**: Input: VCF file with reads mapped to concatenated references, FASTA reference genomes. Output: Multiple sequence alignments of subgenomes.
- **Installation**: Install via bioconda: `conda install -c bioconda alloshp`
- **Citation**: Sancho R, Catalán P, Vogel JP, Contreras-Moreira B (2025). AlloSHP: deconvoluting single homeologous polymorphism for phylogenetic analysis of allopolyploids. Plant Methods 21:134.
- **License**: Apache-2.0

## Pitfalls

- **Reference Genomes**: Requires reference genomes of known or closest extant diploid progenitor species.
- **VCF Quality**: Input VCF must have reads mapped to concatenated reference genomes.
- **Synteny Files**: Requires synteny-based equivalent positions in BED format (produced by WGA).
- **Computational Resources**: Whole genome alignment can be computationally intensive for large genomes.
- **Outgroup Handling**: Outgroup genomes need special configuration in the synteny file.

## Examples

### Display help information
**Args:** `alloshp --help`
**Explanation:** Shows available command-line options and usage instructions.

### Run complete pipeline
**Args:** `alloshp -v variants.vcf.gz -c config.txt -o output_dir`
**Explanation:** Runs the complete AlloSHP pipeline with VCF file and configuration.

### Whole Genome Alignment (WGA) step
**Args:** `alloshp wga -r ref_genomes/ -o wga_output/`
**Explanation:** Performs whole genome alignment on reference genomes.

### VCF to Alignment conversion
**Args:** `alloshp vcf2alignment -v variants.vcf.gz -c config.txt -o alignments/`
**Explanation:** Converts VCF to multiple sequence alignments.

### Synteny-based mapping
**Args:** `alloshp vcf2synteny -v variants.vcf.gz -s synteny.bed -o synteny_output/`
**Explanation:** Uses synteny information to map polymorphisms back to chromosome positions.

### Run with outgroup
**Args:** `alloshp -v variants.vcf.gz -c config.txt -o output_dir -g outgroup.fasta`
**Explanation:** Includes outgroup genome for phylogenetic analysis.

### Set minimum depth
**Args:** `alloshp -v variants.vcf.gz -c config.txt -o output_dir -d 5`
**Explanation:** Sets minimum read depth to 5 for variant calling.

### Output VCF format
**Args:** `alloshp -v variants.vcf.gz -c config.txt -o output_dir --vcf`
**Explanation:** Outputs results in VCF format in addition to FASTA.

### Run in verbose mode
**Args:** `alloshp -v variants.vcf.gz -c config.txt -o output_dir --verbose`
**Explanation:** Runs with verbose output showing detailed processing information.
