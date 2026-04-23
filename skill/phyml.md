---
name: phyml
category: population-genomics
description: Phylogenetic estimation using (Maximum) Likelihood
tags: [phyml, population-genomics]
author: oxo-call-community
source_url: "http://www.atgc-montpellier.fr/phyml/"
---

## Concepts
- **Tool Overview**: PhyML is a software that estimates maximum likelihood phylogenies from alignments of nucleotide or amino acid sequences. The main strength of PhyML lies in the large number of substitution models coupled to various options to search the space of phylogenetic tree topologies, going from very fast and efficient methods to slower but generally more accurate approaches. PhyML was designed to process moderate to large data sets. In theory, alignments with up to 4,000 sequences 2,000,000 character-long can be processed. PhyML can process data sets made of multiple genes and fit sophisticated substitution models with heterogeneous components across partition elements.
- **Core Function**: Phylogenetic estimation using (Maximum) Likelihood
- **Input/Output**: FASTA/BAM/SAM/GFF/GTF
- **Installation**: `conda install -c bioconda phyml`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
