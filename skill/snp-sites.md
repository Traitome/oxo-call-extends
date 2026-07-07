---
name: snp-sites
category: variant-analysis
description: SNP-Sites - Extract SNP sites from multi-FASTA alignments
tags: [snp-sites, variant-analysis, alignment, snps, fasta]
author: oxo-call-community
source_url: "https://sanger-pathogens.github.io/snp-sites"
---

## Concepts

- **Tool Overview**: snp-sites (v2.5.1) - A tool for extracting SNP positions from alignments
- **Core Function**: Identifies SNP sites in multi-FASTA alignment files
- **Input/Output**: Accepts FASTA alignments; outputs SNP positions or alignment
- **Algorithm**: Scans alignment for variable positions
- **Installation**: `conda install -c bioconda snp-sites`
- **Key Features**: SNP extraction, alignment processing, fast execution

## Pitfalls

- **Input Requirements**: Requires properly aligned FASTA sequences
- **Alignment Quality**: Poor alignments produce inaccurate SNP positions
- **Missing Data**: Gaps and missing data affect SNP detection
- **Output Format**: Multiple output formats available
- **Sequence Names**: Sequence names must be unique
- **Memory Usage**: Large alignments require significant memory

## Examples

### Display help
**Args:** `snp-sites --help`
**Explanation:** Shows available options and usage information.

### Extract SNP positions
**Args:** `snp-sites alignment.fasta > snps.txt`
**Explanation:** Extract SNP positions from alignment.

### Output SNP alignment
**Args:** `snp-sites -o snp_alignment.fasta alignment.fasta`
**Explanation:** Output alignment containing only SNP positions.

### Output VCF format
**Args:** `snp-sites -v -o snps.vcf alignment.fasta`
**Explanation:** Output SNPs in VCF format.

### With reference
**Args:** `snp-sites -r reference.fasta alignment.fasta > snps.txt`
**Explanation:** Use reference for SNP extraction.

### Output positions only
**Args:** `snp-sites -c alignment.fasta > positions.txt`
**Explanation:** Output SNP position coordinates only.

### Output statistics
**Args:** `snp-sites -s alignment.fasta > statistics.txt`
**Explanation:** Output SNP statistics.

### Multi-format output
**Args:** `snp-sites -v -c -o snps.vcf positions.txt alignment.fasta`
**Explanation:** Output multiple formats simultaneously.