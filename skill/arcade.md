---
name: arcade
category: variant-calling
description: ARCADE - Allelic Recoding via gram-Schmidt for Dominance Effects
tags: [arcade, variant-calling, genetics, dominance-effects, association-analysis]
author: oxo-call-community
source_url: "https://frhl.github.io/call_chets"
---

## Concepts

- **Tool Overview**: ARCADE (Allelic Recoding via gram-Schmidt for Dominance Effects) is a tool for encoding biallelic variants for non-additive genetic association analysis. Version 1.0.17.
- **Core Function**: Recodes genetic variants to enable detection of dominance effects and non-additive genetic associations in population genetic studies.
- **Biallelic Encoding**: Converts standard variant calls into encodings that capture additive, dominance, and epistasis effects.
- **Genetic Association**: Enables more comprehensive association analysis beyond additive genetic models.
- **Input/Output**: Processes VCF/BCF files and outputs encoded genotypes for downstream analysis.
- **Installation**: `conda install -c bioconda arcade` or build from source on GitHub.

## Pitfalls

- **Input Variant Quality**: Requires high-quality biallelic SNV calls. Multiallelic sites need prior decomposition.
- **Reference Allele Assignment**: Dominance encoding depends on correct reference/alternate allele assignment.
- **Software Dependencies**: May require GSL (GNU Scientific Library) for compilation.
- **Memory Requirements**: Large VCF files require significant memory for encoding operations.
- **Output Format**: Output format may need adaptation for specific statistical software.

## Examples

### Display help
**Args:** `arcade --help`
**Explanation:** Shows all available command-line options and usage information.

### Encode biallelic variants
**Args:** `arcade encode --vcf input.vcf --out encoded_variants.csv`
**Explanation:** Encodes biallelic variants from VCF file into dominance-aware format.

### Dominance analysis
**Args:** `arcade dominance --vcf input.vcf --ped pedigree.ped --out dominance_scores.csv`
**Explanation:** Performs dominance effect analysis using pedigree information.

### Multi-population encoding
**Args:** `arcade encode --vcf populations.vcf --pop popmap.txt --out encoded.csv`
**Explanation:** Encodes variants across multiple populations with population-specific reference alleles.

### Statistical testing
**Args:** `arcade test --encoded encoded.csv --phenotype traits.txt --method dominant --out results.csv`
**Explanation:** Runs association tests for dominance effects on encoded variants.

### Extract specific variants
**Args:** `arcade filter --vcf input.vcf --regions genes.bed --out filtered_variants.vcf`
**Explanation:** Filters VCF to specific genomic regions before encoding.