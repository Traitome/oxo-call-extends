---
name: eagle2
category: variant-calling
description: "The Eagle software estimates haplotype phase either within a genotyped cohort or using a phased reference panel."
tags: [eagle2, variant-calling, phasing, haplotype, imputation]
author: oxo-call-community
source_url: "https://github.com/poruloh/Eagle"
---

## Concepts

- **Tool Overview**: Eagle2 is a fast and accurate haplotype phasing tool using an HMM-based algorithm with positional Burrows-Wheeler transform for improved speed and accuracy.
- **Core Function**: Estimates haplotype phase within a genotyped cohort or using a phased reference panel.
- **Input/Output**: Input: VCF files (genotypes), reference panel (optional). Output: Phased VCF with haplotype information.
- **Algorithm**: Uses Hidden Markov Model (HMM) with positional Burrows-Wheeler transform for efficient haplotype inference.
- **Key Features**: Very fast phasing, high accuracy, supports sequence data, chrX phasing, reference-based and reference-free modes.
- **Installation**: `conda install -c bioconda eagle2`

## Pitfalls

- **Reference Panel**: Requires phased reference panel for optimal performance in reference-based mode.
- **VCF Format**: Input VCF must be properly formatted and sorted by position.
- **Memory Usage**: Large datasets may require significant RAM.
- **Version Compatibility**: Eagle1 algorithm available via --v1 flag for legacy compatibility.
- **Sample Size**: Optimal performance achieved with cohort sizes <50,000.

## Examples

### Phase VCF with reference panel
**Args:** `--vcf input.vcf --refRefHaps ref_panel.vcf --out phased.vcf`
**Explanation:** Phases genotypes using a reference panel for improved accuracy.

### Reference-free phasing
**Args:** `--vcf input.vcf --out phased.vcf`
**Explanation:** Performs phasing without using a reference panel.

### Phase chrX
**Args:** `--vcf input.vcf --refRefHaps ref_panel.vcf --out phased.vcf --chrX`
**Explanation:** Enables X chromosome phasing with proper handling of pseudo-autosomal regions.

### Use Eagle1 algorithm
**Args:** `--vcf input.vcf --refRefHaps ref_panel.vcf --out phased.vcf --v1`
**Explanation:** Uses the older Eagle1 algorithm instead of Eagle2.

### Threaded execution
**Args:** `--vcf input.vcf --refRefHaps ref_panel.vcf --out phased.vcf --numThreads 8`
**Explanation:** Uses 8 threads for faster phasing.