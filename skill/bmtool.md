---
name: bmtool
category: metagenomics
description: Create bitmask database for BMTagger host read removal
tags: [bmtool, bmtagger, metagenomics, host-removal, bitmask]
author: oxo-call-community
source_url: "ftp://ftp.ncbi.nlm.nih.gov/pub/agarwala/bmtagger/"
---

## Concepts

- **Tool Overview**: bmtool creates bitmask databases from reference genomes for use with BMTagger.
- **Core Function**: Builds k-mer bitmask for fast identification of contaminant/host sequences.
- **Workflow**: Run bmtool to create bitmask, then use with bmfilter for read filtering.
- **K-mer Size**: Default 18-mers; adjustable based on specificity needs.
- **Input**: Reference genome FASTA file.
- **Installation**: Install via bioconda: `conda install -c bioconda bmtagger`

## Pitfalls

- **Memory Usage**: Large genomes require significant memory during bitmask creation.
- **K-mer Selection**: Smaller k-mers are faster but less specific; larger k-mers are slower but more specific.
- **Output Path**: Specify full path for output file to avoid confusion with bmfilter.
- **Genome Completeness**: Use complete reference genome for comprehensive filtering.

## Examples

### Create standard bitmask
**Args:** `bmtool -d human_genome.fa -o human.bitmask`
**Explanation:** Creates default 18-mer bitmask from human genome FASTA.

### Create bitmask with custom k-mer size
**Args:** `bmtool -d genome.fa -o genome.bitmask -w 20`
**Explanation:** Creates 20-mer bitmask for more specific matching.

### Create bitmask for multiple genomes
**Args:** `bmtool -d combined_genomes.fa -o combined.bitmask -w 18`
**Explanation:** Creates bitmask from concatenated multiple contaminant genomes.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
