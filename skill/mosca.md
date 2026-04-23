---
name: mosca
category: alignment
description: MOSCA - Meta-Omics Software for Community Analysis
tags: [mosca, alignment]
author: oxo-call-community
source_url: "https://github.com/iquasere/MOSCA"
---

## Concepts

- **Tool Overview**: mosca v2.3.0 - MOSCA (portuguese for fly) is a pipeline designed for performing metagenomics (MG), metatranscriptomics (MT) and metaproteomics (MP) integrated data analysis, in a mostly local and fully automated workflow. Metagenomics is used to build a reference database for MT and MP, beginning with preprocessing of data for removal of Illumina adapters and lower quality regions, folowed by assembly of reads into contigs, gene calling on the contigs and homology-based and domain-based annotation of identified proteins, using the UniProt and COG databases, respectively. If available, MT reads are then aligned to the ORFs for gene expression quantification, and MP spectra are submitted for Peptide-to-Spectrum matching, with the annotated ORFs as reference database. Final steps include differential expression analysis for both MT and MP, and metabolic pathways analysis through KEGG Pathways..
- **Core Function**: MOSCA - Meta-Omics Software for Community Analysis
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mosca`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
