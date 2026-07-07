---
name: comebin
category: assembly
description: Metagenomic contig binning using contrastive multi-view representation learning
tags: [comebin, metagenomics, binning, deep-learning, assembly]
author: oxo-call-community
source_url: "https://github.com/ziyewang/COMEBin"
---

## Concepts

- **Tool Overview**: COMEBin is an effective metagenomic contig binning tool that uses Contrastive Multi-view rEpresentation learning to cluster contigs into genome bins.
- **Core Function**: Bins metagenomic contigs into draft genomes using deep learning-based representation learning from multiple data views.
- **Algorithm**: Employs contrastive learning to integrate sequence composition, coverage patterns, and other features for improved binning accuracy.
- **Input**: Assembled contigs in FASTA format, optional coverage information from multiple samples.
- **Output**: Binned contigs grouped into metagenome-assembled genomes (MAGs).
- **Application**: Metagenome analysis, MAG recovery, and microbial community characterization.
- **Installation**: Install via bioconda: `conda install -c bioconda comebin`

## Pitfalls

- **Coverage Data**: Benefits from multiple samples with varying coverage profiles.
- **Contig Length**: Short contigs may bin less accurately.
- **Computational Resources**: Deep learning approach requires GPU for optimal performance.
- **Training Data**: Pre-trained models may not generalize to all environments.
- **Parameter Tuning**: May require adjustment for complex metagenomes.

## Examples

### Bin metagenomic contigs
**Args:** `comebin -i contigs.fasta -o bins/`
**Explanation:** Bins assembled contigs into metagenome-assembled genomes.

### With coverage information
**Args:** `comebin -i contigs.fasta -c coverage.tsv -o bins/`
**Explanation:** Uses coverage information from multiple samples for improved binning.

### With custom model
**Args:** `comebin -i contigs.fasta -m model.pth -o bins/`
**Explanation:** Uses custom pre-trained model for binning.

### Display help
**Args:** `comebin --help`
**Explanation:** Shows all available options and usage information.