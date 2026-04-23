---
name: eukbin
category: utility
description: "BUSCO-guided binning for eukaryotic metagenomes"
tags: [eukbin, utility]
author: oxo-call-community
source_url: "https://github.com/weiwei12456/eukbin/blob/main/README.md"
---

## Concepts
- **Tool Overview**: EukBin is a specialized binning tool for eukaryotic metagenomes that combines repeat-masked tetranucleotide frequency (TNF), multi-sample coverage information, BUSCO marker gene constraints, and deep learning (β-VAE with contrastive loss) with ploidy-aware refinement.  Key features: - Repeat-masked TNF features to handle repeat-rich eukaryotic genomes - BUSCO-guided constraints for accurate bin estimation - Ploidy-aware refinement (haplotig detection for diploid/polyploid genomes) - Deep learning with β-VAE and contrastive loss - Supports multi-sample binning  This package includes: - eukbin run: Complete binning pipeline (M1-M6 modules) - eukbin evaluate: Quality assessment for any binning tool - eukbin report: Multi-tool comparison report
- **Core Function**: BUSCO-guided binning for eukaryotic metagenomes
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ/BAM/VCF/GFF)
- **Installation**: `conda install -c bioconda eukbin`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
