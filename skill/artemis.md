---
name: artemis
category: annotation
description: A set of Java genome visualization tools including the Artemis genome browser & annotation tool, ACT DNA sequence comparison viewer, DNA Plotter image generation tool and the BamView BAM/CRAM file viewer.
tags: [artemis, annotation, BAM, CRAM]
author: oxo-call-community
source_url: "http://sanger-pathogens.github.io/Artemis/"
---

## Concepts

- **Tool Overview**: artemis (v18.2.0) - A set of Java genome visualization tools including the Artemis genome browser & annotation tool, ACT DNA sequence comparison viewer, DNA Plotter image generation tool and the BamView BAM/CRAM file viewer.
- **Core Function**: A set of Java genome visualization tools including the Artemis genome browser & annotation tool, ACT DNA sequence comparison viewer, DNA Plotter image generation tool and the BamView BAM/CRAM file viewer.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda artemis`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
