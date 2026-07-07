---
name: covar
category: variant-calling
description: Linked-read variant calling tool for wastewater sequencing data
tags: [covar, variant-calling, wastewater, linked-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/andersen-lab/covar"
---

## Concepts

- **Tool Overview**: CoVar is a linked-read variant calling tool specifically designed for wastewater sequencing data, enabling accurate variant detection from complex mixed samples.
- **Core Function**: Calls genetic variants from linked-read sequencing data, with special handling for the unique characteristics of wastewater samples.
- **Algorithm**: Uses linked-read information to improve variant calling accuracy in complex microbial communities.
- **Input**: Linked-read sequencing data (BAM), reference genome (FASTA).
- **Output**: Variant calls in VCF format, including allele frequencies.
- **Application**: Wastewater surveillance, pathogen detection, variant tracking in environmental samples.
- **Installation**: Install via bioconda: `conda install -c bioconda covar`

## Pitfalls

- **Sample Complexity**: Wastewater samples have high microbial diversity.
- **Contamination**: Environmental contaminants may affect results.
- **Coverage Depth**: May require deep sequencing for rare variants.
- **Reference Bias**: Requires appropriate reference genomes.
- **Computational Resources**: Large datasets may require significant memory.

## Examples

### Call variants from BAM
**Args:** `covar -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from aligned linked-read data.

### With allele frequency filter
**Args:** `covar -i aligned.bam -r reference.fasta -f 0.01 -o variants.vcf`
**Explanation:** Filters variants by minimum allele frequency of 1%.

### Specify regions
**Args:** `covar -i aligned.bam -r reference.fasta -t targets.bed -o variants.vcf`
**Explanation:** Calls variants only in specified target regions.

### Output allele frequencies
**Args:** `covar -i aligned.bam -r reference.fasta --freq -o variants.vcf`
**Explanation:** Outputs allele frequencies for each variant.

### Display help
**Args:** `covar --help`
**Explanation:** Shows all available options and usage information.