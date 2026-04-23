---
name: singlem
category: metagenomics
description: At heart, SingleM is a tool for profiling shotgun metagenomes. It was originally designed to determine the relative abundance of bacterial and archaeal taxa in a sample. As of version 0.19.0, it can also be used to profile dsDNA phages (see Lyrebird). It shows good accuracy in estimating the relative abundances of community members, and has a particular strength in dealing with novel lineages. The method it uses also makes it suitable for some related tasks, such as assessing eukaryotic contamination, finding bias in genome recovery, and lineage-targeted MAG recovery. It can also be used as the basis for choosing metagenomes which, when coassembled, maximise the recovery of novel MAGs (see Bin Chicken).
tags: [singlem, metagenomics, sam]
author: oxo-call-community
source_url: "https://wwood.github.io/singlem"
---

## Concepts

- **Tool Overview**: singlem (v0.20.3) - At heart, SingleM is a tool for profiling shotgun metagenomes. It was originally designed to determine the relative abundance of bacterial and archaeal taxa in a sample. As of version 0.19.0, it can also be used to profile dsDNA phages (see Lyrebird). It shows good accuracy in estimating the relative abundances of community members, and has a particular strength in dealing with novel lineages. The method it uses also makes it suitable for some related tasks, such as assessing eukaryotic contamination, finding bias in genome recovery, and lineage-targeted MAG recovery. It can also be used as the basis for choosing metagenomes which, when coassembled, maximise the recovery of novel MAGs (see Bin Chicken).
- **Core Function**: At heart, SingleM is a tool for profiling shotgun metagenomes. It was originally designed to determine the relative abundance of bacterial and archaeal taxa in a sample. As of version 0.19.0, it can also be used to profile dsDNA phages (see Lyrebird). It shows good accuracy in estimating the relative abundances of community members, and has a particular strength in dealing with novel lineages. The method it uses also makes it suitable for some related tasks, such as assessing eukaryotic contamination, finding bias in genome recovery, and lineage-targeted MAG recovery. It can also be used as the basis for choosing metagenomes which, when coassembled, maximise the recovery of novel MAGs (see Bin Chicken).
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda singlem`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `singlem -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run singlem with typical input and output options.
