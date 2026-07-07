---
name: snpsplit
category: alignment
description: SNPsplit - Allele-specific alignment sorter for SNP-aware analysis
tags: [snpsplit, alignment, allele-specific, snps, bam]
author: oxo-call-community
source_url: "https://github.com/FelixKrueger/SNPsplit"
---

## Concepts

- **Tool Overview**: snpsplit (v0.6.0) - An allele-specific alignment sorting tool
- **Core Function**: Determines allelic origin of reads covering SNP positions
- **Input/Output**: Accepts BAM/SAM files; outputs allele-specific alignments
- **Algorithm**: Sorts reads based on SNP positions and allelic origin
- **Installation**: `conda install -c bioconda snpsplit`
- **Key Features**: Allele-specific sorting, SNP-aware analysis, BAM processing

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM/SAM files
- **SNP File**: Requires SNP position file for sorting
- **Reference Genome**: Must use compatible reference genome
- **Memory Usage**: Large BAM files require significant memory
- **Allele Assignment**: Ambiguous reads may not be assigned correctly
- **Output Files**: Multiple output files generated per allele

## Examples

### Display help
**Args:** `SNPsplit --help`
**Explanation:** Shows available options and usage information.

### Basic allele sorting
**Args:** `SNPsplit --sorted --bam input.bam --snps snps.txt --output_dir results/`
**Explanation:** Sort alignments by allelic origin.

### With reference genome
**Args:** `SNPsplit --sorted --bam input.bam --snps snps.txt --genome genome.fa --output_dir results/`
**Explanation:** Use reference genome for sorting.

### Unsorted BAM input
**Args:** `SNPsplit --bam input.bam --snps snps.txt --output_dir results/`
**Explanation:** Process unsorted BAM file.

### With VCF input
**Args:** `SNPsplit --sorted --bam input.bam --vcf variants.vcf --output_dir results/`
**Explanation:** Use VCF file for SNP positions.

### Generate report
**Args:** `SNPsplit --sorted --bam input.bam --snps snps.txt --output_dir results/ --report`
**Explanation:** Generate sorting report.

### Filter by coverage
**Args:** `SNPsplit --sorted --bam input.bam --snps snps.txt --output_dir results/ --min_coverage 5`
**Explanation:** Set minimum coverage threshold.

### Output statistics
**Args:** `SNPsplit --sorted --bam input.bam --snps snps.txt --output_dir results/ --stats`
**Explanation:** Output allele statistics.