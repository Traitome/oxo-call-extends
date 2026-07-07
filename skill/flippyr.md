---
name: flippyr
category: formatting
description: "Flippyr aligns PLINK filesets with FASTA reference genomes, fixing strand flipping and reversed alleles."
tags: [flippyr, formatting, plink, genotype, reference-genome, bioinformatics, genetics]
author: oxo-call-community
source_url: "https://github.com/BEFH/flippyr"
---

## Concepts
- **Tool Overview**: Flippyr ensures PLINK genotype files are properly aligned to a FASTA reference genome. It identifies and fixes strand flipping, reversed alleles, and removes problematic sites.
- **Core Function**: Aligns PLINK filesets with reference genomes by correcting strand issues and filtering ambiguous or mismatched sites.
- **Input/Output**: Input: PLINK binary files (.bed, .bim, .fam), FASTA reference genome. Output: Aligned PLINK files, report of changes.
- **Strand Correction**: Detects and fixes strand flipping (A/T or C/G swaps) to match reference genome orientation.
- **Filtering**: Removes ambiguous palindromic alleles, multi-allelic sites, and indels by default.
- **Allele Matching**: Verifies alleles match reference genome and removes mismatched sites.
- **Installation**: `conda install -c bioconda flippyr` or clone from GitHub.

## Pitfalls
- **Reference Genome Compatibility**: Reference genome must match the build used for variant calling. Mismatched builds cause incorrect alignment.
- **Palindromic SNPs**: Removes palindromic SNPs (A/T, C/G) which cannot be reliably strand-aligned. May reduce dataset size.
- **Multi-allelic Sites**: Default behavior removes multi-allelic sites. Use --keep-multiallelic to retain them.
- **Indel Handling**: Indels are removed by default. Consider pre-filtering indels before running flippyr.
- **PLINK Format**: Requires binary PLINK format (.bed, .bim, .fam). Convert other formats first.
- **Memory Usage**: Large datasets require significant memory. Process in chunks if needed.

## Examples
### Basic PLINK alignment
**Args:** `flippyr --bfile input --ref reference.fasta --out aligned`
**Explanation:** Aligns PLINK files to reference genome, fixing strand issues and filtering problematic sites.

### Keep multi-allelic sites
**Args:** `flippyr --bfile input --ref reference.fasta --out aligned --keep-multiallelic`
**Explanation:** Retains multi-allelic sites that would normally be removed.

### Keep indels
**Args:** `flippyr --bfile input --ref reference.fasta --out aligned --keep-indels`
**Explanation:** Preserves indel sites during alignment.

### Generate detailed report
**Args:** `flippyr --bfile input --ref reference.fasta --out aligned --report report.txt`
**Explanation:** Creates detailed report showing which SNPs were flipped, removed, or kept.

### Dry run mode
**Args:** `flippyr --bfile input --ref reference.fasta --dry-run`
**Explanation:** Shows what changes would be made without modifying files.
