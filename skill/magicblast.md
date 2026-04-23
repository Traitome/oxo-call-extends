---
name: magicblast
category: alignment
description: NCBI BLAST next generation read mapper
tags: [magicblast, alignment]
author: oxo-call-community
source_url: "https://ncbi.github.io/magicblast/"
---

## Concepts

- **Tool Overview**: magicblast v1.7.0 - Magic-BLAST is a tool for mapping large next-generation RNA or DNA sequencing runs against a whole genome or transcriptome. Each alignment optimizes a composite score, taking into account simultaneously the two reads of a pair, and in case of RNA-seq, locating the candidate introns and adding up the score of all exons. This is very different from other versions of BLAST, where each exon is scored as a separate hit and read-pairing is ignored.  Magic-BLAST incorporates within the NCBI BLAST code framework ideas developed in the NCBI Magic pipeline, in particular hit extensions by local walk and jump (http://www.ncbi.nlm.nih.gov/pubmed/26109056), and recursive clipping of mismatches near the edges of the reads, which avoids accumulating artefactual mismatches near splice sites and is needed to distinguish short indels from substitutions near the edges.  More details about the algorithm and comparison with other similar tools are presented here: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2996-x..
- **Core Function**: NCBI BLAST next generation read mapper
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda magicblast`

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
