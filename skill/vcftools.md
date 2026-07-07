---
name: vcftools
category: utility
description: A set of tools written in Perl and C++ for working with VCF files.
tags: [vcftools, utility, vcf, variant-calling, filtering]
author: oxo-call-community
source_url: "https://vcftools.github.io"
---

## Concepts

- **Tool Overview**: VCFtools (v0.1.17+) is a suite of tools for working with Variant Call Format (VCF) files. It provides filtering, statistics, and conversion utilities for variant analysis.
- **Core Function**: Manipulates and analyzes VCF files, including filtering variants, calculating statistics, converting formats, and merging files.
- **Input/Output**: Input: VCF file (compressed or uncompressed). Output: Filtered VCF, statistics files, or converted formats.
- **Algorithm**: Processes VCF files line by line, applying filters based on user-defined criteria such as quality, depth, allele frequency, and genotype.
- **Key Features**: Supports VCF version 4.0-4.3, handles compressed files, calculates various statistics, and provides flexible filtering options.
- **Installation**: `conda install -c bioconda vcftools`

## Pitfalls

- **VCF Format**: Ensure VCF files are properly formatted and follow VCF specification. Malformed VCF files may cause errors.
- **Compression**: VCFtools can read gzipped VCF files directly. Use `.vcf.gz` extension for automatic detection.
- **Filtering Order**: Filters are applied sequentially. Consider the order when combining multiple filters.
- **Memory Usage**: Processing large VCF files may require significant memory. Use `--temp` option to specify temporary directory.
- **Output Redirection**: Some commands output to stdout by default. Redirect output to a file with `>`.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Filter VCF by quality
**Args:** `--vcf input.vcf --minQ 30 --recode --out filtered`
**Explanation:** Filters variants with quality >= 30, outputs filtered VCF as filtered.recode.vcf.

### Remove indels, keep only SNPs
**Args:** `--vcf input.vcf --remove-indels --recode --out snps_only`
**Explanation:** Removes indels from VCF, keeping only SNPs in the output.

### Calculate allele frequency
**Args:** `--vcf input.vcf --freq --out allele_freq`
**Explanation:** Calculates allele frequency for each variant and outputs to allele_freq.frq.

### Filter by genotype quality
**Args:** `--vcf input.vcf --minGQ 20 --recode --out filtered`
**Explanation:** Filters variants with minimum genotype quality of 20.

### Extract specific samples
**Args:** `--vcf input.vcf --keep sample_list.txt --recode --out selected_samples`
**Explanation:** Extracts variants for samples listed in sample_list.txt (one sample per line).

### Calculate missing data statistics
**Args:** `--vcf input.vcf --missing-indv --out missing_stats`
**Explanation:** Calculates missing data per individual and outputs to missing_stats.imiss.

### Filter by depth
**Args:** `--vcf input.vcf --minDP 5 --maxDP 100 --recode --out filtered`
**Explanation:** Filters variants with depth between 5 and 100 reads.

### Convert VCF to BED format
**Args:** `--vcf input.vcf --bed --out variants.bed`
**Explanation:** Converts VCF coordinates to BED format for downstream analysis.

### Calculate Hardy-Weinberg equilibrium
**Args:** `--vcf input.vcf --hardy --out hwe_stats`
**Explanation:** Calculates Hardy-Weinberg equilibrium statistics for each variant.

### Merge multiple VCF files
**Args:** `--merge input1.vcf input2.vcf --out merged`
**Explanation:** Merges multiple VCF files into a single VCF file.